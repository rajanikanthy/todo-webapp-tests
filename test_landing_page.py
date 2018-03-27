import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from uuid import uuid4

class LandingPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.username = str(uuid4())
        self.password = str(uuid4())

    def test_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://localhost:5000/")
        self.assertIn("Login", driver.title)
        user_elem = driver.find_element_by_name("username")
        passwd_elem = driver.find_element_by_name("password")
        user_elem.send_keys("rajaniy")
        passwd_elem.send_keys("raj65241")
        login_btn = driver.find_element_by_xpath("""//input[@type="submit"]""")
        login_btn.click()
        assert "Tasks" in driver.title

    def test_register(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://localhost:5000/")
        self.assertIn("Login", driver.title)
        register_btn = driver.find_element_by_link_text("REGISTER")
        self.assertIsNotNone(obj=register_btn, msg="Expected Register btn, but found none")
        register_btn.click()
        user_elem = driver.find_element_by_name("username")
        passwd_elem = driver.find_element_by_name("password")
        email_elem = driver.find_element_by_name("email_addr")
        user_elem.send_keys(self.username)
        passwd_elem.send_keys(self.password)
        email_elem.send_keys(self.username + "@mailbox")
        confirm_registration = driver.find_element_by_xpath("""//input[@type="submit"]""")
        confirm_registration.click()
        assert "Login" in driver.title

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
        unittest.main()
