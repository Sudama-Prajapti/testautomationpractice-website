
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj = Service(r"C:\drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID, 'name').send_keys()
time.sleep(2)
driver.find_element(By.ID, 'email').send_keys()
time.sleep(2)
driver.find_element(By.ID, 'phone').send_keys()
time.sleep(2)
driver.find_element(By.ID,'textarea').send_keys()
time.sleep(2)
driver.find_element(By.ID, 'male').click()
time.sleep(2)
driver.find_element(By.ID, 'sunday').click()
time.sleep(2)
driver.find_element(By.ID, 'country').send_keys('india')
time.sleep(5)
driver.find_element(By.XPATH,"//option[@value='white']").click()
time.sleep(2)
driver.find_element(By.ID, 'animals').send_keys('dog')
time.sleep(2)
# date pickers
year = '2024'
month = 'october'
days = '10'
driver.find_element(By.ID, 'datepicker').click()
while True:
    mon = driver.find_element(By.CLASS_NAME,'ui-datepicker-month').text
    yyy = driver.find_element(By.CLASS_NAME,'ui-datepicker-year').text

    if mon==month and yyy == year:
        break;
    else:
        driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[1]/span').click()

time.sleep(10)

driver.close()