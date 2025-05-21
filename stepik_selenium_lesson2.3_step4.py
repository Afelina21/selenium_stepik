from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)



try:
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла