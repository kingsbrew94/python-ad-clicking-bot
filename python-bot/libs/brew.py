import re, time

re: object = re


def re_search(pattern: str, search_text: str, flags: int = None, pos: int = None, endpos: int = None) -> object:
    if flags is None:
        if (pos is not None) and (endpos is not None):
            return re.compile(pattern).search(search_text, pos, endpos)
        return re.compile(pattern).search(search_text)
    if (pos is not None) and (endpos is not None):
        return re.compile(pattern, flags).search(search_text, pos, endpos)
    return re.compile(pattern, flags).search(search_text)


def re_search_all(pattern: str, search_text: str, flags: int = None, pos: int = None, endpos: int = None) -> list:
    if flags is None:
        if (pos is not None) and (endpos is not None):
            return re.compile(pattern).findall(search_text, pos, endpos)
        return re.compile(pattern).match(search_text)
    if (pos is not None) and (endpos is not None):
        return re.compile(pattern, flags).findall(search_text, pos, endpos)
    return re.compile(pattern, flags).findall(search_text)


def re_match(pattern: str, search_text: str, flags: int = None, pos: int = None, endpos: int = None) -> object:
    if flags is None:
        if (pos is not None) and (endpos is not None):
            return re.compile(pattern).match(search_text, pos, endpos)
        return re.compile(pattern).match(search_text)
    if (pos is not None) and (endpos is not None):
        return re.compile(pattern, flags).match(search_text, pos, endpos)
    return re.compile(pattern, flags).match(search_text)


def set_time_interval(callback, interval: float = 0.0):
    while True:
        time.sleep(interval)
        flag = callback()
        if not flag:
            break


def heart_beat(Bot, data, before_interval: float = 0.0, after_interval: float = 0.0):
    while True:
        time.sleep(before_interval)
        bot = Bot(data)
        flag: bool = bot.activity()
        if flag == False or flag == -1:
            break
        time.sleep(after_interval)
    return Bot


def find_element(browser, id_name: str = None, class_name: str = None, tag_name: str = None,
                 css_selector: str = None, text: str = None):
    element = None
    try:
        if (id_name is not None) and (type(id_name) == str):
            element = browser.find_element_by_id(id_name)
        elif (class_name is not None) and (type(class_name) == str):
            element = browser.find_element_by_class_name(class_name)
        elif (tag_name is not None) and (type(tag_name) == str):
            element = browser.find_element_by_tag_name(tag_name)
        elif (css_selector is not None) and (type(css_selector) == str):
            element = browser.find_element_by_css_selector(css_selector)
        elif (text is not None) and (type(text) == str):
            element = browser.find_element_by_link_text(text)
    except:
        element = None
    return element


def find_elements(browser, id_name: str = None, class_name: str = None, tag_name: str = None,
                  css_selector: str = None, text: str=None):
    element = None
    try:
        if (id_name is not None) and (type(id_name) == str):
            element = browser.find_elements_by_id(id_name)
        elif (class_name is not None) and (type(class_name) == str):
            element = browser.find_elements_by_class_name(class_name)
        elif (tag_name is not None) and (type(tag_name) == str):
            element = browser.find_elements_by_tag_name(tag_name)
        elif (css_selector is not None) and (type(css_selector) == str):
            element = browser.find_elements_by_css_selector(css_selector)
        elif (text is not None) and (type(text) == str):
            element = browser.find_elements_by_link_text(text)

    except:
        element = None
    return element
