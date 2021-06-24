from selenium import webdriver
import pytest

#@pytest.mark.usefixtures("setup")
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("getting all the prodcuts")

        products = checkoutPage.getAllProducts()
        for product in products:
            productName = checkoutPage.getProdutsName().text
            if productName == "Blackberry":
                product.checkoutPage.RequiredButton().click()

        checkoutPage.checkoutItems().click()
        confirmPage = checkoutPage.checkoutButton()
        log.info("Entering country name as ind")
        confirmPage.enterCountry().send_keys("ind")
        confirmPage.selectCountry().click()
        print(confirmPage.enterCountry().get_attribute("value"))
        confirmPage.clickCheckbox().click()
        confirmPage.clickPurchaseButton().click()
        successText = confirmPage.verifySuccessMessage().text
        log.info("text received from application is"+successText)

        assert "Success! Thank you!" in successText

        #self.driver.get_screenshot_as_file("success.png")