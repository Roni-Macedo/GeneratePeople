<h1 align="center">πππ§ππ«ππ­π-πππ¨π©π₯π</h1>

<h4 align="center">π§ GeneratePeople   Finalizado πππ </h4>

# AVISO β 

## Para fins didΓ‘ticos o mau uso do **GeneratePeople** Γ© total responsabilidade do seu utilizador.

**Todos os dados aqui gerados sΓ£o aleatorios sem valor legal.**

<h2 align="center">'''π ππππππππππππ πππ π πππππ, πππππ π π πππ πππ ππ ππππππππππππ'''</h2>

### IntroduΓ§Γ£o

Inspirado no meu projeto [web-scraping](https://github.com/Roni-Macedo/web-scraping.git)

GeneratePeople faz um web scraping no [site, geradordepessoas](http://www.geradordepessoas.com.br/)
e retorna uma impressΓ£o formato texto

Exemplo 1: retorna formato texto plano.
```bash
      Dados Pessoais
        ------------------------------
            Nome: Carlos Amaral Teixeira
            CPF: 749.203.349-40
            RG: 4.032.894-40
            Data_Nasci: 28/11/1952
            Idade: 70

        EndereΓ§o
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
- [x] endereΓ§o
- [x] telefone
- [x] e-mail

### PrΓ©-requisitos

Antes de comeΓ§ar, vai precisar ter instalado na sua mΓ‘quina:

- [x] [python](https://www.python.org/)

- [x] [Git](https://git-scm.com)

- [x] [beautifullsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

- [x] [unidecode](https://pypi.org/project/Unidecode/)

### π¨βπ» ComeΓ§ando

```bash
# Clone este repositΓ³rio
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

        EndereΓ§o
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

#### π Em breve Generate-People_v2

## Autor

[Roni-Macedo](https://github.com/Roni-Macedo)

### LicenΓ§a

[MIT License](https://github.com/Roni-Macedo/GeneratePeople/blob/main/LICENSE)