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


    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # click edit
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_form(new_contact_data)
        # submit edit
        wd.find_element_by_name("update").click()


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


    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            #for cell in element:
            cells = element.find_elements_by_tag_name("td")
            text = cells[2].text
            #text = element.find_element_by_name("selected[]").get_attribute("accept")
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(contact(name = text, id = id))
        return contacts