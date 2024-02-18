        colName = cells[0].text.strip()  # Assuming this correctly extracts the column name
        input_element = cells[1].find_element(By.XPATH, ".//input")
        input_type = input_element.get_attribute("type")
        print(input_type)