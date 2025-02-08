
'''
Тест для проверки работоспособности гиперссылок.

Основной класс:

- TestUrls: Наследует BaseTest и содержит метод для тестирования гиперссылок

Основной метод:

- test_urls(): Запускает тест, переходит по каждой гиперссылке из списка, прокручивает страницу и возвращается назад
'''

import time
from selenium.webdriver.common.by import By
from page_scroll import page_scroll
from base_test_logic import BaseTest, logger
from config import url_variables

class TestUrls(BaseTest):
    def test_urls(self):
        
        try:

            logger.info("Запуск теста: Тест гиперсылок")
            self.setup(mobile=False)
            
            for url in url_variables:
                cl = self.driver.find_elements(By.XPATH, url)
                cl[0].click()
                time.sleep(1)
                
                page_scroll()
                
                self.driver.back()
                time.sleep(1)
                

        except Exception as e:
            self.log_error(str(e))    
            
        finally:
            self.teardown()

if __name__ == '__main__':
    test = TestUrls()
    test.test_urls()
