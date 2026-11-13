"""Legal pages (privacy, cancellation, terms) in Arabic and English.

Each section is (heading, paragraph, bullets). Bullets may be empty.
Structure follows common Saudi accommodation-provider policies, adapted to
company (B2B) worker housing. The signed contract or quote always prevails.
"""

UPDATED = "2026-11-14"

LEGAL_NAME = "شركة أسبار الموحدة التجارية"
CR = "4030407410"
UNIFIED = "7021495051"

UI = {
    "ar": {"entity": f"تُقدَّم خدمات مساكن أسبار من {LEGAL_NAME} · سجل تجاري رقم {CR} · الرقم الموحد {UNIFIED}",
           "footer_entity": f"{LEGAL_NAME} · س.ت {CR} · الرقم الموحد {UNIFIED}",
           "links": [("privacy", "سياسة الخصوصية"), ("cancellation-policy", "سياسة الإلغاء"), ("terms", "الشروط والأحكام")], "kicker": "السياسات والشروط", "updated": "آخر تحديث: ١٤ نوفمبر ٢٠٢٦", "questions": "لديك سؤال عن هذه السياسة؟",
           "questions_sub": "تواصل مع فريقنا وسنوضح لك ما يخص اتفاقك.", "legal_label": "السياسات"},
    "en": {"entity": f"Aspar Residences services are provided by <bdi lang='ar'>{LEGAL_NAME}</bdi> (Aspar Unified Trading Company) · Commercial Registration No. {CR} · Unified No. {UNIFIED}",
           "footer_entity": f"Aspar Unified Trading Company · CR {CR} · Unified No. {UNIFIED}",
           "links": [("privacy", "Privacy policy"), ("cancellation-policy", "Cancellation policy"), ("terms", "Terms and conditions")], "kicker": "Policies & terms", "updated": "Last updated: 14 November 2026", "questions": "Questions about this policy?",
           "questions_sub": "Contact our team and we will clarify how it applies to your agreement.", "legal_label": "Policies"},
}

PAGES = {
    "ar": [
        {
            "slug": "privacy", "name": "سياسة الخصوصية",
            "title": "سياسة الخصوصية | مساكن أسبار",
            "description": "كيف تجمع مساكن أسبار البيانات الشخصية وتستخدمها وتحميها عند طلب عروض سكن العمالة والنقل والإعاشة، وحقوقك وفق نظام حماية البيانات الشخصية.",
            "intro": "نحترم خصوصية عملائنا وسكان مرافقنا. توضح هذه السياسة البيانات التي نجمعها عند استخدام موقع مساكن أسبار أو التعاقد على خدماتنا، وكيف نستخدمها ونحميها، وفق نظام حماية البيانات الشخصية في المملكة العربية السعودية.",
            "sections": [
                ("البيانات التي نجمعها", "نجمع البيانات اللازمة لتقديم خدماتنا فقط، ومنها:", [
                    "بيانات التواصل: الاسم، اسم الشركة، رقم الجوال والبريد الإلكتروني.",
                    "بيانات الطلب: المدينة أو موقع العمل، عدد الأفراد، الخدمات المطلوبة ومدة السكن وموعد البدء.",
                    "بيانات السكان عند التعاقد: الأسماء وأرقام الهوية أو الإقامة وما تطلبه الأنظمة لتسجيل السكن، وتزوّدنا بها الشركة المتعاقدة.",
                    "بيانات الفوترة والدفع: بيانات المنشأة والسجل التجاري والرقم الضريبي ومعلومات التحويل البنكي.",
                ]),
                ("كيف يعمل نموذج الطلب في الموقع", "عند تعبئة نموذج طلب العرض، تُجهَّز رسالة بالبيانات التي أدخلتها وتُفتح في واتساب لتراجعها وترسلها بنفسك. لا يحفظ الموقع هذه البيانات على خوادمه، وتخضع الرسالة بعد إرسالها لسياسة خصوصية واتساب.", []),
                ("كيف نستخدم البيانات", "نستخدم البيانات للأغراض التالية:", [
                    "إعداد عروض الأسعار والتواصل معك بشأن طلبك.",
                    "تنفيذ العقد: التسكين والنقل والإعاشة وإدارة المرافق.",
                    "إصدار الفواتير وتحصيل المستحقات.",
                    "سلامة السكان والمرافق ومتابعة الملاحظات والصيانة.",
                    "الالتزام بالأنظمة والمتطلبات الصادرة عن الجهات المختصة.",
                ]),
                ("مشاركة البيانات والإفصاح عنها", "لا نبيع البيانات الشخصية ولا نؤجرها. قد نشاركها بالقدر اللازم فقط مع:", [
                    "مقدمي خدمات يعملون لصالحنا، مثل النقل والإعاشة والصيانة وأنظمة الفوترة، ويلتزمون بحمايتها.",
                    "الجهات الحكومية والرقابية عندما يطلب النظام ذلك.",
                    "طرف آخر في حال اندماج الشركة أو استحواذ عليها أو نقل أصولها، مع استمرار حماية البيانات.",
                ]),
                ("أمن البيانات", "نطبق إجراءات تقنية وإدارية معقولة لحماية البيانات من الوصول أو الاستخدام غير المصرح به، ونقصر الاطلاع عليها على الموظفين المعنيين. ومع ذلك، لا توجد وسيلة نقل أو تخزين إلكتروني آمنة بالكامل.", []),
                ("الاحتفاظ بالبيانات", "نحتفظ بالبيانات طوال مدة تقديم الخدمة والمدة التي تفرضها الأنظمة بعدها، مثل المتطلبات المحاسبية والضريبية. بعد ذلك نحذفها بطريقة آمنة أو نجعلها مجهولة الهوية.", []),
                ("حقوقك", "وفق نظام حماية البيانات الشخصية، يحق لك:", [
                    "العلم بكيفية جمع بياناتك واستخدامها.",
                    "الاطلاع على بياناتك والحصول على نسخة منها.",
                    "طلب تصحيح البيانات غير الدقيقة أو استكمالها.",
                    "طلب إتلاف بياناتك عند انتهاء الحاجة إليها، ما لم يوجب النظام الاحتفاظ بها.",
                    "الرجوع عن موافقتك على المعالجة متى كانت الموافقة أساسها.",
                ]),
                ("ملفات تعريف الارتباط", "لا يستخدم موقعنا حاليًا ملفات تعريف ارتباط للتتبع أو الإعلانات. إذا أضفنا أدوات قياس أو تسويق مستقبلًا، سنحدّث هذه السياسة قبل استخدامها.", []),
                ("روابط وخدمات الطرف الثالث", "قد يحتوي الموقع على روابط لخدمات خارجية مثل واتساب أو الخرائط. لا نتحمل مسؤولية ممارسات الخصوصية لدى هذه الجهات، وننصحك بمراجعة سياساتها.", []),
                ("خصوصية القاصرين", "خدماتنا موجهة للشركات وسكن العاملين البالغين. لا نجمع عن قصد بيانات من هم دون ١٨ عامًا، وإذا علمنا بذلك نحذفها.", []),
                ("التغييرات على هذه السياسة", "قد نحدّث هذه السياسة من وقت لآخر. ننشر النسخة المحدثة في هذه الصفحة مع تاريخ التحديث، ونخطر عملاءنا المتعاقدين بالتغييرات الجوهرية عبر البريد الإلكتروني أو وسائل التواصل المعتمدة.", []),
                ("التواصل معنا", "لأي استفسار أو طلب يتعلق ببياناتك الشخصية، راسلنا على info@msakinasbar.com أو اتصل على ‎+966 55 701 1839.", []),
            ],
        },
        {
            "slug": "cancellation-policy", "name": "سياسة الإلغاء",
            "title": "سياسة الإلغاء والاسترداد | مساكن أسبار",
            "description": "شروط إلغاء حجوزات سكن العمالة وتعديلها لدى مساكن أسبار، ونسب الاسترداد ومدة معالجته، وحالات عدم الحضور والظروف الخاصة.",
            "intro": "توضح هذه السياسة أحكام إلغاء الحجز أو تعديله واسترداد المبالغ لخدمات مساكن أسبار. إذا تضمن العقد أو عرض السعر المعتمد شروطًا مختلفة، تُطبَّق شروط العقد.",
            "sections": [
                ("إلغاء الحجز من قبل العميل", "يُحسب موعد الإلغاء من تاريخ بدء الخدمة أو التسكين المؤكد:", [
                    "قبل ٣ أيام أو أكثر من موعد البدء: استرداد ٧٥٪ من المبلغ المدفوع، دون الرسوم الإدارية.",
                    "قبل يوم إلى يومين من موعد البدء: استرداد ٥٠٪ من المبلغ المدفوع، دون الرسوم الإدارية.",
                    "خلال ٢٤ ساعة من موعد البدء: لا يوجد استرداد.",
                    "المغادرة أو إنهاء الخدمة مبكرًا بعد البدء: لا يُسترد مقابل المدة المتبقية من الفترة المفوترة، ما لم ينص العقد على خلاف ذلك.",
                ]),
                ("إلغاء الحجز من قبل مساكن أسبار", "", [
                    "القوة القاهرة: استرداد كامل للمبالغ المدفوعة عن المدة التي لم تُقدَّم فيها الخدمة.",
                    "مخالفة العميل أو السكان لشروط العقد أو قواعد السكن: يحق لنا إنهاء الخدمة دون استرداد.",
                    "مشكلة صيانة أو سلامة تمنع التسكين: نوفر سكنًا بديلًا مماثلًا إن توفر، أو نسترد كامل المبلغ عن المدة المتبقية.",
                ]),
                ("معالجة المبالغ المستردة", "تُعالَج المبالغ المستردة خلال ٧ إلى ١٤ يوم عمل من تاريخ الموافقة على طلب الإلغاء، وتُحوَّل إلى الحساب البنكي للمنشأة المتعاقدة. الرسوم الإدارية ورسوم الخدمة غير قابلة للاسترداد.", []),
                ("تعديل الحجز", "", [
                    "تغيير موعد البدء: مجانًا حتى ٣ أيام قبل الموعد وبحسب التوفر. بعد ذلك قد تُفرض رسوم تعديل بنسبة ١٠٪ من قيمة الفترة الأولى.",
                    "تغيير عدد الأفراد: يُراجع بحسب التوفر، ويُعدَّل العرض والفاتورة وفق العدد الجديد.",
                    "تمديد مدة السكن: متاح بحسب التوفر، ويُحتسب بالسعر الساري وقت الطلب ما لم يحدد العقد سعر التمديد.",
                ]),
                ("عدم الحضور", "يُعد الحجز «عدم حضور» إذا لم يتم التسكين في الموعد المؤكد دون إشعار مسبق، وفي هذه الحالة لا يُسترد أي مبلغ.", []),
                ("الظروف الخاصة", "ندرس كل حالة على حدة، ويكون القرار وفق تقدير مساكن أسبار:", [
                    "الطوارئ الطبية: استرداد كلي أو جزئي عند تقديم وثائق رسمية.",
                    "قيود السفر أو التأشيرات أو إلغاء المشروع بقرار من جهة مختصة: يقدم العميل المستندات الداعمة لمراجعة الطلب.",
                ]),
                ("كيف تقدّم طلب الإلغاء أو التعديل", "أرسل طلبك كتابيًا إلى info@msakinasbar.com متضمنًا اسم المنشأة ورقم العقد أو العرض والتاريخ المطلوب. يُعتمد تاريخ استلام الطلب الكتابي في احتساب المدد.", []),
            ],
        },
        {
            "slug": "terms", "name": "الشروط والأحكام",
            "title": "الشروط والأحكام | مساكن أسبار",
            "description": "الشروط والأحكام المنظمة لخدمات مساكن أسبار: سكن العمالة والنقل والإعاشة وإدارة المرافق، والدفع والتزامات العميل والسكان وحدود المسؤولية.",
            "intro": "تنظم هذه الشروط استخدام موقع مساكن أسبار والخدمات التي نقدمها للشركات، وتشمل سكن العمالة والنقل والإعاشة وإدارة المرافق. بطلبك الخدمة أو توقيعك العقد، فإنك توافق على هذه الشروط. وعند وجود تعارض، تُقدَّم أحكام العقد الموقع.",
            "sections": [
                ("مرافق السكن", "نوفر غرفًا مجهزة ومرافق مشتركة، وتختلف التجهيزات بحسب الموقع والباقة المتفق عليها. نلتزم بالاشتراطات النظامية المعمول بها لسكن العمالة.", []),
                ("الحجز والدفع", "", [
                    "الحجز مرهون بالتوفر، ولا يُعد مؤكدًا إلا بعد توقيع العقد أو اعتماد العرض واستلام الدفعة الأولى أو السداد الكامل بحسب الاتفاق.",
                    "الأسعار بالريال السعودي، وتُضاف ضريبة القيمة المضافة وفق النظام.",
                    "يتم السداد بالتحويل البنكي أو وسائل الدفع المعتمدة لدينا.",
                    "تُسدَّد الفواتير خلال المدة المحددة في العقد، وإن لم تُحدَّد فخلال ٥ أيام من تاريخ إصدار الفاتورة.",
                ]),
                ("الإلغاء والتعديل والاسترداد", "تخضع طلبات الإلغاء والتعديل واسترداد المبالغ لسياسة الإلغاء المنشورة في الموقع ولأحكام العقد.", []),
                ("التسكين والمغادرة", "", [
                    "يتم التسكين والمغادرة في المواعيد المتفق عليها مع الشركة، وقد يترتب على الترتيبات خارجها رسوم إضافية.",
                    "عند انتهاء المدة، تُسلَّم الغرف والمرافق نظيفة وبحالتها عند الاستلام، مع مراعاة الاستهلاك المعتاد.",
                ]),
                ("التزامات العميل", "", [
                    "سداد المستحقات في مواعيدها.",
                    "الالتزام بعدد السكان المتفق عليه، وتزويدنا ببياناتهم النظامية قبل التسكين.",
                    "عدم استخدام السكن لأي غرض مخالف للأنظمة.",
                    "عدم إجراء أي تعديل على الغرف أو المرافق دون موافقة كتابية منا.",
                    "إبلاغ السكان بقواعد السكن والتأكد من التزامهم بها.",
                ]),
                ("قواعد السكن والسلوك", "", [
                    "يلتزم السكان بقواعد السكن المعتمدة، وقد يؤدي تكرار المخالفة أو جسامتها إلى إخراج المخالف دون استرداد.",
                    "ساعات الهدوء من ١٠ مساءً حتى ٧ صباحًا.",
                    "يُمنع التدخين خارج الأماكن المخصصة، وإدخال المواد الممنوعة أو الخطرة.",
                    "يحافظ السكان على نظافة الغرف والمرافق المشتركة.",
                ]),
                ("استخدام المرافق", "تُستخدم المرافق المشتركة للغرض المخصص لها. يحق لنا تقييد الوصول إليها عند المخالفة، وقد تُفرض رسوم عند إساءة الاستخدام. خدمات الإنترنت، إن وُجدت، مقدمة دون ضمان استمرارها بلا انقطاع.", []),
                ("الأمن والسلامة", "نطبق إجراءات السلامة في مرافقنا. ولا نتحمل مسؤولية فقدان الممتلكات الشخصية للسكان أو سرقتها، وننصح باستخدام الخزائن المقفلة. كما لا نتحمل مسؤولية الخلافات بين السكان.", []),
                ("الأضرار والتلفيات", "تتحمل الشركة المتعاقدة تكلفة إصلاح أو استبدال ما يتلفه سكانها من أصول أو تجهيزات بخلاف الاستهلاك المعتاد. تُحدَّد التكلفة بعد المعاينة، وقد تُضاف إليها رسوم خدمة يحددها العقد.", []),
                ("الخصوصية وحماية البيانات", "نعالج البيانات الشخصية وفق سياسة الخصوصية المنشورة في الموقع ونظام حماية البيانات الشخصية.", []),
                ("حدود المسؤولية", "لا نتحمل مسؤولية الإصابات أو الخسائر إلا ما ينتج عن إهمالنا أو إخلالنا بالعقد، وفي حدود قيمة الخدمة عن الفترة التي وقع فيها الضرر. ولا نتحمل مسؤولية الخدمات التي يقدمها أطراف آخرون لم نتعاقد معهم.", []),
                ("إنهاء الخدمة", "يحق لنا إنهاء الخدمة دون استرداد عند إخلال العميل الجوهري بهذه الشروط أو بالعقد، بعد إشعاره ومنحه مهلة معقولة للتصحيح متى أمكن. وفي حالات القوة القاهرة، تُسترد المبالغ المدفوعة عن المدة التي لم تُقدَّم فيها الخدمة.", []),
                ("القانون الحاكم وتسوية النزاعات", "تخضع هذه الشروط لأنظمة المملكة العربية السعودية. نسعى لحل أي خلاف وديًا أولًا، فإن تعذر ذلك يُحال إلى الجهات القضائية المختصة في المملكة.", []),
                ("التعديلات على الشروط", "قد نعدّل هذه الشروط من وقت لآخر، وننشر النسخة المحدثة في هذه الصفحة. لا تسري التعديلات على العقود القائمة إلا باتفاق الطرفين أو بعد إشعار العميل كتابيًا وفق ما ينص عليه العقد.", []),
            ],
        },
    ],
    "en": [
        {
            "slug": "privacy", "name": "Privacy policy",
            "title": "Privacy Policy | Aspar Residences",
            "description": "How Aspar Residences collects, uses and protects personal data when you request worker accommodation, transport and catering, and your rights under Saudi data protection law.",
            "intro": "We respect the privacy of our clients and residents. This policy explains what data we collect when you use the Aspar Residences website or contract our services, how we use and protect it, in line with the Personal Data Protection Law of the Kingdom of Saudi Arabia.",
            "sections": [
                ("Data we collect", "We only collect the data needed to provide our services, including:", [
                    "Contact details: name, company name, mobile number and email.",
                    "Request details: city or work site, headcount, services needed, length of stay and start date.",
                    "Resident details once contracted: names, ID or iqama numbers and what regulations require for housing registration, supplied by the contracting company.",
                    "Billing details: company details, commercial registration, VAT number and bank transfer information.",
                ]),
                ("How the website request form works", "When you fill in the quote form, a message containing your entries is prepared and opened in WhatsApp for you to review and send yourself. The website does not store this data on its servers. Once sent, the message is subject to WhatsApp’s privacy policy.", []),
                ("How we use data", "We use data to:", [
                    "Prepare quotes and contact you about your request.",
                    "Deliver the contract: housing, transport, catering and facilities management.",
                    "Issue invoices and collect payments.",
                    "Keep residents and facilities safe and follow up on issues and maintenance.",
                    "Comply with laws and requirements of the competent authorities.",
                ]),
                ("Sharing and disclosure", "We do not sell or rent personal data. We may share it only as far as necessary with:", [
                    "Service providers working on our behalf, such as transport, catering, maintenance and billing systems, who are bound to protect it.",
                    "Government and regulatory authorities where the law requires.",
                    "Another party in a merger, acquisition or asset transfer, with data protection continuing to apply.",
                ]),
                ("Data security", "We apply reasonable technical and administrative measures to protect data from unauthorised access or use, and limit access to the staff concerned. No method of electronic transmission or storage is completely secure, however.", []),
                ("Data retention", "We keep data for as long as we provide the service and for any period the law requires afterwards, such as accounting and tax requirements. We then delete it securely or anonymise it.", []),
                ("Your rights", "Under the Personal Data Protection Law you have the right to:", [
                    "Be informed of how your data is collected and used.",
                    "Access your data and obtain a copy of it.",
                    "Ask us to correct or complete inaccurate data.",
                    "Ask us to destroy your data once it is no longer needed, unless the law requires us to keep it.",
                    "Withdraw consent where processing is based on consent.",
                ]),
                ("Cookies", "Our website does not currently use tracking or advertising cookies. If we add analytics or marketing tools in future, we will update this policy before using them.", []),
                ("Third-party links and services", "The website may link to external services such as WhatsApp or maps. We are not responsible for their privacy practices and recommend reviewing their policies.", []),
                ("Minors’ privacy", "Our services are for companies and adult workers. We do not knowingly collect data from anyone under 18, and will delete it if we learn we have.", []),
                ("Changes to this policy", "We may update this policy from time to time. We publish the updated version on this page with its date, and notify contracted clients of material changes by email or other agreed channels.", []),
                ("Contact us", "For any question or request about your personal data, email info@msakinasbar.com or call +966 55 701 1839.", []),
            ],
        },
        {
            "slug": "cancellation-policy", "name": "Cancellation policy",
            "title": "Cancellation & Refund Policy | Aspar Residences",
            "description": "Terms for cancelling or changing worker accommodation bookings with Aspar Residences: refund rates, processing times, no-shows and special circumstances.",
            "intro": "This policy sets out how bookings with Aspar Residences can be cancelled or changed, and how refunds work. Where the signed contract or approved quote states different terms, the contract applies.",
            "sections": [
                ("Cancellation by the client", "Notice is counted from the confirmed service or move-in start date:", [
                    "3 or more days before the start date: 75% of the amount paid is refunded, excluding administrative fees.",
                    "1 to 2 days before the start date: 50% of the amount paid is refunded, excluding administrative fees.",
                    "Within 24 hours of the start date: no refund.",
                    "Early departure or termination after the start: no refund for the remainder of the invoiced period, unless the contract states otherwise.",
                ]),
                ("Cancellation by Aspar Residences", "", [
                    "Force majeure: full refund of amounts paid for any period in which the service was not provided.",
                    "Breach of the contract or house rules by the client or residents: we may end the service without a refund.",
                    "A maintenance or safety issue that prevents move-in: we provide comparable alternative housing if available, or refund the full amount for the remaining period.",
                ]),
                ("Refund processing", "Refunds are processed within 7 to 14 business days of the cancellation being approved, and paid to the contracting company’s bank account. Administrative and service fees are non-refundable.", []),
                ("Changing a booking", "", [
                    "Changing the start date: free up to 3 days before, subject to availability. After that, a change fee of 10% of the first period may apply.",
                    "Changing the headcount: reviewed subject to availability, with the quote and invoice adjusted to the new number.",
                    "Extending the stay: subject to availability, charged at the rate in effect at the time of the request unless the contract sets an extension rate.",
                ]),
                ("No-shows", "A booking is a no-show if move-in does not take place on the confirmed date without prior notice. No amount is refunded in that case.", []),
                ("Special circumstances", "Each case is reviewed individually at the discretion of Aspar Residences:", [
                    "Medical emergencies: full or partial refund with official documentation.",
                    "Travel or visa restrictions, or a project cancelled by decision of a competent authority: the client provides supporting documents for review.",
                ]),
                ("How to request a cancellation or change", "Send your request in writing to info@msakinasbar.com, including the company name, contract or quote number and the date requested. Deadlines are counted from the date we receive the written request.", []),
            ],
        },
        {
            "slug": "terms", "name": "Terms and conditions",
            "title": "Terms and Conditions | Aspar Residences",
            "description": "Terms governing Aspar Residences services: worker accommodation, transport, catering and facilities management, payment, client and resident obligations, and liability.",
            "intro": "These terms govern use of the Aspar Residences website and the services we provide to companies, including worker accommodation, transport, catering and facilities management. By requesting a service or signing a contract, you agree to these terms. Where they conflict, the signed contract prevails.",
            "sections": [
                ("Accommodation facilities", "We provide furnished rooms and shared facilities. Furnishings vary by site and agreed package. We comply with the regulatory requirements that apply to worker housing.", []),
                ("Booking and payment", "", [
                    "Bookings are subject to availability and are confirmed only once the contract is signed or the quote approved and the first instalment or full payment is received, as agreed.",
                    "Prices are in Saudi riyals, with VAT added as required by law.",
                    "Payment is by bank transfer or our other accepted payment methods.",
                    "Invoices are due within the period set in the contract or, if none is set, within 5 days of the invoice date.",
                ]),
                ("Cancellation, changes and refunds", "Cancellation, change and refund requests are governed by the cancellation policy published on this website and by the contract.", []),
                ("Move-in and move-out", "", [
                    "Move-in and move-out take place at times agreed with the company; arrangements outside them may incur extra charges.",
                    "At the end of the term, rooms and facilities are returned clean and in the condition received, allowing for normal wear.",
                ]),
                ("Client obligations", "", [
                    "Pay amounts due on time.",
                    "Keep to the agreed number of residents and provide their official details before move-in.",
                    "Not use the accommodation for any unlawful purpose.",
                    "Not alter rooms or facilities without our written approval.",
                    "Inform residents of the house rules and ensure they follow them.",
                ]),
                ("House rules and conduct", "", [
                    "Residents follow the approved house rules. Repeated or serious breaches may lead to removal of the resident without a refund.",
                    "Quiet hours are 10 pm to 7 am.",
                    "Smoking outside designated areas, and bringing in prohibited or hazardous materials, are not allowed.",
                    "Residents keep rooms and shared facilities clean.",
                ]),
                ("Use of facilities", "Shared facilities are used for their intended purpose. We may restrict access in case of breaches, and charges may apply for misuse. Internet service, where provided, is not guaranteed to be uninterrupted.", []),
                ("Safety and security", "We apply safety measures across our facilities. We are not responsible for loss or theft of residents’ personal belongings and recommend using the lockable lockers. Nor are we responsible for disputes between residents.", []),
                ("Damage", "The contracting company bears the cost of repairing or replacing assets or furnishings damaged by its residents beyond normal wear. Costs are set after inspection, and a service fee set out in the contract may be added.", []),
                ("Privacy and data protection", "We process personal data in line with the privacy policy published on this website and the Personal Data Protection Law.", []),
                ("Limitation of liability", "We are not liable for injury or loss except where caused by our negligence or breach of contract, and then only up to the value of the service for the period in which the damage occurred. We are not responsible for services provided by third parties we have not contracted.", []),
                ("Ending the service", "We may end the service without a refund if the client materially breaches these terms or the contract, after notice and a reasonable period to remedy where possible. In force majeure, amounts paid for any period in which the service was not provided are refunded.", []),
                ("Governing law and disputes", "These terms are governed by the laws of the Kingdom of Saudi Arabia. We aim to settle any dispute amicably first; failing that, it is referred to the competent courts in the Kingdom.", []),
                ("Changes to these terms", "We may amend these terms from time to time and publish the updated version on this page. Changes do not apply to existing contracts unless both parties agree or the client is notified in writing as the contract provides.", []),
            ],
        },
    ],
}
