# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from new import New

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_new(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_add_new_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def create_new(self, wd, new):
        # init new creation
        wd.find_element_by_name("firstname").click()
        # fill new firm
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(new.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(new.middlename)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(new.address)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_test_add_new(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new_page(wd)
        self.create_new(wd, New(firstname="Konstantin", middlename="Styagailo", address="Parkovaya, 8"))
        self.logout(wd)

    def test_test_empty_new(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new_page(wd)
        self.create_new(wd, New(firstname="", middlename="", address=""))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
