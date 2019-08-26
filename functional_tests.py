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
        #check out the homepage of the app
        self.browser.get('http://localhost:8000')

        #notice that the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text

        self.assertIn('To-Do', header_text)
        #can be invited to enter a to-do item straight awa
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual( inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #I type 'buy milk' into a text box
        inputbox.send_keys('buy milk')

        #when I hit enter, the page updates, and now the page lists
        #"1: buy milk" as an item in a to-do lists
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1. buy milk' for row in rows))
        #there is still a text box inviting me to add another item. I
        #enter 'get bread'
        self.fail('Finish the test!')

        #page updates again, and now shows both items on my lists

        #How do I remember my lists? Site should generate a unique URL
        #for me -- there will be some explanatory text to that effect

        #I visit the URL - my to-do is still there.
if __name__ == '__main__':
    unittest.main(warnings='ignore')
