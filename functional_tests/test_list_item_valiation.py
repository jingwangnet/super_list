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
        self.wait_for(
            lambda: self.browser.find_element(By.CSS_SELECTOR, '#id-new-item:invalid')
        )
        # John submits 'I will go shoping'
        inputbox = self.browser.find_element(By.ID, 'id-new-item')
        inputbox.send_keys('I will go shiping')
        inputbox.send_keys(Keys.ENTER)
        # '1. I will go shoping.' appears the table of the page.
        self.wait_for_check_row_in_the_table('1. I will go shiping')
        # he input a item of empty again 
        self.browser.find_element(By.ID, 'id-new-item').send_keys(Keys.ENTER)
        # he got a error message too
        self.wait_for(
            lambda: self.browser.find_element(By.CSS_SELECTOR, '#id-new-item:invalid')
        )
        # John submits 'I will get a date with mary'
        inputbox = self.browser.find_element(By.ID, 'id-new-item')
        inputbox.send_keys('I will get a date with mary')
        inputbox.send_keys(Keys.ENTER)
        # '2. I will get a date with mary.' appears the table of the page.
        # '1. I will go shoping.' appears the table of the page.
        self.wait_for_check_row_in_the_table('2. I will get a date with mary')
        self.wait_for_check_row_in_the_table('1. I will go shiping')

    def test_cannot_duplicate_items(self):
        # jing visit homepage  and create new list 
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id-new-item')
        inputbox.send_keys('bla')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_check_row_in_the_table('1. bla')
        self.browser.get(self.live_server_url)
        # she is cerate a duplicate item
        inputbox = self.browser.find_element(By.ID, 'id-new-item')
        inputbox.send_keys('bla')
        # she got a help error infomation
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "You've alreandy got this in your list"
        ))

