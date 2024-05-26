from selenium.webdriver.common.by import By


class Locators:
    # Locators for Login
    # userName = (By.ID, 'user-name')
    # password = (By.ID, 'password')
    # submitButton = (By.ID, 'login-button')
    # swagLabsText = By.XPATH, '//div[@class ="app_logo"]'
    # burgerMenu = By.ID, 'react-burger-menu-btn'
    # logoutButton = By.ID, 'logout_sidebar_link'
    # userName1 = (By.ID, 'user-name')
    # password1 = (By.ID, 'password')
    # TextMessage = By.XPATH, '//h3'
    # userName2 = (By.ID, 'user-name')
    # password2 = (By.ID, 'password')

    # Locators for Registration
    # firstName = By.XPATH, '(//input[@placeholder= "First Name"])'
    # lastName = By.XPATH, '(//input[@placeholder= "Last Name"])'
    # address = By.XPATH, '//textarea[@ng-model="Adress"]'
    # emailAddress = By.XPATH, '//input[@type="email"]'
    # phone = By.XPATH, '(//input[@type="tel"])'
    # maleRadioButton = By.XPATH, '(//input[@name="radiooptions"])[1]'
    # feMaleRadioButton = By.XPATH, '(//input[@name="radiooptions"])[2]'
    #
    # cricket = By.ID, 'checkbox1'
    # movies = By.ID, 'checkbox2'
    # hockey = By.ID, 'checkbox3'
    #
    # language_dropdown = By.ID, 'msdd'
    # arabic = By.XPATH, '(//li[@class="ng-scope"])[1]'
    # languageText = By.XPATH, '//label[text()="Languages"]'
    #
    # skills = By.ID, 'Skills'
    # first_password = By.XPATH, '//input[@id = "firstpassword"]'
    # confirm_password = By.XPATH, '//input[@id = "secondpassword"]'
    # photo = By.XPATH, '//input[@id="imagesrc"]'
    #
    # year = By.ID, 'yearbox'
    # month = By.XPATH, '//select[@ng-model="monthbox"]'
    # day = By.ID, 'daybox'

    # Autocomplete Page
    autocomplete = By.XPATH, '//a[@class="btn btn-lg" and @href="/autocomplete"]'
    Address = By.XPATH, '//input[@placeholder = "Enter address"]'
    OK_Button = By.XPATH, '//button[@class = "dismissButton"]'
    Street_address = By.XPATH, '//input[@id="street_number"]'
    Street_address2 = By.XPATH, '//input[@id="route"]'
    city = By.XPATH, '//input[@id = "locality"]'
    state = By.XPATH, '//input[@id = "administrative_area_level_1"]'
    zip_code = By.XPATH, '//input[@id = "postal_code"]'
    country = By.XPATH, '//input[@id = "country"]'

    # Buttons Page
    buttons = By.XPATH, '//a[@class = "btn btn-lg" and @href = "/buttons" ]'
    Primary_Button = By.XPATH, '//button[@class="btn btn-lg btn-primary"]'
    Success_Button = By.XPATH, '//button[@class="btn btn-lg btn-success"]'
    Info_Button = By.XPATH, '//button[@class="btn btn-lg btn-info"]'
    Warning_Button = By.XPATH, '//button[@class="btn btn-lg btn-warning"]'
    Danger_Button = By.XPATH, '//button[@class="btn btn-lg btn-danger"]'
    Link_Button = By.XPATH, '//button[@class="btn btn-lg btn-link"]'
    Left_Button = By.XPATH, '//button[text()="Left"]'
    Middle_Button = By.XPATH, '//button[text()="Middle"]'
    Right_Button = By.XPATH, '//button[text()="Right"]'
    One_Button = By.XPATH, '//button[text() = 1]'
    Two_Button = By.XPATH, '//button[text() = 2]'
    Dropdown = By.XPATH, '//button[@id = "btnGroupDrop1"]'
    Dropdown_Link1 = By.XPATH, '//a[text()="Dropdown link 1"]'
    Dropdown_Link2 = By.XPATH, '//a[text()="Dropdown link 2"]'

    # Check Box Page
    checkbox = By.XPATH, '//a[@class = "btn btn-lg" and @href = "/checkbox" ]'
    checkbox1 = By.ID, "checkbox-1"
    checkbox2 = By.ID, "checkbox-2"
    checkbox3 = By.ID, "checkbox-3"

    # Datepicker
    datepicker = By.XPATH, '//a[@class = "btn btn-lg" and @href = "/datepicker" ]'
    datepicker1 = By.XPATH, '//input[@id = "datepicker"]'
    datepicker2 = By.XPATH, '//td[@class="today active day" and text()="26"]'
