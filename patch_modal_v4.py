with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
original = html

# ── 1. Backdrop oscuro para que el espacio debajo del contenido no sea blanco ──
html = html.replace(
    '      background: #f9f5ef;\n      z-index: 9999;\n      overflow-y: auto;\n      padding: 0;',
    '      background: rgba(10,8,20,0.80);\n      z-index: 9999;\n      overflow-y: auto;\n      padding: 0;'
)

# ── 2. Director line más grande ──
html = html.replace(
    '      font-size: clamp(0.85rem, 1.2vw, 1.05rem); opacity: 0.85; font-style: italic;',
    '      font-size: clamp(1rem, 1.5vw, 1.2rem); opacity: 0.90; font-style: italic;'
)

# ── 3. CSS para layout sin flyer (una sola columna) y fotos bonus grandes ──
OLD_PENDING_CSS = '    .gal-pending {'
NEW_PENDING_CSS = (
    '    .gal-modal-body--full { grid-template-columns: 1fr; }\n'
    '    .gal-body-dir-block {\n'
    '      margin: 0.8rem 0 1.2rem;\n'
    '      font-family: "Cormorant Garamond", serif;\n'
    '      font-size: 1rem; color: var(--sepia);\n'
    '      border-left: 3px solid rgba(184,146,74,0.4);\n'
    '      padding-left: 0.8rem; line-height: 1.9;\n'
    '    }\n'
    '    .gal-body-dir-block strong { color: var(--ink-deep); font-weight: 600; }\n'
    '    .gal-photos--bonus { grid-template-columns: repeat(3,1fr); }\n'
    '    .gal-photos--bonus img {\n'
    '      aspect-ratio: 4/3; height: auto;\n'
    '    }\n'
    '    .gal-modal-body--full .gal-bonus-header {\n'
    '      text-align: center; margin-bottom: 1.5rem;\n'
    '    }\n'
    '    .gal-pending {'
)
if OLD_PENDING_CSS in html:
    html = html.replace(OLD_PENDING_CSS, NEW_PENDING_CSS)
    print('CSS bonus/dir added: OK')
else:
    print('ERROR: pending CSS not found')

# ── 4. JS: openGal — layout sin flyer + info de dirección + fotos bonus ──
OLD_OPEN = (
    "      h += '<div class=\"gal-modal-body\">';\n"
    "      if (d.fl) { h += '<div class=\"gal-modal-flyer\"><img src=\"' + d.fl + '\" alt=\"Flyer\" onclick=\"openLB(this.src)\" style=\"cursor:zoom-in;\"></div>'; }\n"
    "      h += '<div class=\"gal-modal-info\">';\n"
    "      if (d.trasescena) {\n"
    "        h += '<span class=\"gal-trasescena-label\">Ensamble Trasescena</span><br>';\n"
    "        h += '<span class=\"gal-asist-label\">Rol: Asistente de Dirección y Producción</span><br><br>';\n"
    "      }\n"
    "      if (d.bonus) {\n"
    "        h += '<span class=\"gal-bonus-badge\" style=\"position:static;display:inline-block;margin-bottom:0.8rem;\">Creación Bonus</span><br><br>';\n"
    "      }\n"
    "      if (d.url) {\n"
    "        h += '<a href=\"' + d.url + '\" target=\"_blank\" rel=\"noopener\" class=\"gal-trailer-btn\">';\n"
    "        h += '<svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"white\"><path d=\"M8 5v14l11-7z\"/></svg>';\n"
    "        h += ' Ver Tráiler</a>&nbsp;';\n"
    "      }\n"
    "      if (d.canva) {\n"
    "        h += '<a href=\"' + d.canva + '\" target=\"_blank\" rel=\"noopener\" class=\"gal-canva-btn\">';\n"
    "        h += '<svg width=\"16\" height=\"16\" viewBox=\"0 0 24 24\" fill=\"white\"><path d=\"M19 3H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V5a2 2 0 00-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z\"/></svg>';\n"
    "        h += ' Ver Trabajo en Canva</a>';\n"
    "      }\n"
    "      if (d.url || d.canva) h += '<br><br>';\n"
    "      if (d.syn) h += '<div class=\"gal-synopsis\">' + d.syn + '</div>';"
)

NEW_OPEN = (
    "      var hasFlyer = !!d.fl;\n"
    "      h += '<div class=\"gal-modal-body' + (hasFlyer ? '' : ' gal-modal-body--full') + '\">';\n"
    "      if (hasFlyer) { h += '<div class=\"gal-modal-flyer\"><img src=\"' + d.fl + '\" alt=\"Flyer\" onclick=\"openLB(this.src)\" style=\"cursor:zoom-in;\"></div>'; }\n"
    "      h += '<div class=\"gal-modal-info\">';\n"
    "      if (d.trasescena) {\n"
    "        h += '<span class=\"gal-trasescena-label\">Ensamble Trasescena</span><br>';\n"
    "        h += '<span class=\"gal-asist-label\">Rol: Asistente de Direcci\\u00f3n y Producci\\u00f3n</span><br><br>';\n"
    "      }\n"
    "      if (d.bonus) {\n"
    "        h += '<div class=\"gal-bonus-header\"><span class=\"gal-bonus-badge\" style=\"position:static;display:inline-block;margin-bottom:1rem;\">Creaci\\u00f3n Bonus</span></div>';\n"
    "      }\n"
    "      if (d.url) {\n"
    "        h += '<a href=\"' + d.url + '\" target=\"_blank\" rel=\"noopener\" class=\"gal-trailer-btn\">';\n"
    "        h += '<svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"white\"><path d=\"M8 5v14l11-7z\"/></svg>';\n"
    "        h += ' Ver Tr\\u00e1iler</a>&nbsp;';\n"
    "      }\n"
    "      if (d.canva) {\n"
    "        h += '<a href=\"' + d.canva + '\" target=\"_blank\" rel=\"noopener\" class=\"gal-canva-btn\">';\n"
    "        h += '<svg width=\"16\" height=\"16\" viewBox=\"0 0 24 24\" fill=\"white\"><path d=\"M19 3H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V5a2 2 0 00-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z\"/></svg>';\n"
    "        h += ' Ver Trabajo en Canva</a>';\n"
    "      }\n"
    "      if (d.url || d.canva) h += '<br><br>';\n"
    "      h += '<div class=\"gal-body-dir-block\">';\n"
    "      h += '<strong>Temporada:</strong> ' + d.s + '<br>';\n"
    "      h += '<strong>Direcci\\u00f3n:</strong> ' + d.d;\n"
    "      h += '</div>';\n"
    "      if (d.syn) h += '<div class=\"gal-synopsis\">' + d.syn + '</div>';"
)

if OLD_OPEN in html:
    html = html.replace(OLD_OPEN, NEW_OPEN)
    print('openGal JS updated: OK')
else:
    print('ERROR: openGal block not found')

# ── 5. JS: photos bonus class ──
html = html.replace(
    "        h += '<div class=\"gal-photos\">';",
    "        h += '<div class=\"gal-photos' + (d.bonus ? ' gal-photos--bonus' : '') + '\">';"
)

with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done. Changed:', html != original)
