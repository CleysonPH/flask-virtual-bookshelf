from flask import render_template

from app import app
from app.models import Book


@app.route('/')
def home():
    title = 'Lista de Livros'
    books = Book.query.order_by(Book.title).all()

    return render_template('home.html', title=title, books=books)