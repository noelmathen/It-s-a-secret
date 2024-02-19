import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from column_names import column_names
from dotenv import load_dotenv
import os

try:
    details = pd.DataFrame(columns=column_names)
    driver = webdriver.Chrome()
    load_dotenv()
    URL = os.getenv('URL')
    driver.get(URL)

    dropdown = Select(driver.find_element(By.NAME, "Sid"))
    options = dropdown.options

    for option in options:
        option.click()
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "B1")))
        table = driver.find_element(By.XPATH, "//table[@width='70%']")
        rows = table.find_elements(By.XPATH, ".//tr")
        info = []

        for row in rows:
            try:
                try:
                    second_cell = row.find_element(By.XPATH, ".//td[2]")
                except NoSuchElementException:
                    second_cell = row.find_element(By.XPATH, ".//td[1]")

                input_element = second_cell.find_elements(By.TAG_NAME, "input")
                if input_element:
                    value = input_element[0].get_attribute("value")
                    if value == "":
                        value = "NaN"
                    elif value == 'ON':
                        value = 'YES'
                    elif value == 'OFF':
                        value = 'NO'
                    info.append(value)
                    continue  

                select_element = second_cell.find_elements(By.TAG_NAME, "select")
                if select_element:
                    options = select_element[0].find_elements(By.TAG_NAME, "option")
                    if options:
                        value = options[0].get_attribute("value")
                        if value:
                            info.append(value)
                        else:
                            default_option = options[0].get_attribute("selected")
                            if default_option:
                                value = "NaN"
                                info.append(value)
                            else:
                                value = "NaN"
                                info.append(value)
                    continue

                value = second_cell.text.strip()
                if value == "":
                    value = "NaN"
                info.append(value)

            except (NoSuchElementException, IndexError) as e:
                print(f"Error: {e}")

        print("\nExtracted Data:")
        del info[0]
        del info[43]
        # for index, element in enumerate(info):
        #     print(f"{index + 1}. {element}")

        details.loc[len(details)] = info
        print("\nDataFrame:")
        print(details)
        details.to_excel('details.xlsx', index=False)
        driver.back()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "B2")))


except TimeoutException:
    print("Timeout occurred while waiting for the page to load.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
