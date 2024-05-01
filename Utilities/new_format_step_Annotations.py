import re
def format_step_annotation(step_text, logging):
    try:
        # Mapping of data types to placeholders
        logging.info(f"formatting step annotation for step :{step_text}")
        
        # Regular expression pattern to match parameters
        parameter_pattern = r"'([^']*)'|\"([^\"]*)\"|<([^>]*)>|\$(\d+)|([+-]?\d+\.?\d*)"

        parameters = re.findall(parameter_pattern, step_text)
        
        if parameters:
            step_annotation = step_text
            arg_count = 1  # Counter for masked arguments
            num_arg_count=1
            for group in parameters:
                for param in group:
                    if param:
                        if '<' + param + '>' in step_text:
                            # Replace angled brackets with curly braces without quotes
                            step_annotation = step_annotation.replace('<' + param + '>', '{' + param + '}')
                        elif '"' + param + '"' in step_text or  "'" + param + "'" in step_text:
                            if param.isdigit():
                    
                                # Replace int parameters with numArg placeholders
                                step_annotation = step_annotation.replace('"' + param + '"', "{"f'numArg{num_arg_count}'"}").replace("'" + param + "'", "{"f'numArg{num_arg_count}'"}")
                                num_arg_count += 1                         
                            else:
                                # Replace double quotes with single quotes vise versa and mask the parameter
                                step_annotation = step_annotation.replace('"' + param + '"', "{"f'arg{arg_count}'"}").replace("'" + param + "'", "{"f'arg{arg_count}'"}")
                                arg_count += 1
                        elif param.isdigit():
                            # Replace $ sign parameters with numArg placeholders
                            step_annotation = step_annotation.replace(param, "{"f'numArg{num_arg_count}'"}")
                            num_arg_count+=1
                        else:
                            # Replace the parameter with the corresponding placeholder
                            step_annotation = step_annotation.replace(param, f'arg{arg_count}')
                            arg_count += 1
            return step_annotation
        return step_text
    except Exception as e:
        logging.error(f"Error occurred in format_step_annotation: {str(e)}")
