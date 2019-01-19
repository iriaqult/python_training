# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import group


class TestAddGroup(unittest.TestCase):

    
    def test_add_group(self):

        self.login(username="admin", password="secret")
        self.group_creation(group(name="test", header="fgdjsl", footer="dhjkd"))
        self.logout()


    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def group_creation(self, group):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    



if __name__ == "__main__":
    unittest.main()
