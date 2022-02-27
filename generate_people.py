from get_data import personal_data, get_address, get_telephone


class GeneratePeople:
    def __init__(self, dados_pessoais='', endereco='', telefone=''):
        self.dados_pessoais = personal_data(dados_pessoais)
        self.endereco = get_address(endereco)
        self.telefone = get_telephone(telefone)

    def text_format(self):
        return f'''
        Dados Pessoais
        ------------------------------
            Nome: {self.dados_pessoais[0]}
            CPF: {self.dados_pessoais[1]}
            RG: {self.dados_pessoais[2]}
            Data_Nasci: {self.dados_pessoais[3]}
            Idade: {self.dados_pessoais[4]}

        Endereço
        ------------------------------
            CEP: {self.endereco[0]}
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


p = GeneratePeople()

print(p.text_format())
