'''
Тест для проверки поисковой строки на сайте.

Основной класс:

- Search_box: Наследует BaseTest и содержит метод для тестирования поисковой строки

Основной метод:

- search_box_test(): Запускает тест, выполняет поиск по заданной переменной и прокручивает страницу
'''

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import search_variable
from page_scroll import page_scroll
from base_test_logic import BaseTest, logger

class Search_box(BaseTest):
    def search_box_test(self):
    
        try:
            logger.info("Запуск теста: Поисковая строка")
            self.setup(mobile=False)
            
            search_box = self.driver.find_element(By.NAME, "search")
            
            search_box.clear()
            time.sleep(1)
            search_box.send_keys(search_variable)
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)
            page_scroll()
            
        except Exception as e:
            self.log_error(str(e))
        
        finally:
            self.teardown()

if __name__ == '__main__':
    test = Search_box()
    test.search_box_test()