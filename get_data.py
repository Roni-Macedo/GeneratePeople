from scraping_functions import man_woman, scraping, get_tag


http = man_woman()
resp = scraping(http)
lista = get_tag(resp)


def personal_data(dados):
    nome = lista[5]
    cpf = lista[6]
    rg = lista[7]
    data = lista[8]
    ano = 2022  # passar o ano atual
    ncm = data[-4:]
    idade = ano - int(ncm)
    return nome, cpf, rg, data, idade


def get_address(endereco):
    cep = lista[11]
    rua = lista[12]
    num = lista[13]
    bairro = lista[14]
    cidade = lista[15]
    estado = lista[16]
    return cep, rua, num, bairro, cidade, estado


def get_telephone(tel):
    fixo = lista[17]
    cel = lista[18]
    mail = lista[9]
    return fixo, cel, mail
