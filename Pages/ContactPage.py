from selenium.webdriver.support.select import Select

from Dbox.Locators.LocatorsContact import LocatorsContact
from selenium.webdriver.common.keys import Keys


class contactUsProcess():
    def __init__(self, driver):
        self.driver = driver
        self.contactmenu = LocatorsContact.contactopt_script
        self.email = LocatorsContact.email_ID
        self.names = LocatorsContact.name_ID
        self.msg = LocatorsContact.msg_ID
        self.nextt = LocatorsContact.smsg_script
        self.nextt1 = LocatorsContact.smsg_class
        self.cbtn = LocatorsContact.closebtn_script


    def EnterContactUsMenu(self):
        self.driver.execute_script(self.contactmenu)

    def EnterContactmail(self,mail):
        self.driver.find_element_by_id(self.email).send_keys(mail)

    def EnterContactname(self,name):
        self.driver.find_element_by_id(self.names).send_keys(name)

    def EnterMessage(self,comment):
        self.driver.find_element_by_id(self.msg).send_keys(comment)

    def EntersendMsgBtn(self):
        self.driver.execute_script(self.msg)

    def EntersendMsg1(self):
        #x = self.driver.find_elements_by_class_name(self.nextt1)
        x = self.driver.find_elements_by_tag_name("button")
        print(len(x))
        x[2].click()

    def EnterCloseBtn(self):
        self.driver.execute_script(self.cbtn)