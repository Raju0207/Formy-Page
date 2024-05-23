import time
from tests.base_test import Base_Test
# from pages.registration_page import Registration_Page
from pages.formy_page import Formy_Page
from testdata.data import Data


class Formy_Test(Base_Test):
    def test_formy_autocomplete_data(self):
        acp = Formy_Page(self.driver)

        # Autocomplete
        acp.select_autocomplete()
        time.sleep(2)
        acp.enter_address(Data.ADDRESS)
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

        # Buttons

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
