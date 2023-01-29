# desafio2-backend-bancodedados

Installation and running in development environments

Create the virtual environment:
python -m venv venv

activate the venv:

# Linux
source venv/bin/activate

# Windows
.\venv\Scripts\activate


Instale as dependências:
pip install -r requirements.txt

Run the migrations:
./manage.py migrate

Run the application:
./manage.py runserver

# Routes:

File upload (POST) and list all transactions(GET):
http://127.0.0.1:8000/file/

Stores balance:
http://127.0.0.1:8000/loja/

