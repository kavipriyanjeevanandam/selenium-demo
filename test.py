import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

class ExampleWebsiteTest(unittest.TestCase):

    def setUp(self):
        # Configure Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Enable headless mode
        chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("file:///" + os.path.abspath("index.html")) 

    def tearDown(self):
        self.driver.quit()

    def test_home_page_title(self):
        self.assertEqual(self.driver.title, "Example Website")
    def test_navigation_to_about_section(self):
        about_link = self.wait_until_presence(By.LINK_TEXT, "About")
        about_link.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.assertIn("About Us", self.driver.page_source)
    def test_navigation_to_services_section(self):
        services_link = self.wait_until_presence(By.LINK_TEXT, "Services")
        services_link.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.assertIn("Our Services", self.driver.page_source)
    def test_navigation_to_contact_section(self):
        contact_link = self.wait_until_presence(By.LINK_TEXT, "Contact")
        contact_link.click()
        self.assertIn("Contact Us", self.driver.page_source)

    # Add more test methods here...
    def wait_until_presence(self, by, value, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, value)))

if __name__ == "__main__":
    unittest.main()
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))