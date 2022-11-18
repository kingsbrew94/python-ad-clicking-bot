import requests, datetime
from datetime import date

url = 'http://localhost/control-service/sango'

# sango stop
def _get_request(endpoint: str) -> object:
    try:
        res = requests.get(endpoint)

        return res.text
    except Exception as ex:
        print(ex)
        return None

print(_get_request('{}/{}?LOGS={}&DATE={}'.format(url, 'logExists','realkb7', date.today())))