from selenium.webdriver.support.select import Select

from Dbox.Locators.LocatorsCart import LocatorsCart
from selenium.webdriver.common.keys import Keys


class cartProcess():
    def __init__(self, driver):
        self.driver = driver
        self.cartmenu = LocatorsCart.cart_script
        self.place_order = LocatorsCart.po_xpath
        self.name1 = LocatorsCart.name_xpath
        self.country = LocatorsCart.country_xpath
        self.city = LocatorsCart.city_xpath
        self.credits = LocatorsCart.credit_xpath
        self.month = LocatorsCart.month_xpath
        self.year = LocatorsCart.year_xpath
        self.purch = LocatorsCart.purchase_xpath
        self.okay = LocatorsCart.ok_script
        self.close = LocatorsCart.clssbtn_script


    def EnterCartMenu(self):
        self.driver.execute_script(self.cartmenu)

    def EnterPlaceOrderBtn(self):
        self.driver.find_element_by_xpath(self.place_order).click()

    def EnterNames(self,name2):
        self.driver.find_element_by_xpath(self.name1).send_keys(name2)

    def EnterCountry(self,countries):
        self.driver.find_element_by_xpath(self.country).send_keys(countries)

    def EnterCity(self,cities):
        self.driver.find_element_by_xpath(self.city).send_keys(cities)

    def EnterCreditDetails(self,credit):
        self.driver.find_element_by_xpath(self.credits).send_keys(credit)

    def EnterMonth(self,months):
        self.driver.find_element_by_xpath(self.month).send_keys(months)

    def EnterYear(self,years):
        self.driver.find_element_by_xpath(self.year).send_keys(years)

    def EnterPurchaseBtn(self):
        self.driver.find_element_by_xpath(self.purch).click()

    def EnterOkBtn(self):
        self.driver.execute_script(self.okay)

    def EnterCloseButton(self):
        self.driver.execute_script(self.close)