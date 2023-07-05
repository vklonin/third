from selene import by, be
from selene.support.shared.jquery_style import s


def check_element_visibility_by_class_name(element_class_name):
    s(by.class_name(element_class_name)).should(be.visible)
    return True
