from requests import get
from requests import utils
from datetime import datetime


def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encoding_s = utils.get_encoding_from_headers(response.headers)
    text = response.content.decode(encoding=encoding_s)
    spl_text = text.split('<Valute')
    rates = 0
    for curr_line in spl_text:
        if currency.upper() in curr_line:
            rates_str = (curr_line[(curr_line.find('<Value>') + 7):(curr_line.find('</Value>'))])
            rates = float(rates_str.replace(',', '.'))
            break
        else:
            rates = 'None'
    date_line = spl_text[0]
    cur_date = datetime.strptime(date_line[(date_line.find('Date') + 6):(date_line.find('Date') + 16)], '%d.%m.%Y').date()
    print(cur_date, currency.upper(), rates)


if __name__ == '__main__':
    currency_rates(input('Введите код валюты (USD, EUR, CZK и т.д): '))
