from selenium.webdriver.support.select import Select

from Dbox.Locators.LocatorsHome import LocatorsHome
from selenium.webdriver.common.keys import Keys


class homeProcess():
    def __init__(self, driver):
        self.driver = driver
        self.homemenu = LocatorsHome.homeopt_script
        self.lcar = LocatorsHome.imgprev_xpath
        self.rcar = LocatorsHome.imgnxt_xpath
        self.phones = LocatorsHome.phones_script
        self.htc = LocatorsHome.htc_sript
        self.addcart1 = LocatorsHome.atoc1_xpath
        self.laptops = LocatorsHome.laptop_script
        self.mac = LocatorsHome.macbook_script
        self.addcart2 = LocatorsHome.atoc2_xpath
        self.monitors = LocatorsHome.monitor_script
        self.apple = LocatorsHome.apple_script
        self.addcart3 = LocatorsHome.atoc3_xpath


    def EnterHomeMenu(self):
        self.driver.execute_script(self.homemenu)

    def EnterPrevImage(self):
        self.driver.find_element_by_xpath(self.lcar).click()

    def EnterNextImage(self):
        self.driver.find_element_by_xpath(self.rcar).click()

    def EnterPhoneVariants(self):
        self.driver.execute_script(self.phones)

    def EnterHtcPhone(self):
        self.driver.execute_script(self.htc)

    def EnterAddtoCart1(self):
        self.driver.find_element_by_xpath(self.addcart1).click()

    def EnterLaptopVariants(self):
        self.driver.execute_script(self.laptops)

    def EnterMacBookLaptop(self):
        self.driver.execute_script(self.mac)

    def EnterAddtoCart2(self):
        self.driver.find_element_by_xpath(self.addcart2).click()

    def EnterMonitorVariants(self):
        self.driver.execute_script(self.monitors)

    def EnterApple(self):
        self.driver.execute_script(self.apple)

    def EnterAddtoCart3(self):
        self.driver.find_element_by_xpath(self.addcart3).click()