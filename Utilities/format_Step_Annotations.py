import re
import logging

def format_step_annotation_old(step_text, logging):
    try:
        # Mapping of data types to placeholders
        logging.info(f"Formatting step annotation for step: {step_text}")
        data_type_mapping = {
            'int': '{int}',
            'float': '{float}',
            'bool': '{bool}',
            'String': '{string}',
            # Add more data types and corresponding placeholders as needed
        }
        
        parameters = re.findall(r"'([^']*)'|\"([^\"]*)\"|<([^>]*)>|\$(\d+)|([+-]?\d+\.?\d*)", step_text)
        
        if parameters:
            step_annotation = step_text
            for group in parameters:
                for param in group:
                    if param:
                        if '<' + param + '>' in step_text:
                            # Replace angled brackets with curly braces without quotes
                            step_annotation = step_annotation.replace('<' + param + '>', '{string}')
                        elif "'" + param + "'" in step_text:
                            # If the parameter is inside single quotes, treat it as a string parameter
                            step_annotation = step_annotation.replace("'" + param + "'", '{string}')
                        elif '"' + param + '"' in step_text:
                            # If the parameter is inside double quotes, treat it as a string parameter
                            step_annotation = step_annotation.replace('"' + param + '"', '{string}')
                        elif param.isdigit():
                            # If the parameter is a numerical value, treat it as a string parameter
                            step_annotation = step_annotation.replace(param, '{int}')
                        else:
                            # Determine the data type of the parameter
                            data_type = determine_data_type(param, logging)
                            # Replace the parameter with the corresponding placeholder
                            if data_type in data_type_mapping:
                                step_annotation = step_annotation.replace(param, data_type_mapping[data_type])
            return step_annotation
        return step_text
    except Exception as e:
        logging.error(f"Error occurred in format_step_annotation_old: {str(e)}")


def determine_data_type(param, logging):
    try:
        # Determine the data type of the parameter
        if param.isdigit():
            return 'int'
        try:
            float(param)
            return 'float'
        except ValueError:
            pass
        if param.lower() in ('true', 'false'):
            return 'bool'
        
        return 'String'  # Default to str if cannot determine the data type
    except Exception as e:
        logging.error(f"Error occurred in determine_data_type: {str(e)}")
        return 'String'  # Default to str in case of error
