from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):

        self.browser = webdriver.Firefox()

    def tearDown(self):

        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith has heard about a new online to-do app. She goes
        # to checkout its homepage

        self.browser.get('http://localhost:8000')

        # She notices the page's header and title mention to-do lists

        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do list item right away

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do list item')

        # She types "Buy peacock feathers" into a text box, because her
        # main hobby is tying fly-fishing lures

        inputbox.send_keys("Buy peacock feathers")

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in the to-do list

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertEqual(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )


        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical.)

        self.fail('Finish the test!')

        # The page updates again, and now it shows both items on her list.

        # Edith wonders if the site will remember her list.  Then she sees that
        # the site has generated a unique URL for her -- there is some explanatory
        # text to that affect.

        # She visits the URL - her list is still there

        # Satisfied, she goes back to sleep.

if __name__ == "__main__":

    unittest.main()
