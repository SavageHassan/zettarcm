#!/usr/bin/env python3
"""Generate all ZettaRCM pages with consistent header/footer."""
import os

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | ZettaRCM — Medical Billing & Revenue Cycle Management</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/@tailwindcss/browser@4"></script>
  <style type="text/tailwindcss">
    @theme {{
      --color-brand-navy: #1B3A6B;
      --color-brand-teal: #00B8D4;
      --color-light-bg: #F5F8FF;
    }}
    * {{ font-family: 'Inter', sans-serif; box-sizing: border-box; }}
    .dropdown-parent:hover > .dropdown-menu {{ display: block; }}
    .dropdown-menu {{ display: none; }}
    .faq-answer {{ display: none; }}
    .faq-item.open .faq-answer {{ display: block; }}
    .faq-item.open .faq-icon {{ transform: rotate(45deg); }}
    .faq-icon {{ transition: transform 0.2s; }}
  </style>
</head>
<body class="bg-white text-slate-800">
'''

TOPBAR = '''  <div class="w-full bg-brand-navy text-[12px] text-slate-300 py-2.5 px-4">
    <div class="max-w-7xl mx-auto flex flex-wrap justify-between items-center gap-2">
      <div class="flex flex-wrap gap-5 items-center">
        <a href="tel:+18005160192" class="hover:text-white transition-colors flex items-center gap-1.5"><svg class="w-3 h-3 fill-brand-teal" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>(800) 516-0192</a>
        <a href="tel:+17183030192" class="hover:text-white transition-colors flex items-center gap-1.5"><svg class="w-3 h-3 fill-brand-teal" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>(718) 303-0192</a>
        <a href="mailto:info@zettarcm.com" class="hover:text-white transition-colors flex items-center gap-1.5"><svg class="w-3 h-3 fill-brand-teal" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>info@zettarcm.com</a>
      </div>
      <div class="flex items-center gap-4">
        <a href="/#quote" class="text-brand-teal hover:text-white transition-colors font-medium">Free Practice Audit</a>
        <span class="text-slate-600">|</span>
        <span class="flex items-center gap-1.5"><span class="w-1.5 h-1.5 bg-green-400 rounded-full"></span>HIPAA Secure</span>
      </div>
    </div>
  </div>'''

HEADER = '''  <header class="w-full bg-white border-b border-slate-200 sticky top-0 z-50 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 flex items-center justify-between h-[72px]">
      <a href="/" class="flex items-center gap-3 shrink-0">
        <svg width="44" height="44" viewBox="0 0 44 44" fill="none"><rect width="44" height="44" rx="4" fill="#1B3A6B"/><path d="M8 28 Q13 18 18 22 Q23 26 28 16 Q33 6 38 16" stroke="#00B8D4" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M8 32 Q13 22 18 26 Q23 30 28 20 Q33 10 38 20" stroke="white" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.5"/></svg>
        <div><div class="text-[22px] font-bold text-brand-navy leading-none tracking-tight">Zetta<span class="text-brand-teal">RCM</span></div><div class="text-[9px] tracking-[0.22em] text-slate-400 uppercase font-medium mt-0.5">Revenue Cycle Management</div></div>
      </a>
      <nav class="hidden lg:flex items-center h-full text-[13.5px] font-medium text-brand-navy">
        <a href="/" class="px-4 h-full flex items-center border-b-2 border-transparent hover:border-brand-teal hover:text-brand-teal transition-colors">Home</a>
        <div class="dropdown-parent relative h-full flex items-center">
          <button class="px-4 h-full flex items-center gap-1 hover:text-brand-teal transition-colors cursor-pointer border-b-2 border-transparent hover:border-brand-teal">Why ZettaRCM <svg class="w-3 h-3 fill-current opacity-60" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></button>
          <div class="dropdown-menu absolute top-full left-0 bg-white border border-slate-200 shadow-xl z-50 py-1 min-w-[220px]">
            <a href="/our-company/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Our Company</a>
            <a href="/nationwide-medical-billing/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Nationwide Medical Billing</a>
          </div>
        </div>
        <div class="dropdown-parent relative h-full flex items-center">
          <button class="px-4 h-full flex items-center gap-1 hover:text-brand-teal transition-colors cursor-pointer border-b-2 border-transparent hover:border-brand-teal">Services <svg class="w-3 h-3 fill-current opacity-60" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></button>
          <div class="dropdown-menu absolute top-full left-0 bg-white border border-slate-200 shadow-xl z-50 py-1 min-w-[260px]">
            <a href="/services/medical-billing/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Medical Billing</a>
            <a href="/services/medical-credentialing/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Medical Credentialing</a>
            <a href="/services/medical-coding/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Medical Coding</a>
            <a href="/services/denial-management/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Denial Management</a>
            <a href="/services/ar-follow-up/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">A/R Follow Up</a>
            <a href="/services/out-of-network-billing/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Out of Network Billing</a>
            <a href="/services/revenue-cycle-management/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Revenue Cycle Management</a>
            <a href="/services/prior-authorization/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Prior Authorization</a>
            <a href="/services/front-office-management/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Front Office Management</a>
            <a href="/services/quality-payment-program/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Quality Payment Program</a>
            <a href="/services/eligibility-verification/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Eligibility Verification</a>
            <a href="/services/patient-billing/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Patient Billing</a>
            <a href="/services/payment-posting/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Payment Posting</a>
            <div class="mx-4 my-1 border-t border-slate-100"></div>
            <a href="/services/" class="block px-5 py-3 text-[13px] text-brand-teal font-semibold hover:bg-light-bg transition-all">View All Services →</a>
          </div>
        </div>
        <div class="dropdown-parent relative h-full flex items-center">
          <button class="px-4 h-full flex items-center gap-1 hover:text-brand-teal transition-colors cursor-pointer border-b-2 border-transparent hover:border-brand-teal">Specialties <svg class="w-3 h-3 fill-current opacity-60" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></button>
          <div class="dropdown-menu absolute top-full left-0 bg-white border border-slate-200 shadow-xl z-50 py-1 min-w-[220px]">
            <a href="/specialties/mental-health/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Mental Health</a>
            <a href="/specialties/cardiology/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Cardiology</a>
            <a href="/specialties/radiology/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Radiology</a>
            <a href="/specialties/orthopedics/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Orthopedics</a>
            <a href="/specialties/oncology/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Oncology</a>
            <div class="mx-4 my-1 border-t border-slate-100"></div>
            <a href="/specialties/" class="block px-5 py-3 text-[13px] text-brand-teal font-semibold hover:bg-light-bg transition-all">All 35 Specialties →</a>
          </div>
        </div>
        <div class="dropdown-parent relative h-full flex items-center">
          <button class="px-4 h-full flex items-center gap-1 hover:text-brand-teal transition-colors cursor-pointer border-b-2 border-transparent hover:border-brand-teal">Domain Areas <svg class="w-3 h-3 fill-current opacity-60" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></button>
          <div class="dropdown-menu absolute top-full left-0 bg-white border border-slate-200 shadow-xl z-50 py-1 min-w-[200px]">
            <a href="#" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Revenue Partners</a>
            <a href="#" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Premier Billing State</a>
            <a href="#" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Pioneer States Hub</a>
          </div>
        </div>
        <div class="dropdown-parent relative h-full flex items-center">
          <button class="px-4 h-full flex items-center gap-1 hover:text-brand-teal transition-colors cursor-pointer border-b-2 border-transparent hover:border-brand-teal">Resources <svg class="w-3 h-3 fill-current opacity-60" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></button>
          <div class="dropdown-menu absolute top-full right-0 bg-white border border-slate-200 shadow-xl z-50 py-1 min-w-[200px]">
            <a href="/resources/blog/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Blog</a>
            <a href="/resources/rcm-library/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">RCM Library</a>
            <a href="/resources/newsroom/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Newsroom</a>
            <a href="/resources/case-studies/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Case Studies</a>
            <a href="/resources/faqs/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">FAQs</a>
            <a href="/resources/provider-form/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-light-bg hover:text-brand-teal transition-all border-l-2 border-transparent hover:border-brand-teal">Provider Form</a>
          </div>
        </div>
        <a href="/contact/" class="px-4 h-full flex items-center hover:text-brand-teal transition-colors border-b-2 border-transparent hover:border-brand-teal">Contact Us</a>
      </nav>
      <button class="hidden lg:flex items-center justify-center w-11 h-11 bg-brand-navy hover:bg-brand-teal transition-colors shrink-0">
        <svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
      </button>
    </div>
  </header>'''

PAGE_BANNER = '''  <section class="bg-brand-navy py-14 px-6">
    <div class="max-w-7xl mx-auto">
      <div class="text-[11px] text-slate-400 uppercase tracking-wider mb-3"><a href="/" class="hover:text-brand-teal transition-colors">Home</a>{breadcrumb}</div>
      <h1 class="text-3xl md:text-[42px] font-bold text-white leading-tight">{page_title}</h1>
      <p class="text-[15px] text-slate-400 mt-3 font-light max-w-2xl">{subtitle}</p>
    </div>
  </section>'''

CTA_STRIP = '''  <section class="bg-brand-teal py-12 px-6">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6">
      <div>
        <h3 class="text-brand-navy font-bold text-2xl">Ready to Increase Your Practice Revenue?</h3>
        <p class="text-brand-navy/70 text-[14px] mt-1">Get a free practice audit and see how much you\'re leaving on the table.</p>
      </div>
      <div class="flex gap-3 shrink-0">
        <a href="/#quote" class="bg-brand-navy text-white font-bold text-[13px] uppercase tracking-wider px-8 py-4 hover:bg-white hover:text-brand-navy transition-all">Get Free Audit</a>
        <a href="tel:+18005160192" class="border-2 border-brand-navy text-brand-navy font-bold text-[13px] uppercase tracking-wider px-6 py-4 hover:bg-brand-navy hover:text-white transition-all">(800) 516-0192</a>
      </div>
    </div>
  </section>'''

FOOTER = '''  <footer class="bg-brand-navy pt-16 pb-8 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
      <div class="space-y-4">
        <div><div class="text-white font-bold text-2xl">Zetta<span class="text-brand-teal">RCM</span></div><div class="text-[9px] text-slate-500 tracking-[0.25em] uppercase mt-0.5">Revenue Cycle Management</div></div>
        <p class="text-[13px] text-slate-400 leading-relaxed font-light">A complete Revenue Cycle Management solution that streamlines reimbursements and delivers remarkable results nationwide.</p>
        <div class="space-y-1.5 text-[13px] text-slate-400">
          <div>134 N 4th St, Brooklyn, NY 11249</div>
          <div><a href="tel:+18005160192" class="hover:text-brand-teal transition-colors">(800) 516-0192</a></div>
          <div><a href="mailto:info@zettarcm.com" class="hover:text-brand-teal transition-colors">info@zettarcm.com</a></div>
        </div>
      </div>
      <div class="space-y-4">
        <div class="text-white font-bold text-[13px] uppercase tracking-wider border-b border-slate-700 pb-3">Our Services</div>
        <ul class="space-y-2 text-[13px] text-slate-400">
          <li><a href="/services/medical-billing/" class="hover:text-brand-teal transition-colors">Medical Billing</a></li>
          <li><a href="/services/medical-credentialing/" class="hover:text-brand-teal transition-colors">Medical Credentialing</a></li>
          <li><a href="/services/medical-coding/" class="hover:text-brand-teal transition-colors">Medical Coding</a></li>
          <li><a href="/services/denial-management/" class="hover:text-brand-teal transition-colors">Denial Management</a></li>
          <li><a href="/services/ar-follow-up/" class="hover:text-brand-teal transition-colors">A/R Follow Up</a></li>
          <li><a href="/services/revenue-cycle-management/" class="hover:text-brand-teal transition-colors">Revenue Cycle Management</a></li>
          <li><a href="/services/" class="text-brand-teal font-medium hover:text-white transition-colors">View All Services →</a></li>
        </ul>
      </div>
      <div class="space-y-4">
        <div class="text-white font-bold text-[13px] uppercase tracking-wider border-b border-slate-700 pb-3">Specialties</div>
        <ul class="space-y-2 text-[13px] text-slate-400">
          <li><a href="/specialties/mental-health/" class="hover:text-brand-teal transition-colors">Mental Health</a></li>
          <li><a href="/specialties/cardiology/" class="hover:text-brand-teal transition-colors">Cardiology</a></li>
          <li><a href="/specialties/orthopedics/" class="hover:text-brand-teal transition-colors">Orthopedics</a></li>
          <li><a href="/specialties/radiology/" class="hover:text-brand-teal transition-colors">Radiology</a></li>
          <li><a href="/specialties/oncology/" class="hover:text-brand-teal transition-colors">Oncology</a></li>
          <li><a href="/specialties/" class="text-brand-teal font-medium hover:text-white transition-colors">All 35 Specialties →</a></li>
        </ul>
      </div>
      <div class="space-y-4">
        <div class="text-white font-bold text-[13px] uppercase tracking-wider border-b border-slate-700 pb-3">Company</div>
        <ul class="space-y-2 text-[13px] text-slate-400">
          <li><a href="/our-company/" class="hover:text-brand-teal transition-colors">Our Company</a></li>
          <li><a href="/resources/blog/" class="hover:text-brand-teal transition-colors">Blog</a></li>
          <li><a href="/resources/case-studies/" class="hover:text-brand-teal transition-colors">Case Studies</a></li>
          <li><a href="/resources/faqs/" class="hover:text-brand-teal transition-colors">FAQs</a></li>
          <li><a href="/contact/" class="hover:text-brand-teal transition-colors">Contact Us</a></li>
          <li><a href="/privacy-policy/" class="hover:text-brand-teal transition-colors">Privacy Policy</a></li>
          <li><a href="/terms-and-conditions/" class="hover:text-brand-teal transition-colors">Terms & Conditions</a></li>
        </ul>
      </div>
    </div>
    <div class="max-w-7xl mx-auto pt-8 border-t border-slate-800 flex flex-col sm:flex-row justify-between items-center text-[12px] text-slate-600 gap-3">
      <span>© 2026, ZettaRCM, Inc. All Rights Reserved.</span>
      <div class="flex gap-5"><a href="/privacy-policy/" class="hover:text-slate-400 transition-colors">Privacy Policy</a><a href="/terms-and-conditions/" class="hover:text-slate-400 transition-colors">Terms & Conditions</a></div>
    </div>
  </footer>
</body>
</html>'''

SIDEBAR = '''        <div class="space-y-5">
          <div class="bg-brand-navy p-6">
            <h4 class="text-white font-bold text-[15px] mb-4">Get A Free Quote</h4>
            <form class="space-y-3" onsubmit="event.preventDefault()">
              <input type="text" placeholder="Full Name *" class="w-full bg-white/10 border border-white/20 text-white text-[13px] px-3 py-2.5 outline-none focus:border-brand-teal placeholder-slate-400">
              <input type="email" placeholder="Email Address *" class="w-full bg-white/10 border border-white/20 text-white text-[13px] px-3 py-2.5 outline-none focus:border-brand-teal placeholder-slate-400">
              <input type="tel" placeholder="Phone Number *" class="w-full bg-white/10 border border-white/20 text-white text-[13px] px-3 py-2.5 outline-none focus:border-brand-teal placeholder-slate-400">
              <select class="w-full bg-white/10 border border-white/20 text-slate-300 text-[13px] px-3 py-2.5 outline-none focus:border-brand-teal">
                <option>Select Service</option>
                <option>Medical Billing</option>
                <option>Credentialing</option>
                <option>Medical Coding</option>
                <option>Denial Management</option>
                <option>Revenue Cycle Management</option>
              </select>
              <button type="submit" class="w-full bg-brand-teal text-brand-navy font-bold text-[12px] uppercase tracking-wider py-3 hover:bg-white transition-all cursor-pointer">Submit Request</button>
            </form>
          </div>
          <div class="border border-slate-200 p-5 space-y-3">
            <h4 class="text-brand-navy font-bold text-[14px]">Speak to an Expert</h4>
            <a href="tel:+18005160192" class="flex items-center gap-3 text-brand-teal font-bold text-[16px]"><svg class="w-5 h-5 fill-brand-teal" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>(800) 516-0192</a>
            <p class="text-[12px] text-slate-500">Available 24/7 for your practice</p>
          </div>
          <div class="bg-light-bg border border-slate-200 p-5 space-y-2">
            <h4 class="text-brand-navy font-bold text-[13px] uppercase tracking-wider">Other Services</h4>
            <ul class="space-y-1.5 text-[13px] text-slate-600">
              <li><a href="/services/medical-billing/" class="hover:text-brand-teal transition-colors flex items-center gap-2"><svg class="w-3 h-3 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>Medical Billing</a></li>
              <li><a href="/services/medical-credentialing/" class="hover:text-brand-teal transition-colors flex items-center gap-2"><svg class="w-3 h-3 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>Medical Credentialing</a></li>
              <li><a href="/services/denial-management/" class="hover:text-brand-teal transition-colors flex items-center gap-2"><svg class="w-3 h-3 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>Denial Management</a></li>
              <li><a href="/services/ar-follow-up/" class="hover:text-brand-teal transition-colors flex items-center gap-2"><svg class="w-3 h-3 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>A/R Follow Up</a></li>
              <li><a href="/services/prior-authorization/" class="hover:text-brand-teal transition-colors flex items-center gap-2"><svg class="w-3 h-3 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>Prior Authorization</a></li>
              <li><a href="/services/" class="text-brand-teal font-semibold flex items-center gap-2"><svg class="w-3 h-3 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>All Services</a></li>
            </ul>
          </div>
        </div>'''

def make_page(path, title, breadcrumb, subtitle, content):
    html = HEAD.format(title=title)
    html += TOPBAR + '\n'
    html += HEADER + '\n'
    html += PAGE_BANNER.format(breadcrumb=breadcrumb, page_title=title, subtitle=subtitle) + '\n'
    html += content + '\n'
    html += CTA_STRIP + '\n'
    html += FOOTER
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(html)
    print(f'✓ {path}')

def service_page(slug, title, subtitle, intro, points, img_url):
    bullet_html = ''.join(f'''
              <div class="flex gap-3 py-3 border-b border-slate-100 last:border-0">
                <svg class="w-5 h-5 fill-brand-teal shrink-0 mt-0.5" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg>
                <span class="text-[14px] text-slate-600">{p}</span>
              </div>''' for p in points)
    content = f'''  <section class="py-16 px-6 bg-white">
    <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-12">
      <div class="lg:col-span-2 space-y-8">
        <img src="{img_url}" alt="{title}" class="w-full h-64 object-cover">
        <div class="prose max-w-none">
          <p class="text-[15px] text-slate-600 leading-relaxed font-light">{intro}</p>
        </div>
        <div class="bg-light-bg border border-slate-200 p-7">
          <h3 class="text-brand-navy font-bold text-[18px] mb-4">What We Provide</h3>
          <div class="divide-y divide-slate-100">{bullet_html}
          </div>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div class="bg-brand-navy p-6 text-center"><div class="text-3xl font-bold text-brand-teal">99.2%</div><div class="text-[11px] text-slate-400 uppercase tracking-wider mt-1">First-Pass Rate</div></div>
          <div class="bg-brand-navy p-6 text-center"><div class="text-3xl font-bold text-white">+30%</div><div class="text-[11px] text-slate-400 uppercase tracking-wider mt-1">Revenue Increase</div></div>
          <div class="bg-brand-navy p-6 text-center"><div class="text-3xl font-bold text-brand-teal">24/7</div><div class="text-[11px] text-slate-400 uppercase tracking-wider mt-1">Support Available</div></div>
        </div>
      </div>
      <div>
{SIDEBAR}
      </div>
    </div>
  </section>'''
    return content

def specialty_page(name, subtitle, intro, points, img_url):
    bullet_html = ''.join(f'''
              <div class="flex gap-3 py-3 border-b border-slate-100 last:border-0">
                <svg class="w-5 h-5 fill-brand-teal shrink-0 mt-0.5" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg>
                <span class="text-[14px] text-slate-600">{p}</span>
              </div>''' for p in points)
    return f'''  <section class="py-16 px-6 bg-white">
    <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-12">
      <div class="lg:col-span-2 space-y-8">
        <img src="{img_url}" alt="{name} Billing" class="w-full h-64 object-cover">
        <p class="text-[15px] text-slate-600 leading-relaxed font-light">{intro}</p>
        <div class="bg-light-bg border border-slate-200 p-7">
          <h3 class="text-brand-navy font-bold text-[18px] mb-4">Our {name} Billing Services Include</h3>
          <div class="divide-y divide-slate-100">{bullet_html}
          </div>
        </div>
        <div class="bg-brand-navy p-8 flex flex-col md:flex-row items-center gap-6">
          <div><div class="text-brand-teal font-bold text-[18px]">Specialized {name} Billing Experts</div><div class="text-slate-400 text-[13px] mt-1 font-light">Our certified team knows the unique coding and payer rules for {name}.</div></div>
          <a href="/#quote" class="shrink-0 bg-brand-teal text-brand-navy font-bold text-[12px] uppercase tracking-wider px-7 py-3.5 hover:bg-white transition-all">Get A Free Quote</a>
        </div>
      </div>
      <div>
{SIDEBAR}
      </div>
    </div>
  </section>'''

BASE = '/Users/mac/zettarcm'

# ─── SERVICE PAGES ───────────────────────────────────────────────────────────
services = [
    ('medical-billing', 'Medical Billing Services',
     'Accurate, fast, HIPAA-compliant billing for healthcare providers nationwide.',
     'At ZettaRCM, our medical billing services are designed to maximize your reimbursements while reducing administrative burdens. Our certified billing professionals manage every step of the revenue cycle — from charge entry through final payment posting — ensuring that no revenue is left behind.',
     ['Electronic claim submission within 24 hours of service','Payer-specific billing rules applied automatically','Real-time claim status tracking and reporting','Patient statement generation and mailing','Secondary and tertiary claim filing','HIPAA-compliant EDI transactions','Customized billing reports delivered monthly'],
     'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=900&q=80&fit=crop'),
    ('medical-credentialing', 'Medical Credentialing Services',
     'Fast, accurate provider credentialing and payer enrollment — nationwide.',
     'Provider credentialing is the gateway to getting paid by insurance companies. Without proper credentialing, even perfectly coded claims will be denied. ZettaRCM\'s credentialing specialists handle the entire enrollment process for you — primary source verification, CAQH setup, payer contracting, and ongoing re-credentialing.',
     ['CAQH profile setup and maintenance','Primary source verification with all licensing boards','Payer enrollment for Medicare, Medicaid, and commercial insurers','Hospital privileges credentialing','Re-credentialing and expiration tracking','Group and individual provider enrollment','Contract negotiation support'],
     'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=900&q=80&fit=crop'),
    ('medical-coding', 'Medical Coding Services',
     'ICD-10-CM, CPT, and HCPCS coding by AAPC-certified specialists.',
     'Accurate medical coding is the foundation of successful billing. At ZettaRCM, our AAPC-certified coders apply the correct ICD-10-CM diagnosis codes, CPT procedure codes, and HCPCS Level II codes to every encounter — maximizing your reimbursement while keeping you fully compliant with payer and CMS guidelines.',
     ['ICD-10-CM diagnosis coding for all specialties','CPT and HCPCS Level II procedure coding','Evaluation & Management (E&M) coding optimization','Modifiers applied accurately to prevent denials','Annual CPT code update implementation','Coding audits and compliance reviews','DRG coding for inpatient facilities'],
     'https://images.unsplash.com/photo-1563986768609-322da13575f3?w=900&q=80&fit=crop'),
    ('denial-management', 'Denial Management Services',
     'Identify, appeal, and recover denied claims to protect your revenue.',
     'Insurance denials are a significant drain on practice revenue — the average practice loses up to 15% of revenue to uncollected denied claims. ZettaRCM\'s denial management team analyzes every denial, identifies root causes, files appeals, and implements process improvements to prevent recurrence.',
     ['Root cause analysis for every denied claim','Timely appeals filed within payer deadlines','Medical necessity denial resolution','Coding-related denial correction and resubmission','Prior authorization denial appeals','Systematic denial trend reporting and prevention','Peer-to-peer review facilitation'],
     'https://images.unsplash.com/photo-1504813184591-01572f98c85f?w=900&q=80&fit=crop'),
    ('ar-follow-up', 'A/R Follow Up Services',
     'Chase every outstanding dollar with proactive accounts receivable follow-up.',
     'Aging accounts receivable is money that belongs to your practice. ZettaRCM\'s dedicated A/R specialists proactively follow up on all outstanding claims — contacting payers by phone, portal, and correspondence — ensuring you collect every dollar you\'ve earned.',
     ['Systematic follow-up on all claims over 30 days','Payer portal and phone-based claim status checks','Insurance payment reconciliation','Underpayment identification and recovery','Patient balance follow-up and collections','A/R aging reports with actionable insights','Clean-up projects for high aging backlogs'],
     'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=900&q=80&fit=crop'),
    ('out-of-network-billing', 'Out of Network Billing Services',
     'Maximize reimbursements on out-of-network claims and avoid underpayments.',
     'Out-of-network billing requires specialized expertise to navigate the complex rules around usual and customary rates, balance billing regulations, and No Surprises Act compliance. ZettaRCM\'s OON specialists ensure you receive fair compensation for every out-of-network service.',
     ['Usual and customary rate negotiations','No Surprises Act compliance and IDR process support','Out-of-network benefit verification prior to service','Gap exception and single case agreement negotiations','OON claim submission to all major payers','Underpayment dispute resolution','State-specific OON billing regulation compliance'],
     'https://images.unsplash.com/photo-1633158829875-e5316a358c6f?w=900&q=80&fit=crop'),
    ('revenue-cycle-management', 'Revenue Cycle Management',
     'End-to-end RCM solutions that transform your practice\'s financial performance.',
     'Revenue Cycle Management encompasses every process from the moment a patient schedules an appointment to the final payment collected. ZettaRCM provides comprehensive, end-to-end RCM services that optimize your entire revenue pipeline — so you can focus on clinical care while we maximize your financial performance.',
     ['Patient scheduling and insurance verification','Prior authorization management','Charge capture and medical coding','Claim submission and clearinghouse management','Payment posting and reconciliation','Denial management and appeals','Patient collections and payment plans','Analytics and performance reporting'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('prior-authorization', 'Prior Authorization Services',
     'Faster prior authorization approvals — fewer delays, fewer denials.',
     'Prior authorizations are one of the biggest administrative burdens in healthcare — and a leading cause of claim denials. ZettaRCM\'s dedicated prior auth team handles the entire process: determining auth requirements, submitting requests, following up with payers, and escalating urgent cases.',
     ['Insurance coverage and auth requirement verification','Electronic and phone-based PA submissions','Clinical documentation preparation and submission','Urgent and expedited auth processing','Auth denial appeals and peer-to-peer support','Ongoing auth tracking and status updates','Retroactive authorization requests'],
     'https://images.unsplash.com/photo-1581056771107-24ca5f033842?w=900&q=80&fit=crop'),
    ('front-office-management', 'Front Office Management',
     'Streamlined patient intake, scheduling, and eligibility verification.',
     'The front office is where the revenue cycle begins. Errors in scheduling, eligibility verification, and patient registration lead to claim denials downstream. ZettaRCM\'s front office management services create a solid foundation for clean claims and faster payments.',
     ['Patient appointment scheduling and reminder calls','Insurance eligibility and benefits verification','Copay and deductible collection at time of service','Patient demographic and insurance data entry','Referral and authorization coordination','New patient intake and registration','Check-in and check-out workflow optimization'],
     'https://images.unsplash.com/photo-1516549655169-df83a0774514?w=900&q=80&fit=crop'),
    ('quality-payment-program', 'Quality Payment Program (QPP/MIPS)',
     'MIPS reporting, value-based care, and QPP optimization for eligible clinicians.',
     'The Quality Payment Program (QPP) and Merit-based Incentive Payment System (MIPS) can either boost or cut your Medicare reimbursements by up to 9% — depending on your performance. ZettaRCM\'s QPP specialists help you report accurately, maximize your composite score, and secure positive payment adjustments.',
     ['MIPS eligibility determination and exemption analysis','Quality measure selection and reporting strategy','Promoting Interoperability (PI) reporting','Improvement Activities (IA) documentation','Cost category performance optimization','Annual MIPS submission to CMS','APM pathway evaluation and strategy'],
     'https://images.unsplash.com/photo-1551190822-a9333d879b1f?w=900&q=80&fit=crop'),
    ('eligibility-verification', 'Eligibility Verification Services',
     'Real-time insurance eligibility checks before every patient encounter.',
     'Verifying patient insurance eligibility before every visit is one of the most effective ways to reduce claim denials and improve collections. ZettaRCM performs real-time eligibility checks across all major payers — identifying coverage, benefits, copays, deductibles, and authorization requirements before the patient arrives.',
     ['Real-time eligibility checks for all major payers','Benefits breakdown: deductible, copay, coinsurance, out-of-pocket','Authorization requirement identification','Coverage termination and secondary insurance verification','Batch eligibility processing for scheduled appointments','Patient financial responsibility communication','Eligibility-related denial prevention'],
     'https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=900&q=80&fit=crop'),
    ('patient-billing', 'Patient Billing Services',
     'Clear, professional patient statements that improve collections and satisfaction.',
     'Patient responsibility collections are increasingly important as high-deductible health plans become the norm. ZettaRCM\'s patient billing services make it easy for patients to understand what they owe and provide convenient ways to pay — improving your patient pay collections without damaging the patient relationship.',
     ['Clear, itemized patient statements by mail and email','Online patient payment portal','Payment plan setup and management','Financial counseling and assistance program referrals','Phone-based patient billing support','Bad debt management and collections','HIPAA-compliant patient communications'],
     'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=900&q=80&fit=crop'),
    ('payment-posting', 'Payment Posting Services',
     'Accurate, timely payment posting and EOB reconciliation.',
     'Payment posting is a critical step in the revenue cycle — accurate posting allows you to quickly identify underpayments, denied claims, and patient balances. ZettaRCM\'s payment posting specialists process ERAs, EOBs, and checks with speed and precision, keeping your A/R clean and your reporting accurate.',
     ['Electronic remittance advice (ERA) auto-posting','Manual EOB payment posting with line-item accuracy','Underpayment identification and flagging','Contractual adjustment reconciliation','Patient balance allocation post-insurance','Deposit reconciliation and bank posting','Real-time payment reports and dashboards'],
     'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=900&q=80&fit=crop'),
]

for slug, title, subtitle, intro, points, img in services:
    bc = f' <span class="mx-2">/</span> <a href="/services/" class="hover:text-brand-teal">Services</a> <span class="mx-2">/</span> {title}'
    content = service_page(slug, title, subtitle, intro, points, img)
    make_page(f'{BASE}/services/{slug}/index.html', title, bc, subtitle, content)

# ─── SERVICES INDEX ──────────────────────────────────────────────────────────
all_services = [
    ('Medical Billing', '/services/medical-billing/', 'Accurate claims, faster payments, maximum reimbursements.', 'M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V8l-6-6zm-1 7V3.5L18.5 9H13zm-2 8H7v-2h4v2zm4-4H7v-2h8v2z'),
    ('Medical Credentialing', '/services/medical-credentialing/', 'Enroll with payers quickly and stay current.', 'M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-9 3h2v2h-2V7zm0 4h2v6h-2v-6zm-4-4h2v2H7V7zm0 4h2v6H7v-6zm8-4h2v2h-2V7zm0 4h2v6h-2v-6z'),
    ('Medical Coding', '/services/medical-coding/', 'ICD-10 & CPT coding by AAPC-certified specialists.', 'M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z'),
    ('Denial Management', '/services/denial-management/', 'Identify causes, appeal denials, recover revenue.', 'M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 4l5 2.18V11c0 3.5-2.33 6.79-5 7.93-2.67-1.14-5-4.43-5-7.93V7.18L12 5z'),
    ('A/R Follow Up', '/services/ar-follow-up/', 'Chase every outstanding dollar proactively.', 'M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6h-6z'),
    ('Out of Network Billing', '/services/out-of-network-billing/', 'Maximize reimbursements on OON claims.', 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z'),
    ('Revenue Cycle Management', '/services/revenue-cycle-management/', 'End-to-end RCM solutions for your entire practice.', 'M12 4V1L8 5l4 4V6c3.31 0 6 2.69 6 6 0 1.01-.25 1.97-.7 2.8l1.46 1.46C19.54 15.03 20 13.57 20 12c0-4.42-3.58-8-8-8zm0 14c-3.31 0-6-2.69-6-6 0-1.01.25-1.97.7-2.8L5.24 7.74C4.46 8.97 4 10.43 4 12c0 4.42 3.58 8 8 8v3l4-4-4-4v3z'),
    ('Prior Authorization', '/services/prior-authorization/', 'Faster approvals, fewer delays, fewer denials.', 'M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z'),
    ('Front Office Management', '/services/front-office-management/', 'Streamlined scheduling, eligibility, and intake.', 'M12 3L2 12h3v8h6v-5h2v5h6v-8h3L12 3z'),
    ('Quality Payment Program', '/services/quality-payment-program/', 'MIPS reporting and value-based care optimization.', 'M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z'),
    ('Eligibility Verification', '/services/eligibility-verification/', 'Real-time insurance verification before every visit.', 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z'),
    ('Patient Billing', '/services/patient-billing/', 'Clear statements that improve patient pay collections.', 'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 3c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm7 13H5v-.23c0-.62.28-1.2.76-1.58C7.47 15.82 9.64 15 12 15s4.53.82 6.24 2.19c.48.38.76.97.76 1.58V19z'),
    ('Payment Posting', '/services/payment-posting/', 'Accurate ERA/EOB posting and reconciliation.', 'M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z'),
]

cards = ''.join(f'''        <a href="{url}" class="group bg-white border border-slate-200 p-8 hover:border-brand-teal hover:shadow-lg transition-all flex flex-col gap-4">
          <div class="w-14 h-14 bg-light-bg border border-slate-200 group-hover:border-brand-teal group-hover:bg-brand-teal/10 flex items-center justify-center transition-all">
            <svg class="w-7 h-7 fill-brand-teal" viewBox="0 0 24 24"><path d="{icon}"/></svg>
          </div>
          <div>
            <h3 class="text-brand-navy font-bold text-[16px] group-hover:text-brand-teal transition-colors">{name}</h3>
            <p class="text-[13px] text-slate-500 mt-2 font-light leading-relaxed">{desc}</p>
          </div>
          <span class="text-brand-teal text-[12px] font-bold uppercase tracking-wider mt-auto flex items-center gap-1.5">Learn More <svg class="w-3 h-3 fill-brand-teal" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg></span>
        </a>''' for name, url, desc, icon in all_services)

services_index_content = f'''  <section class="py-16 px-6 bg-slate-50">
    <div class="max-w-7xl mx-auto">
      <div class="text-center max-w-2xl mx-auto mb-12">
        <p class="text-[15px] text-slate-600 font-light leading-relaxed">ZettaRCM provides a full suite of Revenue Cycle Management services designed to reduce administrative burden, eliminate revenue leakage, and maximize your practice's financial performance.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
{cards}
      </div>
    </div>
  </section>'''

make_page(f'{BASE}/services/index.html', 'All Services', ' <span class="mx-2">/</span> Services', 'End-to-end Revenue Cycle Management services for every healthcare practice.', services_index_content)

# ─── SPECIALTY PAGES ─────────────────────────────────────────────────────────
specialties = [
    ('mental-health', 'Mental Health Billing',
     'Expert billing for psychiatry, psychology, therapy, and behavioral health practices.',
     'Mental health billing is uniquely complex — with modifier requirements, session limits, telehealth rules, and payer-specific credentialing requirements that differ from medical billing. ZettaRCM\'s mental health billing specialists understand the nuances of behavioral health reimbursement and work to maximize your collections while keeping you fully compliant.',
     ['CPT coding for psychotherapy, evaluation, and testing', 'Modifier 95 and GT for telehealth sessions', 'TRICARE and Medicaid behavioral health billing', 'Session limit tracking and authorization management', 'HIPAA-compliant records handling', 'Out-of-network mental health benefit billing', 'Group therapy and family session coding'],
     'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&fit=crop'),
    ('radiology', 'Radiology Billing',
     'Specialized billing for radiology groups, imaging centers, and teleradiology.',
     'Radiology billing requires precise knowledge of global, professional, and technical component billing, along with complex modifiers and site-of-service rules. ZettaRCM\'s radiology billing specialists ensure your imaging claims are coded correctly and paid at the maximum allowable rate.',
     ['Global vs. professional/technical component billing', 'CT, MRI, ultrasound, X-ray, and nuclear medicine coding', 'Modifier 26 and TC application', 'Teleradiology billing compliance', 'Contrast and non-contrast coding accuracy', 'Radiologist group and hospital-based billing', 'RVU-based productivity reporting'],
     'https://images.unsplash.com/photo-1559757175-5700dde675bc?w=900&q=80&fit=crop'),
    ('cardiology', 'Cardiology Billing',
     'Expert billing for cardiologists, cardiac surgeons, and cardiovascular practices.',
     'Cardiology has some of the most complex billing in medicine — with numerous interventional procedures, diagnostic tests, and evaluation codes that must be billed precisely to avoid denials and maximize reimbursement. ZettaRCM\'s cardiology billing team has deep expertise in cardiovascular coding.',
     ['Echocardiography (2D, 3D, stress echo) coding', 'Cardiac catheterization and interventional billing', 'Holter monitor and event recorder billing', 'Nuclear stress test and PET scan coding', 'Electrophysiology procedure coding', 'Pacemaker and ICD implant billing', 'Cardiology E&M visit optimization'],
     'https://images.unsplash.com/photo-1628348068343-c6a848d2b6dd?w=900&q=80&fit=crop'),
    ('neurology', 'Neurology Billing',
     'Specialized medical billing for neurologists and neurology practices.',
     'Neurology billing involves a wide range of diagnostic procedures, electrodiagnostic studies, and complex E&M documentation requirements. ZettaRCM\'s neurology billing specialists ensure every service is accurately coded and billed to maximize your reimbursements.',
     ['EEG, EMG, and nerve conduction study coding', 'Sleep study and polysomnography billing', 'Epilepsy monitoring and deep brain stimulation coding', 'Neurology E&M documentation optimization', 'Infusion and injection procedure billing', 'Botox and neurotoxin injection coding', 'Teleneurology billing compliance'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('neurosurgery', 'Neurosurgery Billing',
     'Precise billing for neurosurgeons and spine surgery practices.',
     'Neurosurgery billing requires exceptional accuracy — with high-value procedures, complex modifier rules, and strict documentation requirements. ZettaRCM\'s neurosurgery billing team ensures every procedure is captured accurately and reimbursed fully.',
     ['Cranial and spinal surgery CPT coding', 'Spine fusion and disc procedure billing', 'Deep brain stimulator implant coding', 'Global period and multiple procedure modifier management', 'Assistant surgeon and co-surgery billing', 'Hospital and ASC facility billing coordination', 'Neurosurgery E&M documentation'],
     'https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=900&q=80&fit=crop'),
    ('dermatology', 'Dermatology Billing',
     'Expert billing for dermatologists, Mohs surgeons, and cosmetic practices.',
     'Dermatology billing spans medical, surgical, and cosmetic procedures — each with distinct coding requirements and payer rules. ZettaRCM\'s dermatology billing specialists know how to properly code skin procedures to maximize your reimbursements and minimize denials.',
     ['Skin lesion removal and destruction coding', 'Mohs surgery coding and billing', 'Biopsy and pathology coordination billing', 'Phototherapy and photodynamic therapy coding', 'Cosmetic vs. medical procedure distinction', 'Derm E&M and new vs. established patient coding', 'Acne, psoriasis, and chronic condition billing'],
     'https://images.unsplash.com/photo-1612531386530-97286d97c2d2?w=900&q=80&fit=crop'),
    ('orthopedics', 'Orthopedic Billing',
     'Specialized billing for orthopedic surgeons and musculoskeletal practices.',
     'Orthopedic billing involves complex surgical procedures, fracture management, and joint replacement coding that requires specialist-level expertise. ZettaRCM\'s orthopedic billing team ensures every procedure — from office visits to major surgeries — is captured and billed correctly.',
     ['Joint replacement (hip, knee, shoulder) billing', 'Fracture care and casting coding', 'Arthroscopy and minimally invasive surgery coding', 'Spinal fusion and disc procedure billing', 'Orthopedic injection and aspiration coding', 'Workers\' compensation and auto accident billing', 'DME and orthotic billing coordination'],
     'https://images.unsplash.com/photo-1530026186672-2cd00ffc50fe?w=900&q=80&fit=crop'),
    ('pediatrics', 'Pediatrics Billing',
     'Accurate billing for pediatricians and pediatric subspecialists.',
     'Pediatric billing has unique requirements — well-child visits, immunizations, developmental screening, and age-specific coding rules. ZettaRCM\'s pediatric billing specialists ensure your practice captures revenue for every preventive and sick visit.',
     ['Well-child visit (EPSDT) coding and billing', 'Immunization administration and vaccine billing', 'Developmental and behavioral screening billing', 'ADHD evaluation and management coding', 'Newborn care and nursery billing', 'Pediatric E&M code level optimization', 'Medicaid EPSDT program billing'],
     'https://images.unsplash.com/photo-1516627145497-ae6968895b74?w=900&q=80&fit=crop'),
    ('oncology', 'Oncology Billing',
     'Expert billing for oncologists, infusion centers, and cancer care practices.',
     'Oncology billing is highly complex — with chemotherapy infusion coding, drug administration rules, high-cost medication billing, and strict documentation requirements. ZettaRCM\'s oncology billing team handles every aspect of cancer care billing.',
     ['Chemotherapy administration and infusion coding', 'Drug and biologic billing (J-codes)', 'Radiation therapy coding and billing', 'Concurrent care and multi-specialty billing', 'Oncology E&M complexity documentation', 'Clinical trial billing compliance', 'Patient assistance program coordination'],
     'https://images.unsplash.com/photo-1579165466741-7f35e4755660?w=900&q=80&fit=crop'),
    ('pain-management', 'Pain Management Billing',
     'Specialized billing for pain management physicians and interventional practices.',
     'Pain management billing involves a complex mix of interventional procedures, medication management, and physical medicine — each with distinct coding and documentation requirements. ZettaRCM\'s pain management billing experts maximize your reimbursements for every procedure.',
     ['Epidural steroid injection coding and billing', 'Nerve block and trigger point injection billing', 'Spinal cord stimulator billing', 'Fluoroscopy and imaging guidance billing', 'Drug testing billing and compliance', 'Medication management E&M coding', 'Workers\' compensation pain management billing'],
     'https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=900&q=80&fit=crop'),
    ('gastroenterology', 'Gastroenterology Billing',
     'Expert billing for gastroenterologists and endoscopy practices.',
     'Gastroenterology billing requires precise knowledge of endoscopy coding, polyp removal, and bundling rules. ZettaRCM\'s GI billing specialists ensure your colonoscopy, EGD, and other GI procedure claims are coded correctly to maximize reimbursement.',
     ['Colonoscopy and EGD procedure coding', 'Polypectomy and biopsy add-on code billing', 'Capsule endoscopy billing', 'ERCP and EUS coding', 'Anorectal procedure billing', 'GI motility study coding', 'GI diagnostic test billing (Bravo pH, manometry)'],
     'https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=900&q=80&fit=crop'),
    ('ob-gyn', 'OB/GYN Billing',
     'Specialized billing for OB/GYN practices, midwives, and maternal-fetal medicine.',
     'OB/GYN billing encompasses the global obstetric package, gynecological surgery, and preventive care — each with specific coding and payer rules. ZettaRCM\'s OB/GYN billing specialists ensure accurate billing from prenatal care through delivery.',
     ['Global obstetric package billing', 'Antepartum, delivery, and postpartum coding', 'High-risk pregnancy and MFM billing', 'Gynecological surgery coding', 'Preventive gynecology and Pap smear billing', 'Fertility and IVF billing', 'Ultrasound and fetal monitoring billing'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('urology', 'Urology Billing',
     'Expert billing for urologists and urology surgery centers.',
     'Urology billing covers a wide range of diagnostic procedures, minimally invasive surgeries, and urologic oncology — each requiring specialized coding expertise. ZettaRCM\'s urology billing team ensures accurate claims for all urologic services.',
     ['Cystoscopy and urologic endoscopy coding', 'Prostate biopsy and TURP billing', 'Robotic surgery urology billing', 'Urodynamics study coding', 'Kidney stone procedure billing', 'Male reproductive medicine billing', 'Urologic oncology coding and billing'],
     'https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?w=900&q=80&fit=crop'),
    ('ophthalmology', 'Ophthalmology Billing',
     'Specialized billing for ophthalmologists, optometrists, and eye care centers.',
     'Ophthalmology billing is uniquely complex — with distinct E&M and eye visit code sets, ophthalmic procedure coding, and optical dispensing billing. ZettaRCM\'s ophthalmology billing specialists maximize reimbursements for all eye care services.',
     ['Medical eye exam (92000 series) vs. E&M coding', 'Cataract surgery and IOL billing', 'Retinal procedure coding (laser, injection, surgery)', 'Glaucoma treatment and procedure billing', 'Low vision and visual field testing coding', 'Optical dispensing and spectacle billing', 'Ophthalmic imaging and photography billing'],
     'https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?w=900&q=80&fit=crop'),
    ('urgent-care', 'Urgent Care Billing',
     'Fast, accurate billing for urgent care centers and walk-in clinics.',
     'Urgent care billing requires efficient, high-volume claim processing with accurate E&M coding and procedure billing. ZettaRCM\'s urgent care billing team keeps your revenue flowing with same-day claim submission and aggressive A/R follow-up.',
     ['Urgent care E&M code selection and documentation', 'Minor surgical procedure and laceration repair billing', 'Diagnostic imaging and lab interpretation billing', 'Occupational medicine and workers\' comp billing', 'Telemedicine urgent care billing', 'High-volume claim batching and submission', 'Urgent care credentialing with all major payers'],
     'https://images.unsplash.com/photo-1516549655169-df83a0774514?w=900&q=80&fit=crop'),
    ('chiropractic', 'Chiropractic Billing',
     'Expert billing for chiropractors and chiropractic clinics.',
     'Chiropractic billing requires knowledge of manipulation codes, therapy modalities, and payer-specific limitations on chiropractic visits. ZettaRCM\'s chiropractic billing specialists ensure accurate billing and maximum collections.',
     ['Spinal manipulation CPT code selection', 'Therapy modality billing (ultrasound, E-stim, traction)', 'Active vs. passive therapy documentation', 'Medicare chiropractic billing rules', 'Personal injury and auto accident chiropractic billing', 'Chiropractic visit limit tracking by payer', 'X-ray interpretation billing'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('rehabilitation', 'Rehabilitation Billing',
     'Specialized billing for PT, OT, and speech therapy practices.',
     'Rehabilitation billing encompasses physical therapy, occupational therapy, and speech-language pathology — each with therapy cap rules, functional reporting requirements, and payer-specific documentation standards. ZettaRCM\'s rehab billing specialists keep you compliant and fully reimbursed.',
     ['PT, OT, and SLP procedure code billing', 'Therapy cap tracking and KX modifier application', 'Functional limitation reporting (G-codes)', 'Initial evaluation and re-evaluation coding', 'Medicare therapy compliance documentation', 'Outpatient rehab and hospital-based billing', 'Home health therapy billing coordination'],
     'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=900&q=80&fit=crop'),
    ('allergy-immunology', 'Allergy & Immunology Billing',
     'Expert billing for allergists and immunology practices.',
     'Allergy and immunology billing includes allergy testing, immunotherapy injections, and infusion services that require precise coding to maximize reimbursements. ZettaRCM\'s allergy billing specialists ensure accurate claims for all allergy services.',
     ['Allergy skin testing and patch test billing', 'Immunotherapy (allergy shot) injection coding', 'IVIG and biologic infusion billing', 'Spirometry and pulmonary function billing', 'Food challenge testing coding', 'Allergy E&M documentation optimization', 'Allergy lab panel billing'],
     'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=900&q=80&fit=crop'),
    ('nephrology', 'Nephrology Billing',
     'Specialized billing for nephrologists and dialysis practices.',
     'Nephrology billing involves dialysis monthly capitation payments, ESRD billing, and complex E&M services. ZettaRCM\'s nephrology billing specialists ensure accurate billing for all kidney care services.',
     ['ESRD monthly capitation payment billing', 'Hemodialysis and peritoneal dialysis coding', 'Nephrology E&M (MCP) billing', 'AV fistula and graft procedure billing', 'Kidney biopsy coding and billing', 'CKD management and transition care billing', 'Dialysis facility and physician billing coordination'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('geriatrics', 'Geriatrics Billing',
     'Expert billing for geriatricians and senior care practices.',
     'Geriatric billing involves complex E&M services, care management codes, and cognitive assessment billing that require specialized knowledge. ZettaRCM\'s geriatrics billing team maximizes your collections for senior care services.',
     ['Comprehensive geriatric assessment billing', 'Chronic care management (CCM) billing', 'Transitional care management (TCM) coding', 'Annual wellness visit and AWV billing', 'Cognitive impairment assessment billing', 'Care planning and advance directive coding', 'Nursing facility and assisted living billing'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('podiatry', 'Podiatry Billing',
     'Specialized billing for podiatrists and foot care practices.',
     'Podiatry billing requires knowledge of routine foot care exceptions, surgical procedure coding, and diabetic foot care documentation. ZettaRCM\'s podiatry billing specialists ensure accurate claims for all podiatric services.',
     ['Routine foot care and nail care billing with exceptions', 'Foot and ankle surgery coding', 'Diabetic foot exam billing', 'Orthotics and DME billing', 'Wound care and debridement coding', 'Injection and aspiration billing', 'Workers\' compensation podiatry billing'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('endocrinology', 'Endocrinology Billing',
     'Expert billing for endocrinologists and diabetes care practices.',
     'Endocrinology billing covers diabetes management, thyroid care, and hormone disorder treatment — with complex laboratory, imaging, and procedural coding. ZettaRCM\'s endocrinology billing team maximizes reimbursements for all endocrine services.',
     ['Diabetes management E&M billing', 'Thyroid biopsy and ultrasound coding', 'Continuous glucose monitor billing', 'Insulin pump coding and billing', 'Bone density testing billing', 'Endocrine lab panel billing', 'Nutrition counseling billing coordination'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('wound-care', 'Wound Care Billing',
     'Specialized billing for wound care centers and hyperbaric medicine.',
     'Wound care billing involves debridement coding, skin substitute billing, and hyperbaric oxygen therapy — each with strict documentation and coverage requirements. ZettaRCM\'s wound care billing specialists ensure maximum reimbursements.',
     ['Wound debridement (selective, non-selective, surgical) coding', 'Skin substitute graft billing', 'Hyperbaric oxygen therapy billing', 'Negative pressure wound therapy coding', 'Wound measurement and staging documentation', 'Vascular wound care billing', 'Outpatient wound center billing'],
     'https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=900&q=80&fit=crop'),
    ('anesthesia', 'Anesthesia Billing',
     'Expert billing for anesthesiologists and CRNA practices.',
     'Anesthesia billing uses a unique base unit plus time unit system that differs from all other medical billing. ZettaRCM\'s anesthesia billing specialists understand the nuances of anesthesia coding, qualifying circumstances, and payer conversion factors.',
     ['Base unit and time unit calculation', 'Physical status modifier application', 'Qualifying circumstance code billing', 'MAC billing and monitored anesthesia care coding', 'CRNA and physician anesthesiologist billing', 'Anesthesia claim submission with payer conversion factors', 'Post-anesthesia care unit (PACU) billing'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('pathology', 'Pathology Billing',
     'Specialized billing for pathologists and laboratory practices.',
     'Pathology billing involves surgical pathology specimen coding, cytology billing, and molecular diagnostics — with complex bundling rules and payer-specific coverage policies. ZettaRCM\'s pathology billing team ensures accurate coding for all laboratory and pathology services.',
     ['Surgical pathology (CPT 88300-88309) coding', 'Cytology and Pap smear billing', 'Molecular diagnostic and genetic testing billing', 'Immunohistochemistry billing', 'Autopsy billing', 'Clinical laboratory billing (CBC, metabolic panels)', 'Professional and technical component pathology billing'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('family-practice', 'Family Practice Billing',
     'Accurate billing for family medicine and primary care physicians.',
     'Family medicine billing encompasses preventive care, chronic disease management, acute sick visits, and minor procedures — each with specific coding and documentation requirements. ZettaRCM maximizes reimbursements for primary care practices.',
     ['Annual wellness visit and preventive care billing', 'Chronic care management (CCM) billing', 'E&M code level optimization', 'Minor office procedure coding', 'Immunization billing and vaccine administration', 'Telehealth visit billing', 'Behavioral health integration billing'],
     'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=900&q=80&fit=crop'),
    ('general-surgery', 'General Surgery Billing',
     'Expert billing for general surgeons and ambulatory surgery centers.',
     'General surgery billing requires precise knowledge of surgical procedure coding, global period management, and multiple procedure billing rules. ZettaRCM\'s surgery billing specialists ensure maximum reimbursements for every procedure.',
     ['Laparoscopic and open procedure coding', 'Hernia repair and abdominal surgery billing', 'Appendectomy, cholecystectomy, and bowel surgery billing', 'Global period E&M management', 'Multiple procedure modifier application', 'ASC and hospital outpatient billing', 'Wound closure and skin procedure coding'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('pulmonology', 'Pulmonology Billing',
     'Specialized billing for pulmonologists and sleep medicine practices.',
     'Pulmonology billing covers diagnostic testing, bronchoscopy, and respiratory therapy billing — with complex coding for pulmonary function studies and ventilator management. ZettaRCM\'s pulmonology billing team ensures accurate claims.',
     ['Pulmonary function testing billing', 'Bronchoscopy and airway procedure coding', 'Sleep study (polysomnography) billing', 'CPAP and respiratory equipment billing', 'Ventilator management coding', 'Chest x-ray interpretation billing', 'Critical care pulmonology billing'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('internal-medicine', 'Internal Medicine Billing',
     'Expert billing for internists and general medicine practices.',
     'Internal medicine billing involves complex E&M coding, chronic disease management, and hospital-based billing — requiring expertise across multiple organ systems and service settings. ZettaRCM maximizes reimbursements for all internal medicine services.',
     ['Office and outpatient E&M coding optimization', 'Hospital inpatient and observation billing', 'Chronic disease management and CCM billing', 'Annual wellness visit billing', 'Preventive medicine counseling billing', 'Referral coordination and care management coding', 'Medicare Annual Wellness Visit (AWV) billing'],
     'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=900&q=80&fit=crop'),
    ('hematology', 'Hematology Billing',
     'Specialized billing for hematologists and blood disorder practices.',
     'Hematology billing covers blood disorder management, bone marrow procedures, and infusion therapy — with complex coding for transfusions and hematologic oncology. ZettaRCM\'s hematology billing specialists ensure accurate reimbursements.',
     ['Bone marrow biopsy and aspiration coding', 'Transfusion medicine billing', 'Infusion and injection coding (chemotherapy, biologic)', 'Coagulation disorder management billing', 'Hematologic oncology billing', 'Flow cytometry billing', 'Apheresis procedure coding'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('dental', 'Dental Billing',
     'Expert medical billing for dental procedures covered by medical insurance.',
     'Many dental procedures are covered by medical insurance — including oral surgery, TMJ treatment, sleep apnea appliances, and medically necessary dental care. ZettaRCM\'s dental medical billing specialists ensure you capture all medically billable dental services.',
     ['Oral surgery medical billing (extractions, implants)', 'TMJ disorder treatment billing', 'Sleep apnea oral appliance billing', 'Cleft palate and craniofacial procedure billing', 'Hospital-based dental procedure billing', 'Dental trauma and accident billing', 'Medical necessity documentation for dental claims'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('rheumatology', 'Rheumatology Billing',
     'Specialized billing for rheumatologists and autoimmune disease practices.',
     'Rheumatology billing includes biologic infusion billing, joint injection coding, and chronic disease management — with high-value drug billing that requires precise J-code application. ZettaRCM\'s rheumatology billing team maximizes your reimbursements.',
     ['Biologic infusion and injection billing (J-codes)', 'Joint aspiration and injection coding', 'Rheumatology E&M documentation optimization', 'Autoimmune disease lab panel billing', 'IVIG infusion billing', 'Gout and crystal arthropathy billing', 'Medicare and commercial biologic prior auth'],
     'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=900&q=80&fit=crop'),
    ('neonatology', 'Neonatology Billing',
     'Expert billing for neonatologists and neonatal intensive care units.',
     'Neonatal billing uses distinct critical care codes based on birth weight and age — with intensive care coding that requires specialized expertise. ZettaRCM\'s neonatology billing specialists ensure accurate NICU billing.',
     ['Newborn intensive care (CPT 99478-99480) billing', 'Neonatal critical care coding by weight', 'Initial hospital care and subsequent newborn care billing', 'NICU procedure billing', 'Transport medicine billing', 'Resuscitation billing', 'Neonatal E&M and daily management billing'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('audiology', 'Audiology Billing',
     'Specialized billing for audiologists and hearing care practices.',
     'Audiology billing requires knowledge of diagnostic test codes, hearing aid billing, and cochlear implant services — with payer-specific coverage rules for hearing services. ZettaRCM\'s audiology billing team ensures maximum reimbursements.',
     ['Audiometric test and hearing evaluation billing', 'Cochlear implant mapping and programming billing', 'Tinnitus evaluation and treatment billing', 'Vestibular testing and balance study billing', 'Hearing aid fitting and dispensing billing', 'Auditory brainstem response (ABR) billing', 'Medicare audiology coverage compliance'],
     'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=900&q=80&fit=crop'),
    ('infectious-disease', 'Infectious Disease Billing',
     'Expert billing for infectious disease specialists and ID practices.',
     'Infectious disease billing involves complex E&M services, infusion therapy, and diagnostic testing — with long-term antibiotic and antiviral therapy billing. ZettaRCM\'s ID billing specialists maximize reimbursements for all infectious disease services.',
     ['ID E&M documentation and coding', 'IV antibiotic infusion billing', 'HIV/AIDS management billing', 'Antibiotic stewardship billing', 'Wound infection and sepsis coding', 'Travel medicine and vaccination billing', 'Tropical disease coding and billing'],
     'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=900&q=80&fit=crop'),
]

for slug, title, subtitle, intro, points, img in specialties:
    bc = f' <span class="mx-2">/</span> <a href="/specialties/" class="hover:text-brand-teal">Specialties</a> <span class="mx-2">/</span> {title}'
    content = specialty_page(title.replace(' Billing',''), subtitle, intro, points, img)
    make_page(f'{BASE}/specialties/{slug}/index.html', title, bc, subtitle, content)

# ─── SPECIALTIES INDEX ───────────────────────────────────────────────────────
spec_links = [
    ('Mental Health', '/specialties/mental-health/'),('Radiology', '/specialties/radiology/'),
    ('Cardiology', '/specialties/cardiology/'),('Neurology', '/specialties/neurology/'),
    ('Neurosurgery', '/specialties/neurosurgery/'),('Dermatology', '/specialties/dermatology/'),
    ('Orthopedics', '/specialties/orthopedics/'),('Pediatrics', '/specialties/pediatrics/'),
    ('Oncology', '/specialties/oncology/'),('Pain Management', '/specialties/pain-management/'),
    ('Gastroenterology', '/specialties/gastroenterology/'),('OB/GYN', '/specialties/ob-gyn/'),
    ('Urology', '/specialties/urology/'),('Ophthalmology', '/specialties/ophthalmology/'),
    ('Urgent Care', '/specialties/urgent-care/'),('Chiropractic', '/specialties/chiropractic/'),
    ('Rehabilitation', '/specialties/rehabilitation/'),('Allergy & Immunology', '/specialties/allergy-immunology/'),
    ('Nephrology', '/specialties/nephrology/'),('Geriatrics', '/specialties/geriatrics/'),
    ('Podiatry', '/specialties/podiatry/'),('Endocrinology', '/specialties/endocrinology/'),
    ('Wound Care', '/specialties/wound-care/'),('Anesthesia', '/specialties/anesthesia/'),
    ('Pathology', '/specialties/pathology/'),('Family Practice', '/specialties/family-practice/'),
    ('General Surgery', '/specialties/general-surgery/'),('Pulmonology', '/specialties/pulmonology/'),
    ('Internal Medicine', '/specialties/internal-medicine/'),('Hematology', '/specialties/hematology/'),
    ('Dental', '/specialties/dental/'),('Rheumatology', '/specialties/rheumatology/'),
    ('Neonatology', '/specialties/neonatology/'),('Audiology', '/specialties/audiology/'),
    ('Infectious Disease', '/specialties/infectious-disease/'),
]
spec_cards = ''.join(f'        <a href="{url}" class="bg-white border border-slate-200 px-5 py-4 text-[13px] text-slate-700 font-medium hover:border-brand-teal hover:text-brand-teal hover:bg-light-bg transition-all flex items-center gap-2"><svg class="w-4 h-4 fill-brand-teal shrink-0" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>{name}</a>\n' for name, url in spec_links)

spec_index_content = f'''  <section class="py-16 px-6 bg-slate-50">
    <div class="max-w-7xl mx-auto">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <p class="text-[15px] text-slate-600 font-light leading-relaxed">ZettaRCM provides specialized medical billing and revenue cycle management for over 35 healthcare specialties. Select your specialty below to learn more.</p>
      </div>
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3">
{spec_cards}
      </div>
    </div>
  </section>'''

make_page(f'{BASE}/specialties/index.html', 'Medical Specialties We Serve', ' <span class="mx-2">/</span> Specialties', 'Specialized billing solutions for 35+ healthcare specialties nationwide.', spec_index_content)

print('\nAll specialty and service pages generated!')
