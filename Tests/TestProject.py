import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Dbox.Pages.SignUpPage import signupProcess
from Dbox.Pages.LoginPage import loginProcess
from Dbox.Pages.ContactPage import contactUsProcess
from Dbox.Pages.AboutPage import aboutUsProcess
from Dbox.Pages.HomePage import homeProcess
from Dbox.Pages.CartPage import cartProcess
from Dbox.Pages.LogoutPage import logoutProcess
import time

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/DRIVERS/chromedriver.exe")
    def test_dbox(self):
        baseURL = "https://www.demoblaze.com/index.html"
        driver = self.driver
        driver.get(baseURL)
        driver.maximize_window()
        signup = signupProcess(driver)
        signup.EnterSignUpMenu()
        driver.switch_to.active_element
        time.sleep(10)
        signup.EnterSignUpUsername("Narain")
        signup.EnterSignUpPassword("12345")
        signup.EnterSignUpBtn()
        driver.implicitly_wait(1000)
        WebDriverWait(driver, 100).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        signup.EnterCloseBtn()
        driver.implicitly_wait(30)
        driver.switch_to.active_element
        login = loginProcess(driver)
        time.sleep(10)
        login.EnterLoginMenu()
        time.sleep(10)
        driver.switch_to.active_element
        login.EnterLoginUsername("Narain")
        login.EnterLoginPassword("12345")
        login.EnterLoginBtn()
        login.EnterClsBtn()
        driver.implicitly_wait(30)
        login.EnterWelcomeBtn()
        driver.implicitly_wait(30)
        contact = contactUsProcess(driver)
        time.sleep(10)
        contact.EnterContactUsMenu()
        time.sleep(10)
        driver.implicitly_wait(100)
        driver.switch_to.active_element
        driver.implicitly_wait(100)
        contact.EnterContactmail("mpmnarain@gmail.com")
        contact.EnterContactname("Narain")
        driver.implicitly_wait(30)
        contact.EnterMessage("Good")
        driver.implicitly_wait(30)
        #contact.EntersendMsgBtn()
        contact.EntersendMsg1()
        WebDriverWait(driver, 100).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        contact.EnterCloseBtn()
        driver.implicitly_wait(100)
        print("Before About Process")
        about = aboutUsProcess(driver)
        about.EnterAboutUsMenu()
        time.sleep(10)
        driver.switch_to.active_element
        about.EnterPlayBtn()
        time.sleep(10)
        about.EnterCloseBtn()
        driver.implicitly_wait(100)
        print("Before Home Process")
        time.sleep(10)
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
        cart.EnterPlaceOrderBtn()
        time.sleep(10)
        cart.EnterNames("Narain")
        cart.EnterCountry("India")
        cart.EnterCity("Chennai")
        cart.EnterCreditDetails("6071323255007889")
        cart.EnterMonth("04")
        cart.EnterYear("23")
        cart.EnterPurchaseBtn()
        driver.implicitly_wait(200)
        cart.EnterOkBtn()
        cart.EnterCloseButton()
        time.sleep(10)
        logout = logoutProcess(driver)
        logout.EnterLogoutMenu()






if __name__ == '_main_':
    unittest.main()