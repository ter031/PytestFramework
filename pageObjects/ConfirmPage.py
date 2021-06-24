from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    CountryBox = (By.ID, "country")
    CountrySelect = (By.XPATH, "/html/body/app-root/app-shop/div/app-checkout/div/div[2]/ul/li/a")
    ClickCheckbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
    PurchaseButton = (By.CSS_SELECTOR, "input[class='btn btn-success btn-lg")
    SuccessMessage = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")

    def enterCountry(self):
        return self.driver.find_element(*ConfirmPage.CountryBox)

    def selectCountry(self):
        return self.driver.find_element(*ConfirmPage.CountrySelect)

    def clickCheckbox(self):
        return self.driver.find_element(*ConfirmPage.ClickCheckbox)

    def clickPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.PurchaseButton)

    def verifySuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.SuccessMessage)