from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
   

   def setUp(self):
       options = Options()
       options.headless = True

       self.browser = webdriver.Firefox(options=options)

   def tearDown(self):
       self.browser.close()

   def test_start_a_list_and_retrieve_it_later(self):
       # John visits the website
       try:
           self.browser.get('http://127.0.0.1:8000')
       except WebDriverException:
           pass   
       
       # There is "To-Do" in the title and header_text
       self.assertIn('To-Do', self.browser.title)

       # There is a inputbox

       # 'Submit a item for saving' in the inputbox

       # John submit 'I will go shoping.'
       
       # '1. I will go shoping.' appears the table of the page.

       # John submit 'I will have a date with mary.' agian

       # '2. I will have a date with mary.' appears the table of the page.


if __name__ == '__main__':
    unittest.main()
