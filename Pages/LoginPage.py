from selenium.webdriver.support.select import Select

from Dbox.Locators.LocatorsLogin import LocatorsLogin
from selenium.webdriver.common.keys import Keys


class loginProcess():
    def __init__(self, driver):
        self.driver = driver
        self.loginmenu = LocatorsLogin.loginopt_ID
        self.user = LocatorsLogin.loginusrn_ID
        self.pssd = LocatorsLogin.loginpssd_ID
        self.nextt = LocatorsLogin.loginbtn_xpath
        self.cbtn = LocatorsLogin.clsbtn_script
        self.welopt = LocatorsLogin.welcomeopt_script


    def EnterLoginMenu(self):
        self.driver.find_element_by_id(self.loginmenu).click()

    def EnterLoginUsername(self,names):
        self.driver.find_element_by_id(self.user).send_keys(names)

    def EnterLoginPassword(self,passwd):
        self.driver.find_element_by_id(self.pssd).send_keys(passwd)

    def EnterLoginBtn(self):
        self.driver.find_element_by_xpath(self.nextt).click()

    def EnterClsBtn(self):
        self.driver.execute_script(self.cbtn)

    def EnterWelcomeBtn(self):
        self.driver.execute_script(self.welopt)