import allure
import pytest
from allure_commons.types import AttachmentType

from PageObjects.LoginPage import LoginClass
from Utilities.readconfigfile import Readconfig
from Utilities.Logger import LogGenerator


class Test_UserLogin:
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    log = LogGenerator.loggen()


    @pytest.mark.sanity
    # Allure Decorators
    @allure.feature('Page_Title')
    @allure.story('Verifying the Page Title')
    @allure.issue('ABC-123')
    @allure.title('nopCommerce - test page title')
    @allure.description('My test description')
    @allure.link('https://www.example.com')
    @allure.severity(allure.severity_level.CRITICAL)            # Allure Decorators
    def test_Verify_Url_001(self, setup):

        self.log.info("Testcase test_Verify_Url_001 is Started")
        self.driver = setup
        self.log.info("Opening Browser and Navigating to demo_nopCommerce")
        self.log.info("Page Title is: " + self.driver.title)

        Page_Title = self.driver.title
        print(Page_Title)

        if Page_Title == "Your store. Login":
            self.log.info("Testcase test_Verify_Url_001 is Passed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name = "test_Verify_Url_001-Pass",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_Verify_url_001_Pass.png")
            assert True
        else:
            self.log.info("Testcase test_Verify_Url_001 is Failed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Verify_Url_001-Fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_Verify_url_001_Fail.png")
            assert False
        self.log.info("Testcase test_Verify_Url_001 is Completed")

    @allure.severity(allure.severity_level.NORMAL)
    def test_Login_Logout_002(self, setup):

        self.log.info("Testcase test_Verify_Url_001 is Started")
        self.log.info("Opening Browser")
        self.driver = setup
        self.lp = LoginClass(self.driver)

        self.log.info("Enter Email:" + self.Email)
        self.lp.Enter_Email(self.Email)

        self.log.info("Enter Password:" + self.Password)
        self.lp.Enter_Password(self.Password)

        self.lp.Click_LoginButton()
        self.log.info("Click on Login Button")

        if self.lp.Verify_Login() == "Login Pass":
            self.log.info("Testcase test_Login_Logout_002 is Passed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Login_Logout_002-Pass",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_Login_Logout_002_Pass.png")
            self.log.info("Click on Logout Button")
            self.lp.Verify_Logout()
            assert True
        else:
            self.log.info("Testcase test_Login_Logout_002 is Failed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Login_Logout_002-Fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_Login_Logout_002_Fail.png")
            assert False

#
#
#
#
#
#
# # pytest -v -n=2 --html=HtmlReports/report.html -m sanity -p no:warnings --browser chrome  --> to run single testcase
# # pytest -v -n=2 --html=HtmlReports/report.html -p no:warnings --browser chrome  --> to run both testcases
#
# # pytest -v --alluredir="AllureReports folder path"  --> for allure files
# # pytest -v -n=2 --html=HtmlReports/report.html -p no:warnings --browser chrome --alluredir="AllureReports folder path"
# # pytest -v -n=3 --alluredir="C:\Users\hp\PycharmProjects\nopCommerce_Project\AllureReports" --browser chrome -p no:warnings
# # pytest -v -n=2 --html=HtmlReports/report.html -p no:warnings --browser chrome --alluredir="C:\Users\hp\PycharmProjects\nopCommerce_Project\AllureReports"
#
# # pytest -v allure serve "AllureReports folder path"  --> for allure files
# # allure serve "C:\Users\hp\PycharmProjects\nopCommerce_Project\AllureReports"
#
#
