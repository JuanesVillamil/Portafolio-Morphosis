with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
original = html

# ── 1. Cards menos anchas: más padding lateral en .section y max-width en gal-grid ──
html = html.replace(
    '  padding: 7rem 2rem 5rem;',
    '  padding: 7rem 5rem 5rem;'
)

html = html.replace(
    '    .gal-grid {\n'
    '      display: grid;\n'
    '      grid-template-columns: repeat(4, 1fr);\n'
    '      gap: 1.5rem;\n'
    '      margin: 2rem 0;\n'
    '      align-items: start;\n'
    '    }',
    '    .gal-grid {\n'
    '      display: grid;\n'
    '      grid-template-columns: repeat(4, 1fr);\n'
    '      gap: 1.2rem;\n'
    '      margin: 2rem auto;\n'
    '      max-width: 1100px;\n'
    '      align-items: start;\n'
    '    }'
)

# ── 2. Modal más pequeño ──
html = html.replace(
    '      width: 96%;\n'
    '      max-width: 1300px;\n'
    '      margin: auto;\n'
    '      box-shadow: 0 20px 80px rgba(0,0,0,0.6);',
    '      width: 82%;\n'
    '      max-width: 980px;\n'
    '      margin: auto;\n'
    '      box-shadow: 0 20px 80px rgba(0,0,0,0.6);'
)

# ── 3. Flyer centrado verticalmente (align-items stretch + flyer center) ──
html = html.replace(
    '      display: grid;\n'
    '      grid-template-columns: 1fr 1fr;\n'
    '      gap: 3rem;\n'
    '      align-items: start;\n'
    '    }',
    '      display: grid;\n'
    '      grid-template-columns: 1fr 1fr;\n'
    '      gap: 3rem;\n'
    '      align-items: stretch;\n'
    '    }'
)

html = html.replace(
    '    .gal-modal-flyer {\n'
    '      display: flex;\n'
    '      align-items: flex-start;\n'
    '      justify-content: center;\n'
    '    }',
    '    .gal-modal-flyer {\n'
    '      display: flex;\n'
    '      align-items: center;\n'
    '      justify-content: center;\n'
    '    }'
)

# ── 4. Prólogo real ──
PROLOGUE_OLD = (
    '    <div class="prologue-body">\n'
    '      <p class="prologue-placeholder">\n'
    '        <em>Aquí irá la introducción metafórica que escribirás.</em><br><br>\n'
    '        Una pequeña sinopsis que abra el libro &mdash; por ejemplo:<br>\n'
    '        <span class="prologue-example">"En este libro encontrarás el proceso de transformación de la mariposa Morpho..."</span>\n'
    '        <br><br>\n'
    '        <small>Pendiente de envío · Cuando me lo mandes lo reemplazo aquí.</small>\n'
    '      </p>\n'
    '    </div>'
)

PROLOGUE_NEW = (
    '    <div class="prologue-body">\n'
    '      <p class="prologue-letter">\n'
    '        Querido lector: Te presento \u201cM\u00f3rphosis\u201d.\n'
    '      </p>\n'
    '      <p class="prologue-letter">\n'
    '        En este libro podr\u00e1s encontrar la investigaci\u00f3n de una mariposa Morpho llamada Mar\u00eda Alejandra Morales C\u00e1rdenas, que naci\u00f3 hace cuatro a\u00f1os.\n'
    '      </p>\n'
    '      <p class="prologue-letter">\n'
    '        Te invito a que te inmersas en este universo, a que recorras con atenci\u00f3n cada cap\u00edtulo, para que todo cobre sentido.\n'
    '      </p>\n'
    '      <p class="prologue-letter">\n'
    '        Te dedico cada palabra, cada frase, cada texto, cada poema, cada foto, cada video y cada m\u00ednimo detalle puesto con mucho amor en estas p\u00e1ginas.\n'
    '      </p>\n'
    '      <p class="prologue-letter">\n'
    '        Te regalo mi metamorfosis, los a\u00f1os de vida que llevo y los que me faltan.\n'
    '      </p>\n'
    '      <p class="prologue-letter">\n'
    '        Te otorgo el privilegio de conocer con profundidad a esta mariposa.\n'
    '      </p>\n'
    '      <p class="prologue-letter">\n'
    '        Te agradezco por el inter\u00e9s en este libro; prometo no decepcionarte\u2026\n'
    '      </p>\n'
    '    </div>'
)

if PROLOGUE_OLD in html:
    html = html.replace(PROLOGUE_OLD, PROLOGUE_NEW)
    print('Prologo replaced: OK')
else:
    print('ERROR: prologue not found')

# ── 4b. Estilo para las líneas del prólogo ──
html = html.replace(
    '.prologue-placeholder {',
    '.prologue-letter {\n'
    '  font-family: \'Cormorant Garamond\', serif;\n'
    '  font-size: clamp(1.05rem, 1.6vw, 1.3rem);\n'
    '  line-height: 2;\n'
    '  color: var(--ink-warm);\n'
    '  font-style: italic;\n'
    '  text-align: center;\n'
    '  margin: 0 auto 0.4rem;\n'
    '  max-width: 680px;\n'
    '}\n'
    '.prologue-placeholder {'
)

# ── 4c. Título del prólogo de "Sinopsis" → "Prólogo" ──
html = html.replace(
    '    <div class="chapter-marker"><span class="chapter-num">Pr\u00f3logo</span></div>\n'
    '    <h2>Sinopsis</h2>\n'
    '    <p class="section-subtitle">Antes de entrar al libro</p>',
    '    <div class="chapter-marker"><span class="chapter-num">Pr\u00f3logo</span></div>\n'
    '    <h2>M\u00f3rphosis</h2>\n'
    '    <p class="section-subtitle">Una carta al lector</p>'
)

with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done. Changed:', html != original)
