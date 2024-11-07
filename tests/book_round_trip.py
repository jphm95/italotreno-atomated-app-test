from appium.options.android import UiAutomator2Options

from appium_config import APPIUM_HOST, APPIUM_PORT
from pages.home_page import HomePage


class TestBookRoundTrip:



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
        home = HomePage(appium_driver)

        home.set_origin_city(
             origin_city=["origin_city"]
        )
        home.set_destination_city(
            destination_city=["destination_city"]
        )


    def test_set_dates(self, appium_driver):
        home = HomePage(appium_driver)

        home.set_depart_date(
            depart_month=["depart_month"],
            depart_day=["depart_day"]
        )
        home.set_return_date(
            return_month=["return_month"],
            return_day=["return_day"]
        )







