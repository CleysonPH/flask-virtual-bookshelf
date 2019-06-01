from flask import render_template, request, redirect, url_for

from app import app, db
from app.models import Book


@app.route('/')
def home():
    title = 'Lista de Livros'
    books = Book.query.order_by(Book.title).all()

    return render_template('home.html', title=title, books=books)


@app.route('/book/add', methods=['GET', 'POST'])
def book_add():
    if request.method == 'GET':
        title = 'Cadastrar Livro'
        return render_template('book_form.html', title=title)
    
    book = Book(
        title=request.form.get('title'),
        author=request.form.get('author'),
        publisher=request.form.get('publisher'),
        edition = request.form.get('edition'),
        pages_number = request.form.get('pages_number'),
        img_url = request.form.get('img_url')
    )

    db.session.add(book)
    db.session.commit()

    return redirect(url_for('home'))
