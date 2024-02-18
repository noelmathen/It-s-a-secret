from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from .column_names import column_names


details = pd.DataFrame(columns=column_names)
print(details)

driver = webdriver.Chrome()
URL = "https://www.rajagiritech.ac.in/stud/ktu/Faculty/Fac_details.asp"
driver.get(URL)

dropdown = Select(driver.find_element(By.NAME, "Sid"))
dropdown.select_by_visible_text("SONIA PAUL")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.NAME, "B1")
    )
)

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
            print("Value:", value)
            continue  # Move to the next row
        
        select_element = second_cell.find_elements(By.TAG_NAME, "select")
        if select_element:
            options = select_element[0].find_elements(By.TAG_NAME, "option")
            if options:
                value = options[0].get_attribute("value")
                if value:
                    info.append(value)
                    print("Selected Value:", value)
                else:
                    # Check if the default option is selected (i.e., no option is selected)
                    default_option = options[0].get_attribute("selected")
                    if default_option:
                        value = "NaN"
                        info.append(value)
                        print("No option selected")
                    else:
                        value = "NaN"
                        info.append(value)
                        print("Selected Value:", "")
            else:
                print("No options available")
            continue

        value = second_cell.text.strip()
        if value == "":
            value = "NaN"
        info.append(value)
        print("Text Value:", value)
        
    except IndexError:
        print("No cells found in row")

print("\n")
del info[0]
del info[43]
for index, element in enumerate(info):
    print(f"{index + 1}. {element}")


# # Handle nested table for vehicle information
#         nested_table = second_cell.find_element(By.XPATH, ".//table[@border='0']/tbody")
#         vehicle_info = nested_table.find_elements(By.TAG_NAME, "tr")
#         for info_row in vehicle_info:
#             vehicle_type = info_row.find_element(By.TAG_NAME, "select").get_attribute("value").strip()
#             vehicle_number = info_row.find_element(By.TAG_NAME, "input").get_attribute("value").strip()
#             print("Vehicle Type:", vehicle_type)
#             print("Vehicle Number:", vehicle_number)

        # vTable = second_cell.find_elements(By.XPATH, "./table[@width='100%']")
        # if vTable:
        #     print(vTable[0].text.strip())
        #     continue


# for option in options:
#     option.click()
#     time.sleep(1.5)
#     driver.find_element(By.XPATH, "//input[@type='submit']").click()
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located(
#             (By.NAME, "B1")
#         )
#     )

#     table = driver.find_element(By.XPATH, "//table[@width='70%']")
#     data={}
#     rows = table.find_elements(By.NAME, "tr")
#     for row in rows:
#         cells = row.find_elements(By.NAME, "td")
#         print(cells[0].text)


#     # print(table.text.strip())
#     time.sleep(1.5)
    

#     driver.back()
#     print("Zett")
#     time.sleep(1.5)

# # driver.find_element(By.NAME, "Userid").send_keys("U2109053")
# # driver.find_element(By.NAME, "Password").send_keys("210825")
# # driver.find_element(By.XPATH, "//input[@type='submit']").click()
