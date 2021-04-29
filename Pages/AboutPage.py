from selenium.webdriver.support.select import Select

from Dbox.Locators.LocatorsAbout import LocatorsAbout
from selenium.webdriver.common.keys import Keys


class aboutUsProcess():
    def __init__(self, driver):
        self.driver = driver
        self.aboutmenu = LocatorsAbout.aboutUs_script
        self.playbtn = LocatorsAbout.pushPlay_script
        self.cbtn = LocatorsAbout.closing_script


    def EnterAboutUsMenu(self):
        self.driver.execute_script(self.aboutmenu)

    def EnterPlayBtn(self):
        self.driver.execute_script(self.playbtn)

    def EnterCloseBtn(self):
        self.driver.execute_script(self.cbtn)