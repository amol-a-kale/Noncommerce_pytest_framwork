class Loginpage:
    # enetr all locator

    textbox_Username_Id = "Email"
    textbox_Password_Id = "Password"
    btn_login_xpath = "//div/input[@type='submit']"
    link_logout_linktext = "Logout"

    # initilize the driver
    # catch the driver from test case and pass to the
    # pass the driver to testcase later

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_id(self.textbox_Username_Id).clear()
        self.driver.find_element_by_id(self.textbox_Username_Id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.textbox_Password_Id).clear()
        self.driver.find_element_by_id(self.textbox_Password_Id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
