class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group
        self.fill_group(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.open_groups_page()


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self,new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group(new_group_data)
        # submit edit
        wd.find_element_by_name("update").click()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #submit deletion
        wd.find_element_by_name("delete").click()


    def fill_group(self, group):
        wd = self.app.wd
        self.change_field_name("group_name", group.name)
        self.change_field_name("group_header", group.header)
        self.change_field_name("group_footer", group.footer)


    def change_field_name(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

