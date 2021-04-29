from selenium.webdriver.support.select import Select

from Dbox.Locators.LocatorsLogout import LocatorsLogout
from selenium.webdriver.common.keys import Keys


class logoutProcess():
    def __init__(self, driver):
        self.driver = driver
        self.logoutmenu = LocatorsLogout.logout_ID


    def EnterLogoutMenu(self):
        self.driver.find_element_by_id(self.logoutmenu).click()


