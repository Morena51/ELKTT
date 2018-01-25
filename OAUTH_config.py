from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
driver=webdriver.Chrome('C:\\chromedriver.exe')
driver.get('http://confus.tektorg-elk.arch/auth')
#Нажимаем кнопку Войти через Back Office
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/footer/div/button').click()
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
finally:
    driver.find_element_by_xpath('//input[@name="username"]').send_keys("admin")
    driver.find_element_by_xpath('//input[@name="password"]').send_keys("admin")
    driver.find_element_by_xpath('//button[text()="Войти"]').click()

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print('NoSuchElementException')
        return False
    else:
        print('Success auth in configurator')
        driver.implicitly_wait(10)
        return True
element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
)
check_exists_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[1]/h1[text()="Панель администратора ЕЛК"]')

driver.close()