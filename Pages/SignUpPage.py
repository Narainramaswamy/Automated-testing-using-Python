from selenium.webdriver.support.select import Select

from Dbox.Locators.LocatorsLogin import LocatorsLogin
from selenium.webdriver.common.keys import Keys


class signupProcess():
    def __init__(self,driver):
        self.driver = driver
        self.signupmenu = LocatorsLogin.signupopt_ID
        self.user = LocatorsLogin.signupusrn_ID
        self.pssd = LocatorsLogin.signuppssd_ID
        self.nextt = LocatorsLogin.signupbtn_xpath
        self.cbtn = LocatorsLogin.closebtn_script


    def EnterSignUpMenu(self):
        self.driver.find_element_by_id(self.signupmenu).click()

    def EnterSignUpUsername(self,name):
        self.driver.find_element_by_id(self.user).send_keys(name)

    def EnterSignUpPassword(self,psd):
        self.driver.find_element_by_id(self.pssd).send_keys(psd)

    def EnterSignUpBtn(self):
        self.driver.find_element_by_xpath(self.nextt).click()

    def EnterCloseBtn(self):
        self.driver.execute_script(self.cbtn)