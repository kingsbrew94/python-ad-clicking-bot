from services import driver
import re

class Page:
    
    @staticmethod
    def _test(pattern_text: str):
        return driver.Driver.get_brew().re_search(pattern_text, 
                                                  driver.Driver.get().current_url, re.IGNORECASE | re.VERBOSE)
    
    @staticmethod
    def get():
        _type = None
        if Page._test(r'[/]pages[/]login[/]index'):
            _type = 'LOGIN'
        elif Page._test(r'[/]pages[/]home[/]home'):
            _type = 'HOME'
        elif Page._test(r'[/]pages[/]task[/]home'):
            _type = 'TASK'
        elif Page._test(r'[/]pages[/]record[/]home'):
            _type = 'RECORD'
        elif Page._test(r'[/]pages[/]my[/]home'):
            _type = 'MY'
        return _type
            
        