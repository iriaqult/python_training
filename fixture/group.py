class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group
        self.fill_group(self, group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()


    def edit_first_group(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        #edit group
        self.fill_group(self, group)
        #submit edit
        wd.find_element_by_name("update").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self,new_group_data):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        # select first group
        self.select_first_group(new_group_data)
        wd.find_element_by_name("edit").click()

        # submit edit
        wd.find_element_by_name("update").click()

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        #submit deletion
        wd.find_element_by_name("delete").click()



    def fill_group(self, group):
        wd = self.app.wd
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)


    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)



