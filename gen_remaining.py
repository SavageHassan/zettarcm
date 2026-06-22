#!/usr/bin/env python3
"""Generate all remaining ZettaRCM pages with consistent design."""
import os

def write(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(html)
    print(f'✓ {path}')

# ─── SHARED PARTS ─────────────────────────────────────────────────────────────

def head(title, desc='ZettaRCM — Medical Billing & Revenue Cycle Management New York'):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | ZettaRCM</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/@tailwindcss/browser@4"></script>
  <style type="text/tailwindcss">
    @theme {{--color-brand-navy:#1B3A6B;--color-brand-teal:#00B8D4;--color-light-bg:#F5F8FF;}}
    *{{font-family:'Inter',sans-serif;box-sizing:border-box;}}
    .dd:hover>.dm{{display:block;}}.dm{{display:none;}}
    details>summary{{list-style:none;}}.faq-open .faq-icon{{transform:rotate(45deg);}}
    .faq-icon{{transition:transform .25s;display:inline-block;}}
  </style>
</head>
<body class="bg-white text-slate-800">'''

TOPBAR = '''<div class="w-full bg-brand-navy text-[12px] text-slate-300 py-2.5 px-4">
  <div class="max-w-7xl mx-auto flex flex-wrap justify-between items-center gap-2">
    <div class="flex flex-wrap gap-5 items-center">
      <a href="tel:+18005160192" class="hover:text-white flex items-center gap-1.5"><svg class="w-3 h-3 fill-brand-teal" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>(800) 516-0192</a>
      <a href="tel:+17183030192" class="hover:text-white flex items-center gap-1.5"><svg class="w-3 h-3 fill-brand-teal" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>(718) 303-0192</a>
      <a href="mailto:info@zettarcm.com" class="hover:text-white flex items-center gap-1.5"><svg class="w-3 h-3 fill-brand-teal" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>info@zettarcm.com</a>
    </div>
    <div class="flex items-center gap-4">
      <a href="/#quote" class="text-brand-teal hover:text-white font-medium">Free Practice Audit</a>
      <span class="text-slate-600">|</span>
      <span class="flex items-center gap-1.5"><span class="w-1.5 h-1.5 bg-green-400 rounded-full"></span>HIPAA Secure</span>
    </div>
  </div>
</div>'''

def header(active=''):
    links = [
        ('/', 'Home'),
        ('', 'Why ZettaRCM', [('/our-company/','Our Company'),('/nationwide-medical-billing/','Nationwide Medical Billing')]),
        ('', 'Services', [('/services/medical-billing/','Medical Billing'),('/services/medical-credentialing/','Medical Credentialing'),('/services/medical-coding/','Medical Coding'),('/services/denial-management/','Denial Management'),('/services/ar-follow-up/','A/R Follow Up'),('/services/revenue-cycle-management/','Revenue Cycle Management'),('/services/prior-authorization/','Prior Authorization'),('/services/out-of-network-billing/','Out of Network Billing'),('/services/front-office-management/','Front Office Management'),('/services/quality-payment-program/','Quality Payment Program'),('/services/eligibility-verification/','Eligibility Verification'),('/services/patient-billing/','Patient Billing'),('/services/payment-posting/','Payment Posting'),('|',''),('/services/','View All Services →')]),
        ('', 'Specialties', [('/specialties/mental-health/','Mental Health'),('/specialties/cardiology/','Cardiology'),('/specialties/radiology/','Radiology'),('/specialties/orthopedics/','Orthopedics'),('/specialties/oncology/','Oncology'),('/specialties/neurology/','Neurology'),('/specialties/dermatology/','Dermatology'),('/specialties/pain-management/','Pain Management'),('|',''),('/specialties/','All 35 Specialties →')]),
        ('', 'Domain Areas', [('#','Revenue Partners'),('#','Premier Billing State'),('#','Pioneer States Hub'),('#','City Zones')]),
        ('', 'Resources', [('/resources/blog/','Blog'),('/resources/rcm-library/','RCM Library'),('/resources/newsroom/','Newsroom'),('/resources/case-studies/','Case Studies'),('/resources/faqs/','FAQs'),('/resources/provider-form/','Provider Form'),('|',''),('/resources/insurance-partners/','Insurance Partners')]),
        ('/contact/', 'Contact Us'),
    ]
    nav_html = ''
    for item in links:
        if len(item) == 2:
            href, label = item
            is_active = 'text-brand-teal border-b-2 border-brand-teal' if active == href else 'border-b-2 border-transparent hover:border-brand-teal hover:text-brand-teal'
            nav_html += f'<a href="{href}" class="px-4 h-full flex items-center {is_active} transition-colors">{label}</a>'
        else:
            _, label, children = item
            is_active_parent = 'text-brand-teal border-b-2 border-brand-teal' if any(active == c[0] for c in children if c[0] != '|') else 'border-b-2 border-transparent hover:border-brand-teal hover:text-brand-teal'
            child_html = ''
            for c in children:
                if c[0] == '|':
                    child_html += '<div class="mx-4 my-1 border-t border-slate-100"></div>'
                elif c[1].endswith('→'):
                    child_html += f'<a href="{c[0]}" class="block px-5 py-3 text-[13px] text-brand-teal font-semibold hover:bg-light-bg">{c[1]}</a>'
                else:
                    child_html += f'<a href="{c[0]}" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal border-l-2 border-transparent hover:border-brand-teal transition-all">{c[1]}</a>'
            nav_html += f'''<div class="dd relative h-full flex items-center">
          <button class="px-4 h-full flex items-center gap-1 {is_active_parent} cursor-pointer transition-colors">{label} <svg class="w-3 h-3 fill-current opacity-60" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></button>
          <div class="dm absolute top-full left-0 bg-white border border-slate-200 shadow-xl z-50 py-1 min-w-[230px]">{child_html}</div>
        </div>'''
    return f'''<header class="w-full bg-white border-b border-slate-200 sticky top-0 z-50 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 flex items-center justify-between h-[72px]">
    <a href="/" class="flex items-center gap-3 shrink-0">
      <svg width="44" height="44" viewBox="0 0 44 44" fill="none"><rect width="44" height="44" rx="4" fill="#1B3A6B"/><path d="M8 28 Q13 18 18 22 Q23 26 28 16 Q33 6 38 16" stroke="#00B8D4" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M8 32 Q13 22 18 26 Q23 30 28 20 Q33 10 38 20" stroke="white" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.5"/></svg>
      <div><div class="text-[22px] font-bold text-brand-navy leading-none tracking-tight">Zetta<span class="text-brand-teal">RCM</span></div><div class="text-[9px] tracking-[0.22em] text-slate-400 uppercase font-medium mt-0.5">Revenue Cycle Management</div></div>
    </a>
    <nav class="hidden lg:flex items-center h-full text-[13.5px] font-medium text-brand-navy">{nav_html}</nav>
    <button class="hidden lg:flex items-center justify-center w-11 h-11 bg-brand-navy hover:bg-brand-teal transition-colors shrink-0">
      <svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
    </button>
  </div>
</header>'''

def banner(title, breadcrumb_extra, subtitle):
    return f'''<section class="bg-brand-navy py-14 px-6">
  <div class="max-w-7xl mx-auto">
    <div class="text-[11px] text-slate-400 uppercase tracking-wider mb-3"><a href="/" class="hover:text-brand-teal">Home</a>{breadcrumb_extra}</div>
    <h1 class="text-3xl md:text-[42px] font-bold text-white leading-tight">{title}</h1>
    <p class="text-[15px] text-slate-400 mt-3 font-light max-w-2xl">{subtitle}</p>
  </div>
</section>'''

CTA = '''<section class="bg-brand-teal py-12 px-6">
  <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6">
    <div>
      <h3 class="text-brand-navy font-bold text-2xl">Ready to Maximize Your Practice Revenue?</h3>
      <p class="text-brand-navy/70 text-[14px] mt-1">Get a free practice audit — no obligation, no contracts.</p>
    </div>
    <div class="flex gap-3 shrink-0">
      <a href="/#quote" class="bg-brand-navy text-white font-bold text-[13px] uppercase tracking-wider px-8 py-4 hover:bg-white hover:text-brand-navy transition-all">Free Audit</a>
      <a href="tel:+18005160192" class="border-2 border-brand-navy text-brand-navy font-bold text-[13px] uppercase tracking-wider px-6 py-4 hover:bg-brand-navy hover:text-white transition-all">(800) 516-0192</a>
    </div>
  </div>
</section>'''

FOOTER = '''<footer class="bg-brand-navy pt-16 pb-8 px-6">
  <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
    <div class="space-y-4">
      <div><div class="text-white font-bold text-2xl">Zetta<span class="text-brand-teal">RCM</span></div><div class="text-[9px] text-slate-500 tracking-[0.25em] uppercase mt-0.5">Revenue Cycle Management</div></div>
      <p class="text-[13px] text-slate-400 leading-relaxed font-light">New York's premier Revenue Cycle Management company. Serving 35+ specialties nationwide.</p>
      <div class="space-y-1 text-[13px] text-slate-400">
        <div>134 N 4th St, Brooklyn, NY 11249</div>
        <div><a href="tel:+18005160192" class="hover:text-brand-teal">(800) 516-0192</a></div>
        <div><a href="mailto:info@zettarcm.com" class="hover:text-brand-teal">info@zettarcm.com</a></div>
      </div>
    </div>
    <div class="space-y-4">
      <div class="text-white font-bold text-[13px] uppercase tracking-wider border-b border-slate-700 pb-3">Our Services</div>
      <ul class="space-y-2 text-[13px] text-slate-400">
        <li><a href="/services/medical-billing/" class="hover:text-brand-teal">Medical Billing</a></li>
        <li><a href="/services/medical-credentialing/" class="hover:text-brand-teal">Medical Credentialing</a></li>
        <li><a href="/services/medical-coding/" class="hover:text-brand-teal">Medical Coding</a></li>
        <li><a href="/services/denial-management/" class="hover:text-brand-teal">Denial Management</a></li>
        <li><a href="/services/ar-follow-up/" class="hover:text-brand-teal">A/R Follow Up</a></li>
        <li><a href="/services/" class="text-brand-teal font-medium">View All Services →</a></li>
      </ul>
    </div>
    <div class="space-y-4">
      <div class="text-white font-bold text-[13px] uppercase tracking-wider border-b border-slate-700 pb-3">Specialties</div>
      <ul class="space-y-2 text-[13px] text-slate-400">
        <li><a href="/specialties/mental-health/" class="hover:text-brand-teal">Mental Health</a></li>
        <li><a href="/specialties/cardiology/" class="hover:text-brand-teal">Cardiology</a></li>
        <li><a href="/specialties/orthopedics/" class="hover:text-brand-teal">Orthopedics</a></li>
        <li><a href="/specialties/radiology/" class="hover:text-brand-teal">Radiology</a></li>
        <li><a href="/specialties/oncology/" class="hover:text-brand-teal">Oncology</a></li>
        <li><a href="/specialties/" class="text-brand-teal font-medium">All 35 Specialties →</a></li>
      </ul>
    </div>
    <div class="space-y-4">
      <div class="text-white font-bold text-[13px] uppercase tracking-wider border-b border-slate-700 pb-3">Company</div>
      <ul class="space-y-2 text-[13px] text-slate-400">
        <li><a href="/our-company/" class="hover:text-brand-teal">Our Company</a></li>
        <li><a href="/nationwide-medical-billing/" class="hover:text-brand-teal">Nationwide Billing</a></li>
        <li><a href="/resources/blog/" class="hover:text-brand-teal">Blog</a></li>
        <li><a href="/resources/faqs/" class="hover:text-brand-teal">FAQs</a></li>
        <li><a href="/contact/" class="hover:text-brand-teal">Contact Us</a></li>
        <li><a href="/privacy-policy/" class="hover:text-brand-teal">Privacy Policy</a></li>
        <li><a href="/terms-and-conditions/" class="hover:text-brand-teal">Terms & Conditions</a></li>
      </ul>
    </div>
  </div>
  <div class="max-w-7xl mx-auto pt-8 border-t border-slate-800 flex flex-col sm:flex-row justify-between items-center text-[12px] text-slate-600 gap-3">
    <span>© 2026, ZettaRCM, Inc. All Rights Reserved.</span>
    <div class="flex gap-5">
      <a href="/privacy-policy/" class="hover:text-slate-400">Privacy Policy</a>
      <a href="/terms-and-conditions/" class="hover:text-slate-400">Terms & Conditions</a>
      <a href="/contact/" class="hover:text-slate-400">Contact Us</a>
    </div>
  </div>
</footer>
</body>
</html>'''

SIDEBAR_QUOTE = '''<div class="space-y-5">
  <div class="bg-brand-navy p-6">
    <h4 class="text-white font-bold text-[15px] mb-4">Get A Free Quote</h4>
    <form class="space-y-3" onsubmit="event.preventDefault()">
      <input type="text" placeholder="Full Name *" class="w-full bg-white/10 border border-white/20 text-white text-[13px] px-3 py-2.5 outline-none focus:border-brand-teal placeholder-slate-400">
      <input type="email" placeholder="Email Address *" class="w-full bg-white/10 border border-white/20 text-white text-[13px] px-3 py-2.5 outline-none focus:border-brand-teal placeholder-slate-400">
      <input type="tel" placeholder="Phone Number *" class="w-full bg-white/10 border border-white/20 text-white text-[13px] px-3 py-2.5 outline-none focus:border-brand-teal placeholder-slate-400">
      <button type="submit" class="w-full bg-brand-teal text-brand-navy font-bold text-[12px] uppercase tracking-wider py-3 hover:bg-white transition-all cursor-pointer">Request Free Consultation</button>
    </form>
  </div>
  <div class="border border-slate-200 p-5">
    <h4 class="text-brand-navy font-bold text-[14px] mb-2">Speak to an Expert</h4>
    <a href="tel:+18005160192" class="flex items-center gap-2 text-brand-teal font-bold text-[16px]"><svg class="w-5 h-5 fill-brand-teal" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>(800) 516-0192</a>
    <p class="text-[12px] text-slate-400 mt-1">Available 24/7</p>
  </div>
  <div class="bg-light-bg border border-slate-200 p-5">
    <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-3">Quick Links</div>
    <ul class="space-y-2 text-[13px] text-slate-600">
      <li><a href="/services/" class="hover:text-brand-teal flex items-center gap-2"><svg class="w-3 h-3 fill-brand-teal" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>All Services</a></li>
      <li><a href="/specialties/" class="hover:text-brand-teal flex items-center gap-2"><svg class="w-3 h-3 fill-brand-teal" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>All Specialties</a></li>
      <li><a href="/resources/faqs/" class="hover:text-brand-teal flex items-center gap-2"><svg class="w-3 h-3 fill-brand-teal" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>FAQs</a></li>
      <li><a href="/contact/" class="hover:text-brand-teal flex items-center gap-2"><svg class="w-3 h-3 fill-brand-teal" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>Contact Us</a></li>
    </ul>
  </div>
</div>'''

def stat_row():
    return '''<div class="grid grid-cols-2 sm:grid-cols-4 gap-px bg-slate-200 my-8">
  <div class="bg-brand-navy p-7 text-center"><div class="text-3xl font-bold text-brand-teal">99.2%</div><div class="text-[11px] text-slate-400 uppercase tracking-wider mt-1">First-Pass Rate</div></div>
  <div class="bg-brand-navy p-7 text-center"><div class="text-3xl font-bold text-white">+30%</div><div class="text-[11px] text-slate-400 uppercase tracking-wider mt-1">Revenue Increase</div></div>
  <div class="bg-brand-navy p-7 text-center"><div class="text-3xl font-bold text-brand-teal">35+</div><div class="text-[11px] text-slate-400 uppercase tracking-wider mt-1">Specialties Served</div></div>
  <div class="bg-brand-navy p-7 text-center"><div class="text-3xl font-bold text-white">24/7</div><div class="text-[11px] text-slate-400 uppercase tracking-wider mt-1">Support Available</div></div>
</div>'''

B = '/Users/mac/zettarcm'

# ═══════════════════════════════════════════════════════════════════════════════
# OUR COMPANY
# ═══════════════════════════════════════════════════════════════════════════════
content = f'''
{TOPBAR}
{header('/our-company/')}
{banner('About ZettaRCM', ' <span class="mx-2">/</span> Our Company', 'New York\'s premier Revenue Cycle Management company — built by billing experts, for healthcare providers.')}
<section class="py-20 px-6 bg-white">
  <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
    <div class="space-y-6">
      <span class="text-[11px] font-bold tracking-widest text-brand-teal uppercase">Who We Are</span>
      <h2 class="text-3xl md:text-4xl font-bold text-brand-navy leading-tight">A Different Kind of Medical Billing Company</h2>
      <p class="text-[15px] text-slate-600 leading-relaxed font-light">ZettaRCM was founded with a single mission: to help healthcare providers stop leaving money on the table and receive every dollar they have earned. Based in Brooklyn, New York, we serve practices of all sizes — from solo physicians to large multi-specialty groups — across all 50 states.</p>
      <p class="text-[15px] text-slate-600 leading-relaxed font-light">Unlike large, impersonal billing companies, ZettaRCM assigns a dedicated account manager to every practice. You always have a direct contact who knows your payers, your specialty, and your goals.</p>
      <div class="grid grid-cols-2 gap-4 pt-2">
        <div class="border border-slate-200 p-5 text-center hover:border-brand-teal transition-all"><div class="text-3xl font-bold text-brand-teal">99.2%</div><div class="text-[11px] text-slate-500 uppercase tracking-wider mt-1">First-Pass Claim Rate</div></div>
        <div class="border border-slate-200 p-5 text-center hover:border-brand-teal transition-all"><div class="text-3xl font-bold text-brand-navy">+30%</div><div class="text-[11px] text-slate-500 uppercase tracking-wider mt-1">Average Revenue Increase</div></div>
        <div class="border border-slate-200 p-5 text-center hover:border-brand-teal transition-all"><div class="text-3xl font-bold text-brand-teal">35+</div><div class="text-[11px] text-slate-500 uppercase tracking-wider mt-1">Medical Specialties</div></div>
        <div class="border border-slate-200 p-5 text-center hover:border-brand-teal transition-all"><div class="text-3xl font-bold text-brand-navy">50</div><div class="text-[11px] text-slate-500 uppercase tracking-wider mt-1">States Nationwide</div></div>
      </div>
    </div>
    <div class="relative">
      <img src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=85&fit=crop" alt="ZettaRCM team" class="w-full h-[480px] object-cover">
      <div class="absolute bottom-0 left-0 right-0 bg-brand-teal p-5 flex items-center gap-4">
        <svg class="w-8 h-8 fill-brand-navy shrink-0" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
        <div><div class="text-brand-navy font-bold">HIPAA Compliant · AAPC Certified · CMS Compliant</div><div class="text-brand-navy/70 text-[12px]">Every process meets or exceeds industry standards</div></div>
      </div>
    </div>
  </div>
</section>
<section class="py-20 px-6 bg-slate-50">
  <div class="max-w-7xl mx-auto">
    <div class="text-center max-w-xl mx-auto mb-12"><span class="text-[11px] font-bold tracking-widest text-brand-teal uppercase block mb-3">Our Foundation</span><h2 class="text-3xl md:text-4xl font-bold text-brand-navy">Mission, Vision & Values</h2></div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-white border border-slate-200 p-8 hover:border-brand-teal hover:shadow-md transition-all">
        <div class="w-14 h-14 bg-brand-navy flex items-center justify-center mb-5"><svg class="w-7 h-7 fill-brand-teal" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg></div>
        <h3 class="text-brand-navy font-bold text-[18px] mb-3">Our Mission</h3>
        <p class="text-[14px] text-slate-600 leading-relaxed font-light">To empower healthcare providers with the billing expertise, technology, and dedicated support they need to maximize revenue and focus on patient care.</p>
      </div>
      <div class="bg-brand-navy p-8">
        <div class="w-14 h-14 bg-brand-teal/20 border border-brand-teal flex items-center justify-center mb-5"><svg class="w-7 h-7 fill-brand-teal" viewBox="0 0 24 24"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg></div>
        <h3 class="text-white font-bold text-[18px] mb-3">Our Vision</h3>
        <p class="text-[14px] text-slate-400 leading-relaxed font-light">To be the most trusted Revenue Cycle Management partner for healthcare providers nationwide — recognized for our expertise, integrity, and the measurable financial results we deliver.</p>
      </div>
      <div class="bg-white border border-slate-200 p-8 hover:border-brand-teal hover:shadow-md transition-all">
        <div class="w-14 h-14 bg-brand-navy flex items-center justify-center mb-5"><svg class="w-7 h-7 fill-brand-teal" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
        <h3 class="text-brand-navy font-bold text-[18px] mb-3">Our Values</h3>
        <ul class="text-[14px] text-slate-600 space-y-2 font-light">
          <li class="flex items-center gap-2"><svg class="w-4 h-4 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg>Integrity in every interaction</li>
          <li class="flex items-center gap-2"><svg class="w-4 h-4 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg>Transparency in reporting</li>
          <li class="flex items-center gap-2"><svg class="w-4 h-4 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg>Accountability for results</li>
          <li class="flex items-center gap-2"><svg class="w-4 h-4 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg>Continuous innovation</li>
          <li class="flex items-center gap-2"><svg class="w-4 h-4 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg>Client-first mentality</li>
        </ul>
      </div>
    </div>
  </div>
</section>
<section class="py-20 px-6 bg-white">
  <div class="max-w-7xl mx-auto">
    <div class="text-center max-w-xl mx-auto mb-12"><span class="text-[11px] font-bold tracking-widest text-brand-teal uppercase block mb-3">Why Choose Us</span><h2 class="text-3xl md:text-4xl font-bold text-brand-navy">What Sets ZettaRCM Apart</h2></div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
      <div class="border border-slate-200 p-7 text-center hover:border-brand-teal hover:shadow-md transition-all"><div class="w-16 h-16 bg-light-bg border border-slate-200 flex items-center justify-center mx-auto mb-4"><svg class="w-8 h-8 fill-brand-teal" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg></div><h3 class="text-brand-navy font-bold text-[15px] mb-2">Dedicated Account Managers</h3><p class="text-[13px] text-slate-500 font-light">One specialist assigned exclusively to your practice.</p></div>
      <div class="border border-slate-200 p-7 text-center hover:border-brand-teal hover:shadow-md transition-all"><div class="w-16 h-16 bg-light-bg border border-slate-200 flex items-center justify-center mx-auto mb-4"><svg class="w-8 h-8 fill-brand-teal" viewBox="0 0 24 24"><path d="M22 9V7h-2V5c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2v-2h2v-2h-2v-2h2v-2h-2V9h2z"/></svg></div><h3 class="text-brand-navy font-bold text-[15px] mb-2">EMR/PM Integration</h3><p class="text-[13px] text-slate-500 font-light">Works with your existing software — no disruptions.</p></div>
      <div class="border border-slate-200 p-7 text-center hover:border-brand-teal hover:shadow-md transition-all"><div class="w-16 h-16 bg-light-bg border border-slate-200 flex items-center justify-center mx-auto mb-4"><svg class="w-8 h-8 fill-brand-teal" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg></div><h3 class="text-brand-navy font-bold text-[15px] mb-2">100% HIPAA Compliant</h3><p class="text-[13px] text-slate-500 font-light">Every process meets full HIPAA standards.</p></div>
      <div class="border border-slate-200 p-7 text-center hover:border-brand-teal hover:shadow-md transition-all"><div class="w-16 h-16 bg-light-bg border border-slate-200 flex items-center justify-center mx-auto mb-4"><svg class="w-8 h-8 fill-brand-teal" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 3c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm7 13H5v-.23c0-.62.28-1.2.76-1.58C7.47 15.82 9.64 15 12 15s4.53.82 6.24 2.19c.48.38.76.97.76 1.58V19z"/></svg></div><h3 class="text-brand-navy font-bold text-[15px] mb-2">AAPC Certified Coders</h3><p class="text-[13px] text-slate-500 font-light">All coders hold active certifications and stay current.</p></div>
    </div>
  </div>
</section>
{CTA}
{FOOTER}'''
write(f'{B}/our-company/index.html', head('Our Company') + content)

# ═══════════════════════════════════════════════════════════════════════════════
# NATIONWIDE MEDICAL BILLING
# ═══════════════════════════════════════════════════════════════════════════════
states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
state_grid = ''.join(f'<div class="bg-white border border-slate-200 px-4 py-3 text-[13px] text-slate-600 font-medium text-center hover:border-brand-teal hover:text-brand-teal transition-all">{s}</div>' for s in states)
content = f'''
{TOPBAR}
{header('/nationwide-medical-billing/')}
{banner('Nationwide Medical Billing', ' <span class="mx-2">/</span> Nationwide Medical Billing', 'ZettaRCM serves healthcare providers in all 50 states with the same expert team and proven results.')}
<section class="py-20 px-6 bg-white">
  <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-12">
    <div class="lg:col-span-2 space-y-8">
      <img src="https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop" alt="Nationwide medical billing" class="w-full h-64 object-cover">
      <p class="text-[15px] text-slate-600 leading-relaxed font-light">ZettaRCM provides expert Revenue Cycle Management services to healthcare practices across the United States. No matter where your practice is located, our team brings the same level of expertise, technology, and dedicated support that has made us New York's leading medical billing company.</p>
      <p class="text-[15px] text-slate-600 leading-relaxed font-light">We understand that payer rules, state regulations, and reimbursement rates vary by state. Our billing specialists stay current with state-specific Medicaid programs, workers' compensation rules, and commercial payer contracts in every state we serve.</p>
      <div class="bg-light-bg border border-slate-200 p-7">
        <h3 class="text-brand-navy font-bold text-[18px] mb-4">Why Practices Nationwide Choose ZettaRCM</h3>
        <div class="space-y-3">
          <div class="flex gap-3"><svg class="w-5 h-5 fill-brand-teal shrink-0 mt-0.5" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg><span class="text-[14px] text-slate-600">State-specific Medicaid and commercial payer expertise</span></div>
          <div class="flex gap-3"><svg class="w-5 h-5 fill-brand-teal shrink-0 mt-0.5" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg><span class="text-[14px] text-slate-600">Same dedicated account manager regardless of location</span></div>
          <div class="flex gap-3"><svg class="w-5 h-5 fill-brand-teal shrink-0 mt-0.5" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg><span class="text-[14px] text-slate-600">Credentialing with every major payer in your state</span></div>
          <div class="flex gap-3"><svg class="w-5 h-5 fill-brand-teal shrink-0 mt-0.5" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg><span class="text-[14px] text-slate-600">Workers' compensation and no-fault billing expertise by state</span></div>
          <div class="flex gap-3"><svg class="w-5 h-5 fill-brand-teal shrink-0 mt-0.5" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg><span class="text-[14px] text-slate-600">HIPAA-compliant telehealth billing in all 50 states</span></div>
        </div>
      </div>
      {stat_row()}
      <div>
        <h3 class="text-brand-navy font-bold text-[20px] mb-5">States We Serve</h3>
        <div class="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 gap-2">{state_grid}</div>
      </div>
    </div>
    <div>{SIDEBAR_QUOTE}</div>
  </div>
</section>
{CTA}
{FOOTER}'''
write(f'{B}/nationwide-medical-billing/index.html', head('Nationwide Medical Billing') + content)

# ═══════════════════════════════════════════════════════════════════════════════
# CONTACT
# ═══════════════════════════════════════════════════════════════════════════════
content = f'''
{TOPBAR}
{header('/contact/')}
{banner('Contact ZettaRCM', ' <span class="mx-2">/</span> Contact Us', 'Reach our medical billing experts. We respond within 2 business hours.')}
<section class="py-16 px-6 bg-slate-50">
  <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-10">
    <div class="space-y-6">
      <div class="bg-white border border-slate-200 p-7 space-y-5">
        <h3 class="text-brand-navy font-bold text-[17px] border-b border-slate-100 pb-4">Get In Touch</h3>
        <div class="flex gap-4 items-start"><div class="w-10 h-10 bg-brand-navy flex items-center justify-center shrink-0"><svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg></div><div><div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-1">Phone</div><a href="tel:+18005160192" class="block text-brand-navy font-semibold hover:text-brand-teal">(800) 516-0192</a><a href="tel:+17183030192" class="block text-brand-navy font-semibold hover:text-brand-teal">(718) 303-0192</a></div></div>
        <div class="flex gap-4 items-start"><div class="w-10 h-10 bg-brand-navy flex items-center justify-center shrink-0"><svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></div><div><div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-1">Email</div><a href="mailto:info@zettarcm.com" class="text-brand-navy font-semibold hover:text-brand-teal">info@zettarcm.com</a></div></div>
        <div class="flex gap-4 items-start"><div class="w-10 h-10 bg-brand-navy flex items-center justify-center shrink-0"><svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg></div><div><div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-1">Address</div><div class="text-slate-600 text-[14px]">134 N 4th St<br>Brooklyn, NY 11249</div></div></div>
        <div class="flex gap-4 items-start"><div class="w-10 h-10 bg-brand-navy flex items-center justify-center shrink-0"><svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67V7z"/></svg></div><div><div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-1">Hours</div><div class="text-slate-600 text-[13px]">Mon–Fri: 9 AM – 6 PM EST<br>Sat: 10 AM – 2 PM EST</div></div></div>
      </div>
      <div class="bg-brand-teal p-6"><h4 class="text-brand-navy font-bold text-[15px] mb-2">24/7 Urgent Support</h4><p class="text-brand-navy/70 text-[13px] mb-4">For billing emergencies affecting patient care.</p><a href="tel:+18005160192" class="block bg-brand-navy text-white text-center font-bold text-[13px] uppercase tracking-wider py-3 hover:bg-white hover:text-brand-navy transition-all">(800) 516-0192</a></div>
    </div>
    <div class="lg:col-span-2 bg-white border border-slate-200 p-8">
      <h3 class="text-brand-navy font-bold text-[20px] mb-2">Send Us a Message</h3>
      <p class="text-slate-500 text-[13px] mb-7 font-light">A billing specialist will respond within 2 business hours.</p>
      <form class="space-y-5" onsubmit="this.innerHTML='<div class=\\'text-center py-10\\'><svg class=\\'w-14 h-14 fill-brand-teal mx-auto mb-3\\' viewBox=\\'0 0 24 24\\'><path d=\\'M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z\\'/></svg><div class=\\'text-brand-teal font-bold text-xl\\'>Message Sent!</div><p class=\\'text-slate-500 mt-2\\'>We will contact you within 2 business hours.</p></div>';event.preventDefault()">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
          <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Full Name *</label><input type="text" required placeholder="Dr. Jane Smith" class="w-full border border-slate-200 text-slate-700 text-[14px] px-4 py-3 outline-none focus:border-brand-teal transition-colors"></div>
          <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Practice Name *</label><input type="text" required placeholder="Your Practice" class="w-full border border-slate-200 text-slate-700 text-[14px] px-4 py-3 outline-none focus:border-brand-teal transition-colors"></div>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
          <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Email *</label><input type="email" required placeholder="doctor@practice.com" class="w-full border border-slate-200 text-slate-700 text-[14px] px-4 py-3 outline-none focus:border-brand-teal transition-colors"></div>
          <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Phone *</label><input type="tel" required placeholder="(800) 000-0000" class="w-full border border-slate-200 text-slate-700 text-[14px] px-4 py-3 outline-none focus:border-brand-teal transition-colors"></div>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
          <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Service Needed</label><select class="w-full border border-slate-200 text-slate-600 text-[14px] px-4 py-3 outline-none focus:border-brand-teal cursor-pointer"><option>Medical Billing</option><option>Credentialing</option><option>Medical Coding</option><option>Denial Management</option><option>A/R Follow Up</option><option>Revenue Cycle Management</option><option>Other</option></select></div>
          <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Specialty</label><select class="w-full border border-slate-200 text-slate-600 text-[14px] px-4 py-3 outline-none focus:border-brand-teal cursor-pointer"><option>Mental Health</option><option>Cardiology</option><option>Orthopedics</option><option>Radiology</option><option>Oncology</option><option>Family Practice</option><option>Internal Medicine</option><option>Other</option></select></div>
        </div>
        <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Message</label><textarea rows="5" placeholder="Tell us about your practice and billing needs..." class="w-full border border-slate-200 text-slate-700 text-[14px] px-4 py-3 outline-none focus:border-brand-teal resize-none transition-colors"></textarea></div>
        <button type="submit" class="w-full bg-brand-navy text-white font-bold text-[13px] uppercase tracking-widest py-4 hover:bg-brand-teal hover:text-brand-navy transition-all cursor-pointer">Send Message — Response Within 2 Hours</button>
      </form>
    </div>
  </div>
</section>
{CTA}
{FOOTER}'''
write(f'{B}/contact/index.html', head('Contact Us') + content)

# ═══════════════════════════════════════════════════════════════════════════════
# BLOG
# ═══════════════════════════════════════════════════════════════════════════════
articles = [
    ('Medical Billing','Understanding Patient Billing Statements: A Guide for Healthcare Providers','Learn how transparent billing improves collection rates and reduces patient confusion about balances.','https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=600&q=80&fit=crop','June 15, 2026'),
    ('Denial Management','Top 5 Denial Management Strategies for 2026','The most effective tactics to reduce claim denials and recover lost revenue in today\'s payer environment.','https://images.unsplash.com/photo-1504813184591-01572f98c85f?w=600&q=80&fit=crop','June 10, 2026'),
    ('Medical Coding','2026 CPT Code Updates: What Your Practice Must Know','Stay ahead of the annual CPT updates and how new codes affect reimbursement rates in your specialty.','https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=600&q=80&fit=crop','June 5, 2026'),
    ('Revenue Cycle','How to Reduce Your A/R Days Below 30','Practical steps high-performing practices use to accelerate collections and shrink aging accounts receivable.','https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=600&q=80&fit=crop','May 28, 2026'),
    ('Credentialing','Provider Credentialing Mistakes That Delay Revenue','The most common credentialing errors and how to avoid them so you start getting paid from day one.','https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=600&q=80&fit=crop','May 20, 2026'),
    ('Prior Authorization','Navigating Prior Authorization in 2026: A Practical Guide','How to streamline prior authorizations, reduce delays, and appeal denials effectively.','https://images.unsplash.com/photo-1581056771107-24ca5f033842?w=600&q=80&fit=crop','May 12, 2026'),
]
cards = ''.join(f'''<a href="#" class="group bg-white border border-slate-200 hover:border-brand-teal hover:shadow-md transition-all overflow-hidden flex flex-col">
  <div class="h-48 overflow-hidden"><img src="{img}" alt="{t}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"></div>
  <div class="p-6 flex flex-col flex-1 gap-2">
    <div class="flex items-center justify-between"><span class="text-[11px] font-bold text-brand-teal uppercase tracking-wider">{cat}</span><span class="text-[11px] text-slate-400">{date}</span></div>
    <h3 class="text-[15px] font-bold text-brand-navy leading-tight group-hover:text-brand-teal transition-colors">{t}</h3>
    <p class="text-[13px] text-slate-500 font-light leading-relaxed flex-1">{desc}</p>
    <span class="text-brand-teal text-[12px] font-bold uppercase tracking-wider mt-2 flex items-center gap-1">Read More <svg class="w-3 h-3 fill-current" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg></span>
  </div>
</a>''' for cat,t,desc,img,date in articles)
content = f'''
{TOPBAR}
{header()}
{banner('ZettaRCM Blog','<span class="mx-2">/</span> Resources <span class="mx-2">/</span> Blog','Insights, updates, and expert guidance on medical billing and revenue cycle management.')}
<section class="py-16 px-6 bg-slate-50">
  <div class="max-w-7xl mx-auto">
    <div class="flex flex-wrap gap-3 mb-10">
      <button class="px-5 py-2 bg-brand-navy text-white text-[12px] font-bold uppercase tracking-wider">All Posts</button>
      <button class="px-5 py-2 border border-slate-300 text-slate-600 text-[12px] font-bold uppercase tracking-wider hover:border-brand-teal hover:text-brand-teal transition-all">Medical Billing</button>
      <button class="px-5 py-2 border border-slate-300 text-slate-600 text-[12px] font-bold uppercase tracking-wider hover:border-brand-teal hover:text-brand-teal transition-all">Coding</button>
      <button class="px-5 py-2 border border-slate-300 text-slate-600 text-[12px] font-bold uppercase tracking-wider hover:border-brand-teal hover:text-brand-teal transition-all">Denial Management</button>
      <button class="px-5 py-2 border border-slate-300 text-slate-600 text-[12px] font-bold uppercase tracking-wider hover:border-brand-teal hover:text-brand-teal transition-all">Credentialing</button>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">{cards}</div>
    <div class="text-center mt-12">
      <button class="border border-slate-300 text-slate-600 text-[13px] font-semibold uppercase tracking-wider px-10 py-4 hover:border-brand-teal hover:text-brand-teal transition-all">Load More Articles</button>
    </div>
  </div>
</section>
{CTA}
{FOOTER}'''
write(f'{B}/resources/blog/index.html', head('Blog — Medical Billing Insights') + content)

# ═══════════════════════════════════════════════════════════════════════════════
# FAQs
# ═══════════════════════════════════════════════════════════════════════════════
faqs = [
    ('What is Revenue Cycle Management (RCM)?','Revenue Cycle Management is the financial process healthcare facilities use to track patient care from registration to final payment. It encompasses everything from verifying insurance eligibility before a visit, through coding and claim submission, to collecting patient balances. A well-managed revenue cycle ensures providers receive maximum reimbursement for every service rendered.'),
    ('How much does ZettaRCM charge for billing services?','ZettaRCM typically charges a percentage of collections — meaning we only get paid when you get paid. This aligns our incentives with yours. Our rates vary based on your specialty, volume, and the specific services needed. Contact us for a custom quote — we will provide a transparent pricing proposal with no hidden fees.'),
    ('How quickly will I see results after switching to ZettaRCM?','Most practices see measurable improvement within the first 30–60 days. Claim submission speed improves immediately, and denial rates typically drop within the first billing cycle. Revenue increases are usually visible within 60–90 days as A/R backlogs are cleared and collections improve.'),
    ('Do you work with my existing EMR/PM software?','Yes. ZettaRCM integrates with all major EMR and Practice Management systems including Epic, eClinicalWorks, athenahealth, Kareo, DrChrono, Nextech, Allscripts, and many others. We work within your existing workflow — no costly migrations required.'),
    ('What specialties do you serve?','ZettaRCM serves over 35 medical specialties including Mental Health, Cardiology, Orthopedics, Radiology, Oncology, Neurology, Dermatology, OB/GYN, Urology, Pain Management, Gastroenterology, Pediatrics, and many more. Each specialty is handled by team members with specific expertise in that area\'s coding and payer rules.'),
    ('Are you HIPAA compliant?','Yes — 100%. All ZettaRCM processes, systems, and team members are fully HIPAA compliant. We use encrypted data transmission, secure storage systems, and regular compliance training to protect your patients\' protected health information (PHI) at every step.'),
    ('What is your first-pass claim acceptance rate?','ZettaRCM maintains a 99.2% first-pass claim acceptance rate — significantly above the industry average of 85–90%. This means fewer denials, faster payments, and more revenue for your practice.'),
    ('Do you handle credentialing as well as billing?','Yes. ZettaRCM provides comprehensive credentialing and payer enrollment services alongside our billing services. We handle CAQH profile setup, primary source verification, Medicare and Medicaid enrollment, and commercial payer contracting. We also manage re-credentialing and keep your information current with all payers.'),
    ('Can you take over billing for an existing practice with aged A/R?','Absolutely. We regularly take on billing for practices with significant aged accounts receivable. Our team performs an A/R cleanup project alongside your ongoing billing — systematically following up on old claims, filing appeals where appropriate, and recovering lost revenue.'),
    ('How do I get started with ZettaRCM?','Getting started is simple. Contact us for a free practice audit — we will review your current billing processes, identify revenue gaps, and provide a customized proposal. Once we agree on scope and pricing, our onboarding team handles setup, credentialing verification, and integration with your systems. Most practices are fully onboarded within 2–4 weeks.'),
]
faq_html = ''
for i,(q,a) in enumerate(faqs):
    faq_html += f'''<div class="border border-slate-200 overflow-hidden" id="faq-{i}">
  <button onclick="toggleFaq({i})" class="w-full flex items-center justify-between p-6 text-left hover:bg-light-bg transition-colors group">
    <span class="text-[15px] font-semibold text-brand-navy group-hover:text-brand-teal transition-colors pr-4">{q}</span>
    <span id="icon-{i}" class="faq-icon shrink-0 w-8 h-8 border border-slate-300 flex items-center justify-center text-slate-400 group-hover:border-brand-teal group-hover:text-brand-teal transition-all">+</span>
  </button>
  <div id="ans-{i}" class="hidden px-6 pb-6"><p class="text-[14px] text-slate-600 leading-relaxed font-light">{a}</p></div>
</div>'''

content = f'''
{TOPBAR}
{header()}
{banner('Frequently Asked Questions','<span class="mx-2">/</span> Resources <span class="mx-2">/</span> FAQs','Everything you need to know about ZettaRCM\'s medical billing and revenue cycle services.')}
<section class="py-16 px-6 bg-white">
  <div class="max-w-4xl mx-auto">
    <div class="space-y-3">{faq_html}</div>
    <div class="mt-12 bg-light-bg border border-slate-200 p-8 text-center">
      <h3 class="text-brand-navy font-bold text-[20px] mb-2">Still Have Questions?</h3>
      <p class="text-slate-500 text-[14px] mb-5 font-light">Our billing specialists are available to answer any questions about our services.</p>
      <div class="flex flex-wrap gap-3 justify-center">
        <a href="/contact/" class="bg-brand-navy text-white font-bold text-[13px] uppercase tracking-wider px-8 py-3.5 hover:bg-brand-teal hover:text-brand-navy transition-all">Contact Us</a>
        <a href="tel:+18005160192" class="border border-brand-navy text-brand-navy font-bold text-[13px] uppercase tracking-wider px-8 py-3.5 hover:bg-brand-navy hover:text-white transition-all">(800) 516-0192</a>
      </div>
    </div>
  </div>
</section>
<script>
function toggleFaq(i) {{
  var ans = document.getElementById('ans-'+i);
  var icon = document.getElementById('icon-'+i);
  if (ans.classList.contains('hidden')) {{
    ans.classList.remove('hidden');
    icon.textContent = '×';
    icon.style.transform = 'rotate(0deg)';
  }} else {{
    ans.classList.add('hidden');
    icon.textContent = '+';
  }}
}}
</script>
{CTA}
{FOOTER}'''
write(f'{B}/resources/faqs/index.html', head('FAQs — Medical Billing Questions') + content)

# ═══════════════════════════════════════════════════════════════════════════════
# CASE STUDIES
# ═══════════════════════════════════════════════════════════════════════════════
cases = [
    ('Mental Health Practice, Brooklyn NY','Increased collections by 42% in 90 days','A solo psychiatry practice had an 18% denial rate and $140K in aged A/R. ZettaRCM took over billing, cleared the backlog, and implemented proper modifier usage for telehealth sessions.','42% increase in monthly collections','18% → 2.1% denial rate reduction','$140K in aged A/R recovered','https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=600&q=80&fit=crop'),
    ('Multi-Specialty Group, Queens NY','Reduced denial rate from 22% to under 3%','A 12-provider multi-specialty group was losing significant revenue due to coding errors and slow prior authorization processing. ZettaRCM restructured their entire billing workflow.','$2.1M additional annual revenue captured','22% → 2.8% denial rate','Prior auth approval time cut from 5 days to 24 hours','https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=600&q=80&fit=crop'),
    ('Orthopedic Surgery Center, New Jersey','30% revenue increase within 60 days','An orthopedic surgery center was significantly underbilling for procedures due to outdated fee schedules and missed modifier opportunities. ZettaRCM\'s audit identified $380K in annual underpayments.','30% revenue increase in first 60 days','$380K in annual underpayments recovered','A/R days reduced from 52 to 24','https://images.unsplash.com/photo-1530026186672-2cd00ffc50fe?w=600&q=80&fit=crop'),
]
case_cards = ''.join(f'''<div class="bg-white border border-slate-200 hover:border-brand-teal hover:shadow-lg transition-all overflow-hidden">
  <img src="{img}" alt="{title}" class="w-full h-48 object-cover">
  <div class="p-7 space-y-4">
    <div><div class="text-[11px] font-bold text-brand-teal uppercase tracking-wider">{title}</div><h3 class="text-[17px] font-bold text-brand-navy mt-1">{headline}</h3></div>
    <p class="text-[13px] text-slate-600 font-light leading-relaxed">{desc}</p>
    <div class="space-y-2 pt-2 border-t border-slate-100">
      {''.join(f'<div class="flex items-center gap-2 text-[13px] text-slate-700"><svg class="w-4 h-4 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg>{r}</div>' for r in results)}
    </div>
    <a href="/contact/" class="inline-flex items-center gap-2 text-brand-teal font-bold text-[12px] uppercase tracking-wider hover:text-brand-navy transition-colors">Read Full Case Study <svg class="w-3 h-3 fill-current" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg></a>
  </div>
</div>''' for title,headline,desc,*results,img in [tuple(c) for c in cases])
content = f'''
{TOPBAR}
{header()}
{banner('Case Studies','<span class="mx-2">/</span> Resources <span class="mx-2">/</span> Case Studies','Real results from real healthcare practices that partnered with ZettaRCM.')}
<section class="py-16 px-6 bg-slate-50">
  <div class="max-w-7xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">{case_cards}</div>
    <div class="mt-12 bg-brand-navy p-10 text-center">
      <div class="text-brand-teal font-bold text-[11px] uppercase tracking-widest mb-3">Start Your Success Story</div>
      <h3 class="text-white font-bold text-2xl mb-2">Ready to See Results Like These?</h3>
      <p class="text-slate-400 text-[14px] font-light mb-6">Get a free practice audit and discover exactly how much revenue you\'re leaving behind.</p>
      <a href="/contact/" class="inline-block bg-brand-teal text-brand-navy font-bold text-[13px] uppercase tracking-wider px-10 py-4 hover:bg-white transition-all">Get My Free Practice Audit</a>
    </div>
  </div>
</section>
{CTA}
{FOOTER}'''
write(f'{B}/resources/case-studies/index.html', head('Case Studies — Real Results') + content)

# ═══════════════════════════════════════════════════════════════════════════════
# RCM LIBRARY
# ═══════════════════════════════════════════════════════════════════════════════
resources_items = [
    ('Guide','The Complete Revenue Cycle Management Guide for 2026','A comprehensive guide covering every stage of the revenue cycle from patient registration to final payment.','https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=400&q=80'),
    ('Checklist','Medical Billing Denial Prevention Checklist','30-point checklist to reduce claim denials before submission. Used by 500+ practices nationwide.','https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=400&q=80'),
    ('Guide','ICD-10 Coding Best Practices by Specialty','Specialty-specific coding guidance for 20+ medical specialties to maximize reimbursements.','https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400&q=80'),
    ('Template','Patient Financial Responsibility Agreement Template','HIPAA-compliant template for communicating patient financial responsibility at time of service.','https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=400&q=80'),
    ('Report','2026 State of Medical Billing Report','Annual industry benchmark report covering denial rates, collection rates, and RCM technology trends.','https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400&q=80'),
    ('Webinar','Prior Authorization Best Practices Webinar','Recorded webinar covering strategies to streamline prior auth workflows and reduce approval times.','https://images.unsplash.com/photo-1516549655169-df83a0774514?w=400&q=80'),
]
lib_cards = ''.join(f'''<a href="/contact/" class="group bg-white border border-slate-200 hover:border-brand-teal hover:shadow-md transition-all overflow-hidden flex flex-col">
  <div class="h-36 overflow-hidden"><img src="{img}" alt="{t}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"></div>
  <div class="p-5 flex flex-col flex-1 gap-2">
    <span class="text-[10px] font-bold text-white bg-brand-navy px-2 py-1 w-fit uppercase tracking-wider">{rtype}</span>
    <h3 class="text-[14px] font-bold text-brand-navy leading-tight group-hover:text-brand-teal transition-colors">{t}</h3>
    <p class="text-[12px] text-slate-500 font-light leading-relaxed flex-1">{desc}</p>
    <span class="text-brand-teal text-[12px] font-bold flex items-center gap-1 mt-1">Download Free <svg class="w-3 h-3 fill-current" viewBox="0 0 24 24"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg></span>
  </div>
</a>''' for rtype,t,desc,img in resources_items)
content = f'''
{TOPBAR}
{header()}
{banner('RCM Library','<span class="mx-2">/</span> Resources <span class="mx-2">/</span> RCM Library','Free guides, checklists, templates, and reports for healthcare billing professionals.')}
<section class="py-16 px-6 bg-slate-50">
  <div class="max-w-7xl mx-auto">
    <div class="text-center max-w-xl mx-auto mb-10"><p class="text-[15px] text-slate-600 font-light">Download free resources to improve your practice\'s revenue cycle performance. No email required for most resources.</p></div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">{lib_cards}</div>
  </div>
</section>
{CTA}
{FOOTER}'''
write(f'{B}/resources/rcm-library/index.html', head('RCM Library — Free Resources') + content)

# ═══════════════════════════════════════════════════════════════════════════════
# NEWSROOM
# ═══════════════════════════════════════════════════════════════════════════════
news = [
    ('June 2026','ZettaRCM Named Top Medical Billing Company in New York for 2026','ZettaRCM has been recognized by Healthcare Financial Management Association as a top-rated revenue cycle management company for the second consecutive year.'),
    ('May 2026','ZettaRCM Expands Mental Health Billing Division','In response to growing demand from behavioral health providers, ZettaRCM has expanded its dedicated mental health billing team with five additional AAPC-certified coders.'),
    ('April 2026','New Partnership with Leading EHR Platform','ZettaRCM announces seamless integration with a major EHR platform, enabling automated charge capture for over 200 client practices.'),
    ('March 2026','ZettaRCM Achieves 99.2% First-Pass Claim Rate Milestone','The company reports its highest-ever first-pass claim acceptance rate, significantly above the industry average of 85–90%.'),
]
news_items = ''.join(f'''<article class="bg-white border border-slate-200 p-7 hover:border-brand-teal hover:shadow-md transition-all">
  <div class="text-[11px] font-bold text-brand-teal uppercase tracking-wider mb-2">{date}</div>
  <h3 class="text-[17px] font-bold text-brand-navy mb-3">{t}</h3>
  <p class="text-[14px] text-slate-600 font-light leading-relaxed">{body}</p>
  <a href="/contact/" class="inline-flex items-center gap-1.5 text-brand-teal font-bold text-[12px] uppercase tracking-wider mt-4">Read Full Release <svg class="w-3 h-3 fill-current" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg></a>
</article>''' for date,t,body in news)
content = f'''
{TOPBAR}
{header()}
{banner('Newsroom','<span class="mx-2">/</span> Resources <span class="mx-2">/</span> Newsroom','Latest news, press releases, and announcements from ZettaRCM.')}
<section class="py-16 px-6 bg-slate-50">
  <div class="max-w-4xl mx-auto space-y-5">{news_items}</div>
</section>
{CTA}
{FOOTER}'''
write(f'{B}/resources/newsroom/index.html', head('Newsroom — Latest News') + content)

# ═══════════════════════════════════════════════════════════════════════════════
# PROVIDER FORM
# ═══════════════════════════════════════════════════════════════════════════════
content = f'''
{TOPBAR}
{header()}
{banner('Provider Enrollment Form','<span class="mx-2">/</span> Resources <span class="mx-2">/</span> Provider Form','Submit your practice information to get started with ZettaRCM. We\'ll contact you within 24 hours.')}
<section class="py-16 px-6 bg-slate-50">
  <div class="max-w-3xl mx-auto bg-white border border-slate-200 p-10">
    <h2 class="text-brand-navy font-bold text-[22px] mb-2">Practice Information Form</h2>
    <p class="text-slate-500 text-[13px] mb-8 font-light">Please complete the form below. A ZettaRCM specialist will review your information and contact you within 24 hours with a customized proposal.</p>
    <form class="space-y-6" onsubmit="this.innerHTML='<div class=\\'text-center py-16\\'><svg class=\\'w-16 h-16 fill-brand-teal mx-auto mb-4\\' viewBox=\\'0 0 24 24\\'><path d=\\'M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z\\'/></svg><div class=\\'text-brand-teal font-bold text-2xl\\'>Form Submitted!</div><p class=\\'text-slate-500 mt-3 text-[15px]\\'>Thank you. A ZettaRCM specialist will contact you within 24 hours.</p></div>';event.preventDefault()">
      <div class="border-b border-slate-100 pb-2 mb-2"><div class="text-[11px] font-bold text-brand-teal uppercase tracking-widest">Section 1 — Provider Information</div></div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
        <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Provider Name *</label><input type="text" required class="w-full border border-slate-200 px-4 py-3 text-[14px] outline-none focus:border-brand-teal transition-colors"></div>
        <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Credential (MD, DO, NP...)</label><input type="text" class="w-full border border-slate-200 px-4 py-3 text-[14px] outline-none focus:border-brand-teal transition-colors"></div>
        <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">NPI Number</label><input type="text" class="w-full border border-slate-200 px-4 py-3 text-[14px] outline-none focus:border-brand-teal transition-colors"></div>
        <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Specialty *</label><select required class="w-full border border-slate-200 px-4 py-3 text-[14px] outline-none focus:border-brand-teal cursor-pointer"><option value="">Select Specialty</option><option>Mental Health</option><option>Cardiology</option><option>Orthopedics</option><option>Radiology</option><option>Oncology</option><option>Family Practice</option><option>Internal Medicine</option><option>Other</option></select></div>
      </div>
      <div class="border-b border-slate-100 pb-2 mb-2 mt-4"><div class="text-[11px] font-bold text-brand-teal uppercase tracking-widest">Section 2 — Practice Information</div></div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
        <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Practice Name *</label><input type="text" required class="w-full border border-slate-200 px-4 py-3 text-[14px] outline-none focus:border-brand-teal transition-colors"></div>
        <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Tax ID (EIN)</label><input type="text" class="w-full border border-slate-200 px-4 py-3 text-[14px] outline-none focus:border-brand-teal transition-colors"></div>
        <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Phone *</label><input type="tel" required class="w-full border border-slate-200 px-4 py-3 text-[14px] outline-none focus:border-brand-teal transition-colors"></div>
        <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Email *</label><input type="email" required class="w-full border border-slate-200 px-4 py-3 text-[14px] outline-none focus:border-brand-teal transition-colors"></div>
        <div class="sm:col-span-2"><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Practice Address *</label><input type="text" required class="w-full border border-slate-200 px-4 py-3 text-[14px] outline-none focus:border-brand-teal transition-colors"></div>
      </div>
      <div class="border-b border-slate-100 pb-2 mb-2 mt-4"><div class="text-[11px] font-bold text-brand-teal uppercase tracking-widest">Section 3 — Billing Needs</div></div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
        <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Current EMR/PM System</label><input type="text" placeholder="e.g. Epic, eCW, Kareo..." class="w-full border border-slate-200 px-4 py-3 text-[14px] outline-none focus:border-brand-teal transition-colors"></div>
        <div><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Monthly Claim Volume</label><select class="w-full border border-slate-200 px-4 py-3 text-[14px] outline-none focus:border-brand-teal cursor-pointer"><option>Under 100 claims/month</option><option>100–500 claims/month</option><option>500–1,000 claims/month</option><option>1,000+ claims/month</option></select></div>
        <div class="sm:col-span-2"><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Services Needed</label><div class="grid grid-cols-2 gap-2"><label class="flex items-center gap-2 text-[13px] text-slate-600 cursor-pointer"><input type="checkbox" class="cursor-pointer"> Medical Billing</label><label class="flex items-center gap-2 text-[13px] text-slate-600 cursor-pointer"><input type="checkbox" class="cursor-pointer"> Credentialing</label><label class="flex items-center gap-2 text-[13px] text-slate-600 cursor-pointer"><input type="checkbox" class="cursor-pointer"> Medical Coding</label><label class="flex items-center gap-2 text-[13px] text-slate-600 cursor-pointer"><input type="checkbox" class="cursor-pointer"> Denial Management</label><label class="flex items-center gap-2 text-[13px] text-slate-600 cursor-pointer"><input type="checkbox" class="cursor-pointer"> A/R Follow Up</label><label class="flex items-center gap-2 text-[13px] text-slate-600 cursor-pointer"><input type="checkbox" class="cursor-pointer"> Prior Authorization</label></div></div>
        <div class="sm:col-span-2"><label class="block text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Additional Notes</label><textarea rows="4" class="w-full border border-slate-200 px-4 py-3 text-[14px] outline-none focus:border-brand-teal resize-none transition-colors" placeholder="Tell us more about your billing challenges or what you're looking for..."></textarea></div>
      </div>
      <button type="submit" class="w-full bg-brand-navy text-white font-bold text-[13px] uppercase tracking-widest py-4 hover:bg-brand-teal hover:text-brand-navy transition-all cursor-pointer">Submit Provider Form</button>
    </form>
  </div>
</section>
{CTA}
{FOOTER}'''
write(f'{B}/resources/provider-form/index.html', head('Provider Enrollment Form') + content)

# ═══════════════════════════════════════════════════════════════════════════════
# INSURANCE PARTNERS
# ═══════════════════════════════════════════════════════════════════════════════
payers = ['Medicare','Medicaid','Blue Cross Blue Shield','Aetna','UnitedHealthcare','Cigna','Humana','Molina Healthcare','WellCare','Oscar Health','Anthem','Centene Corporation','MetroPlus','EmblemHealth','HealthFirst','AmeriHealth','Fidelis Care','MVP Health Care','Excellus BlueCross BlueShield','Capital BlueCross','Highmark','Independence Blue Cross','Geisinger Health Plan','UPMC Health Plan','Tufts Health Plan','Harvard Pilgrim Health Care','Fallon Health','Health New England','Community Health Options','Friday Health Plans','Bright Health','Celtic Insurance','Sendero Health Plans','Scott & White Health Plan','PreferredOne','UCare','Medica','HealthPartners','Sanford Health Plan','Avera Health Plans','Sandhills Center','WPS Health Insurance','Dean Health Plan','Group Health Cooperative','Moda Health','PacificSource Health Plans','Providence Health Plan','Regence BlueCross BlueShield','SelectHealth','Arches Health Plan']
payer_grid = ''.join(f'<div class="bg-white border border-slate-200 px-5 py-4 text-center text-[13px] text-slate-600 font-medium hover:border-brand-teal hover:text-brand-teal transition-all">{p}</div>' for p in payers)
content = f'''
{TOPBAR}
{header()}
{banner('Insurance Partners','<span class="mx-2">/</span> Resources <span class="mx-2">/</span> Insurance Partners','ZettaRCM submits claims to all major insurance payers and manages credentialing nationwide.')}
<section class="py-16 px-6 bg-slate-50">
  <div class="max-w-7xl mx-auto">
    <div class="text-center max-w-2xl mx-auto mb-10">
      <p class="text-[15px] text-slate-600 font-light leading-relaxed">We work with hundreds of insurance payers including all Medicare and Medicaid programs, every major commercial insurer, and regional health plans across all 50 states. If you accept it, we can bill it.</p>
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3">{payer_grid}</div>
    <div class="mt-10 bg-brand-navy p-8 text-center">
      <h3 class="text-white font-bold text-[18px] mb-2">Don\'t See Your Payer?</h3>
      <p class="text-slate-400 text-[13px] mb-5 font-light">We work with virtually every payer — contact us and we\'ll confirm coverage for your specific insurers.</p>
      <a href="/contact/" class="inline-block bg-brand-teal text-brand-navy font-bold text-[13px] uppercase tracking-wider px-8 py-3.5 hover:bg-white transition-all">Contact Us</a>
    </div>
  </div>
</section>
{CTA}
{FOOTER}'''
write(f'{B}/resources/insurance-partners/index.html', head('Insurance Partners') + content)

# ═══════════════════════════════════════════════════════════════════════════════
# PRIVACY POLICY
# ═══════════════════════════════════════════════════════════════════════════════
content = f'''
{TOPBAR}
{header()}
{banner('Privacy Policy','<span class="mx-2">/</span> Privacy Policy','How ZettaRCM collects, uses, and protects your information.')}
<section class="py-16 px-6 bg-white">
  <div class="max-w-4xl mx-auto prose-style space-y-8">
    <div class="bg-light-bg border border-slate-200 p-5 text-[13px] text-slate-600"><strong>Effective Date:</strong> January 1, 2026 &nbsp;|&nbsp; <strong>Last Updated:</strong> June 1, 2026</div>
    {"".join(f'''<div class="space-y-3">
      <h2 class="text-brand-navy font-bold text-[20px]">{h}</h2>
      <p class="text-[14px] text-slate-600 leading-relaxed font-light">{body}</p>
    </div>''' for h,body in [
      ('1. Information We Collect','ZettaRCM collects information you provide directly to us, such as when you fill out a contact form, request a quote, or enroll as a client. This may include your name, email address, phone number, practice name, National Provider Identifier (NPI), and other professional information. We also collect information about your use of our website through cookies and similar tracking technologies.'),
      ('2. How We Use Your Information','We use the information we collect to provide, maintain, and improve our Revenue Cycle Management services; communicate with you about our services, promotions, and events; process transactions and send related information; respond to your comments and questions; and comply with legal obligations. We do not sell, trade, or otherwise transfer your personally identifiable information to third parties without your consent, except as described in this policy.'),
      ('3. HIPAA Compliance','ZettaRCM is a Business Associate under the Health Insurance Portability and Accountability Act (HIPAA). We enter into Business Associate Agreements (BAAs) with all covered entities we serve. Protected Health Information (PHI) is handled in full compliance with HIPAA Privacy Rule and Security Rule requirements. We implement administrative, physical, and technical safeguards to protect PHI from unauthorized access, use, or disclosure.'),
      ('4. Information Sharing','We may share your information with third-party vendors and service providers who assist us in providing our services, subject to confidentiality obligations. We may also share information when required by law, such as in response to a subpoena or court order, or to protect the rights, property, or safety of ZettaRCM, our clients, or others.'),
      ('5. Data Security','We implement industry-standard security measures to protect your information, including SSL encryption, secure data centers, access controls, and regular security assessments. However, no method of transmission over the Internet or electronic storage is 100% secure, and we cannot guarantee absolute security.'),
      ('6. Cookies and Tracking','Our website uses cookies and similar tracking technologies to enhance your browsing experience, analyze site traffic, and understand user behavior. You can control cookie settings through your browser settings. Disabling cookies may affect the functionality of our website.'),
      ('7. Your Rights','You have the right to access, correct, or delete your personal information. You may also opt out of marketing communications at any time by clicking "unsubscribe" in any email or contacting us directly. To exercise these rights, contact us at privacy@zettarcm.com.'),
      ('8. Contact Us','If you have any questions about this Privacy Policy or our privacy practices, please contact us at: ZettaRCM, Inc., 134 N 4th St, Brooklyn, NY 11249 | Email: privacy@zettarcm.com | Phone: (800) 516-0192'),
    ])}
  </div>
</section>
{FOOTER}'''
write(f'{B}/privacy-policy/index.html', head('Privacy Policy') + content)

# ═══════════════════════════════════════════════════════════════════════════════
# TERMS AND CONDITIONS
# ═══════════════════════════════════════════════════════════════════════════════
content = f'''
{TOPBAR}
{header()}
{banner('Terms & Conditions','<span class="mx-2">/</span> Terms & Conditions','Please read these terms carefully before using ZettaRCM services.')}
<section class="py-16 px-6 bg-white">
  <div class="max-w-4xl mx-auto space-y-8">
    <div class="bg-light-bg border border-slate-200 p-5 text-[13px] text-slate-600"><strong>Effective Date:</strong> January 1, 2026 &nbsp;|&nbsp; <strong>Last Updated:</strong> June 1, 2026</div>
    {"".join(f'''<div class="space-y-3">
      <h2 class="text-brand-navy font-bold text-[20px]">{h}</h2>
      <p class="text-[14px] text-slate-600 leading-relaxed font-light">{body}</p>
    </div>''' for h,body in [
      ('1. Acceptance of Terms','By accessing or using ZettaRCM\'s website and services, you agree to be bound by these Terms and Conditions and our Privacy Policy. If you do not agree to these terms, please do not use our services. These terms apply to all visitors, users, and clients of ZettaRCM, Inc.'),
      ('2. Services Description','ZettaRCM provides medical billing, coding, credentialing, denial management, revenue cycle management, and related healthcare administrative services. The specific scope of services provided to each client is defined in individual Service Agreements executed between ZettaRCM and the client.'),
      ('3. Client Responsibilities','Clients are responsible for providing accurate and complete information necessary for billing, including patient demographics, insurance information, encounter documentation, and signed authorizations. Clients must promptly notify ZettaRCM of any changes to their practice, payer contracts, or patient information that may affect billing. Clients are responsible for maintaining appropriate medical records to support all claims submitted on their behalf.'),
      ('4. Billing and Payment','ZettaRCM\'s fees are specified in individual Service Agreements and are typically calculated as a percentage of collections. Invoices are issued monthly. Payment is due within 30 days of invoice date. Late payments may be subject to interest charges as specified in the Service Agreement. ZettaRCM reserves the right to suspend services for accounts more than 60 days past due.'),
      ('5. HIPAA and Confidentiality','Both parties agree to comply with all applicable HIPAA requirements. ZettaRCM will execute a Business Associate Agreement (BAA) with each covered entity client. Both parties agree to maintain the confidentiality of all protected health information and proprietary business information shared in the course of the service relationship.'),
      ('6. Limitation of Liability','ZettaRCM\'s liability for any claim arising out of or related to our services shall not exceed the fees paid by the client in the three months preceding the claim. ZettaRCM shall not be liable for indirect, incidental, special, or consequential damages. ZettaRCM does not guarantee specific revenue outcomes, as reimbursements are ultimately determined by payers.'),
      ('7. Termination','Either party may terminate the service agreement with 60 days written notice. ZettaRCM may terminate immediately for material breach, non-payment, or conduct that poses legal or compliance risks. Upon termination, ZettaRCM will provide a transition period to ensure continuity of billing operations.'),
      ('8. Governing Law','These Terms and Conditions are governed by the laws of the State of New York. Any disputes shall be resolved in the state or federal courts located in New York County, New York, and both parties consent to the exclusive jurisdiction of such courts.'),
      ('9. Contact','For questions about these Terms, contact: ZettaRCM, Inc., 134 N 4th St, Brooklyn, NY 11249 | legal@zettarcm.com | (800) 516-0192'),
    ])}
  </div>
</section>
{FOOTER}'''
write(f'{B}/terms-and-conditions/index.html', head('Terms & Conditions') + content)

print('\n✅ All remaining pages generated successfully!')
print(f'Total: our-company, nationwide, contact, blog, FAQs, case-studies, rcm-library, newsroom, provider-form, insurance-partners, privacy-policy, terms-and-conditions')
