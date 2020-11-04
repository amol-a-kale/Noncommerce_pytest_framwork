import time

from selenium.webdriver.support.select import Select


class Addcustomer:
    # add customer page
    lnkcustmers_menu_xpath = "//span[ text ()='Customers'][1]"
    lnkcustmers_menuitem_xpath = "(//span[text()='Customers'])[2]"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickoncustomersmenu(self):
        self.driver.find_element_by_xpath(self.lnkcustmers_menu_xpath).click()

    def clickoncustomersmenuitems(self):
        self.driver.find_element_by_xpath(self.lnkcustmers_menuitem_xpath).click()

    def clickonaddnewbtn(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setfirstname(self, name):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(name)

    def setlastname(self, lastname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastname)

    def setgender(self, gender):
        if gender == "male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == "female":
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()

        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setDob(self, Dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(Dob)

    def setcompnayname(self, company):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(company)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

        # drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        # drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
