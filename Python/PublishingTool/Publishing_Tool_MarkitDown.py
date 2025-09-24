from markitdown import MarkItDown
import re
import os
from functions import create_paths

md = MarkItDown()
paths_variables = create_paths()

docx_path = paths_variables['docx_path']
md_path = paths_variables['md_path']

def word_to_markdown(docx_path, md_path):

    output = md.convert(docx_path)
    #performs the initial md conversion
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(output.text_content)

    #reopens the file in order to wrap emails and replace images
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # 1. Wrap emails with <>
    md_text = re.sub(
        r'(?<!<)(\b[\w\.-]+@[\w\.-]+\.\w{2,}\b)(?!>)',
        r'<\1>',
        md_text)

    # 2. Replace base64 image text to format correctly in md
    figure_count = 1
    pattern = r'!\[[^\]]*\]\(\s*data:image/[^)]+\)'
    md_text, figure_count = re.subn(pattern, f'[Image: Figure{figure_count}.svg]', md_text)

    #save processed version
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_text)



word_to_markdown(docx_path, md_path)
