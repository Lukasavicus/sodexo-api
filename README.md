sodexo-api
==========

API não oficial para extrair informações do site sodexosaldocartao.com.br

### Como usar

Instale as dependencias das libs:
```sh
#ubuntu
sudo apt-get install libjpeg-dev

#MacOS
brew install libjpeg
```
 
Instale as dependências do projeto:
```sh
pip install -r requirements.txt
```

Infome o seu número do cartão SODEXO juntamente com o CPF:
```sh
python saldo.py <numero_cartao> <cpf>
```

O captcha será baixado. Após o preenchimento manual do mesmo, o seu saldo será exibido :)