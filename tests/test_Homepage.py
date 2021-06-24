import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.enterName().send_keys(getData["firstname"])
        homepage.enterEmail().send_keys(getData["email"])
        homepage.clickOptionalCheckox().click()
        dropdown = Select(homepage.clickDropdown())
        dropdown.select_by_visible_text(getData["gender"])
        homepage.selectRadio().click()
        homepage.clickSubmit().click()
        message = homepage.verifyMessageText().text
        log.info("success message received is"+message)

        assert "Success! The" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_Homepage_data)
    def getData(self, request):
        return request.param