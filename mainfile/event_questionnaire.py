####################
# Name:event questionnaire module
# Description: To do some operation
# Author: Alex herbert
# Date: 15-06-2022
####################
# Library use #
import time

import allure
import pyautogui
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from PageObject.Popupwindow import Popupwindow
from PageObject.Popupwindow import Popupwindow
from PageObject.add_form import Add_form
from PageObject.event_questionnaire import Event_questionnaire_tab
from PageObject.eventdiarypage import eventdiarypage
from PageObject.login_page import Loginpage
from Testdata.datareadwritefile import Datareadfile, usernamepass, passwordpass, datawritefail, loggedinpass
from Utilities.BaseClass import Baseclass


#@allure.severity(allure.severity_level.NORMAL)
class TestEpo(Baseclass):
    #@allure.description('To enter the valid username')
    def test_TC_02_username(self):
        log = self.loggerdemo()
        datareadusername = Datareadfile.username
        print(datareadusername)
        loginpage = Loginpage(self.driver)
        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.presence_of_element_located((By.NAME, "userNameOrEmail")))
        loginpage.usernameoremail().send_keys(datareadusername)
        usernamepass()

    #@allure.description('To enter the valid password')
    def test_Test_03_password(self):
        loginpage = Loginpage(self.driver)
        datareadpwd = Datareadfile.password
        print(datareadpwd)
        loginpage.password().send_keys(datareadpwd)
        passwordpass()


    try:
        #@allure.description('only login when entered a valid password')
        def test_TC_04_login_button(self):
            loginpage = Loginpage(self.driver)
            loginpage.loginbutton().click()
            time.sleep(5)
    except Exception as e:
        def test_failedcase(self):
            #allure.attach(self.driver.get_screenshot_as_png(), name="testfailedscreen",
            #            attachment_type=AttachmentType.PNG)
            msg2 = datawritefail()
            self.driver.close()
    finally:
        #@allure.description('Once logged in successfully to take a screenshot')
        def test_TC_05_screen_shot(self):
            pass
            #allure.attach(self.driver.get_screenshot_as_png(), name="testscreenshot",
            #          attachment_type=AttachmentType.PNG)

    @allure.description('To close the popup window')
    def test_TC_06_popup_window(self):
      popupwindow = Popupwindow(self.driver)
      popupwindow.popup().click()

    #@allure.description('when successfully logged in to check the title for confirmation')
    def test_TC_07_logged_conformation(self):
        title1 = self.driver.title
        if title1 == "Event Plan On":
            print("logged in successfully")
            msg1 = loggedinpass()
        else:
            msg2 = datawritefail()

    #@allure.description('To click the desired event')
    def test_TC_08_event_diary(self):
        eventdiary = eventdiarypage(self.driver)
        time.sleep(3)
        eventdiary.eventdiarytask().click()

    #@allure.description('To click the respective module')
    def test_tc_09_event_questionnaire_tab(self):
        event_questionnaire = Event_questionnaire_tab(self.driver)
        time.sleep(4)
        event_questionnaire.More_action().click()
        time.sleep(4)
        event_questionnaire.Questionnaire_tab().click()
        time.sleep(4)

    def test_tc_10_add_form(self):
        add_form = Add_form(self.driver)
        time.sleep(3)
        add_form.Add_form_button().click()
        time.sleep(3)
        add_form.Form_name().send_keys('vendor query')
        time.sleep(3)
        add_form.Titledesc().send_keys('To get the question about lease of product')
        time.sleep(3)
        add_form.Enter_question_name().send_keys('How many product produce per day')
        time.sleep(3)
        add_form.Questiontype_select().click()
        time.sleep(3)
        add_form.Option_select().click()
        time.sleep(3)
        add_form.Required_key().click()
        time.sleep(3)
        add_form.Add_question().click()
        time.sleep(3)
        add_form.Edit_choice1().clear()
        time.sleep(3)
        add_form.Edit_choice1().send_keys('5')
        time.sleep(3)
        add_form.Edit_choice2().clear()
        time.sleep(3)
        add_form.Edit_choice2().send_keys('7')
        time.sleep(3)
        add_form.Edit_choice3().clear()
        time.sleep(3)
        add_form.Edit_choice3().send_keys('6')
        time.sleep(3)
        add_form.Save_question_button().click()
        time.sleep(5)

    def test_tc_11_edit_questionnaire(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[@aria-controls="Edit"]').click()
        time.sleep(4)
        self.driver.find_element_by_xpath('//app-event-questionnaire[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//body[1]/app-root[1]/app-master-layout[1]/div[1]/div[1]/app-event-layout[1]/section[1]/div[2]/div[1]/app-event-questionnaire[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/i[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//app-add-question[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[2]/div[1]/p-dropdown[1]/div[1]/div[3]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem[4]//li').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//app-add-question[1]/div[2]/div[1]/div[2]/div[3]/span[1]/button[1]').click()
        time.sleep(3)

    def test_tc_12_setting_questionnaire(self):
        time.sleep(3)
        self.driver.find_element_by_id('setting-tab').click()
        time.sleep(3)
        self.driver.find_element_by_id('titlename').send_keys('vendor')
        time.sleep(3)
        self.driver.find_element_by_id('des').send_keys('to get vendor product details')
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[contains(text(), "Click to upload")]').click()
        time.sleep(20)
        pyautogui.write(r"G:\thirdeye\others\download.jpg")  # path of File
        time.sleep(15)
        pyautogui.press('enter')
        time.sleep(15)

    def test_tc_13_summary_tab(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//app-event-questionnaire[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/nav[1]/div[1]/a[1]').click()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="summary_tab",
                    attachment_type=AttachmentType.PNG)

    def test_tc_14_share_tab(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//app-event-questionnaire[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[@data-tour="shareactionQuestion"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//app-event-questionnaire[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p-multiselect[1]/div[1]/div[3]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@class="ui-multiselect-items-wrapper"]//ul[1]//p-multiselectitem[3]//li[1]//div[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@class="ui-multiselect-items-wrapper"]//ul[1]//p-multiselectitem[3]//div[2]//p-inputswitch//div').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[@class="ui-multiselect-close ui-corner-all"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//button[@data-tour="eqshareandsent"]').click()
        time.sleep(3)

    def test_tc_16_delete_questionnaire(self):
        time.sleep(10)
        ele = self.driver.find_elements_by_xpath('//app-event-questionnaire[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li/a/div[1]/h4')
        iter1 = -1
        for names in ele:
            iter1 = iter1 + 1
            text1 = names.text
            print(text1)
            if text1 == "vendor query":
                self.driver.find_elements_by_xpath('//div[@ptooltip="Used active"]')[iter1].click()
                time.sleep(3)
                break
        self.driver.find_element_by_xpath('//button[contains(text(), "Yes, Remove it!")]').click()
        time.sleep(6)
