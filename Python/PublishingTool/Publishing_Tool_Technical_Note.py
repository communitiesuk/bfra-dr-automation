
"""
Created on Wednesday 28 January 2026, 15:03:08

Author: Matthew Bandura
"""
from markitdown import MarkItDown
import re
from functions import create_paths


md = MarkItDown()
paths_variables = create_paths()

technical_note_input_path = paths_variables['technical_note_input_path']
technical_note_output_path = paths_variables['technical_note_output_path']

def word_to_markdown(technical_note_input_path, technical_note_output_path):
    print('Converting technical note to markdown...')
    # perform the initial conversion and get the text content into a variable
    conversion = md.convert(technical_note_input_path)
    tn_text = conversion.text_content

    # regex pattern to pick up the text string to which MarkitDown converts embedded images
    pattern = r'!\[[^\]]*\]\(\s*data:image/[^)]+\)'

    # function to increment the figure count every time the pattern is matched, returning the string with which it should be substituted
    figure_count = 0
    def replace_figure(match):
        nonlocal figure_count
        figure_count += 1
        return f'[Image: TechnicalNote_Figure{figure_count}.svg]'

    tn_text = re.sub(pattern, 
                     replace_figure,
                     tn_text)
    
    #save processed version
    with open(technical_note_output_path, 'w', encoding='utf-8') as f:
        f.write(tn_text)
    print('Conversion complete!')
    
word_to_markdown(technical_note_input_path, technical_note_output_path)

