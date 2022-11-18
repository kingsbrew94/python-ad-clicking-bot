from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from libs import brew as bw
import time

OS_USER = 'YOUR OS USER HERE'
class Driver:
    _driver = None
    _profile = None
    _capabilities = None

    @staticmethod
    def _security_settings():
        profile_path = "C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\7ywco37d.default".format(OS_USER)
        Driver._profile = webdriver.FirefoxProfile(profile_path)
        PROXY_HOST = "12.12.12.123"
        PROXY_PORT = "1234"
        PROXY_TYPE = 1
        Driver._profile.set_preference("network.proxy.type", PROXY_TYPE)
        Driver._profile.set_preference("network.proxy.http", PROXY_HOST)
        Driver._profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
        Driver._profile.set_preference("dom.webdriver.enabled", False)
        Driver._profile.set_preference('useAutomationExtension', False)
        Driver._profile.update_preferences()
        Driver._capabilities = DesiredCapabilities.FIREFOX

    @staticmethod
    def _launch_browser():
        Driver._security_settings()
        browser = webdriver.Firefox(firefox_profile=Driver._profile, desired_capabilities=Driver._capabilities)
        time.sleep(5)

        while len(browser.window_handles) > 1:
            browser.switch_to.window(browser.window_handles[-1])
            browser.close()
            time.sleep(0.5)
        browser.switch_to.window(browser.window_handles[0])

        return browser

    @staticmethod
    def set() -> object:
        try:
            Driver._driver = Driver._launch_browser() if Driver._driver is None else Driver._driver
            Driver.get().window_handles[0]

        except Exception as ex:
            print(ex)
            time.sleep(5)
            Driver._driver = Driver._launch_browser()
        return Driver

    @staticmethod
    def get() -> object:
        return Driver._driver

    @staticmethod
    def get_brew():
        return bw
