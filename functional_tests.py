from selenium import webdriver
import unittest

class CV(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Edge()

    def tearDown(self):  
        self.browser.quit()

    def test_can_get_to_CV_page(self):  
        self.browser.get('http://127.0.0.1:8000/cv')
        self.assertIn('CV', self.browser.title) 

if __name__ == '__main__':  
    unittest.main(warnings='ignore')