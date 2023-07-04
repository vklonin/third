from selene import by
from utils.browser_util import configure_browser, browser


class BasePage:

    def __init__(self, url):
        configure_browser(url, 2)
        self.browser = browser
        self.url = url
        self.badges_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/badges"]'))
        self.buttons_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/buttons"]'))
        self.buttons_toggle_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/buttons_toggle"]'))
        self.chips_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/chips"]'))
        self.icons_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/icons"]'))
        self.progress_bar_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/progress_bar"]'))
        self.progress_spinner_link = self.browser.element(
            by.xpath('//a[@href="/jdi-light/vuetify/#/progress_spinner"]'))
        self.ripple_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/ripple"]'))
        self.paginator_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/paginator"]'))
        self.sort_header_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/sort_header"]'))
        self.tables_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/tables"]'))
        self.autocompletes_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/autocompletes"]'))
        self.checkbox_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/checkbox"]'))
        self.datepicker_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/datepicker"]'))
        self.form_field_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/form_field"]'))
        self.input_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/input"]'))
        self.radio_button_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/radio_button"]'))
        self.select_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/select"]'))
        self.slide_toggle_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/slide_toggle"]'))
        self.slider_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/slider"]'))
        self.card_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/card"]'))
        self.divider_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/divider"]'))
        self.panel_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/panel"]'))
        self.grid_list_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/grid_list"]'))
        self.list_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/list"]'))
        self.stepper_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/stepper"]'))
        self.tab_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/tab"]'))
        self.tree_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/tree"]'))
        self.menu_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/menu"]'))
        self.toolbar_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/toolbar"]'))
        self.sidenav_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/sidenav"]'))
        self.bottom_sheet_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/bottom_sheet"]'))
        self.dialog_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/dialog"]'))
        self.snack_bar_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/snack_bar"]'))
        self.tooltip_link = self.browser.element(by.xpath('//a[@href="/jdi-light/vuetify/#/tooltip"]'))

    def load(self):
        browser.open(self.url)

    def navigate_to_badges(self):
        self.badges_link.click()
