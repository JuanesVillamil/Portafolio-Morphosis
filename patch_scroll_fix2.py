with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ── Fix: scroll lives on the overlay, not the content box ──
# The overlay becomes the scrolling container (overflow-y: auto, padding top/bottom)
# The content box just needs max-width + margin, no overflow restrictions

OLD_MODAL = (
    '    .gal-modal {\n'
    '      display: none;\n'
    '      position: fixed; inset: 0;\n'
    '      background: rgba(10,8,20,0.80);\n'
    '      z-index: 9999;\n'
    '      overflow: hidden;          /* el overlay NO scrollea */\n'
    '      align-items: center;\n'
    '      justify-content: center;\n'
    '      padding: 2vh 0;\n'
    '    }\n'
    '    .gal-modal.open { display: flex; }'
)

NEW_MODAL = (
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

if OLD_MODAL in html:
    html = html.replace(OLD_MODAL, NEW_MODAL)
    print('Modal overlay CSS: OK')
else:
    print('ERROR: OLD_MODAL not found')
    idx = html.find('.gal-modal {')
    print(repr(html[idx:idx+400]))

# ── Content box: no overflow restrictions, centered with margin auto ──
OLD_CONTENT = (
    '    /* \u2500\u2500 CAJA BLANCA: aqu\u00ed vive el scroll \u2500\u2500 */\n'
    '    .gal-modal-content {\n'
    '      background: #f9f5ef;\n'
    '      border-radius: 8px;\n'
    '      width: 82%;\n'
    '      max-width: 980px;\n'
    '      max-height: 90vh;          /* nunca pasa del 90% del viewport */\n'
    '      overflow-y: auto;          /* scroll interno */\n'
    '      overflow-x: hidden;\n'
    '      margin: auto;\n'
    '      box-shadow: 0 20px 80px rgba(0,0,0,0.6);\n'
    '      display: flex;\n'
    '      flex-direction: column;\n'
    '    }'
)

NEW_CONTENT = (
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

if OLD_CONTENT in html:
    html = html.replace(OLD_CONTENT, NEW_CONTENT)
    print('Modal content CSS: OK')
else:
    print('ERROR: OLD_CONTENT not found')
    idx = html.find('.gal-modal-content {')
    print(repr(html[idx:idx+400]))

with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

changed = html != original
print('Done. Changed:', changed)
