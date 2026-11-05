"""Generate static, crawlable service pages and shared SEO metadata.

Run from any directory: python3 scripts/build-seo.py
The production domain was confirmed by the site owner on 2026-10-27.
"""
from pathlib import Path
from html import escape
import json
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import seo_en as EN  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://msakinasbar.com"
NAME = "مساكن أسبار"
PAGES = [
    {
        "slug": "worker-accommodation", "name": "سكن العمالة للشركات", "type": "Service",
        "title": "سكن العمالة للشركات | مساكن أسبار",
        "description": "سكن عمالة بغرف مجهزة، مع خيارات النقل والإعاشة وإدارة المرافق من مساكن أسبار. حدّد موقع مشروعك وعدد الأفراد واطلب عرضًا يناسب فريقك.",
        "image": "room-red-bedding.webp", "alt": "غرفة سكن للعمالة مجهزة بأسرّة وخزائن",
        "intro": "مكان يليق بفريقك. نوفّر سكن العمالة للشركات مع غرف مجهزة ومتابعة للتشغيل، ونرتّب الخدمات بحسب موقع المشروع وعدد الأفراد ومدة السكن.",
        "sections": [
            ("سكن يناسب يوم فريقك", "اختيار السكن يبدأ من طبيعة العمل. موقع المشروع، أوقات الورديات ومدة الإقامة تساعد في تحديد الاحتياج. شاركنا هذه التفاصيل لنراجع الخيارات والتجهيزات المناسبة قبل الاتفاق على التشغيل."),
            ("ما الذي يشمله سكن العمالة؟", "تشمل التجهيزات غرفًا مفروشة وأسرّة وخزائن. تتوفر مرافق مشتركة، وتختلف تفاصيل التجهيز والخدمات بحسب الموقع والباقة. نوضح لك ما يشمله العرض وما يحتاج إلى ترتيب إضافي قبل التعاقد."),
            ("سكن ونقل وإعاشة في طلب واحد", "يمكنك طلب الإسكان وحده أو إضافة النقل والإعاشة وإدارة المرافق. عند جمع الخدمات، يصبح احتياج السكن ومواعيد الرحلات والوجبات ضمن خطة متفق عليها، مع جهة واحدة للتواصل والمتابعة."),
            ("النظافة والصيانة أثناء الإقامة", "جاهزية الغرف والمرافق جزء من تجربة السكن. نحدد نطاق النظافة والصيانة والمتابعة التشغيلية في العرض، مع توضيح طريقة رفع الملاحظات ومتابعة معالجتها خلال مدة الخدمة."),
            ("كيف تحصل على عرض سكن لفريقك؟", "جهّز عدد الأفراد، المدينة أو موقع العمل، مدة السكن وموعد البدء المطلوب. أضف احتياجك للنقل أو الإعاشة وأي متطلبات تخص الغرف. هذه المعلومات تساعد فريقنا على إعداد عرض أوضح، دون افتراض أن كل المواقع لها التجهيزات أو التكلفة نفسها."),
        ],
        "checks": ["المدينة وموقع العمل", "عدد الأفراد ومدة السكن", "موعد البدء المطلوب", "الخدمات والتجهيزات المطلوبة"],
        "faq": [("هل يمكن طلب السكن دون خدمات إضافية؟", "نعم، يمكنك اختيار الإسكان وحده أو إضافة النقل والإعاشة وإدارة المرافق، وتوضح التفاصيل في عرض السعر."), ("هل تكلفة سكن العمالة ثابتة؟", "يعتمد العرض على الموقع وعدد الأفراد ومدة السكن والتجهيزات والخدمات المطلوبة. تواصل معنا لمراجعة احتياجك.")],
    },
    {
        "slug": "worker-transport", "name": "نقل العمالة", "type": "Service",
        "title": "نقل العمالة بين السكن والعمل | مساكن أسبار",
        "description": "تنظيم نقل العمالة بين السكن ومواقع العمل وفق الورديات والخطة المتفق عليها. تعرّف على خدمة النقل من مساكن أسبار واطلب عرضًا لمشروعك.",
        "image": "team.webp", "alt": "فريق العمالة وحافلة النقل من بروفايل أسبار",
        "intro": "يومهم يبدأ براحة. ننظّم الرحلات بين السكن والعمل وفق مواعيد فريقك، ونربط تفاصيل النقل بخطة تشغيل واضحة ومتفق عليها.",
        "sections": [
            ("رحلات تبدأ من احتياج المشروع", "قبل ترتيب النقل، نحتاج إلى معرفة موقع السكن وموقع العمل وعدد الأفراد. المسار اليومي ونقاط التجمع ومواعيد الدخول والخروج عناصر تساعد في تحديد خطة الرحلات المناسبة، بدل الاعتماد على تقدير عام."),
            ("نقل يناسب مواعيد الورديات", "إذا كان فريقك يعمل على أكثر من وردية، شاركنا مواعيد كل مجموعة وعدد أفرادها. نراجع تنظيم الرحلات بحسب هذه المواعيد والخطة المتفق عليها، مع توضيح آلية التنسيق عند وجود تعديل في الجدول."),
            ("اربط السكن بخطة النقل", "اختيار السكن بمعزل عن موقع العمل قد يجعل التنقل أكثر تعقيدًا. عند طلب الإسكان والنقل معًا، يمكن مراجعة العلاقة بين الموقعين واحتياج الرحلات ضمن طلب واحد، وتوضيح نطاق كل خدمة في العرض."),
            ("تفاصيل نتفق عليها قبل التشغيل", "تساعد قائمة واضحة بالمواقع والأعداد والمواعيد على تقليل الالتباس. حدّد ما إذا كانت هناك مواقع عمل متعددة أو أيام تختلف عن الجدول المعتاد، حتى يناقش فريقنا هذه التفاصيل معك قبل اعتماد الخطة."),
            ("ما الذي تحتاجه لطلب عرض نقل؟", "أرسل موقع السكن، مواقع العمل، عدد الأفراد لكل وردية، أيام التشغيل وموعد البدء المطلوب. إذا تغيّر احتياج المشروع خلال مدة الخدمة، تكون مراجعة التغيير وفق الترتيب المتفق عليه، ولا يفترض العرض تلقائيًا شمول أي مسار أو رحلة إضافية."),
        ],
        "checks": ["موقع السكن ومواقع العمل", "عدد الأفراد في كل وردية", "أوقات الرحلات وأيام التشغيل", "موعد البدء ومدة الخدمة"],
        "faq": [("هل يمكن تنسيق النقل مع الورديات؟", "نرتب الرحلات وفق مواعيد فريقك والخطة المتفق عليها. شاركنا عدد الأفراد ومواعيد كل وردية عند الطلب."), ("هل يمكن جمع النقل مع السكن؟", "نعم، يمكنك اختيار السكن والنقل ضمن طلب واحد، وإضافة الإعاشة أو إدارة المرافق بحسب احتياجك.")],
    },
    {
        "slug": "worker-catering", "name": "إعاشة العمالة", "type": "Service",
        "title": "إعاشة العمالة وتنظيم الوجبات | مساكن أسبار",
        "description": "خدمة إعاشة العمالة بوجبات متنوعة ومواعيد تناسب المشروع، مع العناية بسلامة الغذاء. حدّد عدد الأفراد والورديات واطلب عرضك من مساكن أسبار.",
        "image": "kitchen.webp", "alt": "المطبخ المركزي وتجهيزات إعداد الوجبات",
        "intro": "عناية في كل وجبة. نرتّب الإعاشة ووجبات فريقك بمواعيد تناسب طبيعة المشروع، مع العناية بسلامة الغذاء وتوضيح نطاق الخدمة من البداية.",
        "sections": [
            ("وجبات ضمن يوم عمل واضح", "تبدأ خطة الإعاشة بعدد الأفراد ومواعيد العمل. أوقات الوجبات ومكان تقديمها وعدد الوجبات المطلوبة يوميًا تساعدنا على مراجعة الخدمة المناسبة. شاركنا احتياجك الفعلي حتى يعكس العرض تفاصيل مشروعك."),
            ("تنوع يناسب احتياج الفريق", "نوفّر وجبات متنوعة بحسب الخطة المتفق عليها. إذا كانت لدى فريقك تفضيلات أو متطلبات غذائية خاصة، اذكرها عند الطلب لمناقشة إمكانية تلبيتها وتوضيحها في العرض قبل بدء الخدمة."),
            ("تنسيق الوجبات مع الورديات", "قد تختلف أوقات الوجبات بين فرق العمل. توضيح أعداد الأفراد ومواعيد كل وردية يساعد في تنظيم الإعاشة وربطها بيوم الفريق، خصوصًا عند طلب السكن والنقل مع الخدمة نفسها."),
            ("سلامة الغذاء ومتابعة الملاحظات", "العناية بسلامة الغذاء جزء من الخدمة. نراجع معك تفاصيل تقديم الوجبات وطريقة التواصل عند وجود ملاحظة، ويحدد الاتفاق نطاق الخدمة ومسؤوليات التشغيل والمتابعة، دون الاعتماد على وصف عام للباقة."),
            ("طلب عرض إعاشة للعمالة", "جهّز عدد الأفراد، عدد الوجبات اليومية، موقع تقديم الخدمة، مواعيد الورديات ومدة التشغيل. اذكر أي متطلبات غذائية منذ البداية. تُراجع التفاصيل قبل اعتماد العرض، وقد يختلف نطاق الخدمة بحسب الموقع والاحتياج المتفق عليه."),
        ],
        "checks": ["عدد الأفراد والوجبات اليومية", "الموقع ومواعيد تقديم الوجبات", "الورديات ومدة التشغيل", "أي متطلبات غذائية خاصة للمراجعة"],
        "faq": [("هل يمكن تحديد مواعيد الوجبات؟", "نراجع مواعيد مشروعك والورديات، ثم نرتب الوجبات وفق الخطة المتفق عليها."), ("هل تشمل باقة السكن الإعاشة تلقائيًا؟", "يمكن إضافة الإعاشة إلى طلب السكن. يحدد عرض السعر الخدمات المشمولة وتفاصيلها بوضوح.")],
    },
    {
        "slug": "facilities-management", "name": "إدارة مرافق سكن العمالة", "type": "Service",
        "title": "إدارة مرافق سكن العمالة والنظافة والصيانة | مساكن أسبار",
        "description": "نظافة وصيانة وإشراف ومتابعة ملاحظات سكن العمالة من مساكن أسبار. تعرّف على إدارة المرافق وحدّد نطاق الخدمة الذي يحتاجه موقعك.",
        "image": "facilities-management.webp", "alt": "ممرات السكن مع تجهيزات السلامة ومخرج الطوارئ",
        "intro": "التفاصيل علينا. نتابع النظافة والصيانة والإشراف وملاحظات التشغيل، لنحافظ على جاهزية مرافق السكن بحسب النطاق المتفق عليه.",
        "sections": [
            ("إدارة تبدأ بمعرفة الموقع", "لكل سكن تفاصيله: الغرف، الممرات والمرافق المشتركة. نراجع احتياج الموقع والخدمات المطلوبة قبل الاتفاق على نطاق إدارة المرافق، حتى تكون مهام التشغيل واضحة لفريقك وفريقنا."),
            ("النظافة في الغرف والمرافق", "يساعد تحديد المساحات المشمولة وأوقات العمل على تنظيم أعمال النظافة. تُوضح تفاصيل الخدمة في العرض بحسب الموقع والباقة، بما يشمل نطاق المرافق المشتركة وما يحتاج إلى ترتيب خاص."),
            ("الصيانة ومتابعة الملاحظات", "رفع الملاحظة بداية المتابعة. نناقش طريقة استقبال ملاحظات السكن ومتابعة معالجتها، مع تحديد مسؤوليات الصيانة ضمن الاتفاق. إذا كانت هناك تجهيزات أو أعمال تتطلب ترتيبات إضافية، ينبغي توضيحها قبل بدء التشغيل."),
            ("الإشراف والتواصل مع جهة واحدة", "بدل توزيع تفاصيل السكن على جهات متعددة، يمكن جمع الإسكان وإدارة المرافق والخدمات المرتبطة في طلب واحد. نوضح نطاق الإشراف والمتابعة والتقارير بحسب الخطة المتفق عليها، لتعرف من تتواصل معه وما الذي تتضمنه الخدمة."),
            ("كيف تحدد نطاق إدارة المرافق؟", "شاركنا الموقع وعدد الأفراد ووصف الغرف والمرافق، وحدّد احتياج النظافة والصيانة والإشراف. أضف أي ملاحظات تشغيلية قائمة وموعد البدء المطلوب. بناءً على هذه المعلومات، يناقش فريقنا تفاصيل الخدمة معك قبل إعداد العرض واعتماد نطاق العمل."),
        ],
        "checks": ["موقع السكن وعدد الأفراد", "وصف الغرف والمرافق المشتركة", "نطاق النظافة والصيانة والإشراف", "الملاحظات الحالية وموعد البدء"],
        "faq": [("هل تشمل الخدمة النظافة والصيانة؟", "تشمل الخدمة النظافة والصيانة والإشراف بحسب نطاق الموقع والباقة المتفق عليها، وتوضح التفاصيل في العرض."), ("كيف تتم متابعة ملاحظات السكن؟", "نتفق معك على طريقة التواصل ورفع الملاحظات ومتابعة معالجتها ضمن نطاق الخدمة.")],
    },
    {
        "slug": "choosing-worker-accommodation", "name": "دليل اختيار سكن العمالة", "type": "Article",
        "title": "كيف تختار سكن العمالة لشركتك؟ | دليل مساكن أسبار",
        "description": "دليل عملي لاختيار سكن العمالة: الموقع والغرف والنقل والإعاشة والنظافة ونطاق التعاقد. قائمة واضحة تساعد شركتك على مقارنة عروض السكن.",
        "image": "room-red-bedding.webp", "alt": "أسرّة وخزائن في غرفة سكن مجهزة",
        "intro": "السكن قرار يؤثر في يوم فريقك. قبل مقارنة الأسعار، قارن ما تتضمنه الخدمة، ومدى ملاءمتها لموقع العمل ومواعيد المشروع.",
        "sections": [
            ("ابدأ بالموقع ومواعيد العمل", "اكتب موقع المشروع ومواعيد الورديات أولًا. راجع مسار الرحلة بين السكن والعمل وناقش أوقات التنقل مع مقدم الخدمة. قرب السكن على الخريطة وحده لا يوضح تفاصيل الوصول أو احتياج النقل اليومي."),
            ("راجع تجهيز الغرف بنفسك", "اطلب وصفًا واضحًا للغرف والأسرّة والخزائن ودورات المياه والمرافق المشتركة. تختلف التجهيزات بين المواقع والباقات، لذلك لا تعتمد على صورة واحدة أو وصف مختصر. اطلب توضيح ما يتوفر فعليًا في الموقع المقترح لفريقك."),
            ("قارن تكلفة الخدمة كاملة", "عند مقارنة عرضين، راجع الخدمات المشمولة في كل منهما: السكن، النقل، الإعاشة، النظافة والصيانة. اسأل عن البنود الإضافية وشروط تغيير العدد أو المدة. المقارنة تصبح أوضح عندما يكون نطاق الخدمة متقاربًا ومكتوبًا."),
            ("حدّد مسؤولية النظافة والصيانة", "اسأل عن المساحات المشمولة بالنظافة، وطريقة رفع ملاحظات الصيانة، والجهة التي تتولى المتابعة. من المفيد الاتفاق على آلية التواصل قبل وصول الفريق إلى السكن، بدل تأجيل هذه التفاصيل إلى أول ملاحظة."),
            ("نسّق الإعاشة مع الورديات", "إذا كنت تحتاج إلى وجبات، حدّد عددها ومواعيدها ومكان تقديمها. اذكر المتطلبات الغذائية الخاصة للمراجعة. تأكد أن تفاصيل الوجبات مذكورة في العرض، خصوصًا إذا كانت مواعيد فرقك مختلفة."),
            ("اطلب نطاقًا مكتوبًا قبل الاتفاق", "اجمع عدد الأفراد ومدة السكن وموعد البدء والخدمات المطلوبة في طلب واحد. راجع العرض مع فريقك، واطلب توضيح أي بند غير محدد. هذه القائمة تساعدك على مناقشة الاحتياج التشغيلي، وتبقى متطلبات الموقع والتراخيص ومسؤوليات الأطراف بحاجة إلى تحقق مستقل قبل التعاقد."),
        ],
        "checks": ["موقع مناسب وخطة تنقل واضحة", "تجهيزات محددة للموقع المقترح", "خدمات مشمولة وتكلفة مفهومة", "آلية تواصل ومتابعة مكتوبة"],
        "faq": [("ما المعلومات الأساسية لطلب عرض سكن؟", "عدد الأفراد، المدينة أو موقع العمل، مدة السكن، موعد البدء والخدمات المطلوبة."), ("كيف أقارن بين عروض سكن العمالة؟", "قارن نطاق الخدمات والتجهيزات والموقع ومدة الخدمة أولًا، ثم راجع التكلفة والبنود الإضافية على أساس متقارب.")],
    },
]


def json_ld(graph):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace('<', '\\u003c') + '</script>'


UPDATED = "2026-11-05"
ORG = {"@type": "Organization", "@id": ORIGIN + "/#organization", "name": NAME,
       "alternateName": ["Aspar Residences", "مساكن اسبار", "أسبار للسكن"],
       "description": "مساكن أسبار شركة متخصصة في توفير وتشغيل سكن العمالة للشركات، مع النقل والإعاشة وإدارة المرافق عبر جهة واحدة.",
       "slogan": "راحتهم مسؤوليتنا، وثقتك أولويتنا",
       "url": ORIGIN + "/",
       "logo": {"@type": "ImageObject", "url": ORIGIN + "/assets/logo-transparent.png", "width": 1254, "height": 1254},
       "image": ORIGIN + "/assets/share/home.jpg",
       "email": "info@msakinasbar.com", "telephone": "+966500558677",
       "knowsAbout": ["سكن العمالة", "سكن عمال للشركات", "نقل العمالة", "إعاشة العمالة", "إدارة المرافق",
                      "Worker accommodation", "Labour accommodation", "Staff transport", "Workforce catering", "Facilities management"],
       "contactPoint": [{"@type": "ContactPoint", "telephone": "+966500558677", "contactType": "sales", "availableLanguage": ["ar", "en"]},
                        {"@type": "ContactPoint", "telephone": "+966557011839", "contactType": "customer service", "availableLanguage": ["ar", "en"]}]}
ORG_EN = dict(ORG, name=EN.NAME, alternateName=[NAME, "مساكن اسبار", "Aspar"],
              description="Aspar Residences provides and operates worker accommodation for companies, with transport, catering and facilities management through one partner.",
              slogan="Their comfort is our responsibility, your trust is our priority")

ICONS = """<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">"""

PREFIX = {"ar": "", "en": "/en"}


def alternates(path):
    """hreflang links for a page, given its Arabic (unprefixed) path."""
    return (f'<link rel="alternate" hreflang="ar" href="{ORIGIN}{path}">\n'
            f'<link rel="alternate" hreflang="en" href="{ORIGIN}/en{path}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{ORIGIN}{path}">')


def metadata(title, description, path="/", share="home", article=False, alt=None, lang="ar"):
    url = ORIGIN + PREFIX[lang] + path
    if lang == "ar":
        image = "https://aspar-residences.vercel.app/assets/share/aspar-social-lyon.jpg"
    else:
        image = f"{ORIGIN}/assets/share/en-{share}.jpg?v={UPDATED.replace('-', '')}"
    alt = escape(alt or title, quote=True)
    site = NAME if lang == "ar" else EN.NAME
    locale, other = ("ar_SA", "en_US") if lang == "ar" else ("en_US", "ar_SA")
    return f"""<!-- seo:start -->
<title>{escape(title)}</title>
<meta name="description" content="{escape(description, quote=True)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}">
{alternates(path)}
<meta property="og:locale" content="{locale}">
<meta property="og:locale:alternate" content="{other}">
<meta property="og:type" content="{'article' if article else 'website'}">
<meta property="og:site_name" content="{site}">
<meta property="og:title" content="{escape(title, quote=True)}">
<meta property="og:description" content="{escape(description, quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title, quote=True)}">
<meta name="twitter:description" content="{escape(description, quote=True)}">
<meta name="twitter:image" content="{image}">
<meta name="twitter:image:alt" content="{alt}">
{ICONS}
<!-- seo:end -->"""


def page_url(p):
    return '/' + ('guides' if p['type'] == 'Article' else 'services') + '/' + p['slug'] + '/'


def pages(lang):
    return PAGES if lang == "ar" else EN.PAGES


def service_links(lang="ar"):
    arrow = ' ←' if lang == "ar" else ' →'
    return ''.join(f'<a href="{PREFIX[lang]}{page_url(p)}">{p["name"]}<span aria-hidden="true">{arrow}</span></a>' for p in pages(lang)[:4])


def build_home(lang="ar"):
    path = ROOT / ('index.html' if lang == "ar" else 'en/index.html')
    base = ORIGIN + PREFIX[lang] + '/'
    org = ORG if lang == "ar" else ORG_EN
    if lang == "ar":
        title = 'مساكن أسبار | سكن العمالة والنقل والإعاشة للشركات'
        meta = metadata(title, 'مساكن أسبار: سكن العمالة للشركات، نقل، إعاشة وإدارة مرافق عبر جهة واحدة. غرف مجهزة وخدمات حسب احتياج مشروعك. حدّد الموقع والعدد واطلب عرضك.', alt='مساكن أسبار — راحتهم مسؤوليتنا، وثقتك أولويتنا')
        list_name, label = "خدمات مساكن أسبار", "تفاصيل خدمات مساكن أسبار"
        guide = '<p class="seo-guide-link">تجهّز سكنًا لفريقك؟ <a href="/guides/choosing-worker-accommodation/">اقرأ دليل اختيار سكن العمالة للشركات ←</a></p>'
    else:
        title = EN.HOME['title']
        meta = metadata(title, EN.HOME['description'], alt=EN.HOME['alt'], lang="en")
        list_name, label = EN.UI['list_name'], EN.UI['services_label']
        guide = f'<p class="seo-guide-link">{EN.UI["guide_prompt"]}<a href="/en/guides/choosing-worker-accommodation/">{EN.UI["guide_read"]}</a></p>'
    html = path.read_text()
    html = re.sub(r'<!-- seo:start -->.*?<!-- seo:end -->\s*', '', html, flags=re.S)
    html = re.sub(r'<title>.*?</title>\s*|<meta name="description"[^>]*>\s*', '', html)
    html = html.replace('<meta name="theme-color"', meta + '\n<meta name="theme-color"', 1)
    html = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', html, flags=re.S)
    html = re.sub(r'<link rel="icon" type="image/svg\+xml" href="data:[^"]*">\s*', '', html)
    graph = [org, {"@type": "WebSite", "@id": base + '#website', "url": base, "name": org["name"], "inLanguage": lang, "publisher": {"@id": ORIGIN + '/#organization'}},
             {"@type": "WebPage", "@id": base + '#webpage', "url": base, "name": title, "inLanguage": lang, "isPartOf": {"@id": base + '#website'}, "about": {"@id": ORIGIN + '/#organization'}, "dateModified": UPDATED, "primaryImageOfPage": {"@type": "ImageObject", "url": ORIGIN + '/assets/share/' + ('home' if lang == 'ar' else 'en-home') + '.jpg', "width": 1200, "height": 630}},
             {"@type": "ItemList", "name": list_name, "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": p["name"], "url": ORIGIN + PREFIX[lang] + page_url(p)} for i, p in enumerate(pages(lang)[:4])]}]
    html = html.replace('</head>', json_ld(graph) + '\n</head>', 1)
    html = re.sub(r'<!-- services-links:start -->.*?<!-- services-links:end -->', '', html, flags=re.S)
    block = f'<!-- services-links:start --><div class="seo-services-links" aria-label="{label}">' + service_links(lang) + '</div>' + guide + '<!-- services-links:end -->'
    html = html.replace('<div class="service-footnote">', block + '<div class="service-footnote">', 1)
    path.write_text(html)


def build_page(p, lang="ar"):
    ar = lang == "ar"
    pre = PREFIX[lang]
    url = ORIGIN + pre + page_url(p)
    home = ORIGIN + pre + '/'
    org = ORG if ar else ORG_EN
    U = None if ar else EN.UI
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "الرئيسية" if ar else U['home'], "item": home}, {"@type": "ListItem", "position": 2, "name": p['name'], "item": url}]}
    entity = {"@type": p['type'], "@id": url + '#content', "name": p['name'], "description": p['description'], "url": url, "inLanguage": lang}
    if p['type'] == 'Service':
        entity.update({"serviceType": p['name'], "provider": {"@id": ORIGIN + '/#organization'}})
    else:
        entity.update({"headline": p['name'], "author": {"@id": ORIGIN + '/#organization'}, "publisher": {"@id": ORIGIN + '/#organization'}, "image": ORIGIN + '/assets/share/' + ('' if ar else 'en-') + p['slug'] + '.jpg', "datePublished": "2026-10-27", "dateModified": UPDATED, "mainEntityOfPage": url})
    sections = ''.join(f'<section><h2>{escape(h)}</h2><p>{escape(t)}</p></section>' for h, t in p['sections'])
    faq = ''.join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in p['faq'])
    checks = ''.join(f'<li>{escape(c)}</li>' for c in p['checks'])
    other = ('/en' if ar else '') + page_url(p)
    if ar:
        t = dict(skip="انتقل إلى المحتوى", home_label="مساكن أسبار — الرئيسية", menu="القائمة الرئيسية", services="خدماتنا", about="عن أسبار", quote="اطلب عرضك", breadcrumb="مسار التصفح", home="الرئيسية", kicker='دليل للشركات' if p['type'] == 'Article' else 'خدماتنا', cta="جهّز احتياج فريقك ←", faq_title='أسئلة عن ' + ('اختيار السكن' if p['type'] == 'Article' else p['name']), before="قبل طلب العرض", before_sub="تفاصيل بسيطة. وعرض أوضح.", contact="تواصل مع فريقنا", related_kicker="شريك واحد. خدمات مترابطة.", related="اكتشف خدمات مساكن أسبار", guide_link="دليل اختيار سكن العمالة للشركات ←", footer="مساكن أسبار · راحتهم مسؤوليتنا.", back="العودة للرئيسية ←", switch='<a href="' + other + '" hreflang="en" lang="en">English</a>', site=NAME)
        css = '<link rel="stylesheet" href="/typography.css?v=numerals-1"><link rel="stylesheet" href="/seo-pages.css?v=1">'
    else:
        t = dict(U, kicker=U['guide_kicker'] if p['type'] == 'Article' else U['services_kicker'], faq_title=U['faq_about'] + ' ' + (U['faq_guide'] if p['type'] == 'Article' else p['name'][0].lower() + p['name'][1:]), switch='<a href="' + other + '" hreflang="ar" lang="ar" aria-label="' + U['switch_label'] + '">' + U['switch'] + '</a>', site=EN.NAME)
        css = '<link rel="stylesheet" href="/typography.ltr.css?v=en-1"><link rel="stylesheet" href="/seo-pages.ltr.css?v=en-1"><link rel="stylesheet" href="/en.css?v=1">'
    html = f"""<!DOCTYPE html>
<html lang="{lang}" dir="{'rtl' if ar else 'ltr'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
{metadata(p['title'], p['description'], page_url(p), share=p['slug'], article=p['type'] == 'Article', alt=p['name'] + ' — ' + t['site'], lang=lang)}
<meta name="theme-color" content="#f43229">
<link rel="preload" href="/assets/fonts/lyon-arabic-display-black.otf" as="font" type="font/otf" crossorigin>
{css}
{json_ld([org, crumbs, entity])}
</head><body class="detail-page"><a class="skip" href="#main">{t['skip']}</a>
<header class="detail-header"><a href="{pre}/" aria-label="{t['home_label']}"><img src="/assets/logo-transparent.webp" width="88" height="88" alt="{t['site']}"></a><nav aria-label="{t['menu']}"><a href="{pre}/#services">{t['services']}</a><a href="{pre}/#about">{t['about']}</a>{t['switch']}<a class="button" href="{pre}/#plan">{t['quote']}</a></nav></header>
<main id="main"><nav class="breadcrumb" aria-label="{t['breadcrumb']}"><a href="{pre}/">{t['home']}</a><span aria-hidden="true"> / </span><span aria-current="page">{p['name']}</span></nav>
<div class="detail-hero"><div><span class="eyebrow">{t['site']} · {t['kicker']}</span><h1>{p['name']}</h1><p>{p['intro']}</p><a class="button" href="{pre}/#plan">{t['cta']}</a></div><img src="/assets/{p['image']}" width="768" height="560" alt="{p['alt']}" fetchpriority="high"></div>
<div class="detail-layout"><article class="detail-copy">{sections}<section class="detail-faq"><h2>{t['faq_title']}</h2>{faq}</section></article><aside class="detail-checklist"><h2>{t['before']}</h2><p>{t['before_sub']}</p><ul>{checks}</ul><a class="button" href="{pre}/#contact">{t['contact']}</a><a class="phone" href="tel:+966500558677" dir="ltr">+966 50 055 8677</a></aside></div>
<section class="related"><span class="eyebrow">{t['related_kicker']}</span><h2>{t['related']}</h2><div class="related-links">{service_links(lang)}</div><a class="guide-link" href="{pre}/guides/choosing-worker-accommodation/">{t['guide_link']}</a></section></main>
<footer><p>{t['footer']}</p><a href="mailto:info@msakinasbar.com">info@msakinasbar.com</a><a href="{pre}/">{t['back']}</a></footer></body></html>"""
    out = ROOT / (pre + page_url(p)).strip('/') / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


def sitemap():
    paths = ['/'] + [page_url(p) for p in PAGES]
    rows = []
    for path in paths:
        alts = (f'<xhtml:link rel="alternate" hreflang="ar" href="{ORIGIN}{path}"/>'
                f'<xhtml:link rel="alternate" hreflang="en" href="{ORIGIN}/en{path}"/>'
                f'<xhtml:link rel="alternate" hreflang="x-default" href="{ORIGIN}{path}"/>')
        for pre in ('', '/en'):
            rows.append(f'  <url><loc>{escape(ORIGIN + pre + path)}</loc><lastmod>{UPDATED}</lastmod>{alts}</url>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(rows) + '\n</urlset>\n')


if __name__ == '__main__':
    assert [p['slug'] for p in PAGES] == [p['slug'] for p in EN.PAGES], "Arabic and English pages must pair up"
    for lang in ('ar', 'en'):
        build_home(lang)
        for page in pages(lang):
            build_page(page, lang)
    (ROOT / 'sitemap.xml').write_text(sitemap())
    (ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: ' + ORIGIN + '/sitemap.xml\n')
    print('Generated Arabic + English: 2 homes, 8 service pages, 2 guides, sitemap.xml and robots.txt.')
