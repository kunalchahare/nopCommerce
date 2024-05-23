# import random
# import string
#
# import allure
# import pytest
# import time
#
# from allure_commons.types import AttachmentType
#
# from PageObjects.AddCustomerPage import AddCustomer
# from PageObjects.LoginPage import LoginClass
# from Utilities.readconfigfile import Readconfig
# from Utilities.Logger import LogGenerator
#
#
# class Test_AddCustomer:
#     Email = Readconfig.getEmail()
#     Password = Readconfig.getPassword()
#     log = LogGenerator.loggen()
#
#     @pytest.mark.Customer
#     def test_AddCustomer_003(self, setup):
#
#         self.log.info("Testcase test_Verify_Url_001 is Started")
#         self.log.info("Opening Browser")
#         self.driver = setup
#         self.lp = LoginClass(self.driver)
#         self.ac = AddCustomer(self.driver)
#
#         def Generate_Email():
#             username = ''.join(random.choices(string.ascii_lowercase, k=3))  # random 3 char lower case  e.g. abc
#             domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
#             return f"{username}@{domain}"  # random 3 char + domain
#
#         self.log.info("Enter Email:" + self.Email)
#         self.lp.Enter_Email(self.Email)
#
#         self.log.info("Enter Password:" + self.Password)
#         self.lp.Enter_Password(self.Password)
#
#         self.lp.Click_LoginButton()
#         self.log.info("Click on Login Button")
#
#         self.ac.Click_Customer_Menu()
#         self.log.info("Click on Menu: Customer")
#
#         self.ac.Click_Customer_Submenu()
#         self.log.info("Click Submenu: Customer")
#
#         self.ac.Click_AddNewCustomer()
#         self.log.info("Click on Add new Customer")
#
#         self.ac.Enter_Email(Generate_Email())
#         self.log.info("Entering Mail")
#
#         self.ac.Enter_Password("Credence@102")
#         self.log.info("Entering Password")
#
#         self.ac.Enter_FirstName("Kunal")
#         self.log.info("Entering First Name: Kunal")
#
#         self.ac.Enter_LastName("Chahare")
#         self.log.info("Entering Last Name: Chahare")
#
#         self.ac.Select_Gender("Male")
#         self.log.info("Selecting Gender as Male")
#
#         self.ac.Enter_DOB("12/16/1994")
#         self.log.info("Entering DOB 12/16/1994")
#
#         self.ac.Enter_CompanyName("Credence")
#         self.log.info("Entering Company Name as Credence")
#
#         self.ac.Checkbox_IsTaxExempt()
#         self.log.info("Checking 'Is Tax Exempt' box")
#
#         # self.ac.Click_NewsLetter()
#         # self.log.info("Click on News Letter")
#         #
#         # self.ac.Click_NewsLetterList()
#         # self.log.info("Click on News Letter List")
#
#         self.ac.DropDown_Manager_of_vendor("Vendor 1")
#         self.log.info("Selecting Vendor 1 from Manager of vendor DropDown")
#
#         self.ac.Checkbox_Active()
#         self.log.info("Checking 'Is Tax Exempt' box")
#
#         self.ac.Enter_Comment("Credence is Best")
#         self.log.info("Entering comment 'Credence is Best'")
#
#         self.ac.Click_SaveButton()
#         self.log.info("Click on Save Button")
#
#         if self.ac.Validate_Success_Message() == "Pass":
#             self.log.info("Taking Screenshot")
#             allure.attach(self.driver.get_screenshot_as_png(), name="test_AddCustomer_003-Pass",
#                           attachment_type=AttachmentType.PNG)
#             self.driver.save_screenshot("..\\Screenshots\\test_AddCustomer_003_Pass.png")
#             self.log.info("The new customer has been added successfully")
#             self.log.info("Testcase test_AddCustomer_003 is Passed")
#             assert True
#         else:
#             self.log.info("Taking Screenshot")
#             allure.attach(self.driver.get_screenshot_as_png(), name="test_AddCustomer_003-Fail",
#                           attachment_type=AttachmentType.PNG)
#             self.driver.save_screenshot("..\\Screenshots\\test_AddCustomer_003_Fail.png")
#             self.log.info("Testcase test_AddCustomer_003 is Failed")
#             assert False











