from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href='/angularpractice/shop']")
    NameTextbox = (By.CSS_SELECTOR, "input[name='name']")
    EmailBox = (By.NAME, "email")
    OptionalChcekbox = (By.ID, "exampleCheck1")
    Dropdown = (By.ID, "exampleFormControlSelect1")
    SelectRadioButton = (By.NAME, "inlineRadioOptions")
    SubmitButton = (By.XPATH, "//input[@type='submit']")
    Message = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def enterName(self):
        return self.driver.find_element(*HomePage.NameTextbox)

    def enterEmail(self):
        return self.driver.find_element(*HomePage.EmailBox)

    def clickOptionalCheckox(self):
        return self.driver.find_element(*HomePage.OptionalChcekbox)

    def clickDropdown(self):
        return self.driver.find_element(*HomePage.Dropdown)

    def selectRadio(self):
        return self.driver.find_element(*HomePage.SelectRadioButton)

    def clickSubmit(self):
        return self.driver.find_element(*HomePage.SubmitButton)

    def verifyMessageText(self):
        return self.driver.find_element(*HomePage.Message)


