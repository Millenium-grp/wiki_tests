'''
Функция для прокрутки страницы вниз и обратно вверх.

Основная функция:

- page_scroll(): Прокручивает страницу до самого низа, а затем возвращается наверх
'''

import time
from config import webdriver

driver = webdriver

def page_scroll():
        current_position = driver.execute_script("return window.pageYOffset;")
        total_height = driver.execute_script("return document.body.scrollHeight;")
        step = 50
        
        while current_position < total_height:
            driver.execute_script(f"window.scrollTo(0, {current_position});")
            current_position += step
            time.sleep(0.05)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)