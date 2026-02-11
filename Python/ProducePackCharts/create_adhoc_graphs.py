"""
Created on Wednesday 11 February 2026, 13:47:25

Author: Matthew Bandura
"""

import time 


# Start the timer
start_time = time.time()

#these imports have all been set up in __init__.py in the NewCombinedCode folder
from NewCombinedCode import create_RAP_estimates_residents_nov25, create_RAP_estimates_residents_NRS, create_RAP_estimates_residents_dec24

from Utility import create_paths, sort_dates

non_accessible_colour_scheme = ['#548235', '#A9D18E', '#E2F0D9', '#FFFF99', '#FFCC00', '#FF9900', '#FF0000']
non_accessible_grey = "#D4D4D4"
non_accessible_secondary_grey = "#979797"
accessible_colour_scheme = ['#2B4215', '#659B2C', '#333366', '#8687C1', '#FFFF00', '#E0612E', '#800000']
accessible_grey = "#D4D4D4"
accessible_secondary_grey = "#979797"
dept_colour = '#00625E'

non_accessible_figure_count = 1
accessible_figure_count = 1

paths_variables = create_paths()
month, year = sort_dates()

data_label_font_dict_white = {
  "fontname": 'Arial',
  "fontsize": 12,
  "fontweight": 'bold',
  "horizontalalignment": 'center',
  "verticalalignment": 'center',
  "color": 'white'
  }

data_label_font_dict_black = {
  "fontname": 'Arial',
  "fontsize": 12,
  "fontweight": 'bold',
  "horizontalalignment": 'center',
  "verticalalignment": 'center',
  "color": 'black'
  }

brace_label_font_dict = {
  "fontname": 'Arial',
  "fontsize": 12,
  "fontweight":'normal',
  "color": 'black'
  }


def create_graphs(non_accessible_colour_scheme, non_accessible_grey, accessible_colour_scheme, accessible_grey, non_accessible_figure_count, accessible_figure_count, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict):

  # Residents
  non_accessible_figure_count = create_RAP_estimates_residents_dec24(0, non_accessible_figure_count, non_accessible_colour_scheme, non_accessible_grey, non_accessible_secondary_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  non_accessible_figure_count = create_RAP_estimates_residents_nov25(0, non_accessible_figure_count, non_accessible_colour_scheme, non_accessible_grey, non_accessible_secondary_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  non_accessible_figure_count = create_RAP_estimates_residents_NRS(0, non_accessible_figure_count, non_accessible_colour_scheme, non_accessible_grey, non_accessible_secondary_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black)


# Call the main function
if __name__ == "__main__":
  create_graphs(non_accessible_colour_scheme, non_accessible_grey, accessible_colour_scheme, accessible_grey, non_accessible_figure_count, accessible_figure_count, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)


# End the timer and print the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Program executed in {elapsed_time:.2f} seconds")
print('Done! Have a nice day :)')