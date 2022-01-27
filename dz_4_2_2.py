from requests import get
from requests import utils


def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encoding_s = utils.get_encoding_from_headers(response.headers)
    text = response.content.decode(encoding=encoding_s)
    spl_text = text.split('<Valute')
    rates_d = 0
    for curr_line in spl_text:
        if currency.upper() in curr_line:
            rates_str = (curr_line[(curr_line.find('<Value>') + 7):(curr_line.find('</Value>'))])
            rates_d = float(rates_str.replace(',', '.'))
            break
        else:
            rates_d = 'None'
    print(currency.upper(), rates_d)


currency_rates(input('Введите код валюты (USD, EUR, CZK и т.д): '))
