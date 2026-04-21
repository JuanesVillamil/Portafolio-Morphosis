with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ── 1. Overlay: position:fixed, sin scroll propio, flex-centrado ──
OLD_MODAL_CSS = (
    '    .gal-modal {\n'
    '      display: none;\n'
    '      position: fixed; inset: 0;\n'
    '      background: rgba(10,8,20,0.80);\n'
    '      z-index: 9999;\n'
    '      overflow-y: auto;          /* el overlay scrollea */\n'
    '      padding: 4vh 1.5rem;\n'
    '    }\n'
    '    .gal-modal.open { display: block; }'
)

NEW_MODAL_CSS = (
    '    .gal-modal {\n'
    '      display: none;\n'
    '      position: fixed; inset: 0;\n'
    '      background: rgba(10,8,20,0.80);\n'
    '      z-index: 9999;\n'
    '      overflow: hidden;\n'
    '      align-items: flex-start;\n'
    '      justify-content: center;\n'
    '      padding: 4vh 1.5rem;\n'
    '    }\n'
    '    .gal-modal.open { display: flex; }'
)

if OLD_MODAL_CSS in html:
    html = html.replace(OLD_MODAL_CSS, NEW_MODAL_CSS)
    print('Overlay CSS: OK')
else:
    print('ERROR: overlay CSS not found')
    idx = html.find('.gal-modal {')
    print(repr(html[idx:idx+300]))

# ── 2. Content box: scroll interno, max-height 90vh ──
OLD_CONTENT_CSS = (
    '    .gal-modal-content {\n'
    '      background: #f9f5ef;\n'
    '      border-radius: 8px;\n'
    '      width: 100%;\n'
    '      max-width: 980px;\n'
    '      margin: 0 auto;\n'
    '      box-shadow: 0 20px 80px rgba(0,0,0,0.6);\n'
    '      display: flex;\n'
    '      flex-direction: column;\n'
    '    }'
)

NEW_CONTENT_CSS = (
    '    .gal-modal-content {\n'
    '      background: #f9f5ef;\n'
    '      border-radius: 8px;\n'
    '      width: 100%;\n'
    '      max-width: 980px;\n'
    '      max-height: 90vh;\n'
    '      overflow-y: auto;\n'
    '      overflow-x: hidden;\n'
    '      margin: 0 auto;\n'
    '      box-shadow: 0 20px 80px rgba(0,0,0,0.6);\n'
    '      display: flex;\n'
    '      flex-direction: column;\n'
    '    }'
)

if OLD_CONTENT_CSS in html:
    html = html.replace(OLD_CONTENT_CSS, NEW_CONTENT_CSS)
    print('Content CSS: OK')
else:
    print('ERROR: content CSS not found')
    idx = html.find('.gal-modal-content {')
    print(repr(html[idx:idx+300]))

# ── 3. JS openGal: bloquear body ──
OLD_OPEN_JS = "      document.getElementById('galModal').classList.add('open');"
NEW_OPEN_JS = (
    "      document.getElementById('galModal').classList.add('open');\n"
    "      document.body.style.overflow = 'hidden';"
)

if OLD_OPEN_JS in html:
    html = html.replace(OLD_OPEN_JS, NEW_OPEN_JS)
    print('openGal JS: OK')
else:
    print('ERROR: openGal JS not found')

# ── 4. JS closeGal: restaurar body ──
OLD_CLOSE_JS = "      document.getElementById('galModal').classList.remove('open');"
NEW_CLOSE_JS = (
    "      document.getElementById('galModal').classList.remove('open');\n"
    "      document.body.style.overflow = '';"
)

if OLD_CLOSE_JS in html:
    html = html.replace(OLD_CLOSE_JS, NEW_CLOSE_JS)
    print('closeGal JS: OK')
else:
    print('ERROR: closeGal JS not found')

with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done. Changed:', html != original)
