from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time 


link = "https://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)



try:
  
  x = browser.find_element(By.ID, "num1").text
  y = browser.find_element(By.ID, "num2").text
  z= str(int(x) +int(y))
  print(z)
  browser.find_element(By.ID, 'dropdown').send_keys(z)
  
  button = browser.find_element(By.XPATH, "//button[@type='submit']")
  button.click()
finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(30)
  # закрываем браузер после всех манипуляций
  browser.quit()

# не забываем оставить пустую строку в конце файла