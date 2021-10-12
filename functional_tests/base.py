from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

MAX_TIME = 3


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True

        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.close()

    def wait_for_check_row_in_the_table(self, TEXT):
        START_TIME = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id-list-table')
                rows = table.find_elements(By.TAG_NAME, 'tr')

                self.assertIn(
                    TEXT,
                    [row.text for row in rows]
                )
                return 
            except (AssertionError, WebDriverException) as e:
                if time.time() - START_TIME > MAX_TIME:
                    raise e
                time.sleep(0.2)

    def wait_for(self, fn):
        START_TIME = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - START_TIME > MAX_TIME:
                    raise e
                time.sleep(0.2)

