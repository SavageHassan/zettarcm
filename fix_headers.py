#!/usr/bin/env python3
"""Replace the header in every page with a single canonical header."""
import os, re

# ─── CANONICAL TOPBAR ─────────────────────────────────────────────────────────
TOPBAR = '''<div class="w-full bg-[#1B3A6B] text-[12px] text-slate-300 py-2.5 px-4">
  <div class="max-w-7xl mx-auto flex flex-wrap justify-between items-center gap-2">
    <div class="flex flex-wrap gap-5 items-center">
      <a href="tel:+18005160192" class="hover:text-white transition-colors flex items-center gap-1.5"><svg class="w-3 h-3" style="fill:#00B8D4" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>(800) 516-0192</a>
      <a href="tel:+17183030192" class="hover:text-white transition-colors flex items-center gap-1.5"><svg class="w-3 h-3" style="fill:#00B8D4" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>(718) 303-0192</a>
      <a href="mailto:info@zettarcm.com" class="hover:text-white transition-colors flex items-center gap-1.5"><svg class="w-3 h-3" style="fill:#00B8D4" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>info@zettarcm.com</a>
    </div>
    <div class="flex items-center gap-4">
      <a href="/make-a-payment/" class="hover:text-white transition-colors">Make A Payment</a>
      <span class="text-slate-600">|</span>
      <a href="/#quote" class="font-medium hover:text-white transition-colors" style="color:#00B8D4">Free Practice Audit</a>
      <span class="text-slate-600">|</span>
      <span class="flex items-center gap-1.5"><span class="w-1.5 h-1.5 bg-green-400 rounded-full inline-block"></span>HIPAA Secure</span>
    </div>
  </div>
</div>'''

# ─── CANONICAL HEADER ─────────────────────────────────────────────────────────
HEADER = '''<header class="w-full bg-white border-b border-slate-200 sticky top-0 z-50 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 flex items-center justify-between h-[72px]">
    <a href="/" class="flex items-center gap-3 shrink-0">
      <svg width="44" height="44" viewBox="0 0 44 44" fill="none"><rect width="44" height="44" rx="4" fill="#1B3A6B"/><path d="M8 28 Q13 18 18 22 Q23 26 28 16 Q33 6 38 16" stroke="#00B8D4" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M8 32 Q13 22 18 26 Q23 30 28 20 Q33 10 38 20" stroke="white" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.5"/></svg>
      <div>
        <div class="text-[22px] font-bold leading-none tracking-tight" style="color:#1B3A6B">Zetta<span style="color:#00B8D4">RCM</span></div>
        <div class="text-[9px] tracking-[0.22em] text-slate-400 uppercase font-medium mt-0.5">Revenue Cycle Management</div>
      </div>
    </a>
    <nav class="hidden lg:flex items-center h-full text-[13.5px] font-medium" style="color:#1B3A6B">
      <a href="/" class="px-4 h-full flex items-center border-b-2 border-transparent hover:border-[#00B8D4] hover:text-[#00B8D4] transition-colors">Home</a>

      <!-- Why ZettaRCM -->
      <div class="zdd relative h-full flex items-center">
        <button class="px-4 h-full flex items-center gap-1 border-b-2 border-transparent hover:border-[#00B8D4] hover:text-[#00B8D4] cursor-pointer transition-colors">Why ZettaRCM <svg class="w-3 h-3 fill-current opacity-60" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></button>
        <div class="zdm absolute top-full left-0 bg-white border border-slate-200 shadow-xl z-50 py-1 min-w-[230px]">
          <a href="/our-company/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Our Company</a>
          <a href="/nationwide-medical-billing/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Nationwide Medical Billing</a>
        </div>
      </div>

      <!-- Services -->
      <div class="zdd relative h-full flex items-center">
        <button class="px-4 h-full flex items-center gap-1 border-b-2 border-transparent hover:border-[#00B8D4] hover:text-[#00B8D4] cursor-pointer transition-colors">Services <svg class="w-3 h-3 fill-current opacity-60" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></button>
        <div class="zdm absolute top-full left-0 bg-white border border-slate-200 shadow-xl z-50 py-1 min-w-[260px]">
          <a href="/services/medical-billing/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Medical Billing</a>
          <a href="/services/medical-credentialing/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Medical Credentialing</a>
          <a href="/services/medical-coding/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Medical Coding</a>
          <a href="/services/denial-management/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Denial Management</a>
          <a href="/services/ar-follow-up/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">A/R Follow Up</a>
          <a href="/services/revenue-cycle-management/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Revenue Cycle Management</a>
          <a href="/services/prior-authorization/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Prior Authorization</a>
          <a href="/services/out-of-network-billing/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Out of Network Billing</a>
          <a href="/services/eligibility-verification/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Eligibility Verification</a>
          <a href="/services/front-office-management/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Front Office Management</a>
          <a href="/services/patient-billing/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Patient Billing</a>
          <a href="/services/payment-posting/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Payment Posting</a>
          <a href="/services/telemedicine-billing/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Telemedicine Billing</a>
          <a href="/services/charge-entry/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Charge Entry</a>
          <a href="/services/practice-management/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Practice Management</a>
          <a href="/services/quality-payment-program/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Quality Payment Program</a>
          <a href="/services/ehr-implementation/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">EHR Implementation</a>
          <a href="/services/healthcare-staffing/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Healthcare Staffing</a>
          <div class="mx-4 my-1 border-t border-slate-100"></div>
          <a href="/services/" class="block px-5 py-3 text-[13px] font-semibold hover:bg-[#F5F8FF] transition-all" style="color:#00B8D4">View All Services →</a>
        </div>
      </div>

      <!-- Specialties -->
      <div class="zdd relative h-full flex items-center">
        <button class="px-4 h-full flex items-center gap-1 border-b-2 border-transparent hover:border-[#00B8D4] hover:text-[#00B8D4] cursor-pointer transition-colors">Specialties <svg class="w-3 h-3 fill-current opacity-60" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></button>
        <div class="zdm absolute top-full left-0 bg-white border border-slate-200 shadow-xl z-50 py-1 min-w-[220px]">
          <a href="/specialties/mental-health/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Mental Health</a>
          <a href="/specialties/cardiology/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Cardiology</a>
          <a href="/specialties/radiology/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Radiology</a>
          <a href="/specialties/orthopedics/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Orthopedics</a>
          <a href="/specialties/oncology/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Oncology</a>
          <a href="/specialties/neurology/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Neurology</a>
          <a href="/specialties/dermatology/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Dermatology</a>
          <a href="/specialties/pain-management/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Pain Management</a>
          <a href="/specialties/gastroenterology/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Gastroenterology</a>
          <a href="/specialties/ob-gyn/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">OB/GYN</a>
          <div class="mx-4 my-1 border-t border-slate-100"></div>
          <a href="/specialties/" class="block px-5 py-3 text-[13px] font-semibold hover:bg-[#F5F8FF] transition-all" style="color:#00B8D4">All 35 Specialties →</a>
        </div>
      </div>

      <!-- Domain Areas -->
      <div class="zdd relative h-full flex items-center">
        <button class="px-4 h-full flex items-center gap-1 border-b-2 border-transparent hover:border-[#00B8D4] hover:text-[#00B8D4] cursor-pointer transition-colors">Domain Areas <svg class="w-3 h-3 fill-current opacity-60" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></button>
        <div class="zdm absolute top-full left-0 bg-white border border-slate-200 shadow-xl z-50 py-1 min-w-[220px]">
          <a href="/domain-areas/revenue-partners/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Revenue Partners</a>
          <a href="/domain-areas/premier-billing-state/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Premier Billing State</a>
          <a href="/domain-areas/pioneer-states-hub/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Pioneer States Hub</a>
          <a href="/domain-areas/city-zones/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">City Zones</a>
          <div class="mx-4 my-1 border-t border-slate-100"></div>
          <a href="/domain-areas/" class="block px-5 py-3 text-[13px] font-semibold hover:bg-[#F5F8FF] transition-all" style="color:#00B8D4">All Domain Areas →</a>
        </div>
      </div>

      <!-- Resources -->
      <div class="zdd relative h-full flex items-center">
        <button class="px-4 h-full flex items-center gap-1 border-b-2 border-transparent hover:border-[#00B8D4] hover:text-[#00B8D4] cursor-pointer transition-colors">Resources <svg class="w-3 h-3 fill-current opacity-60" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></button>
        <div class="zdm absolute top-full right-0 bg-white border border-slate-200 shadow-xl z-50 py-1 min-w-[210px]">
          <a href="/resources/blog/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Blog</a>
          <a href="/resources/rcm-library/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">RCM Library</a>
          <a href="/resources/newsroom/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Newsroom</a>
          <a href="/resources/case-studies/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Case Studies</a>
          <a href="/resources/faqs/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">FAQs</a>
          <a href="/resources/provider-form/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Provider Form</a>
          <a href="/resources/insurance-partners/" class="block px-5 py-3 text-[13px] text-slate-700 hover:bg-[#F5F8FF] hover:text-[#00B8D4] border-l-2 border-transparent hover:border-[#00B8D4] transition-all">Insurance Partners</a>
          <div class="mx-4 my-1 border-t border-slate-100"></div>
          <a href="/resources/" class="block px-5 py-3 text-[13px] font-semibold hover:bg-[#F5F8FF] transition-all" style="color:#00B8D4">All Resources →</a>
        </div>
      </div>

      <a href="/contact/" class="px-4 h-full flex items-center border-b-2 border-transparent hover:border-[#00B8D4] hover:text-[#00B8D4] transition-colors">Contact Us</a>
    </nav>
    <button class="hidden lg:flex items-center justify-center w-11 h-11 hover:bg-[#00B8D4] transition-colors shrink-0" style="background:#1B3A6B">
      <svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
    </button>
  </div>
</header>'''

# ─── CSS FOR DROPDOWNS (works universally, no Tailwind class dependency) ──────
DROPDOWN_CSS = '''<style>
  .zdd:hover > .zdm { display: block; }
  .zdm { display: none; }
</style>'''

# ─── PATTERNS TO FIND AND REPLACE ─────────────────────────────────────────────

# Old topbar pattern start markers
TOPBAR_START_PATTERNS = [
    '<div class="w-full bg-brand-navy',
    '<div class="w-full bg-[#1B3A6B]',
]

# Old header start/end markers
HEADER_START = '<header class="w-full bg-white border-b'
HEADER_END = '</header>'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Remove old dropdown CSS rules that conflict
    content = re.sub(
        r'<style[^>]*>.*?</style>',
        lambda m: re.sub(
            r'\.dropdown-parent:hover[^}]+\}|\.dropdown-menu\s*\{[^}]+\}|'
            r'\.dd:hover[^}]+\}|\.dm\s*\{[^}]+\}|'
            r'\.zdd:hover[^}]+\}|\.zdm\s*\{[^}]+\}',
            '', m.group()
        ),
        content, flags=re.DOTALL
    )

    # 2. Inject fresh dropdown CSS before </head>
    if DROPDOWN_CSS not in content:
        content = content.replace('</head>', DROPDOWN_CSS + '\n</head>', 1)

    # 3. Replace topbar
    for pattern in TOPBAR_START_PATTERNS:
        if pattern in content:
            # Find the full topbar div and replace it
            start = content.find(pattern)
            if start == -1:
                continue
            # Find the matching closing div by counting depth
            depth = 0
            i = start
            while i < len(content):
                if content[i:i+4] == '<div':
                    depth += 1
                elif content[i:i+6] == '</div>':
                    depth -= 1
                    if depth == 0:
                        end = i + 6
                        break
                i += 1
            old_topbar = content[start:end]
            content = content.replace(old_topbar, TOPBAR, 1)
            break

    # 4. Replace header
    header_start = content.find(HEADER_START)
    if header_start != -1:
        header_end_pos = content.find(HEADER_END, header_start)
        if header_end_pos != -1:
            old_header = content[header_start:header_end_pos + len(HEADER_END)]
            content = content.replace(old_header, HEADER, 1)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# ─── RUN ON ALL PAGES ─────────────────────────────────────────────────────────
base = '/Users/mac/zettarcm'
files = []
for root, dirs, fnames in os.walk(base):
    dirs[:] = [d for d in dirs if d not in ('node_modules', '.git', '_shared')]
    for fname in fnames:
        if fname == 'index.html':
            files.append(os.path.join(root, fname))

updated = 0
skipped = 0
for f in sorted(files):
    if process_file(f):
        print(f'✓ {f.replace(base, "")}')
        updated += 1
    else:
        print(f'  (unchanged) {f.replace(base, "")}')
        skipped += 1

print(f'\n✅ Done — {updated} pages updated, {skipped} unchanged')
