import time

from get_data import personal_data, get_address, get_telephone
import json


class GeneratePeople:
    def __init__(self, dados_pessoais='', endereco='', telefone=''):
        self.dados_pessoais = personal_data(dados_pessoais)
        self.endereco = get_address(endereco)
        self.telefone = get_telephone(telefone)

    def text_format(self):
        print('𝐁𝐮𝐬𝐜𝐚𝐧𝐝𝐨 𝐃𝐚𝐝𝐨𝐬...')
        time.sleep(5)
        return f'''
        Dados Pessoais
        ------------------------------
            Nome: {self.dados_pessoais[0]}
            Cpf: {self.dados_pessoais[1]}
            Rg: {self.dados_pessoais[2]}
            Data_Nasci: {self.dados_pessoais[3]}
            Idade: {self.dados_pessoais[4]}

        Endereço
        ------------------------------
            Cep: {self.endereco[0]}
            Endereco: {self.endereco[1]}
            Numero: {self.endereco[2]}
            Bairro: {self.endereco[3]}
            Cidade: {self.endereco[4]}
            Estado: {self.endereco[5]}

        Telefone
        ------------------------------
            Fixo: {self.telefone[0]}
            Cel: {self.telefone[1]}
            mail: {self.telefone[2]}'''

    def json_format(self):
        dictionary = {
            "nome": self.dados_pessoais[0],
            "Cpf": self.dados_pessoais[1],
            "Rg": self.dados_pessoais[2],
            "Data_Nasci": self.dados_pessoais[3],
            "Idade": self.dados_pessoais[4],

            "Cep": self.endereco[0],
            "Endereco": self.endereco[1],
            "Numero": self.endereco[2],
            "Bairro": self.endereco[3],
            "Cidade": self.endereco[4],
            "Estado": self.endereco[5],

            "Fixo": self.telefone[0],
            "Cel": self.telefone[1],
            "mail": self.telefone[2]
        }
        json_object = json.dumps(dictionary, indent=4)
        print('𝐁𝐮𝐬𝐜𝐚𝐧𝐝𝐨 𝐃𝐚𝐝𝐨𝐬...')
        time.sleep(5)
        return json_object


d = GeneratePeople()
print(d.json_format())
