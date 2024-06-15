#stock tracker bot
import matplotlib.pyplot as plt 
import csv
from datetime import date
from pandas import DataFrame
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = Options()
options.add_argument(r"user-data-dir=C:\Users\sidr2\AppData\Local\Google\Chrome\User Data")
options.add_argument("--profile-directory=Profile 3")
options.add_argument("--headless")
options.add_argument('log-level=3')
driver = webdriver.Chrome(r"D:\Homework\chromedriver_win32\chromedriver.exe",options=options)
today = str(date.today())
infosys = "https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT"
sbi = "https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI"
bpcl = "https://www.moneycontrol.com/india/stockpricequote/refineries/bharatpetroleumcorporation/BPC"
Stocksymbols = ["INFY","SBI","BPCL"]
stocklist = [infosys,sbi,bpcl]
stockprices = list()
st1 = list()
for stock in stocklist:
    driver.get(stock)
    a = driver.find_element_by_id("nsecp")

    b = a.get_attribute("data-numberanimate-value")
    b = b.replace(',',"")
    stockprices.append(float(b))
    st1.append([float(b)])
#print(stockprices)
stonks = str()
for i in stockprices:
    stonks = stonks + str(i)+"\n"
driver.quit()
df1 = DataFrame(st1)
df1.to_csv("stockprices.csv")
plt.bar(Stocksymbols,stockprices)
#plt.show()