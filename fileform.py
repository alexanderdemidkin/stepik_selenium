from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()
browser.get(link)
try:
    browser.find_element_by_name("firstname").send_keys("Ivan")
    browser.find_element_by_name("lastname").send_keys("Petrov")
    browser.find_element_by_name("email").send_keys("ip@mail")
    fl = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '1.txt')  # добавляем к этому пути имя файла
    fl.send_keys(file_path)
    browser.find_element_by_tag_name("button").click()

finally:

    time.sleep(10)
    browser.quit()
