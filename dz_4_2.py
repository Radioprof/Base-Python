from requests import get
from requests import utils


def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encoding_s = utils.get_encoding_from_headers(response.headers)
    text = response.content.decode(encoding=encoding_s)
    # spl_text = text.split('<Valute>')
    curr_flag = text.find(currency.upper())
    if curr_flag != -1:
        rates_str = (text[(text.find('<Value>', curr_flag) + 7):(text.find('</Value>', curr_flag))])
        rates = float(rates_str.replace(',', '.'))
        print(currency.upper(), rates)
    else:
        print('None')


currency_rates(input('Введите код валюты (USD, EUR, CZK и т.д): '))
