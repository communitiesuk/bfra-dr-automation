"""
Created on Wednesday 28 August 2025, 09:23:10

author: Matthew Bandura
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from matplotlib.patches import FancyArrowPatch

# Now you can import your functions
from Utility.functions import chop_df



def create_RAP_estimates_residents_nov25(type, figure_count, colours, grey, secondary_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black):
    ###########
    # Main script Notifications
    if type==0:
        print(f'Figure{figure_count}_18m_RAP_estimates')

    if type==1:
        print(f'Accessible_Figure{figure_count}_18m_RAP_estimates')
    ###########


    ###########
    # CREATING THE DF
    ###########
    # Accessing the folder which stores the MI tables

    residents_tables_path = paths_variables['residents_tables_path']
    partial_output_path= paths_variables['partial_output_path'] + r'\Residents'


    dwellings_sheet = pd.read_excel(residents_tables_path, sheet_name='residents_nov25')
    residents_nov25 = chop_df(dwellings_sheet, 3, 4)
    estimates_nov25 = chop_df(dwellings_sheet, 9, 3)

    # Select the required data
    remediation_complete_18m_estimate = residents_nov25.iloc[0, 2] 
    remediation_complete_11m_estimate = residents_nov25.iloc[0, 1] 
    remediation_complete_residents = remediation_complete_18m_estimate + remediation_complete_11m_estimate
    remediation_complete_residents = round(remediation_complete_residents, -3)

    # print(residents_nov25.iloc[0, 2])
    # print(residents_nov25.iloc[0, 1])

    remediation_underway_18m_estimate = residents_nov25.iloc[1, 2] 
    remediation_underway_11m_estimate = residents_nov25.iloc[1, 1] 
    remediation_underway_residents = remediation_underway_18m_estimate + remediation_underway_11m_estimate
    remediation_underway_residents = round(remediation_underway_residents, -3)

    # print(remediation_underway_18m_estimate)
    # print(remediation_underway_11m_estimate)

    remediation_18m_programme_estimate = residents_nov25.iloc[2, 2] 
    remediation_11m_programme_estimate = residents_nov25.iloc[2, 1] 
    # print(remediation_18m_programme_estimate)
    # print(remediation_11m_programme_estimate)
    remediation_programme_residents = remediation_18m_programme_estimate + remediation_11m_programme_estimate
    remediation_programme_residents = round(remediation_programme_residents, -3)



    total_residents = remediation_complete_residents + remediation_underway_residents + remediation_programme_residents

    
    yet_to_identify_lower = round(estimates_nov25.iloc[2,1], -3)   

    yet_to_identify_upper = round(estimates_nov25.iloc[2,2], -3) - yet_to_identify_lower


    data = pd.DataFrame({
        "Complete": [remediation_complete_residents],
        "Identified - remediation underway": [remediation_underway_residents],
        "Identified - in programme": [remediation_programme_residents],
        "Estimated yet to identify - low estimate": [yet_to_identify_lower],
        "Estimated yet to identify - high estimate": [yet_to_identify_upper]
    }, index=["Nov-25"])


    ###########
    # CREATING THE GRAPH
    ###########
    fig, ax = plt.subplots(figsize=(18, 3), constrained_layout=True)
    bottom = np.zeros(len(data.index))
    colours = colours[:3]
    colours.append(secondary_grey)
    colours.append(grey)

    for i in range(data.shape[1]):
        bars = ax.barh(data.index, data.iloc[:, i], left=bottom, color=colours[i], label=data.columns[i], height = 0.5)
        bottom += data.iloc[:, i].astype(float)

        for j, bar in enumerate(bars):
            width = bar.get_width()
            if width <= 0:
                continue

            bar_color = mcolors.to_rgb(colours[i])
            luminance = 0.2126 * bar_color[0] + 0.7152 * bar_color[1] + 0.0722 * bar_color[2]
            font_dict = data_label_font_dict_black if luminance > 0.5 else data_label_font_dict_white
            label = f'{width:,.0f}'
         
            if i < 3:
                if width / total_residents >= 0.019:
                    label = f'{width:,.0f}'
                    ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2, label, **font_dict)    
            elif i == 4:
                start = bar.get_x() - data.iloc[:, 3].values[0]
                end = bar.get_x() + bar.get_width()
                midpoint = (start + end) / 2

                combined_label = f"{data.iloc[:, 3].values[0]:,.0f} – {data.iloc[:, 4].values[0] + data.iloc[:, 3].values[0]:,.0f}"
                ax.text(midpoint, bar.get_y() + bar.get_height() / 2, combined_label, **font_dict)



    # Formatting
    ax.xaxis.tick_top()
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('darkgrey') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('darkgrey')
    
    # Add horizontal arrow
    arrow = FancyArrowPatch((total_residents, -0.1), (total_residents + yet_to_identify_upper + yet_to_identify_lower, -0.1),
                        arrowstyle='<->', color='black',
                        linewidth=2, mutation_scale=20)
    ax.add_patch(arrow)

    ax.tick_params(axis='x', colors='darkgrey')
    ax.set_axisbelow(True)
    ax.legend(fontsize = 12,
            loc='upper center', 
            bbox_to_anchor=(0.5, 1.45),
            fancybox=False,
            shadow=False,
            ncol=3,
            edgecolor = 'white'
            )  
    ax.grid(which = 'major',
          axis = 'x',
          color = 'darkgrey',
          linewidth = 0.3
          )
 

    ##########
    # SAVING THE GRAPH
    ##########
    # Save the plot as SVG file
    if type==0:
        output_filename = f"Figure1_residents_nov25.svg"
        output_path = os.path.join(partial_output_path, output_filename)

    if type==1:
        output_filename = f"Accessible_Figure{figure_count}.svg"
        output_path = os.path.join(partial_output_path, output_filename)
    plt.xticks(rotation=0)
    plt.savefig(output_path)
    plt.close(fig)

    print('DONE!')
    figure_count += 1
    return figure_count

def create_RAP_estimates_residents_dec24(type, figure_count, colours, grey, secondary_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black):
    ###########
    # Main script Notifications
    if type==0:
        print(f'Figure{figure_count}_18m_RAP_estimates')

    if type==1:
        print(f'Accessible_Figure{figure_count}_18m_RAP_estimates')
    ###########


    ###########
    # CREATING THE DF
    ###########
    # Accessing the folder which stores the MI tables

    residents_tables_path = paths_variables['residents_tables_path']
    partial_output_path= paths_variables['partial_output_path']


    dwellings_sheet = pd.read_excel(residents_tables_path, sheet_name='residents_dec24')
    residents_dec24 = chop_df(dwellings_sheet, 3, 4)
    estimates_dec24 = chop_df(dwellings_sheet, 9, 3)

    # Select the required data
    remediation_complete_18m_estimate = residents_dec24.iloc[0, 2] 
    remediation_complete_11m_estimate = residents_dec24.iloc[0, 1] 
    remediation_complete_residents = remediation_complete_18m_estimate + remediation_complete_11m_estimate
    remediation_complete_residents = round(remediation_complete_residents, -3)

    # print(residents_nov25.iloc[0, 2])
    # print(residents_nov25.iloc[0, 1])

    remediation_underway_18m_estimate = residents_dec24.iloc[1, 2] 
    remediation_underway_11m_estimate = residents_dec24.iloc[1, 1] 
    remediation_underway_residents = remediation_underway_18m_estimate + remediation_underway_11m_estimate
    remediation_underway_residents = round(remediation_underway_residents, -3)

    # print(remediation_underway_18m_estimate)
    # print(remediation_underway_11m_estimate)

    remediation_18m_programme_estimate = residents_dec24.iloc[2, 2] 
    remediation_11m_programme_estimate = residents_dec24.iloc[2, 1] 
    # print(remediation_18m_programme_estimate)
    # print(remediation_11m_programme_estimate)
    remediation_programme_residents = remediation_18m_programme_estimate + remediation_11m_programme_estimate
    remediation_programme_residents = round(remediation_programme_residents, -3)



    total_residents = remediation_complete_residents + remediation_underway_residents + remediation_programme_residents

    yet_to_identify_lower = round(estimates_dec24.iloc[2,1], -3)   
    yet_to_identify_upper = round(estimates_dec24.iloc[2,2], -3) - yet_to_identify_lower



    data = pd.DataFrame({
        "Complete": [remediation_complete_residents],
        "Identified - remediation underway": [remediation_underway_residents],
        "Identified - in programme": [remediation_programme_residents],
        "Estimated yet to identify - low estimate": [yet_to_identify_lower],
        "Estimated yet to identify - high estimate": [yet_to_identify_upper]
    }, index=["Dec-24"])


    ###########
    # CREATING THE GRAPH
    ###########
    fig, ax = plt.subplots(figsize=(18, 3), constrained_layout=True)
    bottom = np.zeros(len(data.index))
    colours = colours[:3]
    colours.append(secondary_grey)
    colours.append(grey)

    for i in range(data.shape[1]):
        bars = ax.barh(data.index, data.iloc[:, i], left=bottom, color=colours[i], label=data.columns[i], height = 0.5)
        bottom += data.iloc[:, i].astype(float)

        for j, bar in enumerate(bars):
            width = bar.get_width()
            if width <= 0:
                continue

            bar_color = mcolors.to_rgb(colours[i])
            luminance = 0.2126 * bar_color[0] + 0.7152 * bar_color[1] + 0.0722 * bar_color[2]
            font_dict = data_label_font_dict_black if luminance > 0.5 else data_label_font_dict_white
            label = f'{width:,.0f}'
         
            if i < 3:
                if width / total_residents >= 0.019:
                    label = f'{width:,.0f}'
                    ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2, label, **font_dict)    
            elif i == 4:
                start = bar.get_x() - data.iloc[:, 3].values[0]
                end = bar.get_x() + bar.get_width()
                midpoint = (start + end) / 2

                combined_label = f"{data.iloc[:, 3].values[0]:,.0f} – {data.iloc[:, 4].values[0] + data.iloc[:, 3].values[0]:,.0f}"
                ax.text(midpoint, bar.get_y() + bar.get_height() / 2, combined_label, **font_dict)



    # Formatting
    ax.xaxis.tick_top()
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('darkgrey') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('darkgrey')
    
    # Add horizontal arrow
    arrow = FancyArrowPatch((total_residents, -0.1), (total_residents + yet_to_identify_upper + yet_to_identify_lower, -0.1),
                        arrowstyle='<->', color='black',
                        linewidth=2, mutation_scale=20)
    ax.add_patch(arrow)

    ax.tick_params(axis='x', colors='darkgrey')
    ax.set_axisbelow(True)
    ax.legend(fontsize = 12,
            loc='upper center', 
            bbox_to_anchor=(0.5, 1.45),
            fancybox=False,
            shadow=False,
            ncol=3,
            edgecolor = 'white'
            )  
    ax.grid(which = 'major',
          axis = 'x',
          color = 'darkgrey',
          linewidth = 0.3
          )
 

    ##########
    # SAVING THE GRAPH
    ##########
    # Save the plot as SVG file
    if type==0:
        output_filename = f"Figure1_residents_dec24.svg"
        output_path = os.path.join(partial_output_path, output_filename)

    if type==1:
        output_filename = f"Accessible_Figure{figure_count}.svg"
        output_path = os.path.join(partial_output_path, output_filename)
    plt.xticks(rotation=0)
    plt.savefig(output_path)
    plt.close(fig)

    print('DONE!')
    figure_count += 1
    return figure_count

def create_RAP_estimates_residents_NRS(type, figure_count, colours, grey, secondary_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black):
    ###########
    # Main script Notifications
    if type==0:
        print(f'Figure{figure_count}_18m_RAP_estimates')

    if type==1:
        print(f'Accessible_Figure{figure_count}_18m_RAP_estimates')
    ###########


    ###########
    # CREATING THE DF
    ###########
    # Accessing the folder which stores the MI tables

    residents_tables_path = paths_variables['residents_tables_path']
    partial_output_path= paths_variables['partial_output_path']


    dwellings_sheet = pd.read_excel(residents_tables_path, sheet_name='residents_dec25')
    residents_dec25 = chop_df(dwellings_sheet, 3, 4)
    estimates_dec25 = chop_df(dwellings_sheet, 9, 4)

    # Select the required data
    remediation_complete_18m_estimate = residents_dec25.iloc[0, 2] 
    remediation_complete_11m_estimate = residents_dec25.iloc[0, 1] 
    remediation_complete_residents = remediation_complete_18m_estimate + remediation_complete_11m_estimate
    remediation_complete_residents = round(remediation_complete_residents, -3)

    # print(residents_nov25.iloc[0, 2])
    # print(residents_nov25.iloc[0, 1])

    remediation_underway_18m_estimate = residents_dec25.iloc[1, 2] 
    remediation_underway_11m_estimate = residents_dec25.iloc[1, 1] 
    remediation_underway_residents = remediation_underway_18m_estimate + remediation_underway_11m_estimate
    remediation_underway_residents = round(remediation_underway_residents, -3)

    # print(remediation_underway_18m_estimate)
    # print(remediation_underway_11m_estimate)

    remediation_18m_programme_estimate = residents_dec25.iloc[2, 2] 
    remediation_11m_programme_estimate = residents_dec25.iloc[2, 1] 
    # print(remediation_18m_programme_estimate)
    # print(remediation_11m_programme_estimate)
    remediation_programme_residents = remediation_18m_programme_estimate + remediation_11m_programme_estimate
    remediation_programme_residents = round(remediation_programme_residents, -3)



    total_residents = remediation_complete_residents + remediation_underway_residents + remediation_programme_residents
    eligibility_pending = round(estimates_dec25.iloc[1,1], -2) #round to nearest 100


    yet_to_identify_lower = round((estimates_dec25.iloc[2,1]  - eligibility_pending), -3)
    yet_to_identify_upper = round((estimates_dec25.iloc[2,2] - yet_to_identify_lower - eligibility_pending), -3)



    data = pd.DataFrame({
        "Identified- complete": [remediation_complete_residents],
        "Identified - remediation underway": [remediation_underway_residents],
        "Identified - in programme": [remediation_programme_residents],
        'Identified - eligibility pending (social sector)' : [eligibility_pending],
        "Estimated yet to identify - low estimate": [yet_to_identify_lower],
        "Estimated yet to identify - high estimate": [yet_to_identify_upper]
    }, index=["Dec-25"])


    ###########
    # CREATING THE GRAPH
    ###########
    fig, ax = plt.subplots(figsize=(18, 3), constrained_layout=True)
    bottom = np.zeros(len(data.index))
    eligibility_pending_colour = colours[4]
    colours = colours[:3]
    colours.append(eligibility_pending_colour) 
    colours.append(secondary_grey)
    colours.append(grey)


    for i in range(data.shape[1]):
        bars = ax.barh(data.index, data.iloc[:, i], left=bottom, color=colours[i], label=data.columns[i], height = 0.5)
        bottom += data.iloc[:, i].astype(float)

        for j, bar in enumerate(bars):
            width = bar.get_width()
            if width <= 0:
                continue

            bar_color = mcolors.to_rgb(colours[i])
            luminance = 0.2126 * bar_color[0] + 0.7152 * bar_color[1] + 0.0722 * bar_color[2]
            font_dict = data_label_font_dict_black if luminance > 0.5 else data_label_font_dict_white
            label = f'{width:,.0f}'
         
            if i < 4:
                if width / total_residents >= 0.019:
                    label = f'{width:,.0f}'
                    ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2, label, **font_dict)    
            elif i == 5:
                start = bar.get_x() - data.iloc[:, 4].values[0]
                end = bar.get_x() + bar.get_width()
                midpoint = (start + end) / 2

                combined_label = f"{data.iloc[:, 4].values[0]:,.0f} – {data.iloc[:, 5].values[0] + data.iloc[:, 4].values[0]:,.0f}"
                ax.text(midpoint, bar.get_y() + bar.get_height() / 2, combined_label, **font_dict)



    # Formatting
    ax.xaxis.tick_top()
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('darkgrey') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('darkgrey')
    
    # Add horizontal arrow
    arrow = FancyArrowPatch((total_residents + eligibility_pending, -0.1), (total_residents + eligibility_pending + yet_to_identify_upper + yet_to_identify_lower, -0.1),
                        arrowstyle='<->', color='black',
                        linewidth=2, mutation_scale=20)
    ax.add_patch(arrow)

    ax.tick_params(axis='x', colors='darkgrey')
    ax.set_axisbelow(True)
    ax.legend(fontsize = 12,
            loc='upper center', 
            bbox_to_anchor=(0.5, 1.45),
            fancybox=False,
            shadow=False,
            ncol=3,
            edgecolor = 'white'
            )  
    ax.grid(which = 'major',
          axis = 'x',
          color = 'darkgrey',
          linewidth = 0.3
          )
 

    ##########
    # SAVING THE GRAPH
    ##########
    # Save the plot as SVG file
    if type==0:
        output_filename = f"Figure1_residents_NRS.svg"
        output_path = os.path.join(partial_output_path, output_filename)

    if type==1:
        output_filename = f"Accessible_Figure{figure_count}.svg"
        output_path = os.path.join(partial_output_path, output_filename)
    plt.xticks(rotation=0)
    plt.savefig(output_path)
    plt.close(fig)

    print('DONE!')
    figure_count += 1
    return figure_count

