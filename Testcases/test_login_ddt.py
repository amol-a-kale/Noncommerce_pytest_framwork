import time

from Pageobjectpages.Loginpage import Loginpage
from Utilities.customlogger import LogGen
import pytest
from Utilities.readproperty import ReadConfig
from Utilities import XLUtils



class Test_002_DDT_Login:
    baseURL = ReadConfig.geturl()
    filename = "C:\\Users\\Sanket\\Desktop\\frameworksmyself\\Nopcommerece_Hybrid\\Testdata\\LoginTestdata.xlsx"
    sheetname = 'Sheet1'
    logger = LogGen.loggen()

    @pytest.mark.run(order=3)
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*******Test_002_DDT_Login*********")
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.rows = XLUtils.getrowcount(self.filename, self.sheetname)
        print("Number of rows in excel: ", self.rows)

        lst_status = []
        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.filename, self.sheetname, r, 1)
            self.password = XLUtils.readData(self.filename, self.sheetname, r, 2)
            self.exp = XLUtils.readData(self.filename, self.sheetname, r, 3)
            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.click_login()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("***passed***")
                    self.lp.clicklogout()
                    lst_status.append("pass")
                elif self.exp == "Fail":
                    self.logger.info("***failed***")
                    self.lp.clicklogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("***Failed***")
                    self.lp.clicklogout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***passed***")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
            if "Fail" not in lst_status:
                self.logger.info("Login DDt test passed.....")
                print("Login DDt test passed.....")
                # self.driver.close()
                assert True
            else:
                self.looger.info("Login DDt test failed.....")
                print("Login DDt test failed.....")
                # self.driver.close()
                assert False

            self.logger.info("****** End of Login DDT Test*****")
            self.logger.info("******* completed TC_LoginDDT_002*****")

        self.driver.close()
        self.driver.quit()
