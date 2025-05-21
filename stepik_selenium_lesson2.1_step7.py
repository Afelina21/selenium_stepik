from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)



try:
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
  

    option1 = robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotcheck = option1.get_attribute("checked")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла