from services import helpers as hp, driver as dv


class Struct:

    _url: str = None

    _credit: int = 0
    _level: int = 0

    def __init__(self):
        if hp.stop_on_command():
            raise Exception('...')

        self._metadata = hp.get_meta_data()
        self._accounts = None
        self._login_inputs = self._metadata['$LOGIN_INPUTS']
        self._loaders = self._metadata['$LOADERS']
        self._nav_bar = self._metadata['$NAV_BAR']
        self._home = self._metadata['$HOME']
        self._task = self._metadata['$TASK']
        self._record = self._metadata['$RECORD']
        self._my = self._metadata['$MY']
        self._errors = self._metadata['$ERRORS']
        Struct._url = self._metadata['$URL']
        Struct._level = 0

    @staticmethod
    def get_credits():
        return Struct._credit

    @staticmethod
    def set_credits(credit: int):
        Struct._credit = credit

    @staticmethod
    def get_url() -> str:
        return Struct._url

    @staticmethod
    def account_level():
        return Struct._level

    def get_element(self, selector_type: str, selector: str):
        el = None
        if selector_type == 'css':
            el = dv.Driver.get_brew().find_element(dv.Driver.get(), css_selector=selector)
        elif selector_type == 'id':
            el = dv.Driver.get_brew().find_element(dv.Driver.get(), id_name=selector)
        elif selector_type == 'tag':
            el = dv.Driver.get_brew().find_element(dv.Driver.get(), tag_name=selector)
        elif selector_type == 'class':
            el = dv.Driver.get_brew().find_element(dv.Driver.get(), class_name=selector)
        elif selector_type == 'text':
            el = dv.Driver.get_brew().find_element(dv.Driver.get(), class_name=selector)
        return el

    def get_elements(self, selector_type: str, selector: str):
        el = None
        if selector_type == 'css':
            el = dv.Driver.get_brew().find_elements(dv.Driver.get(), css_selector=selector)
        elif selector_type == 'id':
            el = dv.Driver.get_brew().find_elements(dv.Driver.get(), id_name=selector)
        elif selector_type == 'tag':
            el = dv.Driver.get_brew().find_elements(dv.Driver.get(), tag_name=selector)
        elif selector_type == 'class':
            el = dv.Driver.get_brew().find_elements(dv.Driver.get(), class_name=selector)
        elif selector_type == 'text':
            el = dv.Driver.get_brew().find_elements(dv.Driver.get(), class_name=selector)
        return el

    def search_mdt(self,collection, search_text: str):

        for cln in collection:
            if cln['$NAME'] == search_text:
                return cln
        return None

    def set_accounts(self, user_id: str):
        self._accounts = hp.get_account_info(user_id)

    def accounts(self) -> object:
        return self._accounts

    def login_inputs(self) -> object:
        return self._login_inputs

    def loaders(self) -> object:
        return self._loaders

    def errors(self) -> object:
        return self._errors
    
    def nav_bar(self) -> object:
        return self._nav_bar

    def home(self) -> object:
        return self._home

    def task(self) -> object:
        return self._task

    def record(self) -> object:
        return self._record

    def profile(self) -> object:
        return self._my
