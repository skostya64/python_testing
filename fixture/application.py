from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_add_new_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def create_new(self, new):
        wd = self.wd
        self.open_home_page()
        self.open_add_new_page()
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

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_xpath("//div[@id='content']/form").click()
        # submit group creation
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def destroy(self):
        self.wd.quit()
