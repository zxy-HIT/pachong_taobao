from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

import  smtplib
from email.header import Header
from email.mime.text import MIMEText

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
todayStage = '/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[4]/div[3]/button[1]'
testStage = '/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[2]/div/div[2]/div[4]/div[3]/button[1]'
remainNumber = "/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[1]/div/div[2]/div[4]/div[2]"
testremainNumber = "/html/body/div[1]/div[1]/main/div/div/div[4]/div[1]/div[2]/div/div[2]/div[4]/div[2]"
iAgree = "/html/body/div[1]/div[4]/div/div/div[2]/div/div[2]/div[7]/div/div/div[1]/div"
book = "/html/body/div[1]/div[4]/div/div/div[3]/button[2]"

huoyanid = 'studentID'
huoyanpw = 'Password'

# userid = input("Please input your student ID: \n")
# passwd = input("Please input your student Password: \n")
userid = huoyanid
passwd = huoyanpw


# 发送邮箱
sender='EmailAddress'
# 发送密码，即开启smtp的授权码
psw='SMTP ID'

# 接收邮箱
receiver='Receiver Email Address'
receiverhuoyan = 'Receier Email Address'
# 发送邮箱服务器
smtp_server='smtp.qq.com'

# 邮件正文，可编写HTML类型
msg=MIMEText('Hello,We have book the Swimming chance for you, My boss.','plain','utf-8')

# Header()来定义邮件标题
msg['From']=Header('AI','utf-8')
msg['To']=Header('Xinyang','utf-8')
msg['Subject']=Header('Congratulations for the Swimming chance!','utf-8')

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
    Sure = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div/div/div[3]/button'))
    )
    time.sleep(1)
    Sure.click()

    print('Try to catch, Times: ', i)



    eText = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, remainNumber)))
    print(eText.get_attribute('innerHTML'))
    # print( eText.text.split(' ')[1] )
    if int(eText.text.split(' ')[1]) != 0:
        eTodayStage = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, todayStage)))
        eTodayStage.click()

        print('Get the chance!')
        eiagree = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, iAgree)))
        eiagree.click()

        eibook = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, book)))
        eibook.click()

        print('Success!')
        server = smtplib.SMTP(smtp_server)
        # server.set_debuglevel(1)
        server.starttls()
        server.login(sender, psw)
        server.sendmail(sender, receiver, msg.as_string())
        server.sendmail(sender, receiverhuoyan, msg.as_string())
        server.quit()
        print('Email has been sended!')
        driver.close()

    else:
        print('No chance remained, I will try to catch it, my boss!')
        driver.get(urlSwim)
        # driver.refresh()

    # sSwimming = WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH, swimming)) )
    # sSwimming.click()

    # except:
    #     print("Could not find the button!")
        # driver.close()

# browser.save_screenshot(browser.title+".png")
