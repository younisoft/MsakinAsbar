"""Check indexability, structured data, sitemap coverage and local links.

Optional after deployment: python3 scripts/check-seo.py --base-url https://msakinasbar.com
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from urllib.request import urlopen
import argparse
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://msakinasbar.com'


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.tags, self.ld, self.ids = [], [], []
        self.read_ld = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        self.read_ld = tag == 'script' and attrs.get('type') == 'application/ld+json'

    def handle_data(self, data):
        if self.read_ld:
            self.ld.append(json.loads(data))

    def handle_endtag(self, tag):
        if tag == 'script':
            self.read_ld = False

    def find(self, tag, **attrs):
        return [a for t, a in self.tags if t == tag and all(a.get(k) == v for k, v in attrs.items())]


def resolve(path):
    target = ROOT / path.lstrip('/')
    return target / 'index.html' if target.is_dir() else target


def main():
    args = argparse.ArgumentParser()
    args.add_argument('--base-url')
    base = args.parse_args().base_url
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)

    sitemap = ET.parse(ROOT / 'sitemap.xml')
    urls = [n.text for n in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    check(len(urls) == 12 and len(set(urls)) == 12, 'Expected twelve unique sitemap URLs (6 Arabic + 6 English)')
    check('Sitemap: ' + ORIGIN + '/sitemap.xml' in (ROOT / 'robots.txt').read_text(), 'Missing sitemap in robots.txt')
    check('Disallow: /\n' not in (ROOT / 'robots.txt').read_text(), 'Production crawling is blocked')
    documents = {}
    for url in urls:
        path = urlsplit(url).path
        file = resolve(path)
        check(file.is_file(), 'Missing page: ' + path)
        if not file.is_file():
            continue
        p = Page(file.read_text())
        documents[path] = p
        check(len(p.find('title')) == 1, path + ': title must be unique')
        check(len(p.find('h1')) == 1, path + ': expected one h1')
        check(len(p.ids) == len(set(p.ids)), path + ': duplicate IDs')
        english = path.startswith('/en/')
        check(p.find('html', lang='en', dir='ltr') if english else p.find('html', lang='ar', dir='rtl'), path + ': wrong lang/dir')
        twin = path[3:] if english else '/en' + path
        for lang, target in (('ar', twin if english else path), ('en', path if english else twin), ('x-default', twin if english else path)):
            check(p.find('link', rel='alternate', hreflang=lang, href=ORIGIN + target), path + ': missing hreflang ' + lang)
        check(resolve(twin).is_file(), path + ': missing translated page ' + twin)
        check(len(p.find('meta', name='description')) == 1, path + ': description missing or duplicated')
        check(p.find('link', rel='canonical', href=url), path + ': wrong canonical')
        check(p.find('meta', property='og:url', content=url), path + ': wrong sharing URL')
        check(p.find('meta', property='og:image'), path + ': missing sharing image')
        check(p.find('meta', name='robots', content='index,follow,max-image-preview:large'), path + ': indexability missing')
        check(p.ld and all(d.get('@context') == 'https://schema.org' for d in p.ld), path + ': invalid JSON-LD context')
        for img in p.find('img'):
            check('alt' in img and 'width' in img and 'height' in img, path + ': missing image alt/dimensions')
        if base:
            try:
                with urlopen(base.rstrip('/') + path, timeout=20) as response:
                    body = response.read().decode()
                    check(response.status == 200, path + ': unexpected HTTP status')
                    check(url in body and '<h1' in body, path + ': deployed HTML differs')
                    check('noindex' not in response.headers.get('X-Robots-Tag', '').lower(), path + ': deployment blocks indexing')
            except Exception as exc:
                errors.append(path + ': request failed: ' + str(exc))
    for path, page in documents.items():
        for tag, attrs in page.tags:
            ref = attrs.get('href') if tag in ['a', 'link'] else attrs.get('src') if tag in ['img', 'script'] else None
            if not ref:
                continue
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc:
                if ref.startswith(ORIGIN + '/assets/'):
                    check(resolve(parsed.path).is_file(), path + ': missing social asset ' + ref)
                continue
            local_path = parsed.path if parsed.path.startswith('/') else path + parsed.path
            target = resolve(unquote(local_path)) if parsed.path else resolve(path)
            check(target.is_file(), path + ': broken local URL ' + ref)
            if parsed.fragment and target.is_file() and target.suffix == '.html':
                ids = Page(target.read_text()).ids
                check(unquote(parsed.fragment) in ids, path + ': missing anchor ' + ref)
    error_page = Page((ROOT / '404.html').read_text())
    check(error_page.find('meta', name='robots', content='noindex,follow'), '404 must not be indexed')
    json.loads((ROOT / 'vercel.json').read_text())
    if errors:
        print('\n'.join('FAIL ' + e for e in errors))
        raise SystemExit(1)
    print('PASS: 12 indexable pages (Arabic + English) with reciprocal hreflang; unique titles, descriptions, canonical URLs and H1s; valid JSON-LD; sitemap; robots; image dimensions; all internal links and anchors; non-indexable 404.')
    if not base:
        print('Static validation only. Live status codes, redirects, headers and search indexing require deployment checks.')


if __name__ == '__main__':
    main()
