with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ── 1. Remove the backdrop div we added (merge back into modal) ──
html = html.replace(
    '<div id="galBackdrop" onclick="closeGal()"></div>\n    <div id="galModal" class="gal-modal">',
    '<div id="galModal" class="gal-modal" onclick="if(event.target===this)closeGal()">'
)

# ── 2. Replace all gallery modal CSS in one block ──
# Find the block from #galBackdrop CSS to the end of .gal-modal-content
OLD_CSS = (
    '    /* Dimming backdrop \u2013 click to close, passes nav through */\n'
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

NEW_CSS = (
    '    .gal-modal {\n'
    '      display: none;\n'
    '      position: fixed; inset: 0;\n'
    '      background: rgba(10,8,20,0.78);\n'
    '      z-index: 9999;\n'
    '      overflow-y: auto;\n'
    '      padding: 5rem 1.5rem 3rem;\n'
    '      backdrop-filter: blur(4px);\n'
    '    }\n'
    '    .gal-modal.open { display: block; }\n'
    '    .gal-modal-content {\n'
    '      background: #f9f5ef;\n'
    '      border-radius: 16px;\n'
    '      max-width: 820px; width: 100%;\n'
)

if OLD_CSS in html:
    html = html.replace(OLD_CSS, NEW_CSS)
    print('Modal CSS -> centered: OK')
else:
    print('ERROR: OLD_CSS block not found')
    # Debug: show what's around gal-modal
    idx = html.find('.gal-modal {')
    if idx != -1:
        print('Found .gal-modal at:', idx)
        print(repr(html[idx-200:idx+300]))

# ── 3. Restore margin: 0 auto 2rem on .gal-modal-content ──
html = html.replace(
    '      margin: 0;\n    }\n    .gal-modal-header',
    '      margin: 0 auto 2rem;\n    }\n    .gal-modal-header'
)

# ── 4. Remove the mobile width override we added ──
html = html.replace(
    '    @media(max-width:700px){ .gal-modal { width: 100%; max-width: 100%; } }\n',
    ''
)

# ── 5. JS: openGal – remove galBackdrop reference, keep no body overflow ──
html = html.replace(
    "      document.getElementById('galModal').classList.add('open');\n"
    "      document.getElementById('galBackdrop').classList.add('open');",
    "      document.getElementById('galModal').classList.add('open');"
)

# ── 6. JS: closeGal – remove galBackdrop reference ──
html = html.replace(
    "      document.getElementById('galModal').classList.remove('open');\n"
    "      document.getElementById('galBackdrop').classList.remove('open');",
    "      document.getElementById('galModal').classList.remove('open');"
)

with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done. Changed:', html != original)
