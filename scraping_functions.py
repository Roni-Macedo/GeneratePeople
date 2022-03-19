from random import choice
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unidecode


def man_woman():
    f = 'http://www.geradordepessoas.com.br/gerador-de-pessoas?sexo=feminino&formatacao=sim'
    m = 'http://www.geradordepessoas.com.br/gerador-de-pessoas?sexo=masculino&formatacao=sim'
    random = [f, m]
    generate = input('Feminino[f] masculino[m]: ')
    if generate == 'f':
        return f
    elif generate == 'm':
        return m
    elif generate == '':
        print('is random')
        return choice(random)
    else:
        return 'Opçao invalida'


def scraping(http):
    url = urlopen(http)
    soup = BeautifulSoup(url.read(), "html.parser")
    return soup


def get_tag(resp):
    data_list = []
    list_tag = resp.find_all('input')
    for data in list_tag:
        # unidecode.unidecode(x) tira os acentos.
        data_list.append(unidecode.unidecode(data.get('value')))
    return data_list
