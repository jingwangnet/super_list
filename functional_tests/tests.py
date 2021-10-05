from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.test import LiveServerTestCase
import unittest
import time

MAX_TIME = 3


class NewVisitorTest(LiveServerTestCase):
   

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





    def test_start_a_list_and_retrieve_it_later(self):
        # John visits the website
        try:
            self.browser.get(self.live_server_url)
        except WebDriverException:
            pass   
        
        # There is "To-Do" in the title and header_text
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)


        # There is a inputbox
        inputbox = self.browser.find_element(By.ID, 'id-new-item')

        # 'Submit a item for saving' in the inputbox
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Submit a item for saving'
        )

        # John submit 'I will go shoping.'
        inputbox.send_keys('I will go shoping')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1) 

        # '1. I will go shoping.' appears the table of the page.
        self.wait_for_check_row_in_the_table('1. ' + 'I will go shoping')

        # John submit 'I will have a date with mary.' agian
        inputbox = self.browser.find_element(By.ID, 'id-new-item')
        inputbox.send_keys('I will have a date with mary')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1) 

        # '2. I will have a date with mary.' appears the table of the page.
        # '1. I will go shoping.' appears the table of the page.

        self.wait_for_check_row_in_the_table('2. ' + 'I will have a date with mary')
        self.wait_for_check_row_in_the_table('1. ' + 'I will go shoping')


    def test_create_multiple_list_at_the_diffrent_url(self):
        # John visits the website 
        self.browser.get(self.live_server_url)
        # John submits 'I will have a date with mary'
        inputbox = self.browser.find_element(By.ID, 'id-new-item')
        inputbox.send_keys('I will have a date with mary')
        inputbox.send_keys(Keys.ENTER)
        # He saw '1. I will have a date with mary' after the page redirected
        self.wait_for_check_row_in_the_table('1. ' + 'I will have a date with mary')
        # the url match the URL pattern '/list/.*/'
        URL_OF_JOHN = self.browser.current_url
        self.assertRegex(URL_OF_JOHN, '/list/.*/')
        # He feels good and leaving
        self.browser.quit()

        # Joe visits the website too
        self.setUp()
        self.browser.get(self.live_server_url)
        # Joe expects that item of John does not appear the page 
        html = self.browser.page_source
        self.assertNotIn('I will have a date with mary', html)
        # Joe submits 'Do my homework'  
        inputbox = self.browser.find_element(By.ID, 'id-new-item')
        inputbox.send_keys('Do my homework')
        inputbox.send_keys(Keys.ENTER)
        # He saw '1. Do my homework'
        self.wait_for_check_row_in_the_table('1. ' + 'Do my homework')
        # Joe expects that item of John does not appear the page 
        html = self.browser.page_source
        self.assertNotIn('I will have a date with mary', html)
        # the url match the URL pattern '/list/.*/'
        URL_OF_JOE = self.browser.current_url
        self.assertRegex(URL_OF_JOE, '/list/.*/')
        # the url is not same as John's 
        self.assertNotEqual(URL_OF_JOE, URL_OF_JOHN)
        

    def test_styling_and_layout(self):
        # John visit the website
        self.browser.set_window_size(1024, 768)
        self.browser.get(self.live_server_url)
        # John want to detect the input of the home_page is center or not.
        inputbox = self.browser.find_element(By.ID, 'id-new-item')

        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # John submit some item 
        inputbox.send_keys('I will have a date with mary')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_check_row_in_the_table('1. ' + 'I will have a date with mary')

        # John want to detecot the inputbox of the view_list  is center or not
        inputbox = self.browser.find_element(By.ID, 'id-new-item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )


