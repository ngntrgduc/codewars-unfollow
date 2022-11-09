from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import os
from dotenv import load_dotenv
from time import sleep
import re

browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
load_dotenv()

def sign_in():
    browser.get('https://www.codewars.com/users/sign_in')
    email_form = browser.find_element(By.XPATH, '//*[@id="user_email"]')
    email_form.send_keys(os.getenv('MAIL'))
    password_form = browser.find_element(By.XPATH, '//*[@id="user_password"]')
    password_form.send_keys(os.getenv('PASSWORD'))
    password_form.send_keys(Keys.ENTER)
    pass

def remove_following():
    browser.get(f"https://www.codewars.com/users/{os.getenv('USER_NAME')}/following")
    social_page = browser.current_window_handle
    number_of_followings = re.sub('\D', '', browser.find_element(By.XPATH, '//*[@id="shell_content"]/div[5]/div/div/div[1]/ul/li[1]/a').text)

    for times in range(int(number_of_followings) // 15 + 2):
        browser.get(f"https://www.codewars.com/users/{os.getenv('USER_NAME')}/following")
        followings = [browser.find_element(By.XPATH, f'//*[@id="shell_content"]/div[5]/div/div/div[2]/div/table/tbody/tr[{i}]/td[1]/a').text for i in range(1, 16)]

        browser.switch_to.new_window('tab')        
        for i in range(1, 16):
            try:
                browser.get(f'https://www.codewars.com/users/{followings[i]}')
                sleep(2.5)
                browser.find_element(By.XPATH, '//*[@id="toggle_relationship"]').click()
                sleep(1.5)
            except:
                pass

        browser.close()
        browser.switch_to.window(social_page)
        browser.refresh()
    
    browser.quit()
    pass


sign_in()
sleep(1)
remove_following()