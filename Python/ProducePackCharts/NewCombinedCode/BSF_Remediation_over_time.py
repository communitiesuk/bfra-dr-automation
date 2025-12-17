"""
Created on Thursday 20 February 2025, 11:27:10

author: Harry Simmons
"""

import re
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Now you can import your functions
from Utility.functions import chop_df

def create_BSF_Remediation_over_time(type, figure_count, colours, paths_variables, month, year, data_label_font_dict_white, data_label_font_dict_black):
    if type==0:
        print(f'Figure{figure_count}_BSF_Remediation_over_time')

    if type==1:
        print(f'Accessible_Figure{figure_count}_BSF_Remediation_over_time')

    # Accessing the folder which stores the MI tables

    MI_tables_path = paths_variables['MI_tables_path']
    partial_output_path= paths_variables['partial_output_path']

    # Accessing and transforming BSF_5
    BSF_5 = pd.read_excel(MI_tables_path, sheet_name='BSF_5')
    BSF_5 = chop_df(BSF_5, 5, 5)
    BSF_5 = BSF_5.iloc[:, -14:]

    # Generate headers
    headers = ["Remediation Stage"]
    for i in range(13):
        current_date = datetime(year, month, 1) - relativedelta(months=i)
        header = current_date.strftime('%b-%y')
        headers.append(header)
    headers[1:] = headers[1:][::-1]

    # Make headers strings
    headers = [str(header) for header in headers]

    # Assign headers to the DataFrame
    BSF_5.columns = headers

    remediation_stages = {
        "Remediation Stage": ['Remediation complete', 'Remediation complete awaiting building control sign-off', 'Remediation started', 'Plans in place', 'Intent to Remediate'],
    }

    # Replace the data in the first column
    for col in remediation_stages:
        BSF_5[col] = remediation_stages[col]

    # Convert the numeric columns to float
    BSF_5.iloc[:, 1:] = BSF_5.iloc[:, 1:].astype(float) 

    # Plotting the stacked bar chart
    fig, ax = plt.subplots(figsize = (10,8))
    bottom = np.zeros(len(BSF_5.columns) - 1, dtype=float)  


    # Plot each stack in reverse order
    for i in range(BSF_5.shape[0] - 1, -1, -1):
        bars = ax.bar(BSF_5.columns[1:], BSF_5.iloc[i, 1:], bottom=bottom, color=colours[i], label=BSF_5.iloc[i, 0])
        bottom += BSF_5.iloc[i, 1:].astype(float)

        for j, bar in enumerate(bars):
            height = bar.get_height()
            bar_color = mcolors.to_rgb(colours[i]) # Convert color to RGB tuple
            luminance = 0.2126 * bar_color[0] + 0.7152 * bar_color[1] + 0.0722 * bar_color[2]

            # Choose font color based on luminance
            font_dict = data_label_font_dict_black if luminance > 0.5 else data_label_font_dict_white

            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2,
                    f'{height:.0f}', **font_dict)

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
    labels = labels[::-1]   

    # Create a new legend with the reversed order
    ax.legend(handles, labels, fontsize=13,  
            loc='upper center',
            bbox_to_anchor=(0.5, 1.15),
            fancybox=False,
            shadow=False,
            ncol=2,
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