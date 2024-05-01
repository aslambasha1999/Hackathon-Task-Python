from Utilities.selenium_actions import selenium_keyword_mapping

def implement_selenium_method_body(step_text, logging, arg_names):
    try:
        logging.info(f"Implementing selenium method body for step :{step_text}")
        # Split step text into keywords
        keywords = step_text.lower().split()

        selenium_methods = []
        element_lookup = False  # Flag to indicate whether an element lookup is needed
        i = 0
        while i < len(keywords):
            # Check for multi-word keywords
            for j in range(len(keywords), i, -1):
                multi_word_keyword = ' '.join(keywords[i:j])
                if multi_word_keyword in selenium_keyword_mapping:
                    method = selenium_keyword_mapping[multi_word_keyword]
                    if 'element' in method:
                        selenium_methods.append('element =context.driver.find_element("By.YourLocator", \'Your Locator\')')
                        element_lookup = True
                    selenium_methods.append(method)
                    i = j  # Move to the next keyword after the multi-word keyword
                    break
            else:
                # If no multi-word keyword is found, check for single-word keyword
                if keywords[i] in selenium_keyword_mapping:
                    method = selenium_keyword_mapping[keywords[i]]
                    if 'element' in method:
                        selenium_methods.append('element =context.driver.find_element("By.YourLocator", \'Your Locator\')')
                        element_lookup = True
                    selenium_methods.append(method)
                i += 1

        # Replace placeholders with arguments
        for idx, method in enumerate(selenium_methods):
            if '"Add Your Argument"' in method and arg_names:
                # Pop arg_names to get the next argument if the list is not empty
                arg_value = arg_names.pop(0)
                # Replace the placeholder with the argument value
                selenium_methods[idx] = method.replace('"Add Your Argument"', arg_value)

        return selenium_methods
    except Exception as e:
        # Log the error and return an empty list if an exception occurs
        logging.error(f"Error occurred in implement_method_body: {str(e)}")
        return []
#Working one