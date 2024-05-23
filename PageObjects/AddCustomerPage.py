from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:

    Click_Customer_Menu_Xpath = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
    Click_Customer_Submenu_Xpath = "//a[@href='/Admin/Customer/List']//i[@class='nav-icon far fa-dot-circle']"
    Click_AddNewCustomer_Xpath = "//a[@class='btn btn-primary']"
    Enter_Email_Xpath = "//input[@id='Email']"
    Enter_Password_Xpath = "//input[@id='Password']"
    Enter_FirstName_Xpath = "//input[@id='FirstName']"
    Enter_LastName_Xpath = "//input[@id='LastName']"
    Radio_Male_Xpath = "//input[@id='Gender_Male']"
    Radio_Femail_Xpath = "//input[@id='Gender_Female']"
    Calendar_Xpath = "//input[@id='DateOfBirth']"
    Enter_CompanyName_Xpath = "//input[@id='Company']"
    Checkbox_IsTaxExempt_Xpath = "//input[@id='IsTaxExempt']"
    Click_NewsLetter_Xpath = '//*[@id="customer-info"]/div[2]/div[9]/div[2]/div'
    Click_NewsLetter_YourStoreName_Xpath = "//li[normalize-space()='Your store name']"
    Click_NewsLetterList_Xpath = "//li[normalize-space()='Test store 2']"
    DropDown_Manage_Vendor_Xpath = "//select[@id='VendorId']"
    DropDown_Select_NotVendor_Xpath = '//*[@id="VendorId"]/option[1]'
    DropDown_Select_Vendor1_Xpath = '//*[@id="VendorId"]/option[2]'
    DropDown_Select_Vendor2_Xpath = '//*[@id="VendorId"]/option[3]'
    Checkbox_Active_Xpath = "//input[@id='Active']"
    Enter_Comment_Xpath = "//textarea[@id='AdminComment']"
    Click_SaveButton_Xpath = "//button[@name='save']"
    Success_Message_Xpath = "//div[@class='alert alert-success alert-dismissable']"  # The new customer has been added successfully.

    def __init__(self, driver):
        self.driver = driver

    def Click_Customer_Menu(self):
        self.driver.find_element(By.XPATH, self.Click_Customer_Menu_Xpath).click()

    def Click_Customer_Submenu(self):
        self.driver.find_element(By.XPATH, self.Click_Customer_Submenu_Xpath).click()

    def Click_AddNewCustomer(self):
        self.driver.find_element(By.XPATH, self.Click_AddNewCustomer_Xpath).click()

    def Enter_Email(self, email):
        self.driver.find_element(By.XPATH, self.Enter_Email_Xpath).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.Enter_Password_Xpath).send_keys(password)

    def Enter_FirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.Enter_FirstName_Xpath).send_keys(firstname)

    def Enter_LastName(self, lastname):
        self.driver.find_element(By.XPATH, self.Enter_LastName_Xpath).send_keys(lastname)

    def Select_Gender(self, gender):

        if gender == "Male":
            self.driver.find_element(By.XPATH, self.Radio_Male_Xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.Radio_Femail_Xpath).click()

    def Enter_DOB(self, date):
        self.driver.find_element(By.XPATH, self.Calendar_Xpath).send_keys(date)

    def Enter_CompanyName(self, company_name):
        self.driver.find_element(By.XPATH, self.Enter_CompanyName_Xpath).send_keys(company_name)

    def Checkbox_IsTaxExempt(self):
        self.driver.find_element(By.XPATH, self.Checkbox_IsTaxExempt_Xpath).click()

    def Click_NewsLetter(self):
        self.driver.find_element(By.XPATH, self.Click_NewsLetter_Xpath).click()

    def Click_NewsLetterList(self):
        self.driver.find_element(By.XPATH, self.Click_NewsLetterList_Xpath).click()

    def DropDown_Manager_of_vendor(self, value):
        Select(self.driver.find_element(By.XPATH, self.DropDown_Manage_Vendor_Xpath)).select_by_visible_text(value)

    def Checkbox_Active(self):
        self.driver.find_element(By.XPATH, self.Checkbox_Active_Xpath).click()

    def Enter_Comment(self, comment):
        self.driver.find_element(By.XPATH, self.Enter_Comment_Xpath).send_keys(comment)

    def Click_SaveButton(self):
        self.driver.find_element(By.XPATH, self.Click_SaveButton_Xpath).click()

    def Validate_Success_Message(self):
        try:
            self.driver.find_element(By.XPATH, self.Success_Message_Xpath)
            return "Pass"
        except:
            return "Fail"
