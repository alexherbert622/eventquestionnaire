from selenium.webdriver.common.by import By


class Event_questionnaire_tab:

    def __init__(self, driver):
        self.driver = driver

    more_action = (By.XPATH, '//app-event-layout[1]/section[1]/div[1]/span[1]/ul[1]/li[13]/div[1]/a[1]')
    questionnaire_tab = (By.XPATH, '//app-event-layout[1]/section[1]/div[1]/span[1]/ul[1]/li[13]/div[1]/div[1]/a[2]')

    def More_action(self):
        return self.driver.find_element(*Event_questionnaire_tab.more_action)

    def Questionnaire_tab(self):
        return self.driver.find_element(*Event_questionnaire_tab.questionnaire_tab)