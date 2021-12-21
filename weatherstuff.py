from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = Options()
options.add_argument(r"user-data-dir=C:\Users\sidr2\AppData\Local\Google\Chrome\User Data")
options.add_argument("--profile-directory=Profile 3")
options.add_argument("--headless")
driver = webdriver.Chrome(r"D:\Homework\chromedriver_win32\chromedriver.exe",options=options)

driver.get("https://www.google.com/search?q=thrissur+weather&oq=thrissur+weath&aqs=chrome.0.0i131i433j0l2j69i57j0j0i457j0l4.7291j1j7&sourceid=chrome&ie=UTF-8")

maxtemp = driver.find_element_by_xpath('//*[@id="wob_dp"]/div[1]/div[3]/div[1]/span[1]')
Maxtemperature = "The maximum temperature in Thrissur will be " + maxtemp.text + " Degrees Celcius"
mintemp = driver.find_element_by_xpath('//*[@id="wob_dp"]/div[1]/div[3]/div[2]/span[1]')
Mintemperature = "The minimum temperature in Thrissur will be " + mintemp.text + " Degrees Celsius"
driver.quit() 
#class="wNE31c
#//*[@id="wob_dp"]/div[1]/div[3]/div[2]/span[1]
#<div class="wNE31c"><div class="vk_gy gNCp2e"><span class="wob_t" style="display:inline">31</span><span class="wob_t" style="display:none">88</span>°</div><div class="QrNVmd ZXCv8e"><span class="wob_t" style="display:inline">25</span><span class="wob_t" style="display:none">77</span>°</div></div>
#//*[@id="wob_dp"]/div[1]/div[3]/div[1]/span[1]