#-*- coding:utf-8 -*-
import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
#         self.browser = webdriver.Firefox()
        print 'setUp'
        self.browser = webdriver.Safari()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        print 'testPageTitle'
        self.browser.get('http://www.yahoo.com')
        self.assertIn('Yahoo', self.browser.title)
        print self.browser.service
        print self.browser.title
        print self.browser.capabilities
        print self.browser.session_id
        print self.browser.window_handles
#         print self.browser.page_source

if __name__ == '__main__':
    unittest.main(verbosity=2)