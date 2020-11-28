from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

print('\n')
print('Welcome to use the Swimming booking Script \n')
print('The author is Xinyang Zhao \n')

url1 = "https://booking.hit.edu.cn/sport//#"
login = ".//button[@type='submit' and @class='auth_login_btn primary full_width']"
swimming = "/html/body/div[1]/div/main/div/div/div[2]/div/div[6]/div"
todayStage = "/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[3]/div[3]/button[2]"

userid = input("Please input your student ID: \n")
passwd = input("Please input your student Password: \n")
timeStage = input("Which time do you want to swim?\n Please input the number:\n 1 for Morning\n 2 for Afternoon\n 3 for Night ?\n")

if timeStage == 1:
    todayStage = "/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[1]/div[3]/button[1]"
elif timeStage == 2:
    todayStage = "/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[2]/div[3]/button[1]"
elif timeStage == 3:
    todayStage = "/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[3]/div[3]/button[2]"

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url1)

time.sleep(1)
driver.find_element_by_id('username').send_keys(userid)
print('Input username Success!')
driver.find_element_by_id('password').send_keys(passwd)
print('Input password Success!')
# driver.find_element_by_id('submit').click()
driver.find_element_by_xpath(login).click()
print('Login in Success!')
driver.find_element_by_xpath(swimming).click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[3]/button/span").click()
time.sleep(1)
print(driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[3]/div[2]").get_attribute('innerHTML'))
print('Try to find swimming opportunity for you! My Boss!')
for i in range(50):
    time.sleep(0.5)
    driver.find_element_by_xpath(todayStage).click()
    print('Try to catch, Times: ', i)
    print(driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[3]/div[2]").get_attribute('innerHTML'))

# browser.save_screenshot(browser.title+".png")
