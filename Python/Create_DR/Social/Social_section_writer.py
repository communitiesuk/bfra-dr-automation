# Social_section_writer.py
"""
Created on Wednesday 01 October 2025, 15:55:04

Author: Matthew Bandura
"""
from docx.shared import Cm
import sys
import os

# Add the Utility folder to sys.path
folder_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'Utility'))  # Replace 'folder_name' with the folder's name
sys.path.append(folder_path)

from Utility.functions import create_table, add_hyperlink


def Social_section_writer(Social_section_dict, Social_tables, figure_count, table_count, dates_variables, paths_variables, DR):
    
    cutoff = dates_variables['cutoff']
    last_month = dates_variables['last_month']
    Social_cutoff = dates_variables['social_cutoff']
    Social_previous_release = dates_variables['social_previous_release']
    hyperlink_month = dates_variables['hyperlink_month']
    hyperlink_quarterly_dr = dates_variables['hyperlink_quarterly_dr']

    Social_remediation_table = Social_tables['Social_remediation_table']

    Social_RP_surveyed = Social_section_dict['Social_RP_surveyed']
    Social_RP_excluded = Social_section_dict['Social_RP_excluded']

    Social_life_critical_total_no = Social_section_dict['Social_life_critical_total_no']
    Social_life_critical_total_change = Social_section_dict['Social_life_critical_total_change']

    Social_recent_assessment_total = Social_section_dict['Social_recent_assessment_total']
    Social_recent_assessment_remediated = Social_section_dict['Social_recent_assessment_remediated']

    Social_completed_no = Social_section_dict['Social_completed_no']
    Social_completed_pct = Social_section_dict['Social_completed_pct']
    Social_completed_change = Social_section_dict['Social_completed_change']

    Social_crossover_total = Social_section_dict['Social_crossover_total']

    Social_started_no = Social_section_dict['Social_started_no']
    Social_started_pct = Social_section_dict['Social_started_pct']
    Social_started_change = Social_section_dict['Social_started_change']

    Social_bc_signoff_no = Social_section_dict['Social_bc_signoff_no']
    Social_bc_signoff_pct = Social_section_dict['Social_bc_signoff_pct']
    Social_bc_signoff_change = Social_section_dict['Social_bc_signoff_change']

    Social_not_started_no = Social_section_dict['Social_not_started_no']
    Social_not_started_pct = Social_section_dict['Social_not_started_pct']
    Social_not_started_change = Social_section_dict['Social_not_started_change']

    Social_plans_no = Social_section_dict['Social_plans_no']
    Social_plans_pct = Social_section_dict['Social_plans_pct']
    Social_plans_change = Social_section_dict['Social_plans_change']

    Social_unique_no = Social_section_dict['Social_unique_no']

    Social_18m_starts_pct = Social_section_dict['Social_18m_starts_pct']
    Social_11m_starts_pct = Social_section_dict['Social_11m_starts_pct']

    Social_rp_total = Social_section_dict['Social_rp_total']
    Social_rp_change = Social_section_dict['Social_rp_change']

    Social_rp_prior_completes_no = Social_section_dict['Social_rp_prior_completes_no']
    Social_rp_identified_no =Social_section_dict['Social_rp_identified_no']

    Social_rp_completes_no = Social_section_dict['Social_rp_completes_no']
    Social_rp_completes_pct = Social_section_dict['Social_rp_completes_pct']
    Social_rp_completes_change = Social_section_dict['Social_rp_completes_change']

    Social_rp_starts_no = Social_section_dict['Social_rp_starts_no']
    Social_rp_starts_pct = Social_section_dict['Social_rp_starts_pct']
    Social_rp_starts_change = Social_section_dict['Social_rp_starts_change']

    Social_rp_plans_no = Social_section_dict['Social_rp_plans_no']
    Social_rp_plans_pct = Social_section_dict['Social_rp_plans_pct']
    Social_rp_plans_change = Social_section_dict['Social_rp_plans_change']


    # Heading
    DR.add_paragraph('Social Housing Sector', style = 'Heading 2')

    # Paragraph
    text = f'Information in this section received by Registed Providers of Social Housing is correct as at {Social_cutoff}. Information in this section received from other programmes that relate to social housing is correct as {cutoff}.'
    DR.add_paragraph(text, style = 'Normal')

    # Paragraph
    text = "The estimates in this section include some buildings which are also included in other sections of this data release e.g., those reported under the following sections: ‘ACM Remediation’, ‘Building Safety Fund’, ‘Cladding Safety Scheme’ and ‘Developer Remediation’."
    DR.add_paragraph(text, style = 'Normal')

    # Paragraph
    text = 'From June 2024, the estimates in this section of the release include buildings which have been reported by Registered Providers to have completed remediation since 14 June 2017 but prior to the most recent assessment. They also include social buildings the department has identified in other remediation programmes as having unsafe cladding and are also being monitored in those programmes.'
    DR.add_paragraph(text, style = 'Normal')

    # Figure Title
    paragraph = DR.add_paragraph(style = 'Normal')
    text = f'Figure {figure_count}: {Social_started_pct} of social buildings identified to have unsafe cladding have started or completed remediation works, with {Social_completed_pct} (of identified buildings) having completed remediation works.'
    run = paragraph.add_run(text)
    run.bold = True
 
    # Figure
    DR.add_picture(os.path.join(paths_variables['figure_path'], f'Figure{figure_count}.svg'), width=Cm(17))
    figure_count += 1


    # Table caption
    text = f'Table {table_count}: Remediation status of social buildings with unsafe cladding, {cutoff}.'
    paragraph = DR.add_paragraph(style = 'Normal')
    run = paragraph.add_run(text)
    run.bold = True
    table_count += 1

    # Table
    table_data = Social_remediation_table
    table_widths = [Cm(6.5), Cm(2.65), Cm(2.65), Cm(2.75), Cm(2.75)]
    table_heights = [Cm(1.12), Cm(0.55), Cm(1.13), Cm(0.55), Cm(1.13), Cm(1.13), Cm(0.55)]
    create_table(DR, table_data, table_widths, table_heights)

    # Heading
    DR.add_paragraph('Social Housing remediation: Key statistics', style = 'Heading 3')

    # Paragraph
    text = 'The estimates in this section are based on a combination of self-reported data submitted by registered providers and information that has been imputed from Building Safety Fund (BSF), Cladding Safety Scheme, ACM programme data and data submitted by developers under the Developer Remediation Contract.'
    text += 'A building is identified with life-critical fire safety defects if the registered provider has self-reported cladding defects, the building is eligible for funding in the BSF, CSS or is being monitored under the ACM programme, or the building is reported by developers with cladding defects in their latest quarterly data report.'
    DR.add_paragraph(text, style = 'Normal')

    # Paragraph
    text = f'{Social_RP_surveyed} registered providers of social housing were invited to respond to this round of a survey on their 11m+ stock. {Social_RP_excluded} small registered providers were excluded from this round of the survey because they had indicated that they were not Responsible Entity for any 11m+ residential buildings.'
    DR.add_paragraph(text, style = 'Normal')

    # Paragraph
    text = f'As at {cutoff}, {Social_life_critical_total_no} social buildings 11 metres and over in height have been identified as having life-critical fire-safety cladding defects – {Social_life_critical_total_change} buildings since the {last_month} data release. Of the {Social_life_critical_total_no} buildings identified with unsafe cladding:'
    DR.add_paragraph(text, style = 'Normal')

    # Bullet point
    text = f'{Social_recent_assessment_total} were reported by Registered Providers to have unsafe cladding at the time of their most recent assessment. This could include buildings whose remediation work has been completed but await building control sign off and those awaiting a subsequent assessment to confirm no outstanding life-critical fire-safety defects.'
    text += 'Additional information on these buildings is available in the accompanying management information tables, social housing provider release document and the Regulator for Social Housing’s publication on Fire safety remediation in social housing in England.'
    DR.add_paragraph(text, style = 'List Bullet')

    # Bullet point
    text = f'{Social_recent_assessment_remediated} were reported by Registered Providers to have unsafe cladding since June 2017, but prior to the most recent assessment, which have since been remediated.'
    DR.add_paragraph(text, style = 'List Bullet')

    # Bullet point
    text = f'{Social_crossover_total} were identified under other remediation programmes (BSF, ACM, CSS or developer remediation) as having unsafe cladding and are also being monitored in those programmes.'
    DR.add_paragraph(text, style = 'List Bullet')

    # Paragraph
    text = f'Of the {Social_life_critical_total_no} buildings identified to have unsafe cladding:'
    DR.add_paragraph(text, style = 'Normal')

    # Paragraph
    text = f'{Social_completed_no} buildings ({Social_completed_pct}) are reported to have completed remediation  – {Social_completed_change} since reported in the {last_month} data release. '
    text += f'Of these, {Social_bc_signoff_no} ({Social_bc_signoff_pct} of all buildings with defects) are reported to have received building control sign-off - {Social_bc_signoff_change} since reported in the {last_month} data release.'
    DR.add_paragraph(text, style = 'List Bullet')

    # Paragraph
    text= f'{Social_started_no} buildings ({Social_started_pct}) are reported to have completed remediation  – {Social_started_change} since reported in the {last_month} data release.'
    DR.add_paragraph(text, style = 'List Bullet')

    # Paragraph
    text = f'{Social_not_started_no} buildings ({Social_not_started_pct}) are reported to have not yet started remediation – {Social_not_started_change} since reported in the {last_month} data release.'
    DR.add_paragraph(text, style = 'List Bullet')

    # Paragraph
    text = f'{Social_plans_no} buildings ({Social_plans_pct}) are reported to have not started remediation but have plans in place – {Social_plans_change} since reported in the {last_month} data release.'
    DR.add_paragraph(text, style = 'List Bullet')

    # Paragraph
    text = f'Of the {Social_not_started_no} buildings with cladding defects that have not yet started remediation, {Social_unique_no} buildings are not currently covered by the developer remediation contract or are not currently eligible in another government programme.'
    DR.add_paragraph(text, style = 'Normal')

    # Paragraph
    text = 'Although information from registered providers of social housing is received quarterly, these statistics will be updated monthly as information from other programmes which relate to social building remediation is updated monthly.'
    DR.add_paragraph(text, style = 'Normal')
 
    # Figure Title
    paragraph = DR.add_paragraph(style = 'Normal')
    text = f'Figure {figure_count}: {Social_18m_starts_pct} of the 18m+ social buildings identified to have unsafe cladding have started or completed remediation, compared to {Social_11m_starts_pct} of the 11-18m buildings.'
    run = paragraph.add_run(text)
    run.bold = True

    # Figure
    DR.add_picture(os.path.join(paths_variables['figure_path'], f'Figure{figure_count}.svg'), width=Cm(17))
    figure_count += 1

    # Paragraph
    text = 'Additional information available for individual social housing providers is available in the ' 
    paragraph = DR.add_paragraph(text, style = 'Normal')
    add_hyperlink(paragraph, 'management information tables', f'https://www.gov.uk/government/publications/building-safety-remediation-monthly-data-release-{hyperlink_month}')
    paragraph.add_run( ' and ')
    add_hyperlink(paragraph, 'social housing provider release document', f'https://www.gov.uk/government/publications/building-safety-remediation-monthly-data-release-{hyperlink_quarterly_dr}')
    paragraph.add_run('.')

    # Paragraph
    text =  'The estimates in this section exclude one building identified with unsafe cladding which has been decanted prior to demolition.'
    DR.add_paragraph(text, style = 'Normal')

    # Heading
    paragraph = DR.add_paragraph('Social housing remediation: data reported by registered providers of social housing', style = 'Heading 3')

    # Paragraph
    text = f'The estimates in this section include buildings self-reported by registered providers in the latest survey (as at {Social_cutoff}) as having unsafe cladding since June 2017.'
    DR.add_paragraph(text, style = 'Normal')

    # Paragraph
    text = f'Registered Providers reported that {Social_rp_total} buildings have been found to have unsafe cladding since June 2017, {Social_rp_change} since reported in the {Social_previous_release} Social Housing Remediation data release.'
    text += f'Of these, {Social_rp_prior_completes_no} completed remediation prior to their most recent building works assessment and {Social_rp_identified_no} have been identified with unsafe cladding at the time of the most recent building works assessment. Of the {Social_rp_total} buildings:'
    DR.add_paragraph(text, style = 'Normal')

    # Bullet Point
    text = f'{Social_rp_completes_no} buildings ({Social_rp_completes_pct}) that were identified with unsafe cladding since June 2017 are reported to have completed remediation – {Social_rp_completes_change} buildings since reported in the {Social_previous_release} Social Housing Remediation data release.'
    DR.add_paragraph(text, style = 'List Bullet')

    # Bullet Point
    text = f'{Social_rp_starts_no} buildings ({Social_rp_starts_pct}) are reported to have started or completed remediation – {Social_rp_starts_change} since reported in the {Social_previous_release} Social Housing Remediation data release.'
    text += f'[INSERT STAT HERE] buildings are reported to have started or completed remediation, when they previously were not reported to have started remediation ([INSERT STAT HERE] buildings) or have cladding defects ([INSERT STAT HERE]).'
    text += f'The status of [INSERT STAT HERE] buildings changed from having started or completed remediation to not having cladding defects or no longer being reported in the survey ([INSERT STAT HERE] buildings), or to not having started remediation ([INSERT STAT HERE] buildings).'
    DR.add_paragraph(text, style = 'List Bullet')

    # Paragraph
    text = f'{Social_rp_plans_no} buildings ({Social_rp_plans_pct}) buildings are reported to have not started remediation but have plans in place – {Social_rp_plans_change} since reported in the {Social_previous_release} Social Housing Remediation data release.'
    DR.add_paragraph(text, style = 'List Bullet')

    return figure_count, table_count
