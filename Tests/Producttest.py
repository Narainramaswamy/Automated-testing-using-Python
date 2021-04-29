import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Dbox.Pages.HomePage import homeProcess
from Dbox.Pages.CartPage import cartProcess
import time

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/DRIVERS/chromedriver.exe")
    def test_dbox(self):
        baseURL = "https://www.demoblaze.com/index.html"
        driver = self.driver
        driver.get(baseURL)
        driver.maximize_window()
        home = homeProcess(driver)
        home.EnterHomeMenu()
        driver.implicitly_wait(100)
        home.EnterPhoneVariants()
        time.sleep(10)
        driver.execute_script("window.scrollBy(0, 3500);")
        WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located)
        home.EnterHtcPhone()
        home.EnterAddtoCart1()
        WebDriverWait(driver, 100).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        driver.execute_script("window.scrollTo(0,0);")
        home.EnterHomeMenu()
        print("Before Laptop Process")
        driver.implicitly_wait(100)
        home.EnterLaptopVariants()
        time.sleep(10)
        driver.execute_script("window.scrollBy(0, 3000);")
        home.EnterMacBookLaptop()
        home.EnterAddtoCart2()
        WebDriverWait(driver, 100).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        driver.execute_script("window.scrollTo(0,0);")
        home.EnterHomeMenu()
        print("Before Monitor Process")
        driver.implicitly_wait(100)
        driver.execute_script("window.scrollBy(0, 100);")
        home.EnterMonitorVariants()
        time.sleep(10)
        driver.execute_script("window.scrollBy(0, 500);")
        home.EnterApple()
        home.EnterAddtoCart3()
        WebDriverWait(driver, 100).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        driver.execute_script("window.scrollTo(0,0);")
        home.EnterHomeMenu()
        time.sleep(10)
        cart = cartProcess(driver)
        cart.EnterCartMenu()
        time.sleep(5)
        driver.implicitly_wait(100)
        cart.EnterPlaceOrderBtn()
        cart.EnterNames("Narain")
        cart.EnterCountry("India")
        cart.EnterCity("Chennai")
        cart.EnterCreditDetails("6071323255007889")
        cart.EnterMonth("04")
        cart.EnterYear("23")
        cart.EnterPurchaseBtn()
        driver.implicitly_wait(200)
        cart.EnterOkBtn()


