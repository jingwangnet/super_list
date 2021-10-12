from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_can_add_empty_item(self):
        # John accese the website
        self.browser.get(self.live_server_url)
        # he input a item of empty 
        self.browser.find_element(By.ID, 'id-new-item').send_keys(Keys.ENTER)
        # he got a error message
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has_error').text,
            'You can\'t have an empty item.'
        ))
        # John submits 'I will go shoping'
        self.browser.find_element(By.ID, 'id-new-item').send_keys('I will go shiping')
        self.browser.find_element(By.ID, 'id-new-item').send_keys(Keys.ENTER)
        # '1. I will go shoping.' appears the table of the page.
        self.wait_for_check_row_in_the_table('1. I will go shiping')
        # he input a item of empty again 
        self.browser.find_element(By.ID, 'id-new-item').send_keys(Keys.ENTER)
        # he got a error message too
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has_error').text,
            'You can\'t have an empty item.'
        ))
        # John submits 'I will get a date with mary'
        self.browser.find_element(By.ID, 'id-new-item').send_keys('I ill get a date with mary')
        self.browser.find_element(By.ID, 'id-new-item').send_keys(Keys.ENTER)
        # '2. I will get a date with mary.' appears the table of the page.
        # '1. I will go shoping.' appears the table of the page.
        self.wait_for_check_row_in_the_table('1. I will get a date with mary')
        self.wait_for_check_row_in_the_table('1. I will go shiping')


