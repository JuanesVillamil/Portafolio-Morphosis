with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# 1. Remove body overflow block on open
html = html.replace(
    "      document.getElementById('galModal').classList.add('open');\n"
    "      document.body.style.overflow = 'hidden';",
    "      document.getElementById('galModal').classList.add('open');"
)

# 2. Remove body overflow restore on close
html = html.replace(
    "      document.getElementById('galModal').classList.remove('open');\n"
    "      document.body.style.overflow = '';",
    "      document.getElementById('galModal').classList.remove('open');"
)

# 3. Make sure modal uses position: fixed and pointer-events: none on backdrop
# so clicks on the page still work but the modal stays fixed
# Current modal CSS already has position: fixed; inset: 0 — just confirm overlay is display:block not flex
# and content is centered via margin: 0 auto — already done in previous patch.

with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

changed = html != original
print('Done. Changed:', changed)
print('body.overflow hidden removed:', "body.style.overflow = 'hidden'" not in html)
print('body.overflow restore removed:', "body.style.overflow = ''" not in html)

# Verify modal still has position: fixed
import re
modal_block = re.search(r'\.gal-modal \{[^}]+\}', html)
if modal_block:
    print('Modal CSS snippet:', modal_block.group()[:200])
