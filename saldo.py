# coding=UTF-8
from StringIO import StringIO
import os
import sys
import tempfile
import re

from bs4 import BeautifulSoup
from PIL import Image
import requests


POST_URL = 'https://sodexosaldocartao.com.br/saldocartao/consultaSaldo.do?operation=consult'
CAPTCHA_URL = 'https://sodexosaldocartao.com.br/saldocartao/jcaptcha.do'

def parse_html(html):
    soup = BeautifulSoup(html)
    parsed_amount = __parse_amount(soup)
    parsed_schedule = __parse_schedule(soup)

    amount_output = 'Saldo: ' + parsed_amount
    schedule_output = 'Proxima regarga: ' + parsed_schedule

    return __decorate_output(amount_output, schedule_output)

def get_captcha(session):
    r = session.get(CAPTCHA_URL)
    return Image.open(StringIO(r.content))

def post_card(session, card_number, cpf, captcha_text):
    post_data = {
        'service': '5;1;6',
        'cardNumber': card_number,
        'cpf': cpf,
        'jcaptcha_response': captcha_text,
        'x': '6',
        'y': '9',
    }

    r = session.post(POST_URL, params=post_data)

    return r.content


def get_balance(card_number, cpf):
    session = requests.Session()

    captcha_image = get_captcha(session)

    # TODO: Automate the captcha
    captcha_image.show()
    captcha_text = raw_input("CAPTCHA:")

    return parse_html(post_card(session, card_number, cpf, captcha_text))

def __parse_amount(soup):
    result = soup.find(id='balance')

    if result:
        extracted_amount = re.search('R\$\s[0-9\.]+', result.var.string)
        return extracted_amount.group(0).decode('utf-8')

    return 'Não foi possível verificar o saldo. Possíves razões: captcha inválido ou alteração no DOM da página'

def __parse_schedule(soup):
    result = soup.find('tr', class_='credito')

    if result:
        date = result.find('td')
        amount = date.find_next('td')
        return date.get_text() + ' no valor de R$ ' + amount.get_text()

    return 'N/A'

def __decorate_output(amount_output, schedule_output):
    SEPARATOR = '\n-------------\n'
    return SEPARATOR + amount_output + SEPARATOR + schedule_output + SEPARATOR

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, 'usage: ' + sys.argv[0] + ' card_number cpf'
        sys.exit(1)

    print get_balance(*sys.argv[1:])
