#Microsoft Teams Cloud Based Attendance 
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = Options()

options.add_argument(r"Profile path here")
options.add_argument("--profile-directory=Profile 4")
driver = webdriver.Chrome(r"Chromedriver path here",options=options)

#class links
mat101m = "https://teams.microsoft.com/l/meetup-join/19%3aMdi5h-QuTwuheHieTmhaj2XQkBAUa7J66VdBBKATZQ01%40thread.tacv2/1635138154358?context=%7b%22Tid%22%3a%22ebbbcd62-c0a9-46ff-a92c-5f2300087164%22%2c%22Oid%22%3a%221c808b6d-4112-425c-946a-4b67326f32b6%22%7d"
mat102t = "https://teams.microsoft.com/l/meetup-join/19%3aOH7PBnLjYFj18Q8P4J2Dqe3o19srj-_qVa9C2m9Dhws1%40thread.tacv2/1638195693258?context=%7b%22Tid%22%3a%22ebbbcd62-c0a9-46ff-a92c-5f2300087164%22%2c%22Oid%22%3a%22a6287cff-e528-48db-b618-aba9a6582ae7%22%7d"
mat102f = "https://teams.microsoft.com/l/meetup-join/19%3aOH7PBnLjYFj18Q8P4J2Dqe3o19srj-_qVa9C2m9Dhws1%40thread.tacv2/1635492747170?context=%7b%22Tid%22%3a%22ebbbcd62-c0a9-46ff-a92c-5f2300087164%22%2c%22Oid%22%3a%226890b42d-4ca2-43ee-90d1-7d1028778845%22%7d"
cslabth = "https://teams.microsoft.com/l/meetup-join/19%3au8vhd48UncSrK-X8znP3fvorn6V2PMxsCCZwHfqmg0k1%40thread.tacv2/1634700570499?context=%7b%22Tid%22%3a%22ebbbcd62-c0a9-46ff-a92c-5f2300087164%22%2c%22Oid%22%3a%22b71bf082-4d2f-4fea-9b74-e3e01257bf4f%22%7d"
eee111m = "https://teams.microsoft.com/l/meetup-join/19%3aIqS0Nr73x0kA9cp4BCn_rFLj33D0IxhQLDGmo0YZM_A1%40thread.tacv2/1633502159005?context=%7b%22Tid%22%3a%22ebbbcd62-c0a9-46ff-a92c-5f2300087164%22%2c%22Oid%22%3a%22457d6786-b85b-41c5-8958-4396d1c34ddd%22%7d"
eee111w = "https://teams.microsoft.com/l/meetup-join/19%3aIqS0Nr73x0kA9cp4BCn_rFLj33D0IxhQLDGmo0YZM_A1%40thread.tacv2/1633491271662?context=%7b%22Tid%22%3a%22ebbbcd62-c0a9-46ff-a92c-5f2300087164%22%2c%22Oid%22%3a%22457d6786-b85b-41c5-8958-4396d1c34ddd%22%7d"
eee111th = "https://teams.microsoft.com/l/meetup-join/19%3aIqS0Nr73x0kA9cp4BCn_rFLj33D0IxhQLDGmo0YZM_A1%40thread.tacv2/1633501935275?context=%7b%22Tid%22%3a%22ebbbcd62-c0a9-46ff-a92c-5f2300087164%22%2c%22Oid%22%3a%22457d6786-b85b-41c5-8958-4396d1c34ddd%22%7d"
phy103th = "https://teams.microsoft.com/l/meetup-join/19%3aXbJk3v0XTpYUTwWmHXruIUhpDGYZfjbQu0Bzy0s5Ca41%40thread.tacv2/1635407207803?context=%7b%22Tid%22%3a%22ebbbcd62-c0a9-46ff-a92c-5f2300087164%22%2c%22Oid%22%3a%2264ed5d49-eff5-44e6-9811-507d42b04fb4%22%7d"
phy103f = "https://teams.microsoft.com/l/meetup-join/19%3aXbJk3v0XTpYUTwWmHXruIUhpDGYZfjbQu0Bzy0s5Ca41%40thread.tacv2/1636621977818?context=%7b%22Tid%22%3a%22ebbbcd62-c0a9-46ff-a92c-5f2300087164%22%2c%22Oid%22%3a%2264ed5d49-eff5-44e6-9811-507d42b04fb4%22%7d"

clsdict = {'[10, 0]':mat101m,'[8, 1]':mat102t,'[13, 4]':mat102f,'[8, 3]':cslabth,'[13, 0]':eee111m,'[9, 2]':eee111w,'[10, 3]':eee111th,'[13, 3]':phy103th,'[10, 4]':phy103f}
chour = time.localtime().tm_hour
cday = time.localtime().tm_wday

#Time and day check for class choice
cchoice = str([chour,cday])
#general class join function
def classjoin():
    driver.get(clsdict[cchoice])
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="buttonsbox"]/button[2]').click()
    time.sleep(12)
    driver.find_element_by_xpath('//*[@id="prejoin-options-content"]/button[1]').click()
classjoin()
