from services import driver, helpers as hp
import time, random as rn
from components import login, loader, structure, profile, navbar, home ,errors as ers
from selenium.webdriver.common.keys import Keys


class General:

    def __init__(self, user_id: str):
        self._login_form = login.LoginForm(user_id)
        self._accounts = self._login_form.accounts()
        self._profile = profile.Account()
        self._timeframes = [0.25, 0.30, 0.34, 0.35, 0.40, 0.45, 0.50, 0.55]
        self._navbar = navbar.Menu()
        self._home = home.Home()
        self._timeout = ers.Timedouts()
        self._logged_accounts = []
        self._preempted = False

    def is_preempted(self) -> bool:
        return self._preempted
    
    def preempt(self, flag: bool) -> bool:
        self._preempted = flag
    
    def logged_accounts(self):
        return self._logged_accounts

    def user_accounts(self):
        return self._accounts
    
    def reload_page(self):
        while self._setup(use_base_url=False) is None:
            if hp.stop_on_command():
                raise Exception('...')
            print("Unable to connect to {}, please check your internet connection... ".format(
                driver.Driver.get().current_url))
            time.sleep(5)
            print('Reconnecting to the internet...')
        print('Connection established! Html loaded successfully!')
        return self.watch_loader()

    def switch_tab(self, index: int):
        driver.Driver.get().switch_to.window(driver.Driver.get().window_handles[index])

    def close_tab(self):
        driver.Driver.get().close()

    def get_navbar(self):
        return self._navbar

    def scroll_down(self):
        if self.watch_loader():
            driver.Driver.get_brew()\
                  .find_element(driver.Driver.get(), tag_name='html')\
                  .send_keys(Keys.END)
        
    def _setup(self, use_base_url=True):
        try:
            dv = driver.Driver.set().get()
            dv.get(structure.Struct.get_url() if use_base_url else dv.current_url)
            flag = driver.Driver.get()
            if self._home.app() is None:
                flag = None
        except:
            flag = None
        return flag

    def browse(self):
        while self._setup() is None:
            if hp.stop_on_command():
                raise Exception('...')
            print("Unable to connect to {}, please check your internet connection... ".format(
                structure.Struct.get_url()))
            time.sleep(5)
            print('Reconnecting to the internet...')
        print('Connection established! Html loaded successfully!')
        return True

    def watch_loader(self) -> bool:
        print('Loading HTML...')
        ldr = loader.Loader()
        time.sleep(.52)
        while (ldr.big() is not None) or (ldr.small() is not None):
            time.sleep(.15)
        print('HTML loaded!')
        self.watch_timed_out()
        return True
    
    def watch_timed_out(self):
        while self._timeout.timeout() is not None:
            print('Network timed out, refreshing HTML...')
            self._timeout.timeout().click()
            time.sleep(1.5)
            self.watch_loader()

    def bot_login(self, username: str, password: str):
        print(f'Logging in into account with username: {username}...')
        time.sleep(rn.choice(self._timeframes))
        ui = self._login_form.username_input()
        ui.click()
        ui.send_keys(username)
        time.sleep(rn.choice(self._timeframes))
        pi = self._login_form.password_input()
        pi.click()
        pi.send_keys(password)
        time.sleep(rn.choice(self._timeframes))
        self._login_form.login_button().click()
    
    def clear_login_form(self):
        print('Clearing login form...')
        time.sleep(rn.choice(self._timeframes))
        ui = self._login_form.username_input()
        ui.click()
        ui.send_keys(Keys.CONTROL+'a')
        ui.send_keys(Keys.BACK_SPACE)
        time.sleep(rn.choice(self._timeframes))
        pi = self._login_form.password_input()
        pi.click()
        pi.send_keys(Keys.CONTROL+'a')
        pi.send_keys(Keys.BACK_SPACE)
        time.sleep(rn.choice(self._timeframes))
    
    def login_form_exists(self):
        return (self._login_form.username_input() is not None) and (self._login_form.password_input() is not None)\
                and (self._login_form.login_button() is not None)

    def nav_bar_exists(self):
        return (self._navbar.profile_link() is not None) and (self._navbar.home_link() is not None)\
            and (self._navbar.member_link() is not None) and (self._navbar.task_link() is not None)\
            and (self._navbar.record_link() is not None)
    
    def at_home(self):
        return (self._home.facebook_link() is not None) and (self._home.tiktok_link() is not None)
    
    def bot_logout(self):
        self.scroll_down()
        self._navbar.profile_link().click()
        print('Logging out...')
        if self.watch_loader():
            self.scroll_down()
            self.watch_loader()
            self._profile.logout_link().click()
            print('Logged out successfully!')



