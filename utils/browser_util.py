from selene import browser


def configure_browser(url, timeout):
    browser.config.base_url = url
    browser.config.timeout = timeout
