from datetime import datetime
# from http.server import executable
import time
from cv2 import _InputArray_STD_BOOL_VECTOR
from psutil import ZombieProcess
from regex import P
# from jmespath import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from apscheduler.schedulers.blocking import BlockingScheduler
import os


driver = webdriver.Firefox(executable_path='/opt/firefox/geckodriver')


def smart_wait(element_id):
    for i in range(1000):
        if i > 990:
            print('timeout')
            os.abort()
        try:
            if driver.find_element_by_xpath(element_id):
                break
        except:
            print('wait for element to find. ', i)
            time.sleep(0.01)


def try_click(element_xpath):
    try:
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
    finally:
        print('Cannot load book_button after some time.')
        driver.quit()
    element = driver.find_element(By.XPATH, element_xpath)
    element.click()

def my_book():
    print('my book in...')
    driver.get(url='https://hk.sz.gov.cn:8118/userPage/userCenter')

    id_suggest_confirm = '/html/body/div[5]/div/div/button'
    id_book = '/html/body/div[2]/a[2]/div/div/p'
    id_6th_position = '/html/body/div/div[2]/div/section[6]/div/div[3]/div/button'
    

    try_click(id_suggest_confirm)
    try_click(id_book)
    try_click(id_6th_position)
    while(1):
        print('1')


def login():
    driver.get(url="https://hk.sz.gov.cn:8118/userPage/userCenter")        # http://pecg.hust.edu.cn/cggl/front/yuyuexz
    hesuan_button = driver.find_element_by_xpath('/html/body/div[3]/div/div/button')
    hesuan_button.click()
    select_passport = driver.find_element_by_xpath('//*[@id="select_certificate"]')
    select_passport.click()
    select_passport = driver.find_element_by_xpath('/html/body/div[1]/section[2]/div[1]/div/select/option[5]')
    select_passport.click()
    user_id = driver.find_element_by_xpath('//*[@id="input_idCardNo"]').send_keys('***')
    user_pw = driver.find_element_by_xpath('//*[@id="input_pwd"]').send_keys('***')


if __name__ == '__main__':
    print('ording badminton...')
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')


    driver = webdriver.Firefox(executable_path='/opt/firefox/geckodriver')
    print('excuting "my book"... ')
    login()
    print('You need to login now.')  
    # breakpoint here!
    print('You should have logged in.')
    
    # scheduler.add_job(my_book, 'date', run_date=datetime(2022, 6, 18, 10, 0, 0))
    # scheduler.start()

    my_book()
    while(1):
        pass

