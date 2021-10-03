from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
from selenium import webdriver

options = Options()
options.headless = True


try:
    browser = webdriver.Firefox(options=options)
    browser.get('http://127.0.0.1:8000')
except WebDriverException:
    pass   

try:
    assert 'success' in browser.title, browser.title
except AssertionError as e:
    print(e)
finally:
    browser.close()

