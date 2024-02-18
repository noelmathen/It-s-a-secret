from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

cNames = []


driver = webdriver.Chrome()
URL = "https://www.rajagiritech.ac.in/stud/ktu/Faculty/Fac_details.asp"
driver.get(URL)

dropdown = Select(driver.find_element(By.NAME, "Sid"))
driver.find_element(By.XPATH, "//input[@type='submit']").click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.NAME, "B1")
    )
)

table = driver.find_element(By.XPATH, "//table[@width='70%']")
rows = table.find_elements(By.XPATH, ".//tr")
for row in rows:
    try:
        cells = row.find_elements(By.XPATH, ".//td")
        colName = cells[0].text.strip()
        # if colName == "Vehicles No":
        #     # Find the nested table within the current row
        #     vTable = cells[1].find_element(By.XPATH, ".//table[@border='0']")
        #     vRows = vTable.find_elements(By.XPATH, ".//tr")
        #     vehicle_details_printed = False  # Flag to track whether vehicle details have been printed
        #     for vrow in vRows:
        #         try:
        #             # Find the select element within the current row
        #             select_element = vrow.find_element(By.XPATH, ".//select")
        #             # Extract text from the select element
        #             print(select_element.text.strip())
        #         except NoSuchElementException:
        #             pass
        #         try:
        #             # Find the input element within the current row
        #             input_element = vrow.find_element(By.XPATH, ".//input")
        #             # Extract text from the input element
        #             vehicle_number = input_element.get_attribute("value").strip()
        #             print(vehicle_number)
        #             print("\nHelloooooo\n")
        #             vehicle_details_printed = True  # Set flag to True since vehicle details have been printed
        #         except NoSuchElementException:
        #             pass
        #     # If vehicle details have been printed, skip to the next row
        #     if vehicle_details_printed:
        #         continue
        # # If the column name is not "Vehicles No" or vehicle details haven't been printed, print the column name
        print(colName)
    except IndexError:
        print("No cells found in row")




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
