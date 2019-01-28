class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group
        fill_group(self, group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()


    def edit_first_group(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        #select first group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        #edit group
        fill_group(self, group)
        #submit edit
        wd.find_element_by_name("update").click()

def fill_group(self, group):
    wd = self.app.wd
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



