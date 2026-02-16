# Social_writer_headline.py
"""
Created on Tuesday 30 May 2025, 12:13:00

Author: Matthew Bandura
"""

def Social_headline_writer(Social_headline_dict, dates_variables, DR):

    last_month = dates_variables['last_month']
    this_month = dates_variables['this_month']
    cutoff = dates_variables['cutoff']

    Social_self_funded_total = Social_headline_dict['Social_self_funded_total']
    Social_self_funded_total_change = Social_headline_dict['Social_self_funded_total_change']

    Social_self_funded_started_no = Social_headline_dict['Social_self_funded_started_no']
    Social_self_funded_started_pct = Social_headline_dict['Social_self_funded_started_pct']
    Social_self_funded_started_change = Social_headline_dict['Social_self_funded_started_change']

    # Headline Title
    text = f'Social self-funded remediation – monthly update (as at end {this_month}) since previous publication.'
    DR.add_paragraph(text, style = 'Heading 3')

    # Paragraph
    text = f'As at {cutoff}, there are {Social_self_funded_total} social buildings identified with unsafe cladding where remediation is self-funded by registered providers of social housing – {Social_self_funded_total_change} since the end of {last_month}. '
    DR.add_paragraph(text, style = 'Normal')

    # Paragraph
    text = f'Of these, {Social_self_funded_started_no} ({Social_self_funded_started_pct}) are reported to have started or completed remediation works - {Social_self_funded_started_change} since the end of {last_month}. '
    DR.add_paragraph(text, style = 'Normal')

    # Paragraph
    text = f'While work is underway to migrate data to the NRS, fluctuations in the remediation progress figures for social buildings where registered providers are self-funding remediation is expected.' 
    DR.add_paragraph(text, style = 'Normal')
