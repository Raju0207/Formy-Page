import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators


class Base_Page():

    def __init__(self, driver):
        self.locator = Locators
        self.driver = driver

    def get_element(self, locator):
        # return self.driver.find_element(*locator)
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        self.get_element(locator).click()

    def enter_at(self, locator, data):
        self.get_element(locator).send_keys(data)

    def get_text(self, locator):
        text = self.get_element(locator).text
        return text

    def is_enabled(self, locator):
        return self.get_element(locator).is_enabled()

    def is_selected(self, locator):
        return self.get_element(locator).is_selected()

    def perform_drag_and_drop(self, source_location, destination_location):
        action = ActionChains(self.driver)
        drag = self.get_element(source_location)
        drop = self.get_element(destination_location)
        action.drag_and_drop(drag, drop).perform()

    def switch_to_iframe(self, locator):
        self.driver.switch_to.frame(self.get_element(locator))
