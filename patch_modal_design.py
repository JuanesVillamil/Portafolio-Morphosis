with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ── 1. Fix header border-radius to match 16px content card ──
html = html.replace(
    '      background: var(--morpho-deep); color: #f4ead5;\n'
    '      padding: 1.5rem 3rem 1.2rem 2rem; border-radius: 12px 12px 0 0;\n',
    '      background: var(--morpho-deep); color: #f4ead5;\n'
    '      padding: 1.6rem 3.5rem 1.3rem 2.2rem; border-radius: 16px 16px 0 0;\n'
)

# ── 2. Improve header title size ──
html = html.replace(
    '      font-family: "Cormorant Garamond", serif;\n'
    '      font-size: 1.8rem; margin: 0 0 0.2rem; letter-spacing: 0.04em;\n',
    '      font-family: "Cormorant Garamond", serif;\n'
    '      font-size: 2rem; margin: 0 0 0.3rem; letter-spacing: 0.05em; font-weight: 500;\n'
)

# ── 3. Change modal body to 2-col layout: flyer left, content right ──
html = html.replace(
    '    .gal-modal-body { padding: 1.5rem 2rem; }',
    '    .gal-modal-body { padding: 1.8rem 2.2rem; display: flex; gap: 2rem; align-items: flex-start; }'
)

# ── 4. Style flyer column ──
html = html.replace(
    '    .gal-modal-flyer {\n'
    '      text-align: center; margin-bottom: 1.2rem;\n'
    '    }\n'
    '    .gal-modal-flyer img {\n'
    '      max-width: 280px; width: 100%; border-radius: 8px;\n'
    '      box-shadow: 0 6px 24px rgba(0,0,0,0.2);\n'
    '      border: 1px solid rgba(184,146,74,0.2);\n',
    '    .gal-modal-flyer {\n'
    '      flex: 0 0 200px; text-align: center;\n'
    '    }\n'
    '    .gal-modal-flyer img {\n'
    '      width: 200px; border-radius: 10px;\n'
    '      box-shadow: 0 8px 32px rgba(0,0,0,0.25);\n'
    '      border: 1px solid rgba(184,146,74,0.25);\n'
)

# ── 5. Add a .gal-modal-info wrapper style (right column) ──
# Insert after .gal-modal-flyer img closing brace
html = html.replace(
    '    .gal-synopsis {\n'
    '      font-family: "Cormorant Garamond", serif;\n'
    '      font-size: 1.05rem; line-height: 1.7; color: #3a3028;\n'
    '      margin-bottom: 1.5rem; padding: 1rem 1.2rem;\n',
    '    .gal-modal-info { flex: 1 1 0; min-width: 0; }\n'
    '    .gal-synopsis {\n'
    '      font-family: "Cormorant Garamond", serif;\n'
    '      font-size: 1.05rem; line-height: 1.8; color: #3a3028;\n'
    '      margin-bottom: 1.5rem; padding: 1rem 1.2rem;\n'
)

# ── 6. Mobile: stack columns vertically on small screens ──
html = html.replace(
    '    @media(max-width:500px){ .gal-modal-body { padding: 1rem; } }',
    '    @media(max-width:600px){\n'
    '      .gal-modal-body { flex-direction: column; padding: 1.2rem; }\n'
    '      .gal-modal-flyer { flex: none; width: 100%; }\n'
    '      .gal-modal-flyer img { width: 160px; }\n'
    '    }'
)

# ── 7. Wrap the JS-generated modal body in two columns ──
# openGal builds the HTML string: flyer div then everything else.
# We need to wrap flyer in col-left and the rest in .gal-modal-info
# Current structure:
#   h += '<div class="gal-modal-body">';
#   if (d.fl) { h += '<div class="gal-modal-flyer">...</div>'; }
#   ... rest of content ...
#   h += '</div>';  // closes gal-modal-body
# We change to:
#   h += '<div class="gal-modal-body">';
#   if (d.fl) { h += '<div class="gal-modal-flyer">...</div>'; }
#   h += '<div class="gal-modal-info">';
#   ... rest of content ...
#   h += '</div></div>';

html = html.replace(
    "      h += '<div class=\"gal-modal-body\">';\n"
    "      if (d.fl) { h += '<div class=\"gal-modal-flyer\"><img src=\"' + d.fl + '\" alt=\"Flyer\"></div>'; }",
    "      h += '<div class=\"gal-modal-body\">';\n"
    "      if (d.fl) { h += '<div class=\"gal-modal-flyer\"><img src=\"' + d.fl + '\" alt=\"Flyer\"></div>'; }\n"
    "      h += '<div class=\"gal-modal-info\">';"
)

# Close the .gal-modal-info div before closing .gal-modal-body
# The body ends with:   h += '</div>';   // this is the closing of gal-modal-body
# We need to add </div> for gal-modal-info before it
# Find the pattern in openGal that closes the modal body
html = html.replace(
    "      if (d.pending) {\n"
    "        h += '<div class=\"gal-pending\">&#x1F4F8; Fotograf\u00edas en proceso de edici\u00f3n \u2014 pr\u00f3ximamente disponibles</div>';\n"
    "      }\n"
    "      h += '</div>'; // close modal body",
    "      if (d.pending) {\n"
    "        h += '<div class=\"gal-pending\">&#x1F4F8; Fotograf\u00edas en proceso de edici\u00f3n \u2014 pr\u00f3ximamente disponibles</div>';\n"
    "      }\n"
    "      h += '</div>'; // close gal-modal-info\n"
    "      h += '</div>'; // close modal body"
)

with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Design patch done. Changed:', html != original)

# Quick sanity check
with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'r', encoding='utf-8') as f:
    h2 = f.read()

print('gal-modal-info in CSS:', 'gal-modal-info' in h2)
print('gal-modal-info in JS:', h2.count('gal-modal-info'))
print('flex-direction: column in media:', 'flex-direction: column' in h2)
