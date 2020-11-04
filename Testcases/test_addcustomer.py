import time

import pytest

from Pageobjectpages.Loginpage import Loginpage
from Pageobjectpages.addcustmerpage import Addcustomer
from Utilities.customlogger import LogGen

from Utilities.readproperty import ReadConfig
import string
import random


class Test_003_Addcustomer:
    baseURL = ReadConfig.geturl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.run(order=4)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addcustomer(self, setup):
        self.logger.info("******Test_003_addcustomer********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")
        time.sleep(5)
        self.addcus = Addcustomer(self.driver)
        self.addcus.clickoncustomersmenu()

        time.sleep(5)

        self.addcus.clickoncustomersmenuitems()
        self.addcus.clickonaddnewbtn()
        self.logger.info("************* Providing customer info **********")
        time.sleep(5)
        self.email = random_generator() + "@gmail.com"
        self.addcus.setmail(self.email)
        self.addcus.setpassword("test123")
        self.addcus.setfirstname("amol")
        self.addcus.setlastname("patil")
        self.addcus.setgender("Male")
        self.addcus.setDob("12/06/1996")
        self.addcus.setcompnayname("tcs")
        time.sleep(5)
        self.addcus.setCustomerRoles("Guests")
        self.addcus.setManagerOfVendor("Vendor 2")
        self.addcus.setAdminContent("this is testing")
        self.addcus.clickOnSave()
        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started ****************")
        self.msg = self.driver.find_element_by_tag_name("body").text
        # print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")

        else:
            self.logger.error("********* Add customer Test Failed ************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustmerpage.png")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
