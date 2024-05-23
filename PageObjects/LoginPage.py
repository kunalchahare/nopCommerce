from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginClass:

    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(self.driver, 10)

    Enter_Email_Xpath = "//input[@id='Email']"
    Enter_Password_Xpath = "//input[@id='Password']"
    Click_LoginButton_Xpath = "//button[@type='submit']"
    Click_LogoutButton_Xpath = "//a[normalize-space()='Logout']"
    Verify_Login_Xpath = "//h1[normalize-space()='Dashboard']"
    Verify_Logout_Xpath = "//h1[normalize-space()='Admin area demo']"

    def Enter_Email(self, Email):
        self.driver.find_element(By.XPATH, self.Enter_Email_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Enter_Email_Xpath).send_keys(Email)

    def Enter_Password(self, Password):
        self.driver.find_element(By.XPATH, self.Enter_Password_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Enter_Password_Xpath).send_keys(Password)

    def Click_LoginButton(self):
        self.driver.find_element(By.XPATH, self.Click_LoginButton_Xpath).click()

    def Verify_Login(self):
        try:
            self.driver.find_element(By.XPATH, self.Verify_Login_Xpath)
            return "Login Pass"
        except:
            return "Login Fail"

    def Click_LogoutButton(self):
        # self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Click_LogoutButton_Xpath)))
        self.driver.find_element(By.XPATH, self.Click_LogoutButton_Xpath).click()

    def Verify_Logout(self):
        try:
            self.driver.find_element(By.XPATH, self.Verify_Logout_Xpath)
            return "Logout Pass"
        except:
            return "Logout Fail"


