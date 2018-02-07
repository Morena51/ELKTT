from selenium import webdriver
import time,os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def click_exists_by_xpath(xpath):
    try:
        driver.implicitly_wait(15)
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print('NoSuchElementException')
        driver.get_screenshot_as_file('../Screenshots')
        return False
    else:
        print('Success'+xpath)
        # Кликаем по элементу если мы его нашли
        driver.find_element_by_xpath(xpath).click()
        return True

def check_exists_by_xpath(xpath):
    try:
        driver.implicitly_wait(15)
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print('NoSuchElementException'+xpath)
        driver.get_screenshot_as_file('../Screenshots')
        return False
    else:
        print('Success'+xpath)
        return True

driver=webdriver.Chrome('C:\\chromedriver.exe')
driver.get('http://auth.tektorg-elk.arch/signin')

# Заполняем логин \ пароль
login="admin@burgaz.loc"
password="4f7mLEmCUR85ha9x"
field_email='//input[@name="email"]'
field_pass='//input[@name="password"]'
driver.find_element_by_xpath(field_email).send_keys(login)
driver.find_element_by_xpath(field_pass).send_keys(password)
# Нажимаем кнопку Войти
driver.find_element_by_xpath('//button').click()


#print(driver.window_handles)
#driver.switch_to_window(driver.window_handles[0])
#driver.title
#driver.close()
time.sleep(5)
# Открываем новую пустую вкладку
driver.execute_script("window.open('','_blank');")
# Переключаемся на новую вкладку
driver.switch_to.window(driver.window_handles[1])
# На новой вкладке открываем Бургаз
driver.get("http://burgaz.tektorg-elk.arch/")
# Проверяем что мы на ЭТП и она работает
try:
    assert "Газпром бурение" in driver.title
    print('ЭТП работает')
except AssertionError:
    print('Что-то не так с площадкой')
    driver.get_screenshot_as_file('../Screenshots')

# Заходим на площадку - Ссылка "Войти в систему"
click_exists_by_xpath('//a[text()="Войти в систему"]')
# Чекаем что зашли
check_exists_by_xpath('//button[text()="Настройки"]')

#  Выходим из площадки - Кнопка "Выход"
click_exists_by_xpath('//button[text()="Выход"]')

# Проверяем что мы Вышли из ЭТП
check_exists_by_xpath('//a[text()="Войти в систему"]')

# Переходим на вкладку с ЕЛК
driver.switch_to.window(driver.window_handles[0])
# Обновляем страницу
time.sleep(3)
driver.refresh()

# Чекаем что в ЕЛК не авторизованы
check_exists_by_xpath(field_pass)
