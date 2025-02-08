'''
Базовый класс для тестирования, который используется в других тестовых скриптах.

Основные функции:

- setup(mobile=False): Настраивает окружение для теста, включая открытие браузера и установку размера окна

- teardown(): Завершает тест, закрывает браузер и логирует время выполнения

- log_error(error_message): Логирует сообщения об ошибках
'''

import time
import logging
from config import url, webdriver

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class BaseTest:
    def setup(self, mobile=False):
        self.start_time = time.time()
        self.driver = webdriver
        self.driver.get(url)
        if mobile:
            self.driver.set_window_size(390, 844)
        else:
            self.driver.maximize_window()
        time.sleep(2)

    def teardown(self):
        logger.info("Тест успешно завершен.")
        self.driver.quit()
        execution_time = time.time() - self.start_time
        logger.info(f"Время выполнения: {execution_time:.2f} секунд.")
        
    def log_error(self, error_message):
        logger.error(f"Ошибка: {error_message}")
