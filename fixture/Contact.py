from model.contact import contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_form (contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(new_contact_data, 0)


    def modify_contact_by_index(self, new_contact_data,index):
        wd = self.app.wd
        self.open_home_page()
        #self.select_contact_by_index(index)
        self.click_edit_by_index(index)
        self.fill_form(new_contact_data)
        # submit edit
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def click_edit_by_index(self, index):
        wd = self.app.wd
        #add index here
        wd.find_element_by_css_selector('img[alt="Edit"]').click()

    def fill_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("email", contact.email)
 

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0:
            wd.find_element_by_link_text("home").click()


    contact_cache = None


    def get_contact_list(self):
        wd = self.app.wd
        if self.contact_cache is None:
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(contact(name=firstname, id=id, last_name=lastname,
                                                  homephone=all_phones[0], mobilephone=all_phones[1], workphone=all_phones[2],
                                                  secondaryphone=all_phones[3]))
        return list(self.contact_cache)


    def open_contact_to_view_by_index(self,index):
        wd = self.app.wd
        self.open_home_page()
        row =  wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()


    def contact_from_home_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_elements_by_name("firstname").get_attribute("value")
        lastname = wd.find_elements_by_name("lastname").get_attribute("value")
        id = wd.find_elements_by_name("id").get_attribute("value")
        homephone = wd.find_elements_by_name("home").get_attribute("value")
        mobilephone = wd.find_elements_by_name("work").get_attribute("value")
        workphone = wd.find_elements_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_elements_by_name("phone2").get_attribute("value")
        return contact(name=firstname,last_name=lastname,id=id, homephone=homephone,
                       mobilephone=mobilephone,workphone=workphone,secondaryphone=secondaryphone)


