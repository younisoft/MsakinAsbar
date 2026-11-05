"""English copy for the generated pages (imported by build-seo.py).

Slugs, types and images match the Arabic PAGES so each page pairs with its
Arabic counterpart through hreflang.
"""

NAME = "Aspar Residences"

HOME = {
    "title": "Aspar Residences | Worker Accommodation, Transport & Catering in Saudi Arabia",
    "description": "Aspar Residences provides worker accommodation for companies in Saudi Arabia, with transport, catering and facilities management through one partner. Tell us your site and headcount to get a quote.",
    "alt": "Aspar Residences — their comfort is our responsibility",
}

UI = {
    "skip": "Skip to content", "home_label": "Aspar Residences — home", "menu": "Main menu",
    "services": "Services", "about": "About", "quote": "Get a quote", "breadcrumb": "Breadcrumb",
    "home": "Home", "guide_kicker": "Guide for companies", "services_kicker": "Our services",
    "cta": "Plan your team’s needs →", "faq_about": "Questions about", "faq_guide": "choosing accommodation",
    "before": "Before you request a quote", "before_sub": "A few details. A clearer offer.",
    "contact": "Talk to our team", "related_kicker": "One partner. Connected services.",
    "related": "Explore Aspar Residences services", "guide_link": "Guide: choosing worker accommodation →",
    "footer": "Aspar Residences · Their comfort is our responsibility.", "back": "Back to home →",
    "services_label": "Aspar Residences service details",
    "guide_prompt": "Housing a team? ", "guide_read": "Read our guide to choosing worker accommodation →",
    "list_name": "Aspar Residences services", "switch": "العربية", "switch_label": "الصفحة بالعربية",
}

PAGES = [
    {
        "slug": "worker-accommodation", "name": "Worker accommodation for companies", "type": "Service",
        "title": "Worker Accommodation for Companies | Aspar Residences",
        "description": "Furnished worker accommodation with optional transport, catering and facilities management from Aspar Residences. Share your site and headcount to get a quote that fits your team.",
        "image": "room-red-bedding.webp", "alt": "Worker accommodation room with bunk beds and lockers",
        "intro": "A place worthy of your team. We provide worker accommodation for companies, with furnished rooms and ongoing operations, and arrange services around your project location, headcount and length of stay.",
        "sections": [
            ("Housing that fits your team’s day", "Choosing accommodation starts with the nature of the work. Project location, shift times and length of stay all shape what you need. Share these details and we will review the right options and furnishings before operations are agreed."),
            ("What does worker accommodation include?", "Rooms come furnished with beds and lockers, with shared facilities. Furnishings and services vary by site and package, so we set out exactly what the offer includes, and what needs extra arrangement, before you sign."),
            ("Housing, transport and catering in one request", "You can request accommodation on its own or add transport, catering and facilities management. When services are combined, housing needs, trip times and meals sit within one agreed plan, with a single point of contact for follow-up."),
            ("Cleaning and maintenance during the stay", "Ready rooms and facilities are part of the housing experience. The offer defines the scope of cleaning, maintenance and operational follow-up, and how issues are reported and tracked through to resolution."),
            ("How to get an accommodation quote", "Prepare your headcount, city or work site, length of stay and preferred start date. Add any transport or catering needs and room requirements. This helps our team prepare a clearer offer, without assuming every site has the same furnishings or cost."),
        ],
        "checks": ["City and work site", "Headcount and length of stay", "Preferred start date", "Services and furnishings needed"],
        "faq": [("Can I book accommodation without extra services?", "Yes. You can choose accommodation alone or add transport, catering and facilities management. The quote sets out the details."), ("Is the cost of worker accommodation fixed?", "The offer depends on location, headcount, length of stay, furnishings and services. Contact us to review your needs.")],
    },
    {
        "slug": "worker-transport", "name": "Worker transport", "type": "Service",
        "title": "Worker Transport Between Housing and Work Sites | Aspar Residences",
        "description": "Organized staff transport between accommodation and work sites, aligned with shifts and the agreed plan. Learn about Aspar Residences transport and request a quote for your project.",
        "image": "team.webp", "alt": "Workers and an Aspar Residences transport bus",
        "intro": "Their day starts at ease. We organize trips between accommodation and work around your team’s schedule, and tie transport into a clear, agreed operating plan.",
        "sections": [
            ("Trips that start from your project’s needs", "Before arranging transport, we need the accommodation location, work sites and headcount. Daily routes, pick-up points and start and finish times help define the right trip plan, rather than relying on a general estimate."),
            ("Transport that follows your shifts", "If your team works more than one shift, share each group’s timings and size. We plan trips around these times and the agreed plan, and set out how changes to the schedule are coordinated."),
            ("Link accommodation to the transport plan", "Choosing housing in isolation from the work site can make commuting harder. When you request accommodation and transport together, the link between both locations and the trips needed can be reviewed in one request, with the scope of each service set out in the offer."),
            ("Details agreed before operations start", "A clear list of locations, numbers and times reduces confusion. Note any multiple work sites or days that differ from the usual schedule, so our team can discuss them with you before the plan is approved."),
            ("What you need for a transport quote", "Send the accommodation location, work sites, headcount per shift, operating days and preferred start date. If project needs change during the service, changes are reviewed under the agreed arrangement; the offer does not automatically cover additional routes or trips."),
        ],
        "checks": ["Accommodation and work site locations", "Headcount per shift", "Trip times and operating days", "Start date and service duration"],
        "faq": [("Can transport be coordinated with shifts?", "We arrange trips around your team’s schedule and the agreed plan. Share the headcount and timing of each shift when you request a quote."), ("Can I combine transport with accommodation?", "Yes. You can choose accommodation and transport in one request, and add catering or facilities management as needed.")],
    },
    {
        "slug": "worker-catering", "name": "Worker catering", "type": "Service",
        "title": "Worker Catering and Meal Planning | Aspar Residences",
        "description": "Workforce catering with varied meals at times that suit your project, with attention to food safety. Share your headcount and shifts to get a quote from Aspar Residences.",
        "image": "kitchen.webp", "alt": "Central kitchen and meal preparation equipment",
        "intro": "Care in every meal. We arrange catering for your team at times that suit the project, with attention to food safety and a clear scope of service from the start.",
        "sections": [
            ("Meals within a clear working day", "A catering plan starts with headcount and working hours. Meal times, where meals are served and how many are needed per day help us define the right service. Share your actual needs so the offer reflects your project."),
            ("Variety that suits the team", "We provide varied meals according to the agreed plan. If your team has preferences or special dietary requirements, mention them when you request a quote so we can discuss them and set them out in the offer before service begins."),
            ("Meals coordinated with shifts", "Meal times can differ between teams. Setting out headcount and timing for each shift helps organize catering around the team’s day, especially when accommodation and transport are part of the same service."),
            ("Food safety and follow-up", "Attention to food safety is part of the service. We review how meals are served and how issues are raised, and the agreement defines the scope of service and operating responsibilities rather than relying on a general package description."),
            ("Requesting a catering quote", "Prepare your headcount, number of daily meals, service location, shift times and operating period. Mention any dietary requirements from the start. Details are reviewed before the offer is approved, and scope may vary by site and agreed needs."),
        ],
        "checks": ["Headcount and daily meals", "Location and meal times", "Shifts and operating period", "Any special dietary requirements"],
        "faq": [("Can meal times be scheduled?", "We review your project hours and shifts, then arrange meals according to the agreed plan."), ("Does an accommodation package include catering automatically?", "Catering can be added to an accommodation request. The quote clearly sets out the services included.")],
    },
    {
        "slug": "facilities-management", "name": "Worker accommodation facilities management", "type": "Service",
        "title": "Facilities Management for Worker Accommodation | Aspar Residences",
        "description": "Cleaning, maintenance, supervision and issue tracking for worker accommodation from Aspar Residences. Learn about facilities management and define the scope your site needs.",
        "image": "facilities-management.webp", "alt": "Residence corridor with safety equipment and an emergency exit",
        "intro": "We take care of the details. We handle cleaning, maintenance, supervision and operational follow-up to keep accommodation facilities ready, within the agreed scope.",
        "sections": [
            ("Management that starts with knowing the site", "Every residence has its own details: rooms, corridors and shared facilities. We review the site and the services needed before agreeing the scope of facilities management, so tasks are clear to your team and ours."),
            ("Cleaning in rooms and facilities", "Defining the areas covered and working hours helps organize cleaning. Service details are set out in the offer by site and package, including shared facilities and anything that needs special arrangement."),
            ("Maintenance and issue tracking", "Reporting an issue is where follow-up begins. We agree how residence issues are received and tracked to resolution, and define maintenance responsibilities in the agreement. Any equipment or works needing extra arrangements should be clarified before operations start."),
            ("Supervision through one point of contact", "Instead of spreading housing details across several providers, accommodation, facilities management and related services can be combined in one request. We set out the scope of supervision, follow-up and reporting in the agreed plan, so you know who to contact and what the service covers."),
            ("How to define the scope of facilities management", "Share the location, headcount and a description of rooms and facilities, and set out your cleaning, maintenance and supervision needs. Add any current operational issues and the preferred start date. Our team then discusses the details with you before preparing the offer and approving the scope of work."),
        ],
        "checks": ["Residence location and headcount", "Rooms and shared facilities", "Cleaning, maintenance and supervision scope", "Current issues and start date"],
        "faq": [("Does the service include cleaning and maintenance?", "Yes. The service covers cleaning, maintenance and supervision according to the site scope and agreed package, with details in the offer."), ("How are residence issues tracked?", "We agree with you how issues are reported and tracked to resolution within the scope of service.")],
    },
    {
        "slug": "choosing-worker-accommodation", "name": "Guide to choosing worker accommodation", "type": "Article",
        "title": "How to Choose Worker Accommodation for Your Company | Aspar Residences Guide",
        "description": "A practical guide to choosing worker accommodation: location, rooms, transport, catering, cleaning and contract scope. A clear checklist to help your company compare housing offers.",
        "image": "room-red-bedding.webp", "alt": "Bunk beds and lockers in a furnished residence room",
        "intro": "Housing is a decision that shapes your team’s day. Before comparing prices, compare what the service includes and how well it fits the work site and project schedule.",
        "sections": [
            ("Start with location and working hours", "Write down the project location and shift times first. Review the route between accommodation and work and discuss travel times with the provider. Distance on a map alone does not show access details or daily transport needs."),
            ("Check the room furnishings yourself", "Ask for a clear description of rooms, beds, lockers, bathrooms and shared facilities. Furnishings vary between sites and packages, so do not rely on a single photo or short description. Ask what is actually available at the proposed site for your team."),
            ("Compare the full cost of service", "When comparing two offers, review what each includes: accommodation, transport, catering, cleaning and maintenance. Ask about extra items and the terms for changing headcount or duration. Comparison is clearer when the scope is similar and written down."),
            ("Define responsibility for cleaning and maintenance", "Ask which areas are cleaned, how maintenance issues are reported and who handles follow-up. It helps to agree how communication works before the team moves in, rather than leaving these details until the first issue."),
            ("Coordinate catering with shifts", "If you need meals, specify the number, timing and where they are served. Mention any special dietary requirements for review. Make sure meal details are written into the offer, especially if your teams work different hours."),
            ("Get the scope in writing before you agree", "Put headcount, length of stay, start date and services needed into one request. Review the offer with your team and ask for clarification on anything undefined. This checklist helps you discuss operational needs; site requirements, permits and each party’s responsibilities still need independent verification before contracting."),
        ],
        "checks": ["Suitable location and clear transport plan", "Defined furnishings at the proposed site", "Included services and clear cost", "Written communication and follow-up process"],
        "faq": [("What information do I need to request an accommodation quote?", "Headcount, city or work site, length of stay, start date and the services you need."), ("How do I compare worker accommodation offers?", "Compare scope of services, furnishings, location and service duration first, then review cost and extra items on a like-for-like basis.")],
    },
]
