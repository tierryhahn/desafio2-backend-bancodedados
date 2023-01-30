# desafio2-backend-bancodedados

# O projeto:
A aplicação consiste em analisar um arquiovo txt (CNAB) e guardar as informações (transacções financeiras) numa base de dados.

# Tecnologias:
- Django Framework
- Python 3
- SQLite


 Instalação e funcionamento em ambientes de desenvolvimento:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Rode as migrations:
```bash
./manage.py migrate
```

5. Inicialização do servidor:
```bash
./manage.py runserver
```


# Rotas:

Upload do arquivo (POST) e listagem de todas as transações(GET):
http://127.0.0.1:8000/file/

Balanço das lojas:
http://127.0.0.1:8000/loja/

