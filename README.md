<h1 align="center">𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞-𝐏𝐞𝐨𝐩𝐥𝐞</h1>

<h4 align="center">🚧 GeneratePeople   Finalizado 🚀🚀🚀 </h4>

# AVISO ⚠

## Para fins didáticos o mau uso do **GeneratePeople** é total responsabilidade do seu utilizador.

**Todos os dados aqui gerados são aleatorios sem valor legal.**

<h2 align="center">'''𝒐 𝒄𝒐𝒏𝒉𝒆𝒄𝒊𝒎𝒆𝒏𝒕𝒐 𝒏𝒂𝒐 𝒆 𝒄𝒓𝒊𝒎𝒆, 𝒄𝒓𝒊𝒎𝒆 𝒆 𝒐 𝒎𝒂𝒖 𝒖𝒔𝒐 𝒅𝒐 𝒄𝒐𝒏𝒉𝒆𝒄𝒊𝒎𝒆𝒏𝒕𝒐'''</h2>

### Introdução

Inspirado no meu projeto [web-scraping](https://github.com/Roni-Macedo/web-scraping.git)

GeneratePeople faz um web scraping no [site, geradordepessoas](http://www.geradordepessoas.com.br/)
e retorna uma impressão formato texto

Exemplo 1: retorna formato texto plano.
```bash
      Dados Pessoais
        ------------------------------
            Nome: Carlos Amaral Teixeira
            CPF: 749.203.349-40
            RG: 4.032.894-40
            Data_Nasci: 28/11/1952
            Idade: 70

        Endereço
        ------------------------------
            CEP: 69029-285
            Endereco: Rua Anita Garibald
            Numero: 613
            Bairro: Santo Antonio
            Cidade: Manaus
            Estado: AM

        Telefone
        ------------------------------
            Fixo: (92) 8579-9435
            Cel: (92) 94138-0593
            mail: carlos.teixeira@uol.com.br



```

Exemplo 2: retorno formato json.

```bash
    {
    "nome": "Carlos Teixeira Gomes",
    "Cpf": "680.836.483-45",
    "Rg": "42.943.412-1",
    "Data_Nasci": "14/9/1955",
    "Idade": 67,
    "Cep": "01007-040",
    "Endereco": "Parque Anhangabau",
    "Numero": "542",
    "Bairro": "Centro",
    "Cidade": "Sao Paulo",
    "Estado": "SP",
    "Fixo": "(11) 3257-2672",
    "Cel": "(11) 97295-2789",
    "mail": "carlos.gomes@uol.com.br"
}
```

- [x] dados pessoais
- [x] endereço
- [x] telefone
- [x] e-mail

### Pré-requisitos

Antes de começar, vai precisar ter instalado na sua máquina:

- [x] [python](https://www.python.org/)

- [x] [Git](https://git-scm.com)

- [x] [beautifullsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

- [x] [unidecode](https://pypi.org/project/Unidecode/)

### 👨‍💻 Começando

```bash
# Clone este repositório
$ git clone https://github.com/Roni-Macedo/GeneratePeople.git

$  python

>> from generate_people import GeneratePeople
>>>
>>>
>>> pessoa = GeneratePeople()
>>> print(pessoa.text_format())
>>>
>>>Feminino[f] masculino[m]: m
>>>
#  Retorno
        Dados Pessoais
        ------------------------------
            Nome: Carlos Amaral Teixeira
            CPF: 749.203.349-40
            RG: 4.032.894-40
            Data_Nasci: 28/11/1952
            Idade: 70

        Endereço
        ------------------------------
            CEP: 69029-285
            Endereco: Rua Anita Garibald
            Numero: 613
            Bairro: Santo Antonio
            Cidade: Manaus
            Estado: AM

        Telefone
        ------------------------------
            Fixo: (92) 8579-9435
            Cel: (92) 94138-0593
            mail: carlos.teixeira@uol.com.br
>>>
>>>
>>>print(pessoa.json_format())
>>>
>>>Feminino[f] masculino[m]: f
# Retorno
    {
    "nome": "Giovana Amaral Gomes",
    "Cpf": "015.859.138-04",
    "Rg": "4.032.894-40",
    "Data_Nasci": "12/11/1957",
    "Idade": 65,
    "Cep": "01505-010",
    "Endereco": "Rua Anita Ferraz",
    "Numero": "412",
    "Bairro": "Se",
    "Cidade": "Sao Paulo",
    "Estado": "SP",
    "Fixo": "(11) 2153-9278",
    "Cel": "(11) 92483-9799",
    "mail": "giovana.gomes@uol.com.br"
}
# >>>Feminino[f] masculino[m]: 
# passando a string vazia o retorno sera aleatorio.
```

#### 🔜 Em breve Generate-People_v2

## Autor

[Roni-Macedo](https://github.com/Roni-Macedo)

### Licença

[MIT License](https://github.com/Roni-Macedo/GeneratePeople/blob/main/LICENSE)