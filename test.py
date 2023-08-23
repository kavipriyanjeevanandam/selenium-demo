import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class ExampleWebsiteTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///" + os.path.abspath("index.html")) 

    def tearDown(self):
        self.driver.quit()

    def test_home_page_title(self):
        self.assertEqual(self.driver.title, "Example Website")

    def test_navigation_to_about_section(self):
        about_link = self.wait_until_presence(By.LINK_TEXT, "About")
        about_link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertIn("About Us", self.driver.page_source)

    def test_navigation_to_contact_section(self):
        contact_link = self.wait_until_presence(By.LINK_TEXT, "Contact")
        contact_link.click()
        self.assertIn("Contact Us", self.driver.page_source)

    def wait_until_presence(self, by, value):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((by, value)))

if __name__ == "__main__":
    unittest.main()
