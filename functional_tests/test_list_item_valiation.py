from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_can_add_empty_item(self):
        # John accese the website
        # he input a item of empty 
        # he got a error message
        # John submits 'I will go shoping'
        # '1. I will go shoping.' appears the table of the page.
        # he input a item of empty again 
        # he got a error message too
        # John submits 'I will get a date with mary'
        # '2. I will get a date with mary.' appears the table of the page.
        self.fail('write me')
        


