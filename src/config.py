'''
Конфигурационные параметры для тестов.

Основные параметры:

- url: URL сайта, который будет тестироваться

- webdriver: Настройки для Chrome WebDriver

- search_variable: Переменная для поиска на сайте

- mobile_emulation: Настройки для эмуляции мобильного устройства

- url_variables: Список XPath для гиперссылок, которые будут тестироваться
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
url = "https://ru.wiktionary.org/"

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);

webdriver = webdriver.Chrome(options=chrome_options)

search_variable = "Россия"

mobile_emulation = {
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.77 Mobile Safari/537.36"
            }

url_variables = (
    '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[2]/td[1]/ul/li[1]/a',
    '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[2]/td[1]/ul/li[2]/a',
    '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[2]/td[1]/ul/li[3]/a',
    '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[2]/td[1]/ul/li[4]/a',
    '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[2]/td[1]/ul/li[5]/a',
    '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[2]/td[1]/ul/li[6]/a',
    '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[2]/td[1]/ul/li[7]/a',
    '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[2]/td[1]/ul/li[8]/a',
    '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[2]/td[1]/ul/li[9]/a'
)
