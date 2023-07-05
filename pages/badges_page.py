from selene import by, be
from selene.support.shared.jquery_style import s, ss

from asserts.attributes_checks import check_element_visibility_by_class_name
from pages.base_page import BasePage


class BadgesPage(BasePage):

    def __init__(self):
        super().__init__('https://jdi-testing.github.io/jdi-light/vuetify')
        super().load()
        self.navigate_to_badges()

    @staticmethod
    def is_badge_present(badge_name):
        assert check_element_visibility_by_class_name(badge_name)
