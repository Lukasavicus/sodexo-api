sodexo-api
==========

[![Requirements Status](https://requires.io/github/canassa/sodexo-api/requirements.png?branch=master)](https://requires.io/github/canassa/sodexo-api/requirements/?branch=master)


API não oficial para extrair informações do site sodexosaldocartao.com.br

### Como usar

Instale as dependências do projeto:

    pip install -r requirements.txt

Infome o seu número do cartão SODEXO juntamente com o CPF:

    python saldo.py <numero_cartao> <cpf>

O captcha será baixado. Após o preenchimento manual do mesmo, o seu saldo será exibido :)