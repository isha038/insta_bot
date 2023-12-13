from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

service = Service(executable_path="C:/Development/chromedriver.exe", log_path="NUL")
driver = webdriver.Chrome(service=service)

#usernames
audience = ['soyab_e_a_n', 'hakuna_makun']
message = "Hello from Isha's bot"


class bot:
    def __init__(self, username, password, audience, message):

        self.username = username
        self.password = password
        self.audience = audience
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()
        
    def login(self):
        self.bot.get(self.base_url)
        enter_username = WebDriverWait(self.bot,20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)


        #first pop-up box
        self.bot.find_element(by="xpath", value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
        time.sleep(2)

        #2nd pop-up box
        self.bot.find_element(by="xpath", value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(2)

        #DMs
        self.bot.find_element(by="xpath", value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a/div').click()
        time.sleep(2)

        #Pencil Icon
        self.bot.find_element(by="xpath", value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div').click()
        time.sleep(2)

        #Search
        for i in audience:
            self.bot.find_element(by='xpath', value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input').send_keys(i)
            time.sleep(2)

            #clickonuser
            self.bot.find_element(by="xpath", value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]').click()
            time.sleep(2)

            #clickonchat
            self.bot.find_element(by="xpath", value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div').click()
            time.sleep(2)

            #message
            send = self.bot.find_element(by='xpath', value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
            
            #Types message
            send.send_keys(self.message)
            time.sleep(1)

            #sends message
            send.send_keys(Keys.RETURN)
            time.sleep(2)

            #Finds another username
            self.bot.find_element(by="xpath", value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div').click()
            time.sleep(2)







#Replace username and password with the username and the password of the account that you want to use
def init():
    bot('username', 'passworc', audience, message)
    input("DONE")

init()




