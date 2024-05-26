import time
from tests.base_test import Base_Test
# from pages.registration_page import Registration_Page
from pages.formy_page import Formy_Page
from testdata.data import Data


class Formy_Test(Base_Test):
    def test_formy_autocomplete_data(self):
        acp = Formy_Page(self.driver)
        # Autocomplete Page
        acp.select_autocomplete()
        time.sleep(2)
        acp.enter_address(Data.ADDRESS)
        time.sleep(2)
        acp.select_ok_button()
        time.sleep(2)
        acp.enter_street_address(Data.STREETADDRESS)
        time.sleep(2)
        acp.enter_street_address2(Data.STREETADDRESS2)
        time.sleep(2)
        acp.enter_city(Data.CITY)
        time.sleep(2)
        acp.enter_state(Data.STATE)
        time.sleep(2)
        acp.enter_zip_code(Data.ZIPCODE)
        time.sleep(2)
        acp.enter_country(Data.COUNTRY)
        time.sleep(2)

        # Buttons Page

    def test_formy_buttons(self):
        bp = Formy_Page(self.driver)
        bp.select_buttons()
        time.sleep(2)
        bp.select_primary()
        time.sleep(2)
        bp.select_success()
        time.sleep(2)
        bp.select_info()
        time.sleep(2)
        bp.select_warning()
        time.sleep(2)
        bp.select_danger()
        time.sleep(2)
        bp.select_link()
        time.sleep(2)
        bp.select_left()
        time.sleep(2)
        bp.select_middle()
        time.sleep(2)
        bp.select_right()
        time.sleep(2)
        bp.select_1button()
        time.sleep(2)
        bp.select_2button()
        time.sleep(2)
        bp.select_dropdown()
        time.sleep(2)
        bp.select_dropdown_link1()
        time.sleep(2)
        bp.select_dropdown_link2()
        time.sleep(2)

        # CheckBox

    def test_formy_checkbox(self):
        cbp = Formy_Page(self.driver)
        cbp.select_checkbox()
        time.sleep(2)
        print(f"Should: False ==== {cbp.is_checkbox1_checkbox_selected()}")
        cbp.select_checkbox1()
        print(f"Should: True ==== {cbp.is_checkbox1_checkbox_selected()}")
        time.sleep(2)
        print(f"Should: False ==== {cbp.is_checkbox2_checkbox_selected()}")
        cbp.select_checkbox2()
        print(f"Should: True ==== {cbp.is_checkbox2_checkbox_selected()}")
        time.sleep(2)
        print(f"Should: False ==== {cbp.is_checkbox3_checkbox_selected()}")
        cbp.select_checkbox3()
        print(f"Should: True ==== {cbp.is_checkbox3_checkbox_selected()}")
        time.sleep(2)

    def test_formy_datepicker(self):
        dp = Formy_Page(self.driver)
        dp.select_datepicker()
        time.sleep(2)
        dp.select_datepicker_textbox()
        time.sleep(2)
        dp.select_current_date()
        time.sleep(2)

    def test_drag_and_drop(self):
        dd = Formy_Page(self.driver)
        time.sleep(2)
        dd.click_drag_and_drop_button()
        time.sleep(2)
        # dd.switch_to_iframe_for_drag_and_drop()
        time.sleep(2)
        dd.drag_and_drop()
        time.sleep(5)
