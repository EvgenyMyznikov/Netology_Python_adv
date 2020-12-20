import unittest
import selenium
from selenium import webdriver


class YaDiskAuth(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.driver.get("https://passport.yandex.ru/auth/")

    def test_ya_disk_auth(self):
        login = self.driver.find_element_by_name('UserName')
        password = self.driver.find_element_by_name('Password')

        login.send_keys('')
        password.send_keys('')
        login.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
