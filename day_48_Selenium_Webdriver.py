from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_drive_path = "C:\\Web development\\chromedriver_win32\\chromedriver.exe"

s = Service('C:\Web development\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)
# driver.get("https://rozetka.com.ua/319935640/p319935640/")
# price = driver.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/div[2]/div/div/p')
# print(price.text)
# driver.close()

#---------------Получаем дату--------------------#

driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
for time in event_times:
    print(time.text)

#---------------Получаем текст--------------------#

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for name in event_names:
    print(name.text)
#------------------ генерируем словарь----------------------#
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.close()
driver.quit()



# driver = webdriver.Chrome(executable_path=chrome_drive_path)
# price = driver.find_element_by_class_name("product-prices__big")
# search = driver.find_element_by_name("search")
# logo = driver.find_element_by_class_name("header__logo")
# price = driver.find_element_by_xpath('//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/div[2]/div/div/p')
# price = driver.find_element(by=By.CLASS_NAME,value="a-offscreen")
