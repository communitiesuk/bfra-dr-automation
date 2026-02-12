"""
Created on Tuesday 11 February 2025, 10:53:31

Author: Harry Simmons
"""

import time 


# Start the timer
start_time = time.time()

#these imports have all been set up in __init__.py in the NewCombinedCode folder
from NewCombinedCode import create_Overall_Remediation_over_time3, create_Overall_remediation_estimates2, create_Overall_Remediation2_Curly, create_Overall_Remediation_Across_Schemes2, create_Overall_Height, create_Overall_Tenure, create_ACM_Remediation, create_ACM_By_Tenure, create_BSF_Remediation_Curly, create_BSF_Remediation_over_time, create_BSF_Tenure, create_CSS_Eligibility2, create_CSS_Height, create_CSS_Tenure, create_Developer_Remediation_Curly, create_Developer_Height, create_SocialHousing_Remediation4_Curly, create_SocialHousing3_Height

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

  ##########
  # NON ACCESSIBLE
  ##########


  # Overall
  non_accessible_figure_count = create_Overall_remediation_estimates2(2, non_accessible_figure_count, non_accessible_colour_scheme, non_accessible_grey, non_accessible_secondary_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  non_accessible_figure_count = create_Overall_remediation_estimates2(0, non_accessible_figure_count, non_accessible_colour_scheme, non_accessible_grey, non_accessible_secondary_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black)


  non_accessible_figure_count = create_Overall_Remediation_over_time3(0, non_accessible_figure_count, non_accessible_colour_scheme, non_accessible_secondary_grey, paths_variables, month, year, data_label_font_dict_white, data_label_font_dict_black)
  non_accessible_figure_count = create_Overall_Remediation2_Curly(0, non_accessible_figure_count, non_accessible_colour_scheme, non_accessible_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)
  non_accessible_figure_count = create_Overall_Remediation_Across_Schemes2(0, non_accessible_figure_count, non_accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  non_accessible_figure_count = create_Overall_Height(0, non_accessible_figure_count, non_accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  non_accessible_figure_count = create_Overall_Tenure(0, non_accessible_figure_count, non_accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  
  #map
  non_accessible_figure_count += 1

  # ACM
  non_accessible_figure_count = create_ACM_Remediation(0, non_accessible_figure_count, non_accessible_colour_scheme, non_accessible_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)
  #Figures 8&9
  non_accessible_figure_count += 1
  non_accessible_figure_count += 1
  non_accessible_figure_count = create_ACM_By_Tenure(0, non_accessible_figure_count, non_accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)

  # BSF
  non_accessible_figure_count = create_BSF_Remediation_Curly(0, non_accessible_figure_count, non_accessible_colour_scheme, non_accessible_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)
  non_accessible_figure_count = create_BSF_Remediation_over_time(0, non_accessible_figure_count, non_accessible_colour_scheme, paths_variables, month, year, data_label_font_dict_white, data_label_font_dict_black)
  non_accessible_figure_count = create_BSF_Tenure(0, non_accessible_figure_count, non_accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)

  # CSS
  non_accessible_figure_count = create_CSS_Eligibility2(0, non_accessible_figure_count, non_accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)
  non_accessible_figure_count = create_CSS_Height(0, non_accessible_figure_count, non_accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  non_accessible_figure_count = create_CSS_Tenure(0, non_accessible_figure_count, non_accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)

  # Developer
  non_accessible_figure_count = create_Developer_Remediation_Curly(0, non_accessible_figure_count, non_accessible_colour_scheme, non_accessible_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)
  non_accessible_figure_count = create_Developer_Height(0, non_accessible_figure_count, non_accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)


  # Social
  non_accessible_figure_count = create_SocialHousing_Remediation4_Curly(0, non_accessible_figure_count, non_accessible_colour_scheme, non_accessible_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)
  non_accessible_figure_count = create_SocialHousing3_Height(0, non_accessible_figure_count, non_accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)

  # RAP
  #non_accessible_figure_count = create_18m_RAP_estimates(0, non_accessible_figure_count, non_accessible_colour_scheme, non_accessible_grey, non_accessible_secondary_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  ##########
  # ACCESSIBLE
  ##########

  # Overall
  accessible_figure_count = create_Overall_remediation_estimates2(1, accessible_figure_count, accessible_colour_scheme, accessible_grey, accessible_secondary_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  accessible_figure_count = create_Overall_Remediation_over_time3(1, accessible_figure_count, accessible_colour_scheme,accessible_secondary_grey, paths_variables, month, year, data_label_font_dict_white, data_label_font_dict_black)
  accessible_figure_count = create_Overall_Remediation2_Curly(1, accessible_figure_count, accessible_colour_scheme, accessible_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)
  accessible_figure_count = create_Overall_Remediation_Across_Schemes2(1, accessible_figure_count, accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  accessible_figure_count = create_Overall_Height(1, accessible_figure_count, accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  accessible_figure_count = create_Overall_Tenure(1, accessible_figure_count, accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)

  #Accessible map
  accessible_figure_count += 1

  # ACM
  accessible_figure_count =  create_ACM_Remediation(1, accessible_figure_count, accessible_colour_scheme, accessible_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)

  #Accessible figures 8&9
  accessible_figure_count += 1
  accessible_figure_count += 1
  accessible_figure_count = create_ACM_By_Tenure(1, accessible_figure_count, accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)

  # BSF
  accessible_figure_count = create_BSF_Remediation_Curly(1,accessible_figure_count, accessible_colour_scheme, accessible_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)
  accessible_figure_count = create_BSF_Remediation_over_time(1, accessible_figure_count, accessible_colour_scheme, paths_variables, month, year, data_label_font_dict_white, data_label_font_dict_black)
  accessible_figure_count = create_BSF_Tenure(1,accessible_figure_count, accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)

  # CSS
  accessible_figure_count = create_CSS_Eligibility2(1, accessible_figure_count, accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)
  accessible_figure_count = create_CSS_Height(1, accessible_figure_count, accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  accessible_figure_count = create_CSS_Tenure(1, accessible_figure_count, accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)

  # Developer
  accessible_figure_count = create_Developer_Remediation_Curly(1, accessible_figure_count, accessible_colour_scheme, accessible_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)
  accessible_figure_count = create_Developer_Height(1, accessible_figure_count, accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)
  
  # RAP
  #accessible_figure_count = create_18m_RAP_estimates(1, accessible_figure_count, accessible_colour_scheme, accessible_grey, accessible_secondary_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black)

  # Social
  accessible_figure_count = create_SocialHousing_Remediation4_Curly(1, accessible_figure_count, accessible_colour_scheme, accessible_grey, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)
  accessible_figure_count = create_SocialHousing3_Height(1, accessible_figure_count, accessible_colour_scheme, paths_variables, data_label_font_dict_white, data_label_font_dict_black)


# Call the main function
if __name__ == "__main__":
  create_graphs(non_accessible_colour_scheme, non_accessible_grey, accessible_colour_scheme, accessible_grey, non_accessible_figure_count, accessible_figure_count, paths_variables, data_label_font_dict_white, data_label_font_dict_black, brace_label_font_dict)


# End the timer and print the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Program executed in {elapsed_time:.2f} seconds")
print('Done! Have a nice day :)')