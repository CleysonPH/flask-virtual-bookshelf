# Flask Virtual Bookshelf

Um crud de livros feito com Flask e algumas extenções.

- Flask
- Flask-SQLAlchemy

## Requisitos

- Python 3.6
- Pipenv

## Como começar

Clone o repositorio e entre na pasta do projeto

```sh
git clone https://github.com/CleysonPH/flask-virtual-bookshelf.git
cd flask-virtual-bookshelf
```

Instale os requisitos do projeto com o pipenv

```sh
pipenv install
```

## Como rodar esse projeto

Primeiro crie o banco de dados

```sh
pipenv run python
```

```python
>>> from app import db
>>> db.create_all()
```

Execute o runner do Flask

```sh
pipenv run flask run
```

E por fim acesse a aplicação em http://localhost:5000