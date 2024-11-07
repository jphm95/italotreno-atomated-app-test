from calendar import month

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Locators:

    departure_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter the departure station")')
    departure_station = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    return_station = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    departure_calendar = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Outward")')
    return_calendar = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add Return")')
    calendar_done_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("DONE")')
    search_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Trains Search search")')
    right_arrow = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Next Month")')
    left_arrow = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Previous Month")')


    #Dynamic locators:
    month_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("[month_locator]")')
    depart_day = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("[departure_day]")')
    return_day = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("[return_day]")')


    #Methods:

    def click_departure_field(self):
        self.driver.find_element(*self.departure_field).click()

    def write_departure_station(self, origin_city):
        self.driver.find_element(*self.departure_station).send_keys(origin_city)

    def write_destination_station(self, destination_city):
        self.driver.find_element(*self.return_station).send_keys(destination_city)

    def click_depart_calendar(self):
        self.driver.find_element(*self.departure_calendar).click()

    def click_return_calendar(self):
        self.driver.find_element(*self.return_calendar).click()

    def click_right_arrow(self):
        self.driver.find_element(*self.right_arrow).click()

    def select_depart_month(self, depart_month):
        wait = WebDriverWait(self.driver, 5)
        current_month = wait.until(EC.visibility_of_element_located(self.month_locator))

        month_text = current_month.get_attribute('text')
        current_month = month_text.split(' ')[0]

        while current_month != depart_month:
            self.click_right_arrow()

            current_month = self.driver.find_element(*self.month_locator)
            month_text = current_month.get_attribute('text')
            current_month = month_text.split(' ')[0]

    def select_return_month(self, return_month):
        wait = WebDriverWait(self.driver, 5)
        current_month = wait.until(EC.visibility_of_element_located(self.month_locator))

        month_text = current_month.get_attribute('text')
        current_month = month_text.split('')[0]

        while current_month != return_month:
            self.click_right_arrow()

            current_month = self.driver.find_element(*self.month_locator)
            month_text = current_month.get_attribute('text')
            current_month = month_text.split(' ')[0]

    def select_depart_day(self, depart_day):
        self.driver.find_element(*depart_day).click()

    def select_return_day(self, return_day):
        self.driver.find_element(*return_day).click()


    #Steps:

    def set_origin_city(self, origin_city):
        self.click_departure_field()
        self.write_departure_station(origin_city)

    def set_destination_city(self, destination_city):
        self.write_destination_station(destination_city)

    def set_depart_date(self, depart_month, depart_day):
        self.click_depart_calendar()
        self.select_depart_month(depart_month)
        self.select_depart_day(depart_day)

    def set_return_date(self, return_month, return_day):
        self.click_return_calendar()
        self.select_return_month(return_month)
        self.select_return_day(return_day)















