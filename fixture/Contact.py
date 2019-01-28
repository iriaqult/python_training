class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_form (self, contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self,new_contact_data):
        wd = self.app.wd
        self.select_first_contact()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        #select first contact
        self.select_first_contact()
        self.fill_form(self, contact)
        # submit edit
        wd.find_element_by_name("update").click()



    def fill_form(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.name)
        self.type("middlename", contact.middle_name)
        self.type("lastname", contact.last_name)
        self.type("email", contact.email)
 

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(contact.name)





