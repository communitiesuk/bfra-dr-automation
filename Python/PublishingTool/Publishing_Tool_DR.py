
"""
Created on Wednesday 24 September 2025, 09:21:26

Author: Matthew Bandura
"""
from markitdown import MarkItDown
import re
from functions import create_paths


md = MarkItDown()
paths_variables = create_paths()

docx_path = paths_variables['docx_path']
md_path = paths_variables['md_path']

def word_to_markdown(docx_path, md_path):
    print('Converting to markdown...')
    # perform the initial conversion and get the text content into a variable
    conversion = md.convert(docx_path)
    md_text = conversion.text_content

    # regex search for email pattern, which then wraps them in <> (correct HTML formatting)

    pattern =  r'(?<!<)(\b[\w\.-]+@[\w\.-]+\.\w{2,}\b)(?!>)'
    md_text = re.sub(
        pattern,
        r'<\1>',
        md_text)

    # regex pattern to pick up the text string to which MarkitDown converts embedded images
    pattern = r'!\[[^\]]*\]\(\s*data:image/[^)]+\)'

    # function to increment the figure count every time the pattern is matched, returning the string with which it should be substituted
    figure_count = 0
    def replace_figure(match):
        nonlocal figure_count
        figure_count += 1
        return f'[Image: Figure{figure_count}.svg]'

    md_text = re.sub(pattern, 
                     replace_figure,
                     md_text)
    
    #save processed version
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_text)
    print('Conversion complete!')
    
word_to_markdown(docx_path, md_path)

