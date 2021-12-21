import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = Options()

options.add_argument(r"user-data-dir=C:\Users\sidr2\AppData\Local\Google\Chrome\User Data")
options.add_argument("--profile-directory=Profile 3")

driver = webdriver.Chrome(r"D:\Homework\chromedriver_win32\chromedriver.exe",options=options)

phone = "number here"
amount = "amt here"
driver.get("https://www.amazon.in/hfc/mobileRecharge?ref_=apay_deskhome_MobileRecharge")
time.sleep(3)
driver.find_element_by_id("mobileNumberTextInputId").send_keys(phone)
time.sleep(3)
driver.find_element_by_id("amountTextInputId").send_keys(amount)
driver.find_element_by_id("payButtonText").click()
time.sleep(5)
driver.find_element_by_name("ppw-widgetEvent:SetPaymentPlanSelectContinueEvent").click()
time.sleep(30)
driver.quit()