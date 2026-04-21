with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

html = html.replace(
    "      document.getElementById('galModal').classList.add('open');",
    "      document.getElementById('galModal').classList.add('open');\n      document.body.style.overflow = 'hidden';"
)

html = html.replace(
    "      document.getElementById('galModal').classList.remove('open');",
    "      document.getElementById('galModal').classList.remove('open');\n      document.body.style.overflow = '';"
)

with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

changed = html != original
print('Done. Changed:', changed)
print('overflow hidden added:', "body.style.overflow = 'hidden'" in html)
print('overflow restore added:', "body.style.overflow = ''" in html)
