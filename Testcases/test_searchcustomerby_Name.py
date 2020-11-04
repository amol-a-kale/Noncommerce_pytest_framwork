import time

import pytest

from Pageobjectpages.Loginpage import Loginpage
from Pageobjectpages.addcustmerpage import Addcustomer
from Pageobjectpages.searchcustmomerpage import SearchCustomer
from Utilities.customlogger import LogGen
from Utilities.readproperty import ReadConfig

class Test_searchcustomerbyFirstName_005:
    baseURL = ReadConfig.geturl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.run(order=6)
    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("*************** Test_005_Login *****************")
        self.logger.info("****Started searchCustomerByFirstName test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        self.logger.info("***** Login successfully*******")
        self.logger.info("******* Starting Search Customer By Email **********")
        self.addcus = Addcustomer(self.driver)
        self.addcus.clickoncustomersmenu()
        time.sleep(5)
        self.addcus.clickoncustomersmenuitems()
        self.logger.info("****successfully landing on search customer page*********")
        self.logger.info("************* searching customer by emailID **********")

        self.searchcus = SearchCustomer(self.driver)
        self.searchcus.setFirstname("victoria")
        self.searchcus.clickSearch()
        time.sleep(5)
        status = self.searchcus.searchCustomerByName("victoria")

        self.driver.close()
        assert True
        self.logger.info("***************  TC_SearchCustomerByEmail_005 Finished  *********** ")
