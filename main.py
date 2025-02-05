from datetime import datetime
import time
from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler

# from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options = webdriver.FirefoxOptions()

# chrome根目录打开命令窗口，执行chrome.exe --remote-debugging-port=9222 --user-data-dir="your directory"，在新窗口登录华中科技大学账号，保持窗口常开
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Firefox(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe',
                          options=options)
driver.get(url="http://pecg.hust.edu.cn/cggl/front/yuyuexz")
# 场地号与xpath序号对应关系
zone_dict = {1: [3, 2],
             2: [3, 3],
             3: [3, 4],
             4: [3, 5],
             5: [3, 6],
             21: [3, 7],
             6: [4, 2],
             7: [4, 3],
             8: [4, 4],
             9: [4, 5],
             10: [4, 6],
             11: [5, 2],
             12: [5, 3],
             13: [5, 4],
             14: [5, 5],
             15: [5, 6],
             22: [5, 7],
             16: [6, 2],
             17: [6, 3],
             18: [6, 4],
             19: [6, 5],
             20: [6, 6],
             }

# Select Guanggu GYM
def select_gym():
    book_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]/div[1]/div[2]/span/a')


# 切换窗口
def change_window():
    new_web = driver.window_handles[-1]
    driver.switch_to.window(new_web)


# 切换日期
def change_date():
    nextday = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]')
    nextday.click()
    time.sleep(0.1)


# 选择时间段
def select_duration(duration):
    select_time = driver.find_element_by_xpath('//*[@id="starttime"]/option[%d]' % duration)
    select_time.click()
    time.sleep(0.1)


# 选择同伴
def select_partner():
    partner = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/table/tbody/tr[4]/td/input')
    partner.click()
    time.sleep(0.1)
    partner = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[2]')
    partner.click()
    time.sleep(0.5)


# 选择场地
def select_zone(num):
    row = zone_dict[num][0]
    col = zone_dict[num][1]
    zone = driver.find_element_by_xpath(
        '/html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[%d]/td[%d]' % (row, col))
    zone.click()


# 提交预定
def submit_book():
    submit = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div[3]/input[3]')
    submit.click()
    time.sleep(0.1)


# 执行预定，此处改变时间段和场地号，注意提前排除不可预约场地
def execute_booking(duration=3, zone=21):
    booking = driver.find_element_by_xpath('/html/body/div[2]/div/ul/li[1]/div[1]/div[2]/span/a')
    booking.click()
    time.sleep(0.1)
    change_window()
    change_date()
    change_window()
    change_date()
    select_duration(duration)
    select_partner()
    change_window()
    select_zone(zone)
    time.sleep(0.1)
    submit_book()
    change_window()
    # 确认缴费，测试此脚本前注释下面两行代码
    charge = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div/div[3]/input[2]')
    charge.click()
    driver.quit()


if __name__ == '__main__':
    print('ording badminton...')
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    scheduler.add_job(execute_booking, 'date', run_date=datetime(2022, 6, 8, 9, 25, 0))
    scheduler.start()

# 场地编号与xpath对应关系
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[3]/td[2]:1
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[3]/td[3]:2
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[3]/td[4]:3
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[3]/td[5]:4
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[3]/td[6]:5
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[3]/td[7]:21
#
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[4]/td[2]:6
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[4]/td[3]:7
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[4]/td[4]:8
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[4]/td[5]:9
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[4]/td[6]:10
#
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[5]/td[2]:11
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[5]/td[3]:12
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[5]/td[4]:13
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[5]/td[5]:14
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[5]/td[6]:15
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[5]/td[7]:22
#
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[6]/td[2]:16
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[6]/td[3]:17
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[6]/td[4]:18
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[6]/td[5]:19
# /html/body/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr[6]/td[6]:20
