"""
Created on Tuesday 13 January 2026, 12:14:54

author: Matthew Bandura
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Now you can import your functions
from Utility.functions import chop_df


def create_Overall_Remediation_over_time3(type, figure_count, colours, secondary_grey, paths_variables, month, year, data_label_font_dict_white, data_label_font_dict_black):
    if type==0:
        text = f'Figure{figure_count}_Overall_remediation_over_time3'
        print(text)

    if type==1:
        text = f'Accessible_Figure{figure_count}_Overall_remediation_over_time3'
        print(text)

    # Accessing the folder which stores the MI tables
    MI_tables_path = paths_variables['MI_tables_path']
    partial_output_path = paths_variables['partial_output_path']

    #Combined_6 time series with all remediation categories is stored separately
    combined_ts_path = paths_variables['combined_ts_path']


    # Accessing and transforming Combined_6
    Combined_6 = pd.read_excel(combined_ts_path, sheet_name='Combined_6')
    Combined_6 = Combined_6.iloc[:5, -14:]
    
    # Accessing and transforming Combined_2 for the latest month's data
    Combined_2 = pd.read_excel(MI_tables_path, sheet_name='Combined_2')
    Combined_2 = chop_df(Combined_2, 3, 6)

    #correct colour scheme for the remediation complete - unknown progress buildings
    eligibility_colours = colours[:4] 
    eligibility_colours.insert(0, secondary_grey) #eligibility pending colour should be grey
    
    # Generate headers
    headers = ["Remediation Stage"]
    for i in range(13):
        current_date = datetime(year, month, 1) - relativedelta(months=i)
        header = current_date.strftime('%b-%y')
        headers.append(header)
    
    latest_month = headers[1] #access the name of the most recent month's data

    #dataframe without eligibility pending and unknown remediation stages
    nonelig_data = pd.DataFrame({  
        "Remediation Stage": ['Complete', 'Underway', 'In Programme'],
        f'{latest_month}' : [Combined_2.iloc[0, -2], Combined_2.iloc[1, -2],  Combined_2.iloc[2, -2]]  #total no of buildings without new categories
    })

    headers[1] = f'{latest_month}\neligibility\npending' #add the eligibility pending label to the latest month's data

    #take the order of the months (col 0 is remediation stage so is excluded) and reverse them 
    headers[1:] = headers[1:][::-1]

    # Make headers strings
    headers = [str(header) for header in headers]

    # Match the columns to the month names in the time series
    Combined_6.columns = headers
    remediation_stages = {
        'Remediation Stage' : ['Eligibility Pending\n(social sector)', 'Complete', 'Underway', 'In Programme', 'Remediation stage\ncurrently unknown']
    }

    # remediation_stages = {
    #     "Remediation Stage": ['Eligibility Pending\n(social sector)', 'Complete', 'Underway', 'In Programme', 'Remediation stage\ncurrently unknown'],
    # }
    
    # eligibility_history = eligibility_ts.iloc[1,-13:]
    # unknown_history = eligibility_ts.iloc[0,-13:]

    # Combined_6.loc[3] = eligibility_history
    # Combined_6.loc[4] = unknown_history

    # Replace the data in the first column 
    for col in remediation_stages:
        Combined_6[col] = remediation_stages[col]

    # Convert the numeric columns to float
    # Combined_6.iloc[:, 1:] = Combined_6.iloc[:, 1:].astype(float)  


    # Plotting the stacked bar chart
    fig, ax = plt.subplots(figsize = (12.5,6))
    bottom = np.zeros(len(Combined_6.columns) - 2, dtype=float) 


    ## plotting 11 months with 5 categories of remediation
    for i in range(Combined_6.shape[0] -1, -1, -1):
        bars = ax.bar(Combined_6.columns[1:13], Combined_6.iloc[i, 1:13], bottom=bottom, color=eligibility_colours[i], label=Combined_6.iloc[i, 0], width=0.6)
        bottom += Combined_6.iloc[i, 1:13].astype(float)

        for j, bar in enumerate(bars):
            height = bar.get_height()

            if height == 0: # don't display 0 height bars (i.e. categories with no buildings in them)
                continue
            bar_color = mcolors.to_rgb(eligibility_colours[i]) # Convert color to RGB tuple
            luminance = 0.2126 * bar_color[0] + 0.7152 * bar_color[1] + 0.0722 * bar_color[2]

            # Choose font color based on luminance
            font_dict = data_label_font_dict_black if luminance > 0.5 else data_label_font_dict_white

            label = f'{height:.0f}'
            label_elig = f'~{round(height, -2):.0f}'

            if i == 0:
                 ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2,
                    label_elig, **font_dict) #use a separate label for eligible remaining to indicate uncertainty
            else:
                 ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2,
                    label, **font_dict)
                 

    ## plotting the latest month using only the 3 categories
    bottom = 0
    # Plot each stack in reverse order
    for i in range(nonelig_data.shape[0] - 1, -1, -1):
        bars = ax.bar(nonelig_data.columns[1:], nonelig_data.iloc[i, 1:], bottom=bottom, color=colours[i], label=nonelig_data.iloc[i, 0], width=0.6)
        bottom += nonelig_data.iloc[i, 1:].astype(float)

        for j, bar in enumerate(bars):
            height = bar.get_height()
            if height <= 0: #don't label 0-height bars
                continue

            bar_color = mcolors.to_rgb(colours[i]) # Convert color to RGB tuple
            luminance = 0.2126 * bar_color[0] + 0.7152 * bar_color[1] + 0.0722 * bar_color[2]

            # Choose font color based on luminance
            font_dict = data_label_font_dict_black if luminance > 0.5 else data_label_font_dict_white

            label = f'{height:.0f}'

            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2,
                    label, **font_dict)

    bottom = 0 
    #plotting the latest month's data with all the categories 
    for i in range(Combined_6.shape[0] -1, -1, -1):
        bars = ax.bar(Combined_6.columns[13], Combined_6.iloc[i, 13], bottom=bottom, color=eligibility_colours[i], label=Combined_6.iloc[i, 0], width=0.6)
        bottom += Combined_6.iloc[i, 13].astype(float)

        for j, bar in enumerate(bars):
            height = bar.get_height()

            if height == 0:
                continue
            bar_color = mcolors.to_rgb(eligibility_colours[i]) # Convert color to RGB tuple
            luminance = 0.2126 * bar_color[0] + 0.7152 * bar_color[1] + 0.0722 * bar_color[2]

            # Choose font color based on luminance
            font_dict = data_label_font_dict_black if luminance > 0.5 else data_label_font_dict_white

            label = f'{height:.0f}'
            label_elig = f'~{round(height, -2):.0f}'

            if i == 0:
                 ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2,
                    label_elig, **font_dict) #use a separate label for eligible remaining to indicate uncertainty
            else:
                 ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2,
                    label, **font_dict)
                 


    # Add labels and title
    ax.spines['bottom'].set_color('darkgrey')
    ax.spines['top'].set_color('None') 
    ax.spines['right'].set_color('None')
    ax.spines['left'].set_color('None')
    ax.tick_params(axis='y', colors='None')
    ax.tick_params(axis='x', colors='black', labelsize = 15, rotation = 45)
    ax.yaxis.label.set_color('None')
    ax.xaxis.label.set_color('darkgrey')
    # Get handles and labels from the current legend
    handles, labels = ax.get_legend_handles_labels() 

    # Reverse the order of handles and labels
    handles = handles[::-1] 
    labels = labels[::-1][:5] #remove the duplicate labels from the legend

    #create the dotted line in Nov-25 showing the shift to NRS data
    x_labels = list(Combined_6.columns[1:]) #get the list of months
    if 'Nov-25' in x_labels:
        index = x_labels.index('Nov-25') #get the position of the month
        #0 is the centre of the bar, + 0.5 takes it halfway between 
        midpoint = index + 0.5

        ax.axvline(x= midpoint, ymin=0, ymax=1, color='g', linestyle='--', linewidth=1.5, label='NRS') #add in the line, ymin = 0 for the bottom and ymax =  1 for the top
        
    # Create a new legend with the reversed order
    ax.legend(handles, labels, fontsize=13,  
            loc='upper center',
            bbox_to_anchor=(1.1, 0.5),
            fancybox=False,
            shadow=False,
            ncol=1,
            edgecolor='None')
    fig.tight_layout()

    # Save the plot as SVG file
    if type==0:
        output_filename = f"Figure{figure_count}.svg"
        output_path = os.path.join(partial_output_path, output_filename)

    if type==1:
        output_filename = f"Accessible_Figure{figure_count}.svg"
        output_path = os.path.join(partial_output_path, output_filename)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close(fig)

    print('DONE!')
    figure_count += 1
    return figure_count