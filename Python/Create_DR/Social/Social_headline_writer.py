# Social_writer_headline.py
"""
Created on Tuesday 30 May 2025, 12:13:00

Author: Matthew Bandura
"""
from Utility.functions import add_hyperlink

def Social_headline_writer(Social_headline_dict, dates_variables, DR):

    last_month = dates_variables['last_month']
    cutoff = dates_variables['cutoff']

    Social_self_funded_total = Social_headline_dict['Social_self_funded_total']
    Social_self_funded_total_change = Social_headline_dict['Social_self_funded_total_change']

    Social_started_no = Social_headline_dict['Social_started_no']
    Social_started_pct = Social_headline_dict['Social_started_pct']
    Social_started_change = Social_headline_dict['Social_started_change']

    Social_completed_no = Social_headline_dict['Social_completed_no']
    Social_completed_pct = Social_headline_dict['Social_completed_pct']
    Social_completed_change = Social_headline_dict['Social_completed_change']

    # Headline Title
    text = f'Social self-funded remediation – data as at {cutoff}.'
    DR.add_paragraph(text, style = 'Heading 3')

    # Paragraph
    text = f'As at {cutoff}, there are {Social_self_funded_total} social buildings identified with unsafe cladding where remediation is self-funded by registered providers of social housing – {Social_self_funded_total_change} since the end of {last_month}. '
    text += f'The {Social_life_critical_total_no} buildings have been identified using survey data submitted by Registered Providers of social housing and data on buildings the government in monitoring under other government programmes (ACM programme, BSF, CSS, and Developer Remediation contract).'
    DR.add_paragraph(text, style = 'Normal')

    # Paragraph
    text = f'Of these, {Social_started_no} ({Social_started_pct}) are reported to have started or completed remediation works - {Social_started_change} since reported in the {last_month} data release. '
    text += f'Of these, {Social_completed_no} ({Social_completed_pct} of buildings) have completed remediation - {Social_completed_change} since the end of {last_month}.' 
    DR.add_paragraph(text, style = 'Normal')

    # Paragraph
    text = f'While work is underway to migrate data to the NRS, fluctuations in the remediation progress figures for social buildings where registered providers are self-funding remediation is expected.' 
    DR.add_paragraph(text, style = 'Normal')
