import allure
import pytest
from allure_commons.types import AttachmentType

from PageObjects.LoginPage import LoginClass
from Utilities.readconfigfile import Readconfig
from Utilities.Logger import LogGenerator


class Test_UserLogin_Parameters:
    log = LogGenerator.loggen()

    def test_user_login_parameters_004(self, setup, DataForLogin):
        self.log.info("Testcase test_user_login_parameters_004 is Started")
        self.log.info("Opening Browser")
        self.driver = setup
        self.lp = LoginClass(self.driver)

        self.log.info("Enter Email:" + DataForLogin[0])
        self.lp.Enter_Email(DataForLogin[0])

        self.log.info("Enter Password:" + DataForLogin[1])
        self.lp.Enter_Password(DataForLogin[1])
        self.lp.Click_LoginButton()
        self.log.info("Click on Login Button")

        Status_List = []
        if self.lp.Verify_Login() == "Login Pass":  # actual result # Login pass
            if DataForLogin[2] == "Pass":  # expected result
                Status_List.append("Pass")  # updating the Status List
                self.log.info("Testcase test_user_login_004 is Passed")
                self.log.info("Taking screenshot")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_parameters_004-Pass",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshots\\test_user_login_parameters_004.png")
                self.log.info("Click on Logout Button")
                self.lp.Verify_Logout()
            elif DataForLogin[2] == "Fail":
                Status_List.append("Fail")
        elif self.lp.Verify_Login() == "Login Fail":  # Login Fail
            if DataForLogin[2] == "Fail":
                Status_List.append("Pass")
            elif DataForLogin[2] == "Pass":
                Status_List.append("Fail")
                self.log.info("Test_case test_user_login_004 is Failed")
                self.log.info("Taking screenshot")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_parameters_004-Fail",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshots\\test_user_login_parameters_004.png")
            self.log.info("Test_case test_user_login_parameters_004 is Completed")
        print(Status_List)

        if "Pass" in Status_List:
            assert True
        else:
            assert False
