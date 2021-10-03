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
       try:
           self.browser.get('http://127.0.0.1:8000')
       except WebDriverException:
           pass   
       
       self.assertIn('succese', self.browser.title)
       

if __name__ == '__main__':
    unittest.main()
