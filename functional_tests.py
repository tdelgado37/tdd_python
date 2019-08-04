from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #check out the homepage of the app
        browser.get('http://localhost:8000')

        #notice that the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        #can be invited to enter a to-do item straight awa

        #I type 'buy milk' into a text box

        #when I hit enter, the page updates, and now the page lists
        #"1: buy milk" as an item in a to-do lists

        #there is still a text box inviting me to add another item. I
        #enter 'get bread'

        #page updates again, and now shows both items on my lists

        #How do I remember my lists? Site should generate a unique URL
        #for me -- there will be some explanatory text to that effect

        #I visit the URL - my to-do is still there.
if __name__ == '__main__':
    unittest.main(warnings='ignore')
