import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium_config import APPIUM_HOST, APPIUM_PORT
from pages.home_page import HomePage
from data.data import  Data

class TestBookRoundTrip:


    @pytest.fixture
    def appium_driver(self, appium_service):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.platform_version = '15.0'
        options.device_name = 'Pixel 8a API 35'
        options.automation_name = 'Uiautomator2'
        options.app_package = 'it.italotreno'
        options.app_activity = 'it.italotreno.MainActivity'
        options.no_reset = True

        driver = webdriver.Remote(
            command_executor = f'http://{APPIUM_HOST}:{APPIUM_PORT}',
            options=options)

        yield  driver
        driver.quit()

    def test_set_cities(self, appium_driver):
        data = Data.trip_data
        home = HomePage(appium_driver)

        home.set_origin_city(
             origin_city=data["origin_city"]
        )
        home.set_destination_city(
            destination_city=data["destination_city"]
        )


    def test_set_dates(self, appium_driver):
        data = Data.trip_data
        home = HomePage(appium_driver)

        home.set_depart_date(
            depart_month=data["depart_month"],
            depart_day=data["depart_day"]
        )
        home.set_return_date(
            return_month=data["return_month"],
            return_day=data["return_day"]
        )







