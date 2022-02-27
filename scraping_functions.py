from urllib.request import urlopen
from bs4 import BeautifulSoup
import unidecode


def man_woman():
    f = 'http://www.geradordepessoas.com.br/gerador-de-pessoas?sexo=feminino&formatacao=sim'
    m = 'http://www.geradordepessoas.com.br/gerador-de-pessoas?sexo=masculino&formatacao=sim'
    generate = input('Feminino[f] masculino[m]: ')
    if generate == 'f':
        return f
    elif generate == 'm':
        return m
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


"""
def text_format(lista):
    data = lista
    return f'''
    Dados Pessoais
    ------------------------------
        Nome: {data[5]}
        CPF: {data[6]}
        RG: {data[7]}
        Data_Nasci: {data[8]}

    Endereço
    ------------------------------
        CEP: {data[11]}
        Endereco: {data[12]}
        Numero: {data[13]}
        Bairro: {data[14]}
        Cidade: {data[15]}
        Estado: {data[16]}

    Telefone
    ------------------------------
        Fixo: {data[17]}
        Cel: {data[18]}
        mail: {data[9]}'''
"""

"""def formato_json():
    {
        "Dados Pessoais": {
            "nome": self.dados[0],
            "cpf": self.dados[1]
        }
    }
"""
