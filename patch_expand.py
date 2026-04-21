with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ════════════════════════════════════════
# 1. REMOVE MODAL HTML (keep lightbox)
# ════════════════════════════════════════
OLD_MODAL_HTML = (
    '\n    <div id="galModal" class="gal-modal" onclick="if(event.target===this)closeGal()">\n'
    '      <div class="gal-modal-content">\n'
    '        <button class="gal-close" onclick="closeGal()">&#x2715;</button>\n'
    '        <div id="galModalInner"></div>\n'
    '      </div>\n'
    '    </div>\n'
)
NEW_MODAL_HTML = '\n    <div id="gal-details-container"></div>\n'

if OLD_MODAL_HTML in html:
    html = html.replace(OLD_MODAL_HTML, NEW_MODAL_HTML)
    print('Modal HTML removed: OK')
else:
    print('ERROR: modal HTML not found')

# ════════════════════════════════════════
# 2. REMOVE ALL MODAL CSS (block between .gal-modal { and .gal-lightbox {)
# ════════════════════════════════════════
import re

# Find and remove the entire modal CSS block
OLD_MODAL_CSS_BLOCK = re.search(
    r'    /\* \u2500+ CAJA BLANCA.*?\.gal-lightbox-close \{.*?\}\n',
    html, re.DOTALL
)
if not OLD_MODAL_CSS_BLOCK:
    # Try simpler boundary
    OLD_MODAL_CSS_BLOCK = re.search(
        r'    \.gal-modal \{.*?\.gal-lightbox-close \{.*?\}\n',
        html, re.DOTALL
    )

if OLD_MODAL_CSS_BLOCK:
    print('Found modal CSS block, length:', len(OLD_MODAL_CSS_BLOCK.group()))
    html = html[:OLD_MODAL_CSS_BLOCK.start()] + '    ' + html[OLD_MODAL_CSS_BLOCK.end():]
    print('Modal CSS removed: OK')
else:
    print('ERROR: modal CSS block not found - trying targeted removal')
    # Remove individual known blocks
    blocks_to_remove = [
        # overlay
        (r'    \.gal-modal \{[^}]+\}\n    \.gal-modal\.open \{[^\}]+\}\n', ''),
        # content
        (r'    \.gal-modal-content \{[^}]+\}\n', ''),
        # header
        (r'    \.gal-modal-header \{[^}]+\}\n', ''),
        # h2
        (r'    \.gal-modal-header h2 \{[^}]+\}\n', ''),
        # dir line
        (r'    \.gal-modal-header \.gal-dir-line \{[^}]+\}\n', ''),
        # body
        (r'    \.gal-modal-body \{[^}]+\}\n', ''),
        # close btn
        (r'    \.gal-close \{[^}]+\}\n', ''),
    ]
    for pattern, replacement in blocks_to_remove:
        html = re.sub(pattern, replacement, html, flags=re.DOTALL)

# ════════════════════════════════════════
# 3. ADD NEW CSS for .gal-detail expand panels
# ════════════════════════════════════════
NEW_CSS = '''    /* ════════════════════════════════════════
       GAL-DETAIL — expand panel (inline, no modal)
       ════════════════════════════════════════ */
    .gal-detail {
      display: none;
      margin: 0.5rem 0 2rem;
      background: var(--parchment);
      border: 1px solid rgba(184,146,74,0.30);
      border-radius: 10px;
      position: relative;
      box-shadow: 0 6px 32px rgba(0,0,0,0.08);
      overflow: hidden;
    }
    .gal-detail.active {
      display: block;
      animation: galFadeIn 0.42s cubic-bezier(0.22,1,0.36,1);
    }
    @keyframes galFadeIn {
      from { opacity: 0; transform: translateY(18px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .gal-det-header {
      background: var(--morpho-deep);
      color: #f4ead5;
      padding: 1.4rem 3rem 1.2rem 2rem;
      border-radius: 10px 10px 0 0;
    }
    .gal-det-header h2 {
      font-family: 'Italiana', serif;
      font-size: clamp(1.4rem, 2.5vw, 2rem);
      margin: 0 0 0.25rem;
      letter-spacing: 0.04em;
    }
    .gal-det-dir-line {
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(0.85rem, 1.3vw, 1rem);
      opacity: 0.82;
      font-style: italic;
    }
    .gal-det-body {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
      padding: 1.8rem 2rem;
      align-items: start;
    }
    .gal-det-body--full {
      grid-template-columns: 1fr;
    }
    .gal-det-flyer {
      display: flex;
      align-items: flex-start;
      justify-content: center;
    }
    .gal-det-flyer img {
      width: 100%;
      max-width: 320px;
      border-radius: 8px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.22);
      border: 1px solid rgba(184,146,74,0.2);
      cursor: zoom-in;
      transition: transform 0.22s;
    }
    .gal-det-flyer img:hover { transform: scale(1.015); }
    .gal-det-info { min-width: 0; }
    .gal-det-meta {
      font-family: 'Cormorant Garamond', serif;
      font-size: 0.95rem;
      color: var(--sepia);
      border-left: 3px solid rgba(184,146,74,0.4);
      padding-left: 0.8rem;
      line-height: 1.9;
      margin-bottom: 1.2rem;
    }
    .gal-det-meta strong { color: var(--ink-deep); font-weight: 600; }
    .gal-det-synopsis {
      font-family: 'Cormorant Garamond', serif;
      font-size: 1.05rem;
      line-height: 1.85;
      color: var(--ink-warm);
      padding: 1rem 1.2rem;
      background: rgba(184,146,74,0.07);
      border-radius: 6px;
      border-left: 3px solid rgba(184,146,74,0.35);
      margin-bottom: 1.2rem;
    }
    .gal-det-photos {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.7rem;
      margin-top: 1rem;
    }
    .gal-det-photos img {
      width: 100%;
      aspect-ratio: 3/2;
      object-fit: cover;
      border-radius: 5px;
      cursor: zoom-in;
      transition: transform 0.2s;
    }
    .gal-det-photos img:hover { transform: scale(1.03); }
    .gal-det-photos--bonus img { aspect-ratio: 4/3; }
    .gal-det-pending {
      font-family: 'Cormorant Garamond', serif;
      font-style: italic;
      color: var(--sepia);
      opacity: 0.7;
      font-size: 0.95rem;
      margin-top: 0.8rem;
    }
    .gal-det-close {
      position: absolute;
      top: 1rem; right: 1.2rem;
      background: none; border: none;
      color: rgba(244,234,213,0.7);
      font-size: 1.3rem;
      cursor: pointer;
      transition: color 0.2s;
      line-height: 1;
    }
    .gal-det-close:hover { color: #f4ead5; }
    .gal-card.active {
      outline: 2px solid rgba(184,146,74,0.6);
      outline-offset: 2px;
    }
    @media(max-width:700px){
      .gal-det-body { grid-template-columns: 1fr; gap: 1.2rem; padding: 1.2rem; }
    }
'''

# Insert new CSS right before closing </style> in the gallery section
# Find the lightbox-close rule as anchor, insert after it
OLD_CSS_ANCHOR = '    </style>\n\n    <div class="gal-grid">'
NEW_CSS_ANCHOR = NEW_CSS + '    </style>\n\n    <div class="gal-grid">'

if OLD_CSS_ANCHOR in html:
    html = html.replace(OLD_CSS_ANCHOR, NEW_CSS_ANCHOR)
    print('New CSS inserted: OK')
else:
    print('ERROR: CSS anchor not found')
    idx = html.find('<div class="gal-grid">')
    print('gal-grid found at:', idx)
    print(repr(html[idx-100:idx+20]))

# ════════════════════════════════════════
# 4. REPLACE openGal / closeGal JS + add panel builder
# ════════════════════════════════════════
OLD_JS = '''    function openGal(id) {
      var d = GD[id]; if (!d) return;
      var h = '<div class="gal-modal-header"><h2>' + d.t + '</h2>';
      h += '<div class="gal-dir-line">' + d.s + ' &nbsp;&middot;&nbsp; Dir. ' + d.d + '</div></div>';
      var hasFlyer = !!d.fl;
      h += '<div class="gal-modal-body' + (hasFlyer ? '' : ' gal-modal-body--full') + '">';
      if (hasFlyer) { h += '<div class="gal-modal-flyer"><img src="' + d.fl + '" alt="Flyer" onclick="openLB(this.src)" style="cursor:zoom-in;"></div>'; }
      h += '<div class="gal-modal-info">';
      if (d.trasescena) {
        h += '<span class="gal-trasescena-label">Ensamble Trasescena</span><br>';
        h += '<span class="gal-asist-label">Rol: Asistente de Direcci\u00f3n y Producci\u00f3n</span><br><br>';
      }
      if (d.bonus) {
        h += '<div class="gal-bonus-header"><span class="gal-bonus-badge" style="position:static;display:inline-block;margin-bottom:1rem;">Creaci\u00f3n Bonus</span></div>';
      }
      if (d.url) {
        h += '<a href="' + d.url + '" target="_blank" rel="noopener" class="gal-trailer-btn">';
        h += '<svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>';
        h += ' Ver Tr\u00e1iler</a>&nbsp;';
      }
      if (d.canva) {
        h += '<a href="' + d.canva + '" target="_blank" rel="noopener" class="gal-canva-btn">';
        h += '<svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M19 3H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V5a2 2 0 00-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>';
        h += ' Ver Trabajo en Canva</a>';
      }
      if (d.url || d.canva) h += '<br><br>';
      h += '<div class="gal-body-dir-block">';
      h += '<strong>Temporada:</strong> ' + d.s + '<br>';
      h += '<strong>Direcci\u00f3n:</strong> ' + d.d;
      h += '</div>';
      if (d.syn) h += '<div class="gal-synopsis">' + d.syn + '</div>';
      if (d.ph && d.ph.length > 0) {
        h += '<div class="gal-photos' + (d.bonus ? ' gal-photos--bonus' : '') + '">';
        for (var i = 0; i < d.ph.length; i++) {
          h += '<img src="' + d.ph[i] + '" alt="Foto" onclick="openLB(this.src)" loading="lazy">';
        }
        h += '</div>';
      } else if (d.pending) {
        h += '<p class="gal-pending">Fotos pendientes</p>';
      } else if (d.trasescena) {
        h += '<p class="gal-pending">Participante como asistente de direcci\u00f3n</p>';
      } else if (!d.bonus) {
        h += '<p class="gal-pending">Fotos pendientes</p>';
      }
      h += '</div>'; // close gal-modal-info
      h += '</div>'; // close gal-modal-body
      document.getElementById('galModalInner').innerHTML = h;
      document.getElementById('galModal').classList.add('open');
      document.body.style.overflow = 'hidden';
    }
    function closeGal() {
      document.getElementById('galModal').classList.remove('open');
      document.body.style.overflow = '';
    }'''

NEW_JS = '''    /* ── Build all detail panels from GD on page load ── */
    function buildGalPanels() {
      var container = document.getElementById('gal-details-container');
      if (!container) return;
      var frag = '';
      for (var id in GD) {
        var d = GD[id];
        var hasFlyer = !!d.fl;
        frag += '<div class="gal-detail" id="gal-det-' + id + '">';
        // Header
        frag += '<div class="gal-det-header">';
        frag += '<button class="gal-det-close" onclick="closeGal()">&times;</button>';
        frag += '<h2>' + d.t + '</h2>';
        frag += '<div class="gal-det-dir-line">' + d.s + ' &nbsp;&middot;&nbsp; ' + d.d + '</div>';
        frag += '</div>';
        // Body
        frag += '<div class="gal-det-body' + (hasFlyer ? '' : ' gal-det-body--full') + '">';
        // Left: flyer
        if (hasFlyer) {
          frag += '<div class="gal-det-flyer"><img src="' + d.fl + '" alt="Flyer" onclick="openLB(this.src)" loading="lazy"></div>';
        }
        // Right: info
        frag += '<div class="gal-det-info">';
        if (d.trasescena) {
          frag += '<div style="margin-bottom:0.8rem"><span class="gal-trasescena-label">Ensamble Trasescena</span><br>';
          frag += '<span class="gal-asist-label">Rol: Asistente de Direcci\u00f3n y Producci\u00f3n</span></div>';
        }
        if (d.bonus) {
          frag += '<div style="margin-bottom:0.8rem"><span class="gal-bonus-badge" style="position:static;display:inline-block;">Creaci\u00f3n Bonus</span></div>';
        }
        // Buttons
        if (d.url) {
          frag += '<a href="' + d.url + '" target="_blank" rel="noopener" class="gal-trailer-btn">';
          frag += '<svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>';
          frag += ' Ver Tr\u00e1iler</a> ';
        }
        if (d.canva) {
          frag += '<a href="' + d.canva + '" target="_blank" rel="noopener" class="gal-canva-btn">';
          frag += '<svg width="14" height="14" viewBox="0 0 24 24" fill="white"><path d="M19 3H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V5a2 2 0 00-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>';
          frag += ' Ver en Canva</a>';
        }
        if (d.url || d.canva) frag += '<br><br>';
        // Meta block
        frag += '<div class="gal-det-meta">';
        frag += '<strong>Temporada:</strong> ' + d.s + '<br>';
        frag += '<strong>Direcci\u00f3n:</strong> ' + d.d;
        frag += '</div>';
        // Synopsis
        if (d.syn) frag += '<div class="gal-det-synopsis">' + d.syn + '</div>';
        // Photos
        if (d.ph && d.ph.length > 0) {
          frag += '<div class="gal-det-photos' + (d.bonus ? ' gal-det-photos--bonus' : '') + '">';
          for (var i = 0; i < d.ph.length; i++) {
            frag += '<img src="' + d.ph[i] + '" alt="Foto ' + (i+1) + '" onclick="openLB(this.src)" loading="lazy">';
          }
          frag += '</div>';
        } else if (d.pending) {
          frag += '<p class="gal-det-pending">&#128247; Fotos pendientes de edici\u00f3n</p>';
        } else if (d.trasescena) {
          frag += '<p class="gal-det-pending">Participaci\u00f3n como asistente de direcci\u00f3n</p>';
        } else if (!d.bonus) {
          frag += '<p class="gal-det-pending">&#128247; Fotos pendientes</p>';
        }
        frag += '</div>'; // gal-det-info
        frag += '</div>'; // gal-det-body
        frag += '</div>'; // gal-detail
      }
      container.innerHTML = frag;
    }

    function openGal(id) {
      var det = document.getElementById('gal-det-' + id);
      if (!det) return;
      var isOpen = det.classList.contains('active');
      // Close all
      document.querySelectorAll('.gal-detail').forEach(function(d) { d.classList.remove('active'); });
      document.querySelectorAll('.gal-card').forEach(function(c) { c.classList.remove('active'); });
      if (!isOpen) {
        det.classList.add('active');
        // Mark active card
        var card = document.querySelector('[onclick="openGal(\\'' + id + '\\')"]');
        if (card) card.classList.add('active');
        // Smooth scroll to panel
        setTimeout(function() {
          det.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 60);
      }
    }

    function closeGal() {
      document.querySelectorAll('.gal-detail').forEach(function(d) { d.classList.remove('active'); });
      document.querySelectorAll('.gal-card').forEach(function(c) { c.classList.remove('active'); });
    }'''

if OLD_JS in html:
    html = html.replace(OLD_JS, NEW_JS)
    print('JS replaced: OK')
else:
    print('ERROR: JS not found — trying partial match')
    idx = html.find('function openGal(id)')
    print('openGal found at:', idx)
    if idx != -1:
        print(repr(html[idx:idx+100]))

# ════════════════════════════════════════
# 5. CALL buildGalPanels on DOMContentLoaded
# ════════════════════════════════════════
OLD_DOMREADY = "    document.addEventListener('keydown', function(e) {\n      if (e.key === 'Escape') { closeGal(); closeLB(); }\n    });"
NEW_DOMREADY = ("    document.addEventListener('DOMContentLoaded', buildGalPanels);\n"
                "    document.addEventListener('keydown', function(e) {\n"
                "      if (e.key === 'Escape') { closeGal(); closeLB(); }\n"
                "    });")

if OLD_DOMREADY in html:
    html = html.replace(OLD_DOMREADY, NEW_DOMREADY)
    print('DOMContentLoaded hook added: OK')
else:
    print('ERROR: keydown listener not found')

# ════════════════════════════════════════
# 6. REMOVE stale body overflow lines (if any leftover)
# ════════════════════════════════════════
html = html.replace("      document.body.style.overflow = 'hidden';\n", "")
html = html.replace("      document.body.style.overflow = '';\n", "")
print('Body overflow lines removed')

with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done. Changed:', html != original)
