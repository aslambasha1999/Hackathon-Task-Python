
import re,os,sys
from datetime import datetime
sys.path.append(os.getcwd())
from Utilities.format_Step_Annotations import format_step_annotation_old
from Utilities.generate_Imports import write_imports
from Utilities.selenium_actions import selenium_keyword_mapping
from Utilities.new_format_step_Annotations import format_step_annotation
from Utilities.format_Step_Funtion_name import format_step_function_name
from Utilities.New_Implements_Selenium_Methods import *
import logging

# Add the current directory to the Python path java
sys.path.append(os.getcwd())

# Configure Logs
logs_file_path = os.path.join("Logs", "Individual Logs", "individualFile.log")
logging.basicConfig(filename=logs_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def write_step_definitions(feature_file, output_file, scenario, logging):

    # Split the scenario into lines and remove leading/trailing whitespace
    scenario_lines = scenario.strip().split('\n')

    # Extract the name of the scenario from the first line
    scenario_name = scenario_lines[0].strip()

    if scenario_name=='Hide and show an element on the web page':
        error_message = f'Failing Intentioanlly : {scenario_name}'
        raise Exception(error_message)

    # Extract steps along with their associated data tables using a helper function
    steps_with_tables=extract_steps_from_scenario(scenario_lines,logging)

    # Check if no steps are found
    if not steps_with_tables:
        error_message = f'No Steps found in Scenario : {scenario_name}'
        logging.error(error_message)
        raise Exception(error_message)
    
    # Extract lines containing data tables (lines with '|')
    data_table_lines = [line for line in scenario_lines if '|' in line]
    
    with open(output_file, 'a') as file:
        logging.info(f'Writing step definitions for Scenario: {scenario_name} in feature file: {feature_file}')
        logging.info("==================================================================================")
        
        existing_step_texts = read_existing_steps(output_file)

        # Initialize previous step type
        prev_step_type = None

        for step_type, step_text, data_table_lines in steps_with_tables:
            try:
                # Determine the step type
                if step_type == "And":
                    # Use the previous step type if available
                    if prev_step_type:
                        step_type = prev_step_type
                    else:
                        # Default to "Given" if no previous step type is available
                        step_type = "Given"

                # Update the previous step type
                prev_step_type = step_type

                # Format step annotation text and function name
                step_annotation = format_step_annotation(step_text, logging)
                step_function_name = format_step_function_name(step_text, logging)

                # Check for duplicate step text across the feature file
                if step_function_name not in existing_step_texts:
                    existing_step_texts.add(step_function_name)

                    # Generate step definition
                    step_definition = f'@{step_type.lower()}(r"{step_annotation}")\n'

                    # Generate function parameters as arg1, arg2, etc. if not already determined from data table
                    params_data = extract_parameters_from_step_text(step_text, step_annotation, data_table_lines,logging)
                    parameter_string = params_data[0]
                    arg_names_with_context = parameter_string.split(',')
                    arg_names = arg_names_with_context[1:]  # Extracting argument names without context
                    column_names = params_data[1] if len(params_data) > 1 else None  # Check if column_names are returned

                    if parameter_string:
                        logging.info(f'Paramters Identified for the {step_text} are: {parameter_string}')
                        step_definition += f'def {step_function_name}({parameter_string}):\n'
                    else:
                        step_definition += f'def {step_function_name}():\n'

                    #Identifying Selenium Methods
                    # Check if Selenium methods are present
                    selenium_methods = implement_selenium_method_body(step_text, logging,arg_names)

                    if column_names:
                        # Generate data table implementation
                        data_table_imp = data_table_implementation(column_names,logging)
                        step_definition += '\t' + data_table_imp + '\n\n'
                        


                        if selenium_methods:
                            logging.info(f'Selenium methods identified for the step: {selenium_methods}')
                            for method in selenium_methods:
                                step_definition += '\t' + method + '\n\n'
                    else:

                        if selenium_methods:
                            logging.info(f'Selenium methods identified for the step: {selenium_methods}')
                            for method in selenium_methods:
                                step_definition += '\t' + method + '\n\n'
                        else:
                            logging.info('No Selenium methods identified for the step.')
                            step_definition += '    # Add your code here\n'
                            step_definition += '    pass\n\n'

                    file.write(step_definition) #Writing StepDefinition into file
                    logging.info(f'Step definition generated successfully for step: {step_text}')

                else:
                    logging.info(f'Duplicate step found for step: {step_text} in Scenario: {scenario_name}')
            except Exception as e:
                error_message = f"Error: {str(e)} while processing the step: {step_text}"
                logging.error(error_message)
                raise Exception(error_message)

    return scenario_name
def read_existing_steps(output_file):
    existing_steps = set()

    try:
        with open(output_file, 'r') as file:
            step_definitions_content = file.read()
            # Extract existing step texts
            existing_steps.update(re.findall(r'def\s+(\w+)\s*\(.*?\):\s*\n', step_definitions_content))
    except FileNotFoundError:
        pass

    return existing_steps
def data_table_implementation(column_names):
    # Define the parameter names based on the column names available
    parameters = ', '.join(column_names)
    
    # Generate the implementation code
    implementation_code = ""
    if parameters:
        implementation_code = f"for row in context.table:\n"
        for column_name in column_names:
            implementation_code += f"\t\t{column_name} = row['{column_name}']\n"
        implementation_code += f"\t\tprint({parameters})"
    else:
        implementation_code = "No column names provided"
    
    return implementation_code
def extract_steps_from_scenario(scenario_lines,logging):
    """
    Extracts steps along with their associated data tables from a scenario.

    Args:
        scenario (str): The scenario string.

    Returns:
        list: A list of tuples containing step type, step text, and associated data table lines.
    """
    try:
        steps_with_tables = []  # To store steps along with their associated data tables

        # Iterate through each line of the scenario
        for i, line in enumerate(scenario_lines):
            # Check if the line contains a step
            match = re.match(r'^\s*(Given|When|Then|And|But)\s+(.*?)$', line)
            if match:
                step_type, step_text = match.groups()
                data_table_lines = []  # To store data table associated with the current step
                
                # Check subsequent lines for a data table
                for j in range(i + 1, len(scenario_lines)):
                    if '|' in scenario_lines[j]:
                        data_table_lines.append(scenario_lines[j])
                    else:
                        break  # Exit loop if no more data table lines are found
                
                # Store the step along with its associated data table
                steps_with_tables.append((step_type, step_text, data_table_lines))
        
        return steps_with_tables
    except Exception as e:
        error_message = f"An error occurred while extracting steps with tables: {str(e)}"
        logging.error(error_message)
        raise
def extract_parameters_from_step_text(step_text, step_annotation, data_table_lines,logging):
    """
    Extracts parameters from the step text and data table lines.

    Args:
        step_text (str): The text of the step.
        data_table_lines (list): List of lines containing the data table associated with the step.

    Returns:
        tuple: A tuple containing the parameters as argument names and the column names.
    """
    try:
        column_names = []
        if data_table_lines:
            logging.info(f'Data table is identified for the step: {step_text}')
            # Extract column names from the header row
            column_names = [column.strip() for column in data_table_lines[0].split('|') if column.strip()]
        
        # Find parameters in the step annotation
        parameters = re.findall(r'\{([^{}]*)\}', step_annotation)
        
        parameter_string = ','.join(parameters)
        
        if parameter_string:
            # If parameters are found, include 'context' in the parameter string
            parameter_string = f"context,{parameter_string}"
        else:
            # If no parameters are found, set parameter_string to just 'context'
            parameter_string = "context"

        return parameter_string, column_names if column_names else None
    
    except Exception as e:
        logging.error(f"An error occurred while extracting parameters from step text '{step_text}': {str(e)}")
        raise
def identify_scenarios(feature_file,logging):
    try:
        with open(feature_file, 'r') as file:
            logging.info(f'Reading the Feature File: {feature_file}')
            feature_content = file.read()

        # Check if the file is empty
        if not feature_content.strip():
            raise Exception(f"The feature file '{feature_file}' is empty.")

        # Splitting feature content into scenarios and scenario outlines
        scenarios = re.split(r'^\s*(?:Scenario(?: Outline)?)\s*:', feature_content, flags=re.MULTILINE | re.IGNORECASE)[1:]
        
        return scenarios
    
    except Exception as e:
        logging.error(f"An error occurred while identifying Scenarios: {str(e)}")
        raise
def extract_parameters_from_step_text_java(step_text, step_annotation, data_table_lines):
    """
    Extracts parameters from the step text and data table lines.

    Args:
        step_text (str): The text of the step.
        step_annotation (str): The formatted step annotation.
        data_table_lines (list): List of lines containing the data table associated with the step.

    Returns:
        tuple: A tuple containing the parameters as method arguments and the column names.
    """
    try:
        column_names = []
        if data_table_lines:
            logging.info(f'Data table is identified for the step: {step_text}')
            # Extract column names from the header row
            column_names = [column.strip() for column in data_table_lines[0].split('|') if column.strip()]
        
        # Find parameters in the step annotation
        parameters = re.findall(r'\{([^{}]*)\}', step_annotation)
        
        method_arguments = []  # Store method arguments
        
        # Format parameters as method arguments
        param_count = 0
        for param in parameters:
            param_count += 1
            # Determine parameter type (assuming all non-numeric values are strings)
            param_type = "Integer" if param=='int' else "String"
            # Mask parameter name as arg1, arg2, arg3, etc.
            masked_param_name = f"arg{param_count}"
            # Add parameter to method arguments list
            method_arguments.append(f"{param_type} {masked_param_name}")
        

        
        # If data_table is provided, include it in the method arguments
        if data_table_lines:
            method_arguments.append("io.cucumber.datatable.DataTable dataTable")
        
        method_arguments_str = ', '.join(method_arguments)
        
        return method_arguments_str, column_names if column_names else None
    
    except Exception as e:
        logging.error(f"An error occurred while extracting parameters from step text '{step_text}': {str(e)}")
        raise
def write_step_definitions_java(feature_file, output_file, scenario, logging):
    try:
        # Split the scenario into lines and remove leading/trailing whitespace
        scenario_lines = scenario.strip().split('\n')
        

        # Extract the name of the scenario from the first line
        scenario_name = scenario_lines[0].strip()

        # Extract steps along with their associated data tables using a helper function
        steps_with_tables = extract_steps_from_scenario(scenario_lines, logging)
        class_name_parts=feature_file.split(".feature")[0].split("\\")
        if len(class_name_parts) == 1:
            # Splitting by "\\" resulted in only one part
            # This means that the feature_file does not contain "\\"
            # You can now split by "/" to extract the class name
            class_name_parts = feature_file.split(".feature")[0].split("/")
            class_name = class_name_parts[1] + "_step_definitions"
        elif len(class_name_parts) == 2:
            # Splitting by "\\" resulted in two parts
            # This means that the feature_file contains "\\"
            class_name = class_name_parts[1] + "_step_definitions"

        # Check if no steps are found
        if not steps_with_tables:
            error_message = f'No Steps found in Scenario : {scenario_name}'
            logging.error(error_message)
            raise Exception(error_message)

        # Extract lines containing data tables (lines with '|')
        data_table_lines = [line for line in scenario_lines if '|' in line]
        with open(output_file, 'w') as file:
            file.write('// Auto-generated step definitions\n\n')
            file.write('import io.cucumber.java.en.*;\n\n')  # Import statements
            file.write(f"public class {class_name} \n")  # Class declaration
            file.write('{\n\n')
            for step_type, step_text, data_table_lines in steps_with_tables:
                try:
                    step_annotation = format_step_annotation_old(step_text, logging)
                    step_function_name = format_step_function_name(step_text, logging)
                    params_data=extract_parameters_from_step_text_java(step_text, step_annotation, data_table_lines)
                    parameters_str = params_data[0]
                    file.write(f'\t@{step_type}("{step_annotation}")\n')
                    file.write(f'\tpublic void {step_function_name}({parameters_str}) ' + '{\n')
                    # Log parameters
                    logging.info(f"Step: {step_text}, Parameters: {', '.join(parameters_str)}")
                    file.write('\t\t// Add your code here\n')
                    file.write('\t}\n\n')
                except Exception as e:
                    logging.error(f"An error occurred while processing step: {step_text}. Error: {str(e)}")
            file.write('}\n\n')
        logging.info('Step definitions written to Java file successfully')
    except Exception as e:
        logging.error(f"An error occurred while writing step definitions to Java file: {str(e)}")
def step_definitions_generator(feature_file, output_file, logging, output_file_extension):
    try:
        scenarios = identify_scenarios(feature_file, logging)  # Identifying scenarios
        if scenarios:
            logging.info('Scenarios Identified Successfully')
        else:
            scenario_status='Fail'
            raise Exception(f'No Scenarios found in feature file: {feature_file}')
        
   
        scenario_execution_results = []
        error_message = ""
        write_imports_flag = True  # Flag to control whether to write imports
        for scenario in scenarios:
            scenario_exec_start_time = datetime.now()
            try:
                if output_file_extension.lower() == 'java':
                # Generate Java step definitions
                    scenario_executed=write_step_definitions_java(feature_file, output_file, scenario, logging)
                else:
                    # Generate Python step definitions
                    if write_imports_flag:
                        write_imports(output_file)  # writing Necessary Imports
                        logging.info('Import statements added successfully')
                    scenario_executed=write_step_definitions(feature_file, output_file, scenario, logging)

                scenario_status = "Pass"
                scenario_exec_end_time = datetime.now()
                scenario_execution_time = scenario_exec_end_time - scenario_exec_start_time
                scenario_execution_results.append((scenario_executed, scenario_status, scenario_execution_time.total_seconds(), error_message))

            except Exception as e:
                scenario_status = "Fail"
                error_message = str(e)  # Capture the error message
                # # Split the scenario into lines and remove leading/trailing whitespace
                scenario_lines = scenario.strip().split('\n')
                # Extract the name of the scenario from the first line
                scenario_name = scenario_lines[0].strip()
                scenario_execution_results.append((scenario_name, scenario_status,0.0, error_message))
                logging.error(f"An error occurred while generating step definitions for scenario: {scenario_name}, Error: {str(e)}")
            
            write_imports_flag = False  # Set flag to False after writing imports for the first scenario    

        return scenario_execution_results
            
    except Exception as e:
        logging.error(f"An error occurred while generating step definitions: {str(e)}")
        #raise
        return str(e)  # Raise the exception to indicate failure
        

feature_file = 'Features/ScenariowithMultipleSeleniumKeywords.feature'  # Example feature file path
#feature_file = 'Features/FeatureWithDataTable.feature'
output_file = 'steps/step_definitions.py'  # Example output file path
step_definitions_generator(feature_file, output_file, logging,"py")