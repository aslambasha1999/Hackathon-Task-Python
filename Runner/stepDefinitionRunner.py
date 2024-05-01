import os
import sys
import platform
import logging
from datetime import datetime
sys.path.append(os.getcwd())# Add the current directory to the Python path
from Utilities.generate_report import generate_html_report
from Utilities.config import *


# # Check if the script is run from StepDefinitionRunner.py
if os.path.basename(__file__) in sys.argv[0]:
    print("Running from StepDefinitionRunner.py")
    logs_folder, reports_folder, features_folder, steps_folder = setup_folders() #The setup_folders function reads folders' paths from configurations.
    setup_logging(logs_folder)  #setup logging configuration from config.py
else:
    print("Running from StepDefinitionGenerator.py")

# Import the generate_step_definitions function from StepDefinitionGenerator module
from Main.StepDefinitionGenerator import step_definitions_generator

#Get the path to the reports where you want to store the generated reports
report_file_path = setup_reports(reports_folder)

# Initialize execution results lists
feature_file_execution_results = []
scenario_execution_results = []


# Start overall execution timer
overall_start_time = datetime.now()

try:
    # Get all .feature files in the Features folder
    feature_files = [file for file in os.listdir(features_folder) if file.endswith(".feature")]

    # Generate step definitions for each feature file
    for feature_file in feature_files:
        feature_file_path = os.path.join(features_folder, feature_file)
        output_file_name = os.path.splitext(feature_file)[0] + "_step_definitions.py"
        output_file_path = os.path.join(os.getcwd(), "steps", output_file_name)

        # Start feature file execution timer
        feature_start_time = datetime.now()

        try:
            # Generate step definitions for the feature file
            scenario_results = step_definitions_generator(feature_file_path, output_file_path, logging, "py")
            
            if isinstance(scenario_results, str):  # Check if scenario_results is an error message
                raise Exception(scenario_results)  # Raise exception with the error message
        

            # Append feature file name to each scenario result
            scenario_results_with_feature = [(feature_file,) + result for result in scenario_results]
            scenario_execution_results.extend(scenario_results_with_feature)
                # Check if any scenario has failed
            for scenario_result in scenario_results:
                if scenario_result[1] == "Fail":
                    feature_status = "Fail"
                    break
                else:
                    feature_status = "Pass"
        except Exception as e:
            #logging.error(f"An error occurred while generating step definitions for feature file {feature_file}: {str(e)}")
            feature_status = "Fail"

        # End feature file execution timer
        feature_end_time = datetime.now()
        feature_execution_time = feature_end_time - feature_start_time

        # Append feature file execution results
        feature_file_execution_results.append((feature_file, feature_status, feature_execution_time.total_seconds()))

    # Generate HTML report for feature files and scenarios
    generate_html_report(feature_file_execution_results, scenario_execution_results, report_file_path)

except Exception as e:
    logging.error(f"An error occurred during execution: {e}")

#fully Working code