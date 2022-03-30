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
 
## Instruções para instalar e rodar o projeto
 
* Instalar Python 3.10.3
>    https://www.python.org/downloads/release/python-3103/

* Clonar o repositório com git clone ou baixar no formato zip
> git clone https://github.com/leonardo-felipe/desafioapi.git

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

Na raiz do projeto há um arquivo com nome env.example, você precisará abrir este arquivo e alterar seu conteúdo. Será necessário inserir as variáveis de ambiente que foram enviadas no email de entrega do projeto. Após isto basta renomear o arquivo env.example para .env

* Migrations
> python manage.py migrate


* Rodar o projeto
> python manage.py runserver

* Crie um super usuário para o Django Admin
> python manage.py createsuperuser

  
## Autor
 
* **Leonardo Felipe**: @leonardo-felipe (https://github.com/leonardo-felipe)
