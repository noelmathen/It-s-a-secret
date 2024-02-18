from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

column_names = [
    'Enroll Number',
    'Name',
    'Faculty Code(3 Digit Code eg:"AGP")',
    'Designation',
    'Gender',
    'Date of Birth [Official]',
    'Date of Birth [Actual]',
    'Qualifications',
    'Additional Eligibility/Qualifications',
    'Department',
    'KTU-ID',
    'Google Scholar ID',
    'ORCID iD',
    'Year of obtaining Ph. D.(if Applicable)',
    'Year of recognition as Ph.D. guide(if Applicable)',
    'Ph.D Guideship',
    'Religion',
    'Caste',
    'Category',
    'Communication Address',
    'Permanent Address',
    'Blood Group',
    'Physically Handicapped',
    'Aadhar No.',
    'Experience',
    'Area of Interest',
    'Memberships, if any',
    'Email Address(RAJAGIRITECH.EDU.IN)',
    'Email Address(GMAIL)',
    'Mobile Number',
    'Whatsapp Number',
    'Facebook Profile[link]',
    'Linkedin Profile[link]',
    'Instagram Profile[link]',
    'Twitter Profile[link]',
    'Threads Profile[link]',
    'Personal Website',
    'Landline',
    'Emergency Contact Number',
    'Staff/Lab Phone Extn. No',
    'Staff/Lab Room No',
    'Staff/Lab Room Name',
    'Primary Vehicle Type',
    'Vehicle No',
    'Secondary Vehicle Type',
    'Vehicle No',
    'Third Vehicle Type',
    'Vehicle No',
    'Rajagiri Valley South Indian Bank A/C No',
    'College Laptop Number(if Any)',
    'College Laptop Make(if Any)',
    'Laptop Issue Date',
    'Active',
    'Date of Join',
    'Date of Joining in Teaching Profession',
    'No of Years Spent Other than Teaching Jobs',
    'Last Promotion Date'
]

details = pd.DataFrame(columns=column_names)
print(details)

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
        second_cell = row.find_element(By.XPATH, ".//td[2]")

        # vTable = second_cell.find_elements(By.XPATH, "./table[@width='100%']")
        # if vTable:
        #     print(vTable[0].text.strip())
        #     continue

        input_element = second_cell.find_elements(By.TAG_NAME, "input")
        if input_element:
            value = input_element[0].get_attribute("value")
            print("Value:", value)
            continue  # Move to the next row
        
        select_element = second_cell.find_elements(By.TAG_NAME, "select")
        if select_element:
            options = select_element[0].find_elements(By.TAG_NAME, "option")
            if options:
                value = options[0].get_attribute("value")
                if value:
                    print("Selected Value:", value)
                else:
                    print("No option selected")
            else:
                print("No options available")
            continue

        
        value = second_cell.text.strip()
        print("Text Value:", value)
        
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
