def format_step_function_name(step_text, logging):
    try:
        logging.info(f"formatting step function name for step :{step_text}")
        step_function_name = step_text.lower().replace('#','_').replace('%','_').replace(',','_').replace('$','_').replace('.', '_').replace("@","_").replace('//', "_").replace(":", "_").replace(' ', '_').replace("<", '').replace(">", '').replace('"', '').replace("'", '').replace('(', '').replace(')', '').replace('-', '_').replace("@","_").replace("/","_")
        return step_function_name
    except Exception as e:
        logging.error(f"Error occurred in format_step_function_name: {str(e)}")
        return ""
