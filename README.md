<h1 align="center">Generate-People</h1>

<h4 align="center">🚧 GeneratePeople 🚀 Em construção... 🚧</h4>

# AVISO ⚠

## Para fins didáticos o mau uso do **GeneratePeople** é total responsabilidade do seu utilizador.

**Todos os dados aqui gerados são aleatorios sem valor legal.**

<h2 align="center">'''o conhecimento não é crime, crime é o mau uso do conhecimento'''</h2>

### Introdução

Inspirado no meu projeto [web-scraping](https://github.com/Roni-Macedo/web-scraping.git)

GeneratePeople faz um web scraping no [site, geradordepessoas](http://www.geradordepessoas.com.br/)
e retorna uma impressão formato texto

Ex:
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

#  Resultado
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
```

#### 🔜 Em breve impresão json_format()

## Autor

[Roni-Macedo](https://github.com/Roni-Macedo)

### Licença

[MIT License](https://github.com/Roni-Macedo/GeneratePeople/blob/main/LICENSE)