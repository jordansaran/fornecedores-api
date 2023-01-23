# API - Fornecedores

<p align="center">
    <h2 align="center">Flask password verify</h2>
    <a href="https://github.com/jordansaran/fornecedores-api/actions">
      <img alt="Tests Passing" src="https://github.com/jordansaran/fornecedores-api/workflows/Test-Coverage/badge.svg" />
    </a>
    <a href="https://codecov.io/gh/jordansaran/fornecedores-api">
      <img src="https://codecov.io/gh/jordansaran/fornecedores-api/branch/main/graph/badge.svg" />
    </a>
    <a href="https://github.com/jordansaran/fornecedores-api/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/jordansaran/fornecedores-api?color=0088ff" />
    </a>
    <a href="https://github.com/jordansaran/fornecedores-api/pulls">
      <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/jordansaran/fornecedores-api?color=0088ff" />
    </a>
</p>

Foi desenvolvido uma API onde seu objetivo gerar e obter dados de Fornecedores. 
# Instalação
Certifique-se de utilizar a última versão do código fonte, que normalmente fica na branch "main"(principal) do Git.
````shell
# clone o repositório
$ git clone https://github.com/jordansaran/fornecedores-api
$ cd fornecedores-api
````
Crie um virtualenv em ambiente UNIX e ative-o:
````shell
$ python3 -m venv venv
$ . venv/bin/activate
````
Ou no WINDOWS cmd:
````shell
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
````
Instalando as dependências do projeto fornecedores-api.
````shell
$ pip install -r requirements.txt
````
Antes de executar a API crie um arquivo **.env** na raiz do projeto caso ele não tenha sido criado.
O arquivo deve conter os seguintes variáveis de ambiente. O diretório **'<your_path>'** você precisa definir o diretório
 de onde o banco de dados sqllite irá ser criado. Caso deseje utilizar outro banco de dados modifique a variável ambiente
**SQLALCHEMY_DATABASE_URI**.
````dotenv
SECRET_KEY=
FLASK_DEBUG=1
FLASK_APP=app.py
SQLALCHEMY_DATABASE_URI=sqlite:///<your_path>/database.db
SQLALCHEMY_TRACK_MODIFICATIONS=0
RESTX_MASK_SWAGGER=False
RESTX_VALIDATE=True
````
A variável **SECRET_KEY** deve conter um hash que será utilizado quando a API for utilizada em **Production**.
A variável **FLASK_DEBUG** deve possuir o valores 1 ou 0 para referenciar a condição de **True** ou **False** para
executar aplicação em modo **DEBUG**.
A variável **FLASK_APP** é utilizada para destacar qual o arquivo .py deve ser utilizado como referência para executar
a aplicação.
# Executar aplicação
````shell
$ flask run
````
Abra http://127.0.0.1:5000/api/v1/ui em seu navegador para acessar a documentação da API Fornecedor.
# Teste/Coverage
Executar com coverage report:
````shell
coverage run -m pytest
coverage report
coverage html  # abrir htmlcov/index.html em um navegador
````
# Utilizar Docker
Para replicar o ambiente de desenvolvimento e colocar em execução a API, execute o comando logo abaixo. 
Destacando que é necessário que seu ambiente de desenvolvimento possua [**Docker**](https://www.docker.com/products/docker-desktop/) instalado.
```shell
docker-compose up -d
```
## Observações
A url de acesso a API é **http://127.0.0.1:5000/api/v1/ui**, caso deseje alterar a porta de acesso modifique
o arquivo **docker-compose.yml** no parametro **ports** (5000:5000).