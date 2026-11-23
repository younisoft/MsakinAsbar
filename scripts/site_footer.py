"""Shared bilingual footer. ISO marks identify standards, not certificate documents."""
def render_footer(lang='ar'):
    ar = lang == 'ar'
    home = '/' if ar else '/en/'
    links = [(home+'#contact', 'تواصل معنا' if ar else 'Contact us'), ('/assets/aspar-profile.pdf?v=20261104', 'ملف الشركة التعريفي' if ar else 'Company profile'), (home+'#services', 'خدماتنا' if ar else 'Our services'), (home+'#faq', 'الأسئلة الشائعة' if ar else 'Frequently asked questions'), (home+'guides/choosing-worker-accommodation/', 'دليل اختيار السكن' if ar else 'Accommodation guide'), (home+'terms/', 'الشروط والأحكام' if ar else 'Terms and conditions'), (home+'privacy/', 'سياسة الخصوصية' if ar else 'Privacy policy'), (home+'cancellation-policy/', 'سياسة الإلغاء' if ar else 'Cancellation policy')]
    nav = ''.join(f'<a href="{url}">{label}</a>' for url,label in links)
    social_accounts = [
        ('LinkedIn', 'https://www.linkedin.com/in/msakin-asbar-85256b44a/', '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 10v7m4 0v-7m0 3a3 3 0 0 1 6 0v4"/><circle cx="7" cy="7" r=".7" fill="currentColor" stroke="none"/>'),
        ('X', 'https://x.com/msakinasbar', '<path d="M4 3h4l12 18h-4L4 3Zm16 0L4 21"/>'),
        ('Instagram', 'https://www.instagram.com/msakinasbar/', '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/>'),
        ('TikTok', 'https://www.tiktok.com/@msakinasbar?_r=1&_t=ZS-9BNhf3B268D', '<path d="M14 3h3c.5 2.5 2 4 4 4v3a8 8 0 0 1-4-1v7a5 5 0 1 1-5-5v3a2 2 0 1 0 2 2V3Z"/>'),
    ]
    from html import escape
    social_links = ''.join(f'<a href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="{name} — {"يفتح في تبويب جديد" if ar else "opens in a new tab"}" title="{name}"><svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{icon}</svg></a>' for name, url, icon in social_accounts)
    standards = [('9001:2015', 'إدارة الجودة', 'Quality management'), ('45001:2018', 'الصحة والسلامة المهنية', 'Occupational health & safety'), ('41001:2018', 'إدارة المرافق', 'Facility management')]
    badges = ''.join(f'<div class="aspar-iso" aria-label="ISO {code} — {arabic if ar else english}"><div class="aspar-iso-mark" aria-hidden="true"><span>ISO</span></div><b dir="ltr">{code}</b></div>' for code,arabic,english in standards)
    return f'''<footer class="aspar-footer" aria-label="{'تذييل الموقع' if ar else 'Site footer'}">
  <div class="aspar-footer-inner">
    <nav class="aspar-footer-nav" aria-label="{'روابط مفيدة' if ar else 'Useful links'}">{nav}<a class="aspar-footer-language" href="{'/en/' if ar else '/'}" lang="{'en' if ar else 'ar'}" hreflang="{'en' if ar else 'ar'}">{'English ↗' if ar else 'العربية ↗'}</a></nav>
    <div class="aspar-footer-company"><a class="aspar-footer-logo" href="{home}" aria-label="{'مساكن أسبار — الرئيسية' if ar else 'Aspar Residences — Home'}"><img src="/assets/logo-transparent.webp?v=asbar-2" alt="{'مساكن أسبار' if ar else 'Aspar Residences'}" width="160" height="140" loading="lazy"></a><p>{'شركة أسبار الموحدة التجارية' if ar else 'Aspar Unified Trading Company'}</p><address class="aspar-footer-address"><strong>{'المقر الرئيسي:' if ar else 'Head office:'}</strong> {'جدة، طريق الملك فهد الفرعي، حي البوادي، 23443' if ar else 'Jeddah, King Fahad Branch Road, Al Bawadi District, 23443'}</address><nav class="aspar-footer-social" aria-label="{'حسابات التواصل الاجتماعي' if ar else 'Social media'}">{social_links}</nav><div class="aspar-footer-standards" aria-label="{'معايير الأيزو' if ar else 'ISO standards'}">{badges}</div></div>
    <div class="aspar-footer-bottom"><small>© <span id="year">2026</span> {'مساكن أسبار. جميع الحقوق محفوظة.' if ar else 'Aspar Residences. All rights reserved.'}</small><span>{'راحتهم مسؤوليتنا.' if ar else 'Their comfort is our responsibility.'}</span></div>
  </div>
</footer>'''
