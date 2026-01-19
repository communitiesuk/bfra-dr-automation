# BSF_writer_headline.py
"""
Created on Monday 20 January 2025, 14:11:13

Author: Harry Simmons
"""

from Utility.functions import add_hyperlink


def BSF_headline_writer(BSF_headline_dict, dates_variables, DR):
    cutoff = dates_variables['cutoff']
    last_month = dates_variables['last_month']
    this_month = dates_variables['this_month']
    hyperlink_month = dates_variables['hyperlink_month']

    BSF_BSF_5_total = BSF_headline_dict['BSF_BSF_5_total']
    BSF_started_nc_no = BSF_headline_dict['BSF_started_nc_no']
    BSF_started_nc_pct = BSF_headline_dict['BSF_started_nc_pct']
    BSF_signoff_c_no = BSF_headline_dict['BSF_signoff_c_no']
    BSF_signoff_c_pct = BSF_headline_dict['BSF_signoff_c_pct']
    BSF_started_c_no = BSF_headline_dict['BSF_started_c_no']
    BSF_started_c_pct = BSF_headline_dict['BSF_started_c_pct']
    BSF_started_c_line = BSF_headline_dict['BSF_started_c_line']
    BSF_signoff_c_line = BSF_headline_dict['BSF_signoff_c_line']

    # Headline Title
    text = f'Building Safety Fund (BSF) – monthly update (as at end {this_month}) since previous publication.'
    paragraph = DR.add_paragraph(text, style = 'Heading 3')

    # # Paragraph
    # text = f'As at {cutoff}, of the {BSF_BSF_5_total} high-rise (18 metres and over in height) residential buildings proceeding with an application for funding through the Building Safety Fund, {BSF_started_nc_no} buildings ({BSF_started_nc_pct}) have started remediation works and {BSF_signoff_c_no} buildings ({BSF_signoff_c_pct}) have completed remediation on unsafe non-ACM cladding, including those awaiting building control sign-off.'
    # paragraph = DR.add_paragraph(text, style = 'Normal')

    # # Paragraph
    # paragraph = f'Overall, {BSF_started_c_no} high-rise buildings ({BSF_started_c_pct}) in the BSF have either started or completed remediation works on non-ACM cladding, {BSF_started_c_line} since the end of {last_month}.'

    # text+= f' Of these, {BSF_signoff_c_no} buildings ({BSF_signoff_c_pct} of buildings) have completed remediation works, {BSF_signoff_c_line} since the end of {last_month}.'
    # paragraph = DR.add_paragraph(text, style = 'Normal')


    # Paragraph
    paragraph = DR.add_paragraph(style = 'Normal')
    paragraph.add_run(f'As at {cutoff}, of the {BSF_BSF_5_total} high-rise (18 metres and over in height) residential buildings proceeding with an application for funding through the Building Safety Fund, {BSF_started_nc_no} buildings ({BSF_started_nc_pct}) have started remediation works and {BSF_signoff_c_no} buildings ({BSF_signoff_c_pct}) have completed remediation on unsafe non-ACM cladding, including those awaiting building control sign-off. Further detail is available in the ')
    add_hyperlink(paragraph, 'Building Safety Fund section', f'https://www.gov.uk/government/publications/building-safety-remediation-monthly-data-release-{hyperlink_month}#building-safety-fund')
    paragraph.add_run(f' of the data release. Overall, {BSF_started_c_no} high-rise buildings ({BSF_started_c_pct}) in the BSF have either started or completed remediation works on non-ACM cladding, {BSF_started_c_line} since the end of {last_month}.')
    paragraph.add_run(f' Of these, {BSF_signoff_c_no} buildings ({BSF_signoff_c_pct} of buildings) have completed remediation works, {BSF_signoff_c_line} since the end of {last_month}.')
