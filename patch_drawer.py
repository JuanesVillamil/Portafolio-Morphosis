import re

with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ── 1. Nav z-index: 1000 → 10001 so it floats above the drawer ──
html = html.replace('  z-index: 1000;\n  background: linear-gradient(180deg, rgba(244,234,213,0.97)',
                    '  z-index: 10001;\n  background: linear-gradient(180deg, rgba(244,234,213,0.97)')

# ── 2. Replace modal CSS (full-screen overlay → right-side drawer) ──
OLD_MODAL_CSS = (
    '    .gal-modal {\n'
    '      display: none; position: fixed; inset: 0;\n'
    '      background: rgba(10,8,20,0.82); z-index: 9999;\n'
    '      overflow-y: auto;\n'
    '      padding: 2rem 1rem; backdrop-filter: blur(3px);\n'
    '    }\n'
    '    .gal-modal.open { display: block; }\n'
    '    .gal-modal-content {\n'
    '      background: #f9f5ef; border-radius: 12px;\n'
    '      max-width: 820px; width: 100%;\n'
)

NEW_MODAL_CSS = (
    '    /* Dimming backdrop – click to close, passes nav through */\n'
    '    #galBackdrop {\n'
    '      display: none; position: fixed; inset: 0;\n'
    '      background: rgba(10,8,20,0.50); z-index: 9997;\n'
    '      cursor: pointer;\n'
    '    }\n'
    '    #galBackdrop.open { display: block; }\n'
    '    /* Right-side drawer panel */\n'
    '    .gal-modal {\n'
    '      position: fixed; top: 0; right: 0;\n'
    '      width: 58%; max-width: 740px; height: 100vh;\n'
    '      background: #f9f5ef; z-index: 9999;\n'
    '      overflow-y: auto;\n'
    '      box-shadow: -12px 0 60px rgba(0,0,0,0.45);\n'
    '      visibility: hidden;\n'
    '      transform: translateX(100%);\n'
    '      transition: transform 0.38s cubic-bezier(0.4,0,0.2,1),\n'
    '                  visibility 0s linear 0.38s;\n'
    '    }\n'
    '    .gal-modal.open {\n'
    '      visibility: visible;\n'
    '      transform: translateX(0);\n'
    '      transition: transform 0.38s cubic-bezier(0.4,0,0.2,1),\n'
    '                  visibility 0s linear 0s;\n'
    '    }\n'
    '    .gal-modal-content {\n'
    '      background: #f9f5ef; border-radius: 0;\n'
    '      width: 100%;\n'
)

if OLD_MODAL_CSS in html:
    html = html.replace(OLD_MODAL_CSS, NEW_MODAL_CSS)
    print('Modal CSS replaced: OK')
else:
    print('Modal CSS NOT FOUND – check string')

# ── 3. Fix .gal-modal-content closing styles (remove max-width / margin auto) ──
# Remove the old "margin: 0 auto 2rem;" line that centred the content
html = html.replace(
    '      margin: 0 auto 2rem;\n    }\n    .gal-modal-header',
    '      margin: 0;\n    }\n    .gal-modal-header'
)

# ── 4. Add backdrop div before the modal div in HTML ──
OLD_MODAL_DIV = '<div id="galModal" class="gal-modal" onclick="if(event.target===this)closeGal()">'
NEW_MODAL_DIV = '<div id="galBackdrop" onclick="closeGal()"></div>\n    <div id="galModal" class="gal-modal">'
if OLD_MODAL_DIV in html:
    html = html.replace(OLD_MODAL_DIV, NEW_MODAL_DIV)
    print('Backdrop div added: OK')
else:
    print('Modal div NOT FOUND – check string')

# ── 5. JS: openGal – remove body.style.overflow = 'hidden' ──
html = html.replace(
    "      document.getElementById('galModal').classList.add('open');\n"
    "      document.body.style.overflow = 'hidden';",
    "      document.getElementById('galModal').classList.add('open');\n"
    "      document.getElementById('galBackdrop').classList.add('open');"
)

# ── 6. JS: closeGal – remove body.style.overflow restore ──
html = html.replace(
    "      document.getElementById('galModal').classList.remove('open');\n"
    "      document.body.style.overflow = '';",
    "      document.getElementById('galModal').classList.remove('open');\n"
    "      document.getElementById('galBackdrop').classList.remove('open');"
)

# ── 7. Mobile: drawer goes full-width on small screens ──
MEDIA_INSERT = "    @media(max-width:500px){ .gal-modal-body { padding: 1rem; } }"
MEDIA_NEW = (
    "    @media(max-width:500px){ .gal-modal-body { padding: 1rem; } }\n"
    "    @media(max-width:700px){ .gal-modal { width: 100%; max-width: 100%; } }"
)
html = html.replace(MEDIA_INSERT, MEDIA_NEW)

with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

changed = html != original
print('File saved. Changed:', changed)
