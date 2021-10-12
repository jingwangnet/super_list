from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class StylingAndLayoutTest(FunctionalTest):

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
    
