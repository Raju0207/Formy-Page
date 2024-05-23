class Base_Page():

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)

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
