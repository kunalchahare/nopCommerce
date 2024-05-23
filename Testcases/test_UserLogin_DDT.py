# import allure
# # import pytest
# from allure_commons.types import AttachmentType
#
# from PageObjects.LoginPage import LoginClass
# from Utilities import ExcelMethods
# from Utilities.Logger import LogGenerator
#
#
# class Test_Login_DDT:
#     log = LogGenerator.loggen()
#     Excel_File_Path = "C:\\Users\\hp\\PycharmProjects\\nopCommerce_Project\\Testcases\\TestData\\Test_Data.xlsx"
#
#     def test_user_login_DDT_005(self, setup):
#         self.log.info("Testcase test_user_login_DDT_005 is Started")
#         self.driver = setup
#         self.log.info("Opening Browser")
#         self.lp = LoginClass(self.driver)
#         self.rows = ExcelMethods.numRows(self.Excel_File_Path, 'LoginData')
#
#         Status_List = []
#         for r in range(2, self.rows + 1):  # iteration r=2
#             self.username = ExcelMethods.readData(self.Excel_File_Path, 'LoginData', r, 2)
#             self.password = ExcelMethods.readData(self.Excel_File_Path, 'LoginData', r, 3)
#             self.Expected_Result = ExcelMethods.readData(self.Excel_File_Path, 'LoginData', r, 4)
#
#             self.log.info("Enter Email:" + self.username)
#             self.lp.Enter_Email(self.username)
#
#             self.log.info("Enter Password:" + self.password)
#             self.lp.Enter_Password(self.password)
#
#             self.lp.Click_LoginButton()
#             self.log.info("Click on Login Button")
#
#             if self.lp.Verify_Login() == "Login Pass":  # actual result # Login pass
#                 self.log.info("Login Pass")
#                 ExcelMethods.writenData(self.Excel_File_Path, 'LoginData', r, 5, "Pass")
#                 if self.Expected_Result == "Pass":  # expected result
#                     Status_List.append("Pass")  # updating the Status List
#                     self.log.info("Testcase test_user_login_004 is Passed")
#                     self.log.info("Taking screenshot")
#                     allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_parameters_004-Pass",
#                                   attachment_type=AttachmentType.PNG)
#                     self.driver.save_screenshot("..\\Screenshots\\test_user_login_parameters_004.png")
#                     self.log.info("Click on Logout Button")
#                     self.lp.Click_LogoutButton()
#                 elif self.Expected_Result == "Fail":
#                     self.log.info("Expected Fail")
#                     Status_List.append("Fail")
#                     ExcelMethods.writenData(self.Excel_File_Path, 'LoginData', r, 5, "Pass")
#                     self.log.info("Taking screenshot")
#                     allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_parameters_004-Pass",
#                                   attachment_type=AttachmentType.PNG)
#                     self.driver.save_screenshot("..\\Screenshots\\test_user_login_parameters_004.png")
#                     self.log.info("Click on Logout Button")
#                     self.lp.Click_LogoutButton()
#             elif self.lp.Verify_Login() == "Login Fail":  # Login Fail
#                 ExcelMethods.writenData(self.Excel_File_Path, 'LoginData', r, 5, "Fail")
#                 self.log.info("Login Fail")
#                 if self.Expected_Result == "Fail":
#                     self.log.info("Expected Fail")
#                     Status_List.append("Pass")
#                 elif self.Expected_Result == "Pass":
#                     self.log.info("Expected Pass")
#                     Status_List.append("Fail")
#                     self.log.info("Test_case test_user_login_004 is Failed")
#                     self.log.info("Taking screenshot")
#                     allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_parameters_004-Fail",
#                                   attachment_type=AttachmentType.PNG)
#                     self.driver.save_screenshot("..\\Screenshots\\test_user_login_parameters_004.png")
#
#         print(Status_List)
#
#         if "Pass" in Status_List:
#             self.log.info("Test_case test_user_login_004 is Passed")
#             assert True
#         else:
#             self.log.info("Test_case test_user_login_004 is Failed")
#             assert False
#
#         self.log.info("Test_case test_user_login_DDT_005 is Completed")