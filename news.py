import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = Options()

options.add_argument(r"user-data-dir=C:\Users\sidr2\AppData\Local\Google\Chrome\User Data")
options.add_argument("--profile-directory=Profile 3")
options.add_argument("--headless")
options.add_argument("--ignore-certificate-errors-spki-list")
options.add_argument('log-level=3')
#options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(r"D:\Homework\chromedriver_win32\chromedriver.exe",options=options)
a = str()
driver.get("https://www.ndtv.com/latest")
time.sleep(2)
n1 = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[3]/article/div/div/div/div[1]/div/div[1]/div[2]/h2/a")
n2 = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[3]/article/div/div/div/div[1]/div/div[2]/div[2]/h2/a")
n3 = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[3]/article/div/div/div/div[1]/div/div[5]/div[2]/h2/a")
daynews = [n1.text,n2.text,n3.text]
for news in daynews:
    a = a + news + "\n"
driver.quit()
#/html/body/div[2]/div/div/section/div[3]/article/div/div/div/div[1]/div/div[1]/div[2]/h2/a