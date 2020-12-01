from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

print('\n')
print('Welcome to use the Swimming booking Script \n')
print('The author is Xinyang Zhao \n')

url1 = "https://booking.hit.edu.cn/sport//#"
urlSwim = "https://booking.hit.edu.cn/sport//#/eventbooking/88b696df-fc3a-4b16-81c9-ec5a0db20a53"
login = "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[5]/button"
swimming = "/html/body/div[1]/div/main/div/div/div[2]/div/div[6]/div"
todayStage = '/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[3]/div[3]/button[2]'
remainNumber = "/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[3]/div[2]"
iAgree = "/html/body/div[1]/div[4]/div/div/div[2]/div/div[2]/div[7]/div/div/div[1]/div/i"
book = "/html/body/div[1]/div[4]/div/div/div[3]/button[2]"

# userid = input("Please input your student ID: \n")
# passwd = input("Please input your student Password: \n")
userid = '17b904014'
passwd = '123Zxy456@'

# timeStage = input("Which time do you want to swim?\n Please input the number:\n 1 for Morning\n 2 for Afternoon\n 3 for Night ?\n")
#
# if timeStage == 1:
#     todayStage = "/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[1]/div[3]/button[1]"
# elif timeStage == 2:
#     todayStage = "/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[2]/div[3]/button[1]"
# elif timeStage == 3:
#     todayStage = "/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[3]/div[3]/button[2]"

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
# driver.find_element_by_xpath(swimming).click()
# time.sleep(3)
# try:
#     element = WebDriverWait(driver,10).until(
#         EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div/div/div[3]/button'))
#     )
#     element.click()
# except:
#     print("Could not find the button! First!")
print('Try to find swimming opportunity for you! My Boss!')


for i in range(100000):
    # try:
    driver.get(urlSwim)
    Sure = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div/div/div[3]/button'))
    )
    time.sleep(1)
    Sure.click()

    eTodayStage = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.XPATH, todayStage)) )
    eTodayStage.click()

    print('Try to catch, Times: ', i)
        
    eText = WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH, remainNumber)) )
    print(eText.get_attribute('innerHTML'))
    driver.get(urlSwim)
        # driver.refresh()

    # sSwimming = WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH, swimming)) )
    # sSwimming.click()

    # except:
    #     print("Could not find the button!")
        # driver.close()

# browser.save_screenshot(browser.title+".png")
