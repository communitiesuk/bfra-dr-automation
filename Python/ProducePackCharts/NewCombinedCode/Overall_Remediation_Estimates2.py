"""
Created on Tuesday January 13 2026, 12:02:23

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

def create_Overall_remediation_estimates2(type, figure_count, colours, grey, secondary_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black):
    #initialise the variables
    buildings_remaining_low = 0
    buildings_remaining_high = 0

    ###########
    # Main script Notifications

    # type = 0 is the published version of the graph using published estimates of number of buildings left to remediate
    if type==0:
        print(f'Figure{figure_count}_Overall_Remediation_estimates2')
        buildings_remaining_low = 5723
        buildings_remaining_high = 8584

    if type==1:
        print(f'Accessible_Figure{figure_count}_Overall_Remediation_estimates2')

    # type = 2 corresponds to internal version of the graph using up to date estimates of number of buildings left to remediate
    if type==2:
        print(f'Figure{figure_count}_Overall_Remediation_estimates2_internal')
        buildings_remaining_low = 6100
        buildings_remaining_high = 9200
    ###########


    ###########
    # CREATING THE DF
    ###########
    # Accessing the folder which stores the MI tables

    MI_tables_path = paths_variables['MI_tables_path']
    partial_output_path= paths_variables['partial_output_path']


    # Accessing and transforming Combined_2 for the total number
    Combined_2 = pd.read_excel(MI_tables_path, sheet_name='Combined_2')
    Combined_2 = chop_df(Combined_2, 11, 6)


    # Select the required column
    no_11m_buildings = Combined_2.iloc[:, 5].reset_index(drop=True)
    total_buildings = no_11m_buildings[5] - no_11m_buildings[4] #all buildings not including eligibility pending 
    eligibility_pending = round(no_11m_buildings[4], -2) #round to nearest 100

    yet_to_identify_lower = buildings_remaining_low - total_buildings - eligibility_pending
    yet_to_identify_lower = round(yet_to_identify_lower, -2) #round to the nearest 100
    yet_to_identify_upper = buildings_remaining_high - total_buildings - yet_to_identify_lower - eligibility_pending
    yet_to_identify_upper = round(yet_to_identify_upper, -2) #round to the nearest 100

    data = pd.DataFrame({
        "Identified - Remediation progress monitored": [total_buildings],
        "Identified - eligibility pending (social sector)" : [eligibility_pending],
        "Estimated yet to identify - low estimate": [yet_to_identify_lower],
        "Estimated yet to identify - high estimate": [yet_to_identify_upper]
    }, index=["Number of buildings"])



    ###########
    # CREATING THE GRAPH
    ###########
    fig, ax = plt.subplots(figsize=(13, 6), constrained_layout=True)
    bottom = np.zeros(len(data.index))
    eligibility_pending_colour = colours[4] #extract eligibility pending colour
    colours = colours[:1] #use this colour for 'remediation progress monitored'
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
            label = f'{width:.0f}'
         
            if i == 0:
                if width / total_buildings >= 0.019:
                    label = f'{width:.0f}'
                    ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2, label, **font_dict)

            #label for the buildings known to be eligible not yet in the CSS - includes a ~
            elif i == 1:
                if width / total_buildings >= 0.019: 
                    label = f'~{width:.0f}'
                    ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2, label, **font_dict)

            #label for the estimated buildings to remediate - shows the range            
            elif i == 3:
                start = bar.get_x() - data.iloc[:, 2].values[0]
                end = bar.get_x() + bar.get_width()
                midpoint = (start + end) / 2

                combined_label = f"{data.iloc[:, 2].values[0]:.0f} – {data.iloc[:, 3].values[0] + data.iloc[:, 2].values[0]:.0f}"
                ax.text(midpoint, bar.get_y() + bar.get_height() / 2, combined_label, **font_dict)



    # Formatting
    ax.xaxis.tick_top()
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('darkgrey') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('darkgrey')
    
    # Add horizontal arrow
    arrow = FancyArrowPatch((total_buildings + eligibility_pending, -0.1), (total_buildings + eligibility_pending + yet_to_identify_upper + yet_to_identify_lower, -0.1),
                        arrowstyle='<->', color='black',
                        linewidth=2, mutation_scale=20)
    ax.add_patch(arrow)

    ax.tick_params(axis='x', colors='darkgrey')
    ax.set_axisbelow(True)
    ax.legend(fontsize = 13,
            loc='upper center', 
            bbox_to_anchor=(0.5, 1.25),
            fancybox=False,
            shadow=False,
            ncol=2,
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
        output_filename = f"Figure{figure_count}.svg"
        output_path = os.path.join(partial_output_path, output_filename)

    if type==1:
        output_filename = f"Accessible_Figure{figure_count}.svg"
        output_path = os.path.join(partial_output_path, output_filename)
    # output internal graph in separate folder
    if type == 2:
        output_filename = f"Internal_Figure{figure_count}.svg"
        output_path = os.path.join(partial_output_path + r'\Internal', output_filename)
    

    plt.xticks(rotation=0)
    plt.savefig(output_path)
    plt.close(fig)

    print('DONE!')
    if type != 2: # internal grah should not increase figure count
        figure_count += 1
    return figure_count