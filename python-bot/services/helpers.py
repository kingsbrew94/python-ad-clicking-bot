import json, requests, pyperclip
from datetime import datetime
from services import driver

url = 'http://localhost/control-service/sango'

def _get_request(endpoint: str) -> object:
    try:
        res = requests.get(endpoint)
        res = json.loads(res.text)
        return res['payload'] if res['state'] else []
    except Exception as ex:
        print(ex)
        return None


def get_meta_data() -> object:
    return _get_request('{}/{}'.format(url, 'getMetadata'))


def get_account_info(user_id: str) -> object:
    return _get_request('{}/{}?userId={}'.format(url, 'getAccounts', user_id))


def log_exists(logs: str, date: str) -> object:
    return _get_request('{}/{}?LOGS={}&DATE={}'.format(url, 'logExists', logs, date))

def add_logs(logs: dict):
    try:
        res = requests.get('{}/{}'.format(url,'addLog'), logs)
        return json.loads(res.text)
    except Exception as ex:
        print(ex)
    return None

def working_time():
    dat = datetime.today()
    hour = int(str(dat).split(' ')[1].strip().split(':')[0].strip())
    return (hour >= 2) and (hour <= 22)

def resting_time():
    dat = datetime.today()
    hour = int(str(dat).split(' ')[1].strip().split(':')[0].strip())
    return (hour >= 23) or (hour < 1)

def stop_on_command():
    pivot = str(pyperclip.paste()).replace(' ', '').strip().upper()
    return pivot == 'SANGOSTOP'

def start_on_command():
    pivot = str(pyperclip.paste()).replace(' ', '').strip().upper()
    return pivot == 'SANGOSTART'

def safe_close_tab():
    try:
        driver.Driver.get().close()
    except:
        pass
    
