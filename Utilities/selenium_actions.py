selenium_keyword_mapping = {
    'open': 'context.driver.get("Add Your Argument")',
    'opens': 'context.driver.get("Add Your Argument")',
    'open the browser': 'context.driver = webdriver.Chrome(executable_path="Your chromedriver.exe Path")',
    'opens the browser': 'context.driver = webdriver.Chrome(executable_path="Your chromedriver.exe Path")',
    'launch the browser': 'context.driver = webdriver.Chrome(executable_path="Your chromedriver.exe Path")',
    'navigate': 'context.driver.navigate.to("Add Your Argument")',
    'navigates': 'context.driver.navigate.to("Add Your Argument")',
    'launch': 'context.driver.get("Add Your Argument")',
    'launches': 'context.driver.get("Add Your Argument")',
    'visit': 'context.driver.get("Add Your Argument")',
    'visits': 'context.driver.get("Add Your Argument")',
    'go to': 'context.driver.get("Add Your Argument")',
    'goes to': 'context.driver.get("Add Your Argument")',
    'enter': 'element.send_keys("Add Your Argument")',
    'enters': 'element.send_keys("Add Your Argument")',
    'type': 'element.send_keys("Add Your Argument")',
    'types': 'element.send_keys("Add Your Argument")',
    'input': 'element.send_keys("Add Your Argument")',
    'inputs': 'element.send_keys("Add Your Argument")',
    'click': 'element.click()',
    'clicks': 'element.click()',
    'press the enter': 'element.send_keys(Keys.ENTER)',
    'submit': 'element.submit()',
    'check': 'element.click()',
    'select': 'Select(element).select_by_visible_text("Add Your Argument") or Select(element).select_by_value("Add Your Argument")',
    'selects': 'Select(element).select_by_visible_text("Add Your Argument") or Select(element).select_by_value("Add Your Argument")',
    'choose': 'Select(element).select_by_visible_text("Add Your Argument") or Select(element).select_by_value("Add Your Argument")',
    'scroll': 'context.driver.execute_script("window.scrollBy(0, 250);")',
    'scroll up': 'context.driver.execute_script("window.scrollBy(0, -250);")',
    'scroll ups': 'context.driver.execute_script("window.scrollBy(0, -250);")',
    'scroll down': 'context.driver.execute_script("window.scrollBy(0, 250);")',
    'scroll downs': 'context.driver.execute_script("window.scrollBy(0, 250);")',
    'scroll to element': 'context.driver.execute_script("arguments[0].scrollIntoView();", element)',
    'move to element': 'ActionChains(context.driver).move_to_element(element).perform()',
    'hover': 'ActionChains(context.driver).move_to_element(element).perform()',
    'clear': 'element.clear()',
    'reset': 'element.clear()',
    'refresh': 'context.driver.refresh()',
    'back': 'context.driver.back()',
    'forward': 'context.driver.forward()',
    'maximize': 'context.driver.maximize_window()',
    'minimize': 'context.driver.minimize_window()',
    'resize': 'context.driver.set_window_size("Add width", "Add height")',
    'close': 'context.driver.close()',
    'quit': 'context.driver.quit()',
    'alert': 'context.driver.switch_to.alert',
    'switch to frame': 'context.driver.switch_to.frame("frame_element")',
    'switch to window': 'context.driver.switch_to.window("window_handle")',
    'switch to default content': 'context.driver.switch_to.default_content()',
    'enter username and password': 'element.send_keys("Add Your Argument")\n\telement =context.driver.find_element(By.XPATH, "your_xpath")\n\telement.send_keys("Add Your Argument")',
    'execute script': 'context.driver.execute_script("javascript_code")',
    'wait': 'WebDriverWait(context.driver, timeout).until("Add Your Argument")',
    'sleep': 'time.sleep("Add Your Argument")',
    'assert': 'assert "expected_value" =="Add Your Argument"',
    'verify': 'assert "expected_value" == "Add Your Argument"',
    'verifies':'assert "expected_value" == "Add Your Argument"',
    'capture': 'context.driver.save_screenshot("filename")',
    'get text': 'element.text',
    'get attribute': 'element.get_attribute("attribute")',
    'get title': 'context.driver.title',
    'get url': 'context.driver.current_url',
    'get page source': 'context.driver.page_source',
    'get window handle': 'context.driver.window_handles',
    'get window title': 'context.driver.title',
    'get window size': 'context.driver.get_window_size()',
    'get window position': 'context.driver.get_window_position()',
    'set window size': 'context.driver.set_window_size("Add width", "Add height")',
    'set window position': 'context.driver.set_window_position("x", "y")',
    'drag and drop': 'ActionChains(context.driver).drag_and_drop("source_element", "target_element").perform()',
    'swipe': 'TouchAction(context.driver).press("x_start", "y_start").move_to("x_end", "y_end").release().perform()',
    'double click': 'ActionChains(context.driver).double_click(element).perform()',
    'right click': 'ActionChains(context.driver).context_click(element).perform()',
    'click and hold': 'ActionChains(context.driver).click_and_hold(element).perform()',
    'release': 'ActionChains(context.driver).release(element).perform()',
    'navigate back': 'context.driver.back()',
    'navigate forward': 'context.driver.forward()',
    'upload file': 'element.send_keys("/path/to/file")',
    'download file': 'Depends on browser settings',
    'wait for element present': 'WebDriverWait(context.driver, timeout).until(expected_conditions.presence_of_element_located(("Add Your Locator")))',
    'wait for element visible': 'WebDriverWait(context.driver, timeout).until(expected_conditions.visibility_of_element_located(("Add Your Locator")))',
    'wait for element clickable': 'WebDriverWait(context.driver, timeout).until(expected_conditions.element_to_be_clickable(("Add Your Locator")))',
    'wait for element selected': 'WebDriverWait(context.driver, timeout).until(expected_conditions.element_to_be_selected(("Add Your Locator")))',
    'wait for element text': 'WebDriverWait(context.driver, timeout).until(expected_conditions.text_to_be_present_in_element(("Add Your Locator"), "expected_text"))',
    'wait for title': 'WebDriverWait(context.driver, timeout).until(expected_conditions.title_is("expected_title"))',
    'wait for url': 'WebDriverWait(context.driver, timeout).until(expected_conditions.url_to_be("expected_url"))',
    'assert element present': 'assert element.is_displayed()',
    'assert element visible': 'assert element.is_displayed()',
    'assert element clickable': 'assert element.is_enabled()',
    'assert element selected': 'assert element.is_selected()',
    'assert element text': 'assert element.text == "Add Your Argument"',
    'assert title': 'assert context.driver.title == "Add Your Argument"',
    'verifies title': 'assert context.driver.title == "Add Your Argument"',
    'verifies the title': 'assert context.driver.title == "Add Your Argument"',
    'assert url': 'assert context.driver.current_url == "expected_url"',
    'zoom in': 'context.driver.execute_script("document.body.style.zoom=\'zoom_level%\'")',
    'zoom out': 'context.driver.execute_script("document.body.style.zoom=\'zoom_level%\'")',
    'set cookie': 'context.driver.add_cookie({"name": "cookie_name", "value": "cookie_value"})',
    'delete cookie': 'context.driver.delete_cookie("cookie_name")',
    'hover over': 'ActionChains(context.driver).move_to_element(element).perform()',
    'highlight': 'context.driver.execute_script("arguments[0].style.border=\'3px solid red\';", element)',
    'hide element': 'context.driver.execute_script("arguments[0].style.display=\'none\';", element)',
    'show element': 'context.driver.execute_script("arguments[0].style.display=\'block\';", element)',
}
