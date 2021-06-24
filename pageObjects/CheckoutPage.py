from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    AllProducts = (By.XPATH, "//div[@class='card h-100']")
    ProductsName = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    RequiredButton = (By.XPATH, "//div[@class='card h-100']/div/button")
    CheckoutItems = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    CheckoutButton = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def getAllProducts(self):
        return self.driver.find_elements(*CheckoutPage.AllProducts)

    def getProdutsName(self):
        return self.driver.find_element(*CheckoutPage.ProductsName)

    def addCartButton(self):
        return self.driver.find_element(*CheckoutPage.RequiredButton)

    def checkoutItems(self):
        return self.driver.find_element(*CheckoutPage.CheckoutItems)

    def checkoutButton(self):
        self.driver.find_element(*CheckoutPage.CheckoutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage


