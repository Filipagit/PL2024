import re
import markdown

def markdown_to_html(markdown):
    # Headers
    markdown = re.sub(r'^#\s(.*)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^##\s(.*)$', r'<h2>\1</h2>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^###\s(.*)$', r'<h3>\1</h3>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^####\s+(.*?)$', r'<h4>\1</h4>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^#####\s+(.*?)$', r'<h5>\1</h5>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^######\s+(.*?)$', r'<h6>\1</h6>', markdown, flags=re.MULTILINE)
    # Bold
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)
    markdown = re.sub(r'__(.*?)__', r'<b>\1</b>', markdown)

    
    # Italic
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)
    markdown = re.sub(r'_(.*?)_', r'<i>\1</i>', markdown)

    # BLOCKQUOTE
    markdown = re.sub(r'^>\s+(.*?)$', r'<blockquote>\1</blockquote>', markdown)
    
    # Numbered List
    markdown = re.sub(r'^\d+\.\s(.*)$', r'<li>\1</li>', markdown, flags=re.MULTILINE | re.Un)
    markdown = '<ol>\n' + markdown + '\n</ol>'
    
    # Links
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)
    
    # Images
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)

    return markdown

def convert_markdown_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    html_text = markdown.markdown(markdown_text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_text)

# Nome dos arquivos de entrada e saída
input_file = 'input.md'
output_file = 'output.html'

# Converter Markdown para HTML
convert_markdown_file(input_file, output_file)
