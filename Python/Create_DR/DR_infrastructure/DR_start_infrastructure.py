# DR_start_infrastructure.py
"""
Created on Monday 03 February 2025, 14:13:42

Author: Harry Simmons
"""


def DR_start(dates_variables, DR):
    # Unpack date variables
    publishing_date_1 = dates_variables['publishing_date_1']

    # Next publication date
    paragraph = DR.add_paragraph(style = 'Normal')
    run = paragraph.add_run('Date of next publication:')
    run.bold = True
    text = f' 9.30am on Thursday {publishing_date_1}'
    run = paragraph.add_run(text)

    # Paragraph
    paragraph = DR.add_paragraph(style='Normal')
    run = paragraph.add_run('All figures in this release can also be found in an [interactive dashboard](DASHBOARD LINK).')


    # Section Title
    paragraph = DR.add_paragraph('Headlines', style = 'Heading 2')