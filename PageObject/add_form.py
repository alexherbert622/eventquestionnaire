from selenium.webdriver.common.by import By


class Add_form:

    def __init__(self, driver):
        self.driver = driver

    add_form_button = (By.XPATH, '//a[@ptooltip="Add Form"]')
    form_name = (By.ID, 'titlename')
    titledesc = (By.ID, 'titledes')
    enter_question_name = (By.ID, 'questionname')
    question_type_select = (By.XPATH, '//app-add-question[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[4]/div[2]/div[1]/p-dropdown[1]/div[1]/div[3]')
    option_select = (By.XPATH, '//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem[3]//li')
    required_key = (By.TAG_NAME, 'p-inputswitch')
    add_question = (By.XPATH, '//button[@data-tour="addQuestion"]')
    edit_choice1 = (By.XPATH, '//input[@ng-reflect-model="Choice 1"]')
    edit_choice2 = (By.XPATH, '//input[@ng-reflect-model="Choice 2"]')
    edit_choice3 = (By.XPATH, '//input[@ng-reflect-model="Choice 3"]')
    save_question_button = (By.XPATH, '//button[@data-tour="saveQuestion"]')

    def Add_form_button(self):
        return self.driver.find_element(*Add_form.add_form_button)

    def Form_name(self):
        return self.driver.find_element(*Add_form.form_name)

    def Titledesc(self):
        return self.driver.find_element(*Add_form.titledesc)

    def Enter_question_name(self):
        return self.driver.find_element(*Add_form.enter_question_name)

    def Questiontype_select(self):
        return self.driver.find_element(*Add_form.question_type_select)

    def Option_select(self):
        return self.driver.find_element(*Add_form.option_select)

    def Required_key(self):
        return self.driver.find_element(*Add_form.required_key)

    def Add_question(self):
        return self.driver.find_element(*Add_form.add_question)

    def Edit_choice1(self):
        return self.driver.find_element(*Add_form.edit_choice1)

    def Edit_choice2(self):
        return self.driver.find_element(*Add_form.edit_choice2)

    def Edit_choice3(self):
        return self.driver.find_element(*Add_form.edit_choice3)

    def Save_question_button(self):
        return self.driver.find_element(*Add_form.save_question_button)