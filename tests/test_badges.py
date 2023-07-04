import allure
import pytest
from pages.badges_page import BadgesPage
from utils.logger import get_logger
from data.test_data import test_data


@allure.feature('Badges present')
@allure.story('Badges')
@pytest.mark.parametrize('badge, expected', test_data)
def test_badges(badge, expected):
    logger = get_logger('TestBadges')
    page = BadgesPage()
    assert page.is_badge_present(badge)

    logger.info(f"Badge '{badge}' is present.")
