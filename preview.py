import urllib.request
import json
import os
import webbrowser

with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

req = urllib.request.Request('https://api.github.com/markdown', 
    data=json.dumps({"text": text}).encode('utf-8'),
    headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
)
resp = urllib.request.urlopen(req)
html_content = resp.read().decode('utf-8')

html = f"""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
<style>
    body {{ background-color: #0d1117; color: #c9d1d9; }}
    .markdown-body {{ box-sizing: border-box; min-width: 200px; max-width: 980px; margin: 0 auto; padding: 45px; }}
    /* override some styles for dark theme to match github better */
</style>
</head>
<body class="markdown-body" data-color-mode="dark" data-dark-theme="dark">
{html_content}
</body>
</html>
"""
with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(html)

webbrowser.open('file://' + os.path.realpath('preview.html'))
