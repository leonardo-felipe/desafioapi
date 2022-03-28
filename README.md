# desafioapi
   
## Desafio API
 
Estrutura da API

/admin     - Admin

/register  - Cadastro

/login     - Login

/logout    - Logout

/items     - Lista de items
 
 
## Principais tecnologias utilizadas
 
* Python version 3.10.3
* Django==3.2.12
* djangorestframework==3.13.1
 
## Getting started
 
* Instalar Python 3.10.3
>    https://www.python.org/downloads/release/python-3103/

* Clonar o repositório git clone
>    https://github.com/leonardo-felipe/desafioapi.git

* Ir até a pasta do projeto

* Criar Virutalenv
* Para Linux/Mac:
> python3 -m venv venv
* Para Windows
> python -m venv venv

* Ativar a virtual env no Linux:
> source venv/bin/activate
* Ativar a virtual env no Windows:
> venv\Scripts\activate

* Instalar dependências
> pip install -r requirements.txt

* Variáveis de ambiente

Na raiz do projeto há um arquivo com nome .env.example, você precisará renomeá-lo para .env ou criar outro arquivo .env e excluir o .env.example. As variáveis de ambiente serão enviados no e-mail de entrega do projeto. Basta copiá-las e colar no arquivo .env

* Migrations
> python manage.py migrate


* Rodar o projeto
> python manage.py runserver

* Crie um super usuário para acessar o django-admin
> python manage.py createsuperuser

  
## Autor
 
* **Leonardo Felipe**: @leonardo-felipe (https://github.com/leonardo-felipe)
