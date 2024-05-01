import re
def extract_parameters_from_step_text_java(step_text, step_annotation,data_table_lines,logging):
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