from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import time


class NewVisitorTest(unittest.TestCase):
   

   def setUp(self):
       options = Options()
       options.headless = True

       self.browser = webdriver.Firefox(options=options)

   def tearDown(self):
       self.browser.close()

   def check_row_in_the_table(self, TEXT):
       table = self.browser.find_element(By.ID, 'id-list-table')
       rows = table.find_elements(By.TAG_NAME, 'tr')

       self.assertIn(
           TEXT,
           [row.text for row in rows]
       )

   def test_start_a_list_and_retrieve_it_later(self):
       # John visits the website
       try:
           self.browser.get('http://127.0.0.1:8000')
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
       self.check_row_in_the_table('1. ' + 'I will go shoping')

       # John submit 'I will have a date with mary.' agian
       inputbox = self.browser.find_element(By.ID, 'id-new-item')
       inputbox.send_keys('I will have a date with mary')
       inputbox.send_keys(Keys.ENTER)

       time.sleep(1) 

       # '2. I will have a date with mary.' appears the table of the page.
       # '1. I will go shoping.' appears the table of the page.

       self.check_row_in_the_table('2. ' + 'I will have a date with mary')
       self.check_row_in_the_table('1. ' + 'I will go shoping')


if __name__ == '__main__':
    unittest.main()
