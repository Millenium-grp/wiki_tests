'''
Тест для проверки мобильной версии сайта.

Основной класс:

- MobileScrollTest: Наследует BaseTest и содержит метод для тестирования прокрутки на мобильном устройстве

Основной метод:

- mobile_scroll_test(): Запускает тест, настраивает мобильную эмуляцию и выполняет прокрутку страницы
'''

import time
from config import mobile_emulation
from page_scroll import page_scroll
from base_test_logic import BaseTest, logger


class MobileScrollTest(BaseTest):
    def mobile_scroll_test(self):
        
        try:
            logger.info("Запуск теста: Мобильная версия сайта")
            self.setup(mobile=True)
            
            self.driver.execute_cdp_cmd("Network.setUserAgentOverride", mobile_emulation)
            
            page_scroll()
            time.sleep(1)
            
        except Exception as e:
            self.log_error(str(e))

        finally:
            self.teardown()
        
if __name__ == '__main__':
    test = MobileScrollTest()
    test.mobile_scroll_test()

