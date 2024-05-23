import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Base_Page
from locators.locators import Locators


# from validate_email import validate_email


class Formy_Page(Base_Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = Locators

    # Autocomplete Page
    def enter_address(self, address):
        self.enter_at(self.locator.Address, address)

    def enter_street_address(self, streetaddress):
        self.enter_at(self.locator.Street_address, streetaddress)

    def enter_street_address2(self, streetaddress2):
        self.enter_at(self.locator.Street_address2, streetaddress2)

    def enter_city(self, city):
        self.enter_at(self.locator.city, city)

    def enter_state(self, state):
        self.enter_at(self.locator.state, state)

    def enter_zip_code(self, zipcode):
        self.enter_at(self.locator.zip_code, zipcode)

    def enter_country(self, country):
        self.enter_at(self.locator.country, country)

    def select_autocomplete(self):
        self.click_element(self.locator.autocomplete)

    # Buttons Page
    def select_buttons(self):
        self.click_element(self.locator.buttons)

    def select_primary(self):
        self.click_element(self.locator.Primary_Button)

    def select_success(self):
        self.click_element(self.locator.Success_Button)

    def select_info(self):
        self.click_element(self.locator.Info_Button)

    def select_warning(self):
        self.click_element(self.locator.Warning_Button)

    def select_danger(self):
        self.click_element(self.locator.Danger_Button)

    def select_link(self):
        self.click_element(self.locator.Link_Button)

    def select_left(self):
        self.click_element(self.locator.Left_Button)

    def select_middle(self):
        self.click_element(self.locator.Middle_Button)

    def select_right(self):
        self.click_element(self.locator.Right_Button)

    def select_1button(self):
        self.click_element(self.locator.One_Button)

    def select_2button(self):
        self.click_element(self.locator.Success_Button)

    def select_dropdown(self):
        self.click_element(self.locator.Dropdown)

    def select_dropdown_link1(self):
        self.click_element(self.locator.Dropdown_Link1)

    def select_dropdown_link2(self):
        self.click_element(self.locator.Dropdown_Link2)

    # def is_valid_email(self):
    #     return validate_email(self)
    #
    # email = "example@example.com"
    # if is_valid_email(email):
    #     print("Valid email address")
    # else:
    #     print("Invalid email address")

    def select_male(self):
        self.click_element(self.locator.maleRadioButton)

    def select_female(self):
        self.click_element(self.locator.feMaleRadioButton)

    def is_male_radio_button_selected(self):
        return self.is_selected(self.locator.maleRadioButton)

    def is_female_radio_button_selected(self):
        return self.is_selected(self.locator.feMaleRadioButton)

    def select_cricket(self):
        self.click_element(self.locator.cricket)

    def is_cricket_checkbox_selected(self):
        return self.is_selected(self.locator.cricket)

    def select_movies(self):
        self.click_element(self.locator.movies)

    def is_movies_checkbox_selected(self):
        return self.is_selected(self.locator.movies)

    def select_hockey(self):
        self.click_element(self.locator.hockey)

    def is_hockey_checkbox_selected(self):
        return self.is_selected(self.locator.hockey)

    def select_language(self):
        self.click_element(self.locator.language_dropdown)
        time.sleep(1)
        self.click_element(self.locator.arabic)
        time.sleep(1)
        self.click_element(self.locator.languageText)
        time.sleep(1)

    def select_skills(self):
        # element = self.get_element(self.locator.skills)
        select = Select(self.get_element(self.locator.skills))
        # select.select_by_index(1)
        # select.select_by_value("Analytics")
        select.select_by_visible_text("Android")

    def upload_photo(self):
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "image/photo.jpg"))
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        file_input = self.get_element(self.locator.photo)
        action = ActionChains(self.driver)
        action.scroll_to_element(file_input).perform()
        file_input.send_keys(upload_file)

    def select_year(self):
        select = Select(self.get_element(self.locator.year))
        select.select_by_value('2000')

    def select_month(self):
        select = Select(self.get_element(self.locator.month))
        select.select_by_value('April')

    def select_day(self):
        select = Select(self.get_element(self.locator.day))
        select.select_by_value('20')

