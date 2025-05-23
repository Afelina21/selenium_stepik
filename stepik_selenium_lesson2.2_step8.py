from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 


link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)



try:
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Angelina")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Makurina")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("izarenkova@yandex.ru")

    

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла