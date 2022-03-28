# desafioapi
 
Instalar Python 3.10.3 https://www.python.org/downloads/release/python-3103/

Clonar o repositório
git clone https://github.com/leonardo-felipe/desafioapi.git

Ir até a pasta do projeto
 
Criar Virutalenv

Será preciso criar uma virtual env e também ativa-la

Para criar a virutal env use os seguintes comandos no terminal/cmd.

Para Linux/Mac:

python3 -m venv venv

Para Windwos

python -m venv venv

e para ativar a virtual env

Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

Instalar dependências
pip install -r requirements.txt

Variáveis de ambiente

Na raiz do projeto há um arquivo com nome .env.example, você precisará renomeá-lo para .env ou criar outro arquivo .env e excluir o .env.example. As variáveis de ambiente serão enviados no e-mail de entrega do projeto. Basta copiá-las e colar no arquivo .env


Rodar o projeto

Digite o comando:

python manage.py runserver


Estrutura

/admin     - Admin

/register  - Cadastro

/login     - Login

/logout    - Logout

/items     - Lista de items



