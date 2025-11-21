# Social_writer_headline.py
"""
Created on Tuesday 30 May 2025, 12:13:00

Author: Matthew Bandura
"""

def Social_headline_writer(Social_headline_dict, dates_variables, DR):

    social_cutoff = dates_variables['social_cutoff']
    last_month = dates_variables['last_month']
    cutoff = dates_variables['cutoff']


    Social_life_critical_total_no = Social_headline_dict['Social_life_critical_total_no']
    Social_life_critical_total_change = Social_headline_dict['Social_life_critical_total_change']

    Social_started_no = Social_headline_dict['Social_started_no']
    Social_started_pct = Social_headline_dict['Social_started_pct']
    Social_started_change = Social_headline_dict['Social_started_change']

    Social_completed_no = Social_headline_dict['Social_completed_no']
    Social_completed_pct = Social_headline_dict['Social_completed_pct']
    Social_completed_change = Social_headline_dict['Social_completed_change']

    # Headline Title
    text = f'Social housing sector – quarterly data received from Registered Providers of social housing is at {social_cutoff}. Where data from other government programmes has been used to supplement this, the data is as at {cutoff}.'
    DR.add_paragraph(text, style = 'Heading 3')

    # Paragraph
    text = f'As at {cutoff}, {Social_life_critical_total_no} 11 metres and over in height have been identified as having life-critical fire safety cladding defects. This is {Social_life_critical_total_change} since reported in the {last_month} data release.'
    text += f'The {Social_life_critical_total_no} buildings have been identified using survey data submitted by Registered Providers of social housing and data on buildings the government in monitoring under other government programmes (ACM programme, BSF, CSS, and Developer Remediation contract).'
    DR.add_paragraph(text, style = 'Normal')

    # Paragraph
    text = f'Of these, {Social_started_no} ({Social_started_pct}) are reported to have started or completed remediation works - {Social_started_change} since reported in the {last_month} data release.'
    text += f'Of these, {Social_completed_no} ({Social_completed_pct} of buildings) have completed remediation - {Social_completed_change} since the {last_month} data release. Further detail is available in the social housing section of the data release.'
    DR.add_paragraph(text, style = 'Normal')
