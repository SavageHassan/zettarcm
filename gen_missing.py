#!/usr/bin/env python3
"""Generate all remaining missing pages."""
import os, sys
sys.path.insert(0, '/Users/mac/zettarcm')
# Re-use helpers from gen_remaining
exec(open('/Users/mac/zettarcm/gen_remaining.py').read())

B = '/Users/mac/zettarcm'

# ─── MISSING SERVICE PAGES ────────────────────────────────────────────────────
missing_services = [
    ('practice-management', 'Practice Management Services',
     'Full-service practice management — operations, billing, compliance, and analytics.',
     'Running a successful medical practice requires more than clinical expertise. ZettaRCM\'s practice management services handle the operational side — scheduling optimization, staff workflows, payer contract management, compliance monitoring, and financial reporting — so your team can concentrate on delivering excellent patient care.',
     ['Scheduling workflow optimization and templates','Staff training and billing process documentation','Payer contract review and negotiation support','KPI dashboards and monthly financial reporting','Compliance monitoring and audit preparation','EHR/PM system optimization','Practice growth strategy and credentialing expansion'],
     'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=900&q=80&fit=crop'),
    ('telemedicine-billing', 'Telemedicine Billing Services',
     'Accurate, compliant billing for telehealth visits across all payers and states.',
     'Telehealth has become a permanent fixture in healthcare delivery, but telemedicine billing is uniquely complex — with state-specific coverage rules, modifier requirements, place-of-service coding, and rapidly evolving payer policies. ZettaRCM\'s telehealth billing specialists keep you current and fully reimbursed for every virtual visit.',
     ['Modifier 95 and GT for synchronous telehealth','Place of service 02 and 10 coding accuracy','Audio-only visit billing compliance','Telehealth parity law billing by state','Store-and-forward telemedicine billing','Remote patient monitoring (RPM) billing (CPT 99453-99458)','Platform-specific billing documentation guidance'],
     'https://images.unsplash.com/photo-1587854692152-cbe660dbde88?w=900&q=80&fit=crop'),
    ('ehr-implementation', 'EHR Implementation & Optimization',
     'Expert EHR setup, workflow design, and billing integration for healthcare practices.',
     'A properly implemented EHR system is the backbone of an efficient revenue cycle. ZettaRCM\'s EHR specialists help practices select, implement, and optimize their electronic health record systems — ensuring seamless integration with your billing workflow to maximize clean claim rates from day one.',
     ['EHR system selection guidance and demos','Billing workflow configuration and template setup','Staff training and go-live support','Charge capture optimization within EHR','Clearinghouse and payer EDI integration','Post-go-live optimization and troubleshooting','EHR-to-PM data migration support'],
     'https://images.unsplash.com/photo-1516549655169-df83a0774514?w=900&q=80&fit=crop'),
    ('charge-entry', 'Charge Entry Services',
     'Accurate, timely charge entry to ensure no revenue is missed.',
     'Charge entry is where the revenue cycle begins at the claim level. Missing a charge, entering an incorrect code, or using the wrong diagnosis linkage can cost your practice thousands in lost revenue. ZettaRCM\'s charge entry specialists review every encounter — capturing all services rendered and entering them correctly the first time.',
     ['Same-day charge entry from superbills and encounter notes','Diagnosis-to-procedure code linkage validation','Modifier review and application','Fee schedule verification and updates','Charge reconciliation — visits vs. charges','Missing charge identification and follow-up','High-volume batch charge entry for large practices'],
     'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=900&q=80&fit=crop'),
    ('healthcare-staffing', 'Healthcare Staffing Solutions',
     'Qualified medical billing and coding professionals for your practice.',
     'Finding and retaining qualified medical billing and coding professionals is one of the biggest challenges facing healthcare practices today. ZettaRCM\'s healthcare staffing solutions connect your practice with pre-vetted, experienced billing specialists — whether you need a single coder or an entire billing department.',
     ['AAPC-certified medical coders for all specialties','Experienced medical billing specialists','Credentialing coordinators and enrollment specialists','Denial management and A/R analysts','Front office and eligibility verification staff','Temporary, contract, and permanent placement options','Remote and on-site staffing solutions'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
]

for slug, title, subtitle, intro, points, img in missing_services:
    bc = f' <span class="mx-2">/</span> <a href="/services/" class="hover:text-brand-teal">Services</a> <span class="mx-2">/</span> {title}'
    bullet_html = ''.join(f'<div class="flex gap-3 py-3 border-b border-slate-100 last:border-0"><svg class="w-5 h-5 fill-brand-teal shrink-0 mt-0.5" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg><span class="text-[14px] text-slate-600">{p}</span></div>' for p in points)
    content = f'''
{TOPBAR}
{header()}
{banner(title, bc, subtitle)}
<section class="py-16 px-6 bg-white">
  <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-12">
    <div class="lg:col-span-2 space-y-8">
      <img src="{img}" alt="{title}" class="w-full h-64 object-cover">
      <p class="text-[15px] text-slate-600 leading-relaxed font-light">{intro}</p>
      <div class="bg-light-bg border border-slate-200 p-7">
        <h3 class="text-brand-navy font-bold text-[18px] mb-4">What We Provide</h3>
        <div class="divide-y divide-slate-100">{bullet_html}</div>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div class="bg-brand-navy p-6 text-center"><div class="text-3xl font-bold text-brand-teal">99.2%</div><div class="text-[11px] text-slate-400 uppercase tracking-wider mt-1">First-Pass Rate</div></div>
        <div class="bg-brand-navy p-6 text-center"><div class="text-3xl font-bold text-white">+30%</div><div class="text-[11px] text-slate-400 uppercase tracking-wider mt-1">Revenue Increase</div></div>
        <div class="bg-brand-navy p-6 text-center"><div class="text-3xl font-bold text-brand-teal">24/7</div><div class="text-[11px] text-slate-400 uppercase tracking-wider mt-1">Support Available</div></div>
      </div>
    </div>
    <div>{SIDEBAR_QUOTE}</div>
  </div>
</section>
{CTA}
{FOOTER}'''
    write(f'{B}/services/{slug}/index.html', head(title) + content)

# ─── DOMAIN AREA PAGES ────────────────────────────────────────────────────────
domain_pages = [
    ('revenue-partners', 'Revenue Partners', 'Strategic billing partnerships for hospitals, health systems, and large group practices.'),
    ('premier-billing-state', 'Premier Billing State', 'ZettaRCM\'s flagship markets — New York, New Jersey, Florida, Texas, and California.'),
    ('pioneer-states-hub', 'Pioneer States Hub', 'Expanding coverage across underserved healthcare markets in emerging states.'),
    ('city-zones', 'City Zones', 'Local expertise for major metropolitan healthcare markets across the country.'),
]

city_data = {
    'revenue-partners': {
        'subtitle': 'ZettaRCM partners with hospitals, health systems, physician networks, and large multi-specialty groups to deliver enterprise-level RCM solutions.',
        'intro': 'Healthcare organizations of all sizes trust ZettaRCM as their Revenue Cycle Management partner. From solo practices to large hospital systems, we tailor our services to match the complexity and volume of each partner. Our Revenue Partners program offers dedicated support teams, custom reporting, and performance guarantees for qualifying organizations.',
        'features': [
            ('Hospital & Health System Billing', 'Full-service RCM for hospital outpatient departments, professional billing, and facility billing across all service lines.', 'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 3c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm7 13H5v-.23c0-.62.28-1.2.76-1.58C7.47 15.82 9.64 15 12 15s4.53.82 6.24 2.19c.48.38.76.97.76 1.58V19z'),
            ('Physician Group Partnerships', 'Dedicated account teams for multi-provider groups with 10+ physicians, offering economies of scale and customized reporting.', 'M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z'),
            ('ACO & Value-Based Care', 'Specialized billing and quality reporting for Accountable Care Organizations and value-based care arrangements.', 'M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z'),
            ('MSO & Management Services', 'Revenue cycle outsourcing for Management Services Organizations supporting independent physician practices.', 'M20 6h-2.18c.07-.44.18-.88.18-1.36C18 2.08 15.86 0 13.27 0c-1.43 0-2.67.6-3.55 1.56L9 3.12l-.72-1.56C7.39.6 6.15 0 4.73 0 2.14 0 0 2.08 0 4.64c0 .48.11.92.18 1.36H0v14h20V6zm-8.83 12H4V8h7.17v10zm8.83 0h-7.17V8H20v10z'),
        ],
        'img': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop',
    },
    'premier-billing-state': {
        'subtitle': 'Specialized billing expertise in ZettaRCM\'s flagship markets — New York, New Jersey, Florida, Texas, and California.',
        'intro': 'ZettaRCM\'s Premier Billing States are our core markets where we have the deepest payer relationships, the most experienced local billing teams, and the strongest track records. In these states, we know every major commercial payer\'s quirks, every Medicaid program\'s requirements, and every workers\' compensation rule — giving your practice a decisive advantage.',
        'features': [
            ('New York', 'Expert billing for NY Medicaid, Empire BlueCross, Healthfirst, MetroPlus, EmblemHealth, and all NYC-area payers. No-fault and workers\' comp specialists.', 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z'),
            ('New Jersey', 'Deep expertise with Horizon BCBS, Aetna Better Health NJ, NJ FamilyCare, and all Garden State payers. Workers\' comp billing specialists.', 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z'),
            ('Florida', 'Specialists in Florida Medicaid, Sunshine Health, Simply Healthcare, and all major Florida Blue plans across South, Central, and North Florida.', 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z'),
            ('Texas', 'Expert billing for Texas Medicaid CHIP, STAR+PLUS, Community First Health Plans, and all major Texas commercial payers.', 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z'),
        ],
        'img': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=900&q=80&fit=crop',
    },
    'pioneer-states-hub': {
        'subtitle': 'ZettaRCM is actively expanding into new healthcare markets across underserved regions of the United States.',
        'intro': 'As healthcare delivery evolves, ZettaRCM is expanding its footprint into emerging markets where quality revenue cycle management expertise has historically been hard to find. Our Pioneer States Hub program brings ZettaRCM\'s full suite of RCM services — with dedicated local account managers — to practices in fast-growing healthcare markets.',
        'features': [
            ('Midwest Expansion', 'Dedicated billing teams for practices in Illinois, Ohio, Michigan, Indiana, and Wisconsin — with deep Medicaid and Blue Cross expertise.', 'M20.5 3l-.16.03L15 5.1 9 3 3.36 4.9c-.21.07-.36.25-.36.48V20.5c0 .28.22.5.5.5l.16-.03L9 18.9l6 2.1 5.64-1.9c.21-.07.36-.25.36-.48V3.5c0-.28-.22-.5-.5-.5z'),
            ('Southeast Growth', 'Expanding coverage in Georgia, North Carolina, South Carolina, Tennessee, and Alabama with specialized Medicaid billing expertise.', 'M20.5 3l-.16.03L15 5.1 9 3 3.36 4.9c-.21.07-.36.25-.36.48V20.5c0 .28.22.5.5.5l.16-.03L9 18.9l6 2.1 5.64-1.9c.21-.07.36-.25.36-.48V3.5c0-.28-.22-.5-.5-.5z'),
            ('Southwest Markets', 'Growing presence in Arizona, Colorado, Nevada, and Utah — with expertise in Medicaid expansion programs and managed care billing.', 'M20.5 3l-.16.03L15 5.1 9 3 3.36 4.9c-.21.07-.36.25-.36.48V20.5c0 .28.22.5.5.5l.16-.03L9 18.9l6 2.1 5.64-1.9c.21-.07.36-.25.36-.48V3.5c0-.28-.22-.5-.5-.5z'),
            ('Pacific Northwest', 'Building expertise in Washington, Oregon, and Idaho — serving practices navigating the region\'s unique managed care landscape.', 'M20.5 3l-.16.03L15 5.1 9 3 3.36 4.9c-.21.07-.36.25-.36.48V20.5c0 .28.22.5.5.5l.16-.03L9 18.9l6 2.1 5.64-1.9c.21-.07.36-.25.36-.48V3.5c0-.28-.22-.5-.5-.5z'),
        ],
        'img': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop',
    },
    'city-zones': {
        'subtitle': 'Local medical billing expertise in major metropolitan healthcare markets from New York to Los Angeles.',
        'intro': 'ZettaRCM operates dedicated City Zone teams in the nation\'s largest healthcare markets. Each city zone has specialists who understand the local payer mix, hospital systems, and regulatory environment — giving your practice a competitive edge in collections. Our city teams are embedded in local healthcare communities and maintain relationships with local payer representatives.',
        'features': [
            ('New York City Metro', 'Serving Manhattan, Brooklyn, Queens, Bronx, Staten Island, Long Island, and Northern New Jersey. Specialists in all NYC-area payers, Medicaid, and no-fault billing.', 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z'),
            ('Miami-Fort Lauderdale', 'South Florida specialists serving Dade, Broward, and Palm Beach counties. Expertise in Spanish-speaking patient populations, Florida Medicaid, and South Florida commercial payers.', 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z'),
            ('Dallas-Houston', 'Texas medical billing specialists across DFW, Houston, San Antonio, and Austin. Deep expertise in Texas Medicaid STAR programs and Texas workers\' compensation.', 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z'),
            ('Los Angeles & Chicago', 'West Coast and Midwest specialists for LA County, the South Bay, Chicagoland, and surrounding metro areas. Experts in California Medi-Cal and Illinois Medicaid billing.', 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z'),
        ],
        'img': 'https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=900&q=80&fit=crop',
    },
}

os.makedirs(f'{B}/domain-areas', exist_ok=True)
for slug, title, subtitle in domain_pages:
    d = city_data[slug]
    bc = f' <span class="mx-2">/</span> Domain Areas <span class="mx-2">/</span> {title}'
    feat_cards = ''.join(f'''<div class="bg-white border border-slate-200 p-7 hover:border-brand-teal hover:shadow-md transition-all">
      <div class="w-12 h-12 bg-brand-navy flex items-center justify-center mb-4"><svg class="w-6 h-6 fill-brand-teal" viewBox="0 0 24 24"><path d="{icon}"/></svg></div>
      <h3 class="text-brand-navy font-bold text-[16px] mb-2">{name}</h3>
      <p class="text-[13px] text-slate-500 font-light leading-relaxed">{desc}</p>
    </div>''' for name,desc,icon in d['features'])
    content = f'''
{TOPBAR}
{header()}
{banner(title, bc, d['subtitle'])}
<section class="py-16 px-6 bg-white">
  <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-12">
    <div class="lg:col-span-2 space-y-8">
      <img src="{d['img']}" alt="{title}" class="w-full h-64 object-cover">
      <p class="text-[15px] text-slate-600 leading-relaxed font-light">{d['intro']}</p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-5">{feat_cards}</div>
      <div class="bg-brand-navy p-8 flex flex-col md:flex-row items-center gap-6">
        <div><div class="text-brand-teal font-bold text-[17px]">Ready to Partner with ZettaRCM?</div><div class="text-slate-400 text-[13px] mt-1 font-light">Contact us to discuss how we can serve your practice in this market.</div></div>
        <a href="/contact/" class="shrink-0 bg-brand-teal text-brand-navy font-bold text-[12px] uppercase tracking-wider px-7 py-3.5 hover:bg-white transition-all">Get In Touch</a>
      </div>
    </div>
    <div>{SIDEBAR_QUOTE}</div>
  </div>
</section>
{CTA}
{FOOTER}'''
    write(f'{B}/domain-areas/{slug}/index.html', head(title) + content)

# ─── DOMAIN AREAS INDEX ───────────────────────────────────────────────────────
da_cards = ''.join(f'''<a href="/domain-areas/{s}/" class="group bg-white border border-slate-200 p-8 hover:border-brand-teal hover:shadow-md transition-all">
  <h3 class="text-brand-navy font-bold text-[18px] group-hover:text-brand-teal transition-colors mb-2">{t}</h3>
  <p class="text-[13px] text-slate-500 font-light leading-relaxed">{sub}</p>
  <span class="mt-4 inline-flex items-center gap-1 text-brand-teal text-[12px] font-bold uppercase tracking-wider">Explore <svg class="w-3 h-3 fill-current" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg></span>
</a>''' for s,t,sub in domain_pages)
content = f'''
{TOPBAR}
{header()}
{banner('Domain Areas', ' <span class="mx-2">/</span> Domain Areas', 'ZettaRCM\'s market coverage — from flagship premier states to pioneer expansion zones and city-specific teams.')}
<section class="py-16 px-6 bg-slate-50">
  <div class="max-w-7xl mx-auto">
    <div class="text-center max-w-2xl mx-auto mb-12"><p class="text-[15px] text-slate-600 font-light leading-relaxed">ZettaRCM serves healthcare providers nationwide, with concentrated expertise in specific markets. Our domain area specialists bring local payer knowledge and regulatory expertise to every engagement.</p></div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5">{da_cards}</div>
  </div>
</section>
{CTA}
{FOOTER}'''
write(f'{B}/domain-areas/index.html', head('Domain Areas') + content)

# ─── RESOURCES LANDING ────────────────────────────────────────────────────────
res_cards = [
    ('/resources/blog/', 'Blog', 'Billing insights, coding updates, and revenue cycle best practices from our experts.', 'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z'),
    ('/resources/rcm-library/', 'RCM Library', 'Free guides, checklists, templates, and reports to improve your revenue cycle.', 'M20 2H8c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-8.5 7.5c0 .83-.67 1.5-1.5 1.5H9v2H7.5V7H10c.83 0 1.5.67 1.5 1.5v1zm5 2c0 .83-.67 1.5-1.5 1.5h-2.5V7H15c.83 0 1.5.67 1.5 1.5v3zm4-3H19v1h1.5V11H19v2h-1.5V7h3v1.5zM9 9.5h1v-1H9v1zM4 6H2v14c0 1.1.9 2 2 2h14v-2H4V6zm10 5.5h1v-3h-1v3z'),
    ('/resources/case-studies/', 'Case Studies', 'Real revenue results from practices that partnered with ZettaRCM.', 'M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6h-6z'),
    ('/resources/newsroom/', 'Newsroom', 'Latest announcements, press releases, and company news from ZettaRCM.', 'M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 14H4V8l8 5 8-5v10zm-8-7L4 6h16l-8 5z'),
    ('/resources/faqs/', 'FAQs', 'Answers to the most common questions about medical billing and our services.', 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z'),
    ('/resources/provider-form/', 'Provider Form', 'Get started with ZettaRCM — submit your practice information for a custom proposal.', 'M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V8l-6-6zm4 18H6V4h7v5h5v11zM8 15.01l1.41 1.41L11 14.84V19h2v-4.16l1.59 1.59L16 15.01 12.01 11 8 15.01z'),
    ('/resources/insurance-partners/', 'Insurance Partners', 'View all payers and insurance companies we work with across the country.', 'M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z'),
]
rc = ''.join(f'''<a href="{url}" class="group bg-white border border-slate-200 p-7 hover:border-brand-teal hover:shadow-md transition-all flex flex-col gap-4">
  <div class="w-13 h-13 w-14 h-14 bg-brand-navy flex items-center justify-center"><svg class="w-7 h-7 fill-brand-teal" viewBox="0 0 24 24"><path d="{icon}"/></svg></div>
  <div><h3 class="text-brand-navy font-bold text-[17px] group-hover:text-brand-teal transition-colors">{name}</h3><p class="text-[13px] text-slate-500 font-light mt-2 leading-relaxed">{desc}</p></div>
  <span class="text-brand-teal text-[12px] font-bold uppercase tracking-wider mt-auto flex items-center gap-1">Explore <svg class="w-3 h-3 fill-current" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg></span>
</a>''' for url,name,desc,icon in res_cards)
content = f'''
{TOPBAR}
{header()}
{banner('Resources', ' <span class="mx-2">/</span> Resources', 'Guides, tools, and insights to help your practice maximize revenue and stay compliant.')}
<section class="py-16 px-6 bg-slate-50">
  <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">{rc}</div>
</section>
{CTA}
{FOOTER}'''
write(f'{B}/resources/index.html', head('Resources') + content)

# ─── MAKE A PAYMENT ───────────────────────────────────────────────────────────
content = f'''
{TOPBAR}
{header()}
{banner('Make A Payment', ' <span class="mx-2">/</span> Make A Payment', 'Securely submit your payment to ZettaRCM online or by phone.')}
<section class="py-16 px-6 bg-slate-50">
  <div class="max-w-3xl mx-auto space-y-6">
    <div class="bg-white border border-slate-200 p-8 text-center space-y-4">
      <div class="w-16 h-16 bg-brand-navy flex items-center justify-center mx-auto"><svg class="w-8 h-8 fill-brand-teal" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z"/></svg></div>
      <h2 class="text-brand-navy font-bold text-[22px]">Secure Online Payment</h2>
      <p class="text-slate-500 text-[14px] font-light leading-relaxed max-w-lg mx-auto">To make a payment, please contact our billing department. We accept all major credit cards, ACH bank transfers, and checks. Our team will send you a secure payment link.</p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center pt-2">
        <a href="tel:+18005160192" class="bg-brand-navy text-white font-bold text-[13px] uppercase tracking-wider px-8 py-4 hover:bg-brand-teal hover:text-brand-navy transition-all">(800) 516-0192 — Call to Pay</a>
        <a href="mailto:billing@zettarcm.com" class="border border-brand-navy text-brand-navy font-bold text-[13px] uppercase tracking-wider px-8 py-4 hover:bg-brand-navy hover:text-white transition-all">billing@zettarcm.com</a>
      </div>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
      <div class="bg-white border border-slate-200 p-5 text-center"><svg class="w-8 h-8 fill-brand-teal mx-auto mb-3" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z"/></svg><div class="text-brand-navy font-bold text-[14px]">Credit / Debit Card</div><div class="text-slate-500 text-[12px] mt-1">Visa, Mastercard, Amex, Discover</div></div>
      <div class="bg-white border border-slate-200 p-5 text-center"><svg class="w-8 h-8 fill-brand-teal mx-auto mb-3" viewBox="0 0 24 24"><path d="M4 10v7h3v-7H4zm6 0v7h3v-7h-3zm-5 9h13v3H5v-3zm11-9v7h3v-7h-3zm-6-9L2 6v2h20V6L12 1z"/></svg><div class="text-brand-navy font-bold text-[14px]">ACH Bank Transfer</div><div class="text-slate-500 text-[12px] mt-1">Direct bank-to-bank transfer</div></div>
      <div class="bg-white border border-slate-200 p-5 text-center"><svg class="w-8 h-8 fill-brand-teal mx-auto mb-3" viewBox="0 0 24 24"><path d="M21.99 8c0-.72-.37-1.35-.94-1.7L12 1 2.95 6.3C2.38 6.65 2 7.28 2 8v10c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2l-.01-10zM12 13L3.74 7.84 12 3l8.26 4.84L12 13z"/></svg><div class="text-brand-navy font-bold text-[14px]">Check / Money Order</div><div class="text-slate-500 text-[12px] mt-1">Mail to our Brooklyn office</div></div>
    </div>
    <div class="bg-brand-navy p-6 text-center"><div class="text-brand-teal font-bold mb-1">Mailing Address for Checks</div><div class="text-white text-[14px]">ZettaRCM, Inc. &nbsp;·&nbsp; 134 N 4th St, Brooklyn, NY 11249</div></div>
  </div>
</section>
{FOOTER}'''
write(f'{B}/make-a-payment/index.html', head('Make A Payment') + content)

# ─── INDIVIDUAL BLOG POSTS ────────────────────────────────────────────────────
os.makedirs(f'{B}/resources/blog', exist_ok=True)

blog_posts = [
    ('understanding-patient-billing-statements', 'Understanding Patient Billing Statements: A Guide for Healthcare Providers', 'Medical Billing', 'June 15, 2026',
     'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=900&q=80&fit=crop',
     'Patient billing statements are one of the most overlooked opportunities in the revenue cycle. When patients cannot understand what they owe and why, they delay payment — or don\'t pay at all. Clear, professional billing statements are proven to improve patient pay collections by 20–35%.',
     [('Why Clarity Matters in Patient Billing', 'Studies show that 70% of patients say they would pay their medical bills faster if they understood the statement better. Yet most practices still send dense, confusing statements that list procedure codes without explanation, show insurance adjustments without context, and provide no convenient payment options. The result: aging patient balances, bad debt write-offs, and frustrated patients.'),
      ('The Anatomy of an Effective Patient Statement', 'An effective patient statement should include: the provider\'s name and contact information prominently displayed; the patient\'s name, date of service, and account number; a plain-language description of services rendered (not just CPT codes); the original charge, insurance payment, contractual adjustment, and patient responsibility — clearly labeled; and multiple payment options including online, phone, and mail.'),
      ('Digital Statements Improve Collection Rates', 'Practices that send digital statements via email or patient portal see collection rates 25–40% higher than those relying on paper-only statements. Digital statements allow patients to click directly to a payment portal, review their account history, and set up payment plans — all without picking up the phone. ZettaRCM\'s patient billing services include both paper and digital statement options.'),
      ('Payment Plans Reduce Bad Debt', 'Offering payment plans for balances over $100 dramatically reduces bad debt write-offs. When patients can spread payments over 3–12 months, they are far more likely to pay in full. ZettaRCM sets up and manages payment plans on your behalf, sending automated reminders and processing payments without requiring staff time.'),
     ]),
    ('top-5-denial-management-strategies-2026', 'Top 5 Denial Management Strategies for 2026', 'Denial Management', 'June 10, 2026',
     'https://images.unsplash.com/photo-1504813184591-01572f98c85f?w=900&q=80&fit=crop',
     'The average medical practice loses 15–20% of potential revenue to claim denials — and recovers less than half of denied claims. In 2026, with payers becoming increasingly aggressive about finding reasons to deny, a proactive denial management strategy is not optional. Here are the five most effective approaches.',
     [('1. Prevent Denials Before They Happen', 'The most effective denial management strategy is prevention. This means verifying insurance eligibility before every patient visit, checking authorization requirements proactively, applying the correct modifiers, and using payer-specific rules in your billing system. Practices with strong front-end processes have denial rates under 3% — versus the industry average of 12–15%.'),
      ('2. Track and Categorize Every Denial', 'You cannot fix what you do not measure. Categorize every denial by reason code, payer, provider, and service type. Most practices find that 20% of denial root causes account for 80% of denied revenue — and those top causes are usually fixable with simple process changes. ZettaRCM provides monthly denial trend reports that highlight exactly where your revenue is leaking.'),
      ('3. Appeal Quickly and Persistently', 'Payers count on providers giving up on denied claims. Don\'t. Most payers must be appealed within 60–180 days of the denial date — and most appeals, when filed correctly with supporting documentation, are overturned. ZettaRCM files appeals within 72 hours of receiving a denial and tracks every appeal through to resolution.'),
      ('4. Leverage Peer-to-Peer Reviews', 'For clinical denials — especially medical necessity and prior authorization denials — a peer-to-peer review between your physician and the payer\'s medical director can be remarkably effective. When a ZettaRCM appeals specialist identifies a case likely to benefit from P2P review, we facilitate the scheduling and prepare your physician with the supporting clinical documentation.'),
      ('5. Fix Root Causes Systemically', 'When the same denial reason appears more than five times in a month, it is a systemic problem — not a random occurrence. ZettaRCM\'s denial management team identifies recurring patterns and works with your practice to fix the underlying cause: whether it is a documentation issue, an authorization gap, a coding error, or a payer-specific rule your team was not aware of.'),
     ]),
    ('2026-cpt-code-updates', '2026 CPT Code Updates: What Your Practice Must Know', 'Medical Coding', 'June 5, 2026',
     'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=900&q=80&fit=crop',
     'The AMA releases CPT code updates annually, effective January 1. For 2026, there are 270 code changes including 230 new codes, 49 revised codes, and 65 deleted codes. Understanding which changes affect your specialty is critical — using a deleted code or missing a new code can result in denials or significant underpayments.',
     [('Major Changes for Evaluation & Management', 'The 2026 CPT update includes revised E&M guidelines for split/shared visits, telehealth services, and prolonged services. The new guidelines allow more flexibility in how time is counted for E&M code selection, potentially increasing code levels for many visits. However, documentation must explicitly support the new criteria — check your templates.'),
      ('New Codes for Digital Health Services', 'In response to the continued growth of digital health, 2026 introduces 18 new CPT codes for remote patient monitoring, virtual care management, and asynchronous telehealth services. Practices offering RPM programs should ensure they are capturing all newly payable services — many practices leave $50,000+ annually on the table by not billing RPM codes properly.'),
      ('Surgery and Procedure Code Changes', 'Orthopedic, spine, and cardiovascular surgery codes see significant changes in 2026. Several bundled procedures have been unbundled into separately reportable codes, while some previously separate codes have been combined. Your coding team should audit claims for these specialties in the first quarter to identify any pattern changes needed.'),
      ('How to Prepare Your Practice', 'To prepare for 2026 CPT changes: update your EMR charge capture templates; train all providers and coding staff on relevant changes; audit your top 20 procedure codes for any that were deleted or revised; and review your payer fee schedules to ensure new codes have been priced. ZettaRCM handles all CPT update implementation for our billing clients automatically.'),
     ]),
]

for slug, title, cat, date, img, intro, sections in blog_posts:
    bc = f' <span class="mx-2">/</span> <a href="/resources/blog/" class="hover:text-brand-teal">Blog</a> <span class="mx-2">/</span> {cat}'
    section_html = ''.join(f'<div class="space-y-2"><h3 class="text-brand-navy font-bold text-[18px]">{h}</h3><p class="text-[14px] text-slate-600 leading-relaxed font-light">{b}</p></div>' for h,b in sections)
    content = f'''
{TOPBAR}
{header()}
{banner(title, bc, f'{cat} · {date}')}
<section class="py-16 px-6 bg-white">
  <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-12">
    <div class="lg:col-span-2 space-y-8">
      <img src="{img}" alt="{title}" class="w-full h-72 object-cover">
      <div class="flex items-center gap-4 pb-4 border-b border-slate-100">
        <span class="bg-brand-navy text-brand-teal text-[11px] font-bold uppercase tracking-wider px-3 py-1">{cat}</span>
        <span class="text-[13px] text-slate-400">{date}</span>
      </div>
      <p class="text-[15px] text-slate-600 leading-relaxed font-light">{intro}</p>
      <div class="space-y-8">{section_html}</div>
      <div class="bg-light-bg border border-slate-200 p-7 mt-8">
        <h3 class="text-brand-navy font-bold text-[17px] mb-2">Need Help with Your Revenue Cycle?</h3>
        <p class="text-[13px] text-slate-600 font-light mb-4">ZettaRCM\'s billing experts are available to answer your questions and provide a free practice audit.</p>
        <div class="flex flex-wrap gap-3">
          <a href="/contact/" class="bg-brand-navy text-white font-bold text-[12px] uppercase tracking-wider px-6 py-3 hover:bg-brand-teal hover:text-brand-navy transition-all">Contact Us</a>
          <a href="tel:+18005160192" class="border border-brand-navy text-brand-navy font-bold text-[12px] uppercase tracking-wider px-6 py-3 hover:bg-brand-navy hover:text-white transition-all">(800) 516-0192</a>
        </div>
      </div>
    </div>
    <div class="space-y-5">
      {SIDEBAR_QUOTE}
      <div class="bg-white border border-slate-200 p-5">
        <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-3">Recent Posts</div>
        <ul class="space-y-3">
          <li><a href="/resources/blog/top-5-denial-management-strategies-2026/" class="text-[13px] text-slate-700 hover:text-brand-teal transition-colors leading-snug block">Top 5 Denial Management Strategies for 2026</a></li>
          <li><a href="/resources/blog/2026-cpt-code-updates/" class="text-[13px] text-slate-700 hover:text-brand-teal transition-colors leading-snug block">2026 CPT Code Updates: What Your Practice Must Know</a></li>
          <li><a href="/resources/blog/understanding-patient-billing-statements/" class="text-[13px] text-slate-700 hover:text-brand-teal transition-colors leading-snug block">Understanding Patient Billing Statements</a></li>
        </ul>
        <a href="/resources/blog/" class="inline-block mt-3 text-brand-teal text-[12px] font-bold uppercase tracking-wider">All Posts →</a>
      </div>
    </div>
  </div>
</section>
{CTA}
{FOOTER}'''
    write(f'{B}/resources/blog/{slug}/index.html', head(title) + content)

print('\n✅ All missing pages generated!')
print('Pages created:')
print('  - 5 missing service pages (practice management, telemedicine, EHR, charge entry, staffing)')
print('  - 4 domain area pages + domain areas index')
print('  - Resources landing page')
print('  - Make A Payment page')
print('  - 3 individual blog posts')
