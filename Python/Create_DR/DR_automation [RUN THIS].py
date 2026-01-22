# DR_automation.py
"""
Created on Wednesday 18 December 2024, 08:02:22

Author: Harry Simmons
"""

"""
This code takes all of the the individual sections of this projects and runs them in order here.
This was done to:
    - Make it easier to navigate this project by splitting up parts of it
"""

import time
import os 
# Start the timer
start_time = time.time()
##__init__ files in each subfolder set up these imports 
from Utility import sort_dates, create_paths

from DR_infrastructure import setup_doc, DR_start, DR_introduction, DR_enquiries, DR_building_safety_overview, DR_end

from Portfolio import Portfolio_retrieve_data, Portfolio_variable_creator, Portfolio_headline_writer, Portfolio_section_writer

from Estimates import Estimates_variable_creator, Estimates_section_writer

from Costs import Costs_retrieve_data, Costs_variable_creator, Costs_section_writer

from ACM import ACM_retrieve_data, ACM_variable_creator, ACM_headline_writer, ACM_section_writer

from BSF import BSF_retrieve_data, BSF_variable_creator, BSF_headline_writer, BSF_section_writer

from CSS import CSS_retrieve_data, CSS_variable_creator, CSS_headline_writer, CSS_section_writer

from Developer import Developer_retrieve_data_last_month, Developer_retrieve_data_this_month, Developer_variable_creator, Developer_headline_writer, Developer_section_writer

from Social import Social_retrieve_data_last_quarter, Social_retrieve_data_last_month, Social_retrieve_data_this_month, Social_variable_creator, Social_headline_writer, Social_section_writer

from Enforcement import Enforcement_retrieve_data, Enforcement_variable_creator, Enforcement_headline_writer, Enforcement_section_writer


def create_DR():
    # Handle data
    figure_count = 1
    table_count = 1
    dates_variables = sort_dates()
    paths_variables = create_paths()

    Portfolio_handled_data = Portfolio_retrieve_data(paths_variables)
    Costs_handled_data = Costs_retrieve_data(paths_variables)
    ACM_handled_data = ACM_retrieve_data(dates_variables, paths_variables)
    BSF_handled_data = BSF_retrieve_data(paths_variables)
    CSS_handled_data = CSS_retrieve_data(paths_variables)
    Developer_handled_data_last_month = Developer_retrieve_data_last_month(paths_variables)
    Developer_handled_data_this_month = Developer_retrieve_data_this_month(paths_variables)
    #Social_handled_data_last_quarter = Social_retrieve_data_last_quarter(paths_variables)
    #Social_handled_data_last_month = Social_retrieve_data_last_month(paths_variables)
    #Social_handled_data_this_month = Social_retrieve_data_this_month(paths_variables)
#    RAP_handled_data = RAP_retrieve_data(paths_variables)
    Enforcement_handled_data = Enforcement_retrieve_data(paths_variables)

    # Format variables
    print('Formatting Variables')
    Estimates_tables, Estimates_headline_dict, Estimates_section_dict = Estimates_variable_creator(Portfolio_handled_data)
    Costs_tables, Costs_section_dict = Costs_variable_creator(Costs_handled_data)
    Portfolio_tables, Portfolio_headline_dict, Portfolio_section_dict = Portfolio_variable_creator(Portfolio_handled_data)
    ACM_tables, ACM_headline_dict, ACM_section_dict = ACM_variable_creator(ACM_handled_data, dates_variables)
    BSF_tables, BSF_headline_dict, BSF_section_dict, BSF_developer_transfers = BSF_variable_creator (BSF_handled_data)
    CSS_tables, CSS_headline_dict, CSS_section_dict = CSS_variable_creator (CSS_handled_data)
    Developer_tables, Developer_headline_dict, Developer_section_dict = Developer_variable_creator(Developer_handled_data_last_month, Developer_handled_data_this_month, dates_variables)
#    RAP_section_dict = RAP_variable_creator(RAP_handled_data)
    #Social_tables, Social_headline_dict, Social_section_dict = Social_variable_creator(Social_handled_data_last_quarter, Social_handled_data_this_month, Social_handled_data_last_month)
    Enforcement_headline_dict, Enforcement_section_dict = Enforcement_variable_creator(Enforcement_handled_data)
    print('DONE!')

    # Write DR
    print('Writing Data Release')
    DR = setup_doc()
    DR_start(dates_variables, DR)
    figure_count = Portfolio_headline_writer(Portfolio_headline_dict, Estimates_headline_dict, figure_count, dates_variables, paths_variables, DR)
    ACM_headline_writer(ACM_headline_dict, dates_variables, DR)
    BSF_headline_writer(BSF_headline_dict, dates_variables, DR)
    CSS_headline_writer(CSS_headline_dict, dates_variables, DR)
    Developer_headline_writer(Developer_headline_dict, dates_variables, DR)
    #Social_headline_writer(Social_headline_dict, dates_variables, DR)
    Enforcement_headline_writer(Enforcement_headline_dict, dates_variables, DR)
    DR_introduction(DR, figure_count)
    DR_enquiries(dates_variables, DR)
    DR_building_safety_overview(DR)
    table_count = Estimates_section_writer(Estimates_section_dict, Estimates_tables, table_count, dates_variables, DR)
    table_count = Costs_section_writer(Costs_section_dict, Costs_tables, table_count, dates_variables, DR)
    figure_count, table_count= Portfolio_section_writer(Portfolio_section_dict, Portfolio_tables, figure_count, table_count, dates_variables, paths_variables, DR)
    figure_count, table_count = ACM_section_writer(ACM_section_dict, ACM_tables, figure_count, table_count, dates_variables, paths_variables, DR)
    figure_count, table_count = BSF_section_writer(BSF_section_dict, BSF_tables, figure_count, table_count, dates_variables, paths_variables, DR)
    figure_count, table_count = CSS_section_writer(CSS_section_dict, CSS_tables, figure_count, table_count, dates_variables, paths_variables, DR)
    figure_count, table_count = Developer_section_writer(Developer_section_dict, BSF_developer_transfers, Developer_tables, figure_count, table_count, dates_variables, paths_variables, DR)
#    figure_count = RAP_section_writer(RAP_section_dict,figure_count, dates_variables, DR)
    #figure_count, table_count = Social_section_writer(Social_section_dict, Social_tables, figure_count, table_count, dates_variables, paths_variables, DR)
    Enforcement_section_writer(Enforcement_section_dict, dates_variables, DR)
    DR_end(DR, dates_variables)
    print('DONE!')

    # Saving the document
    this_month = dates_variables['this_month']
    save_path = paths_variables['save_path']

    output_path = os.path.join(save_path, f'Building Safety Release {this_month}.docx')
    DR.save(output_path)



# Call the main function
if __name__ == "__main__":
    create_DR()

# End the timer and print the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Program executed in {elapsed_time:.2f} seconds")
print('Done! Have a nice day :)')