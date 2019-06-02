from flask import render_template, request, redirect, url_for

from app import app, db
from app.models import Book


@app.errorhandler(404)
def error_404(e):
    title = '404 página não encontrada'
    
    return render_template('404.html', title=title), 404


@app.route('/')
def home():
    title = 'Lista de Livros'
    books = Book.query.order_by(Book.title).all()

    return render_template('home.html', title=title, books=books)


@app.route('/book/detail/<int:id>')
def book_detail(id):
    book = Book.query.get_or_404(id)
    title = 'Detalhes do Livro'

    return render_template('book_detail.html', title=title, book=book)


@app.route('/book/add', methods=['GET', 'POST'])
def book_add():
    book = 0
    if request.method == 'GET':
        title = 'Cadastrar Livro'
        return render_template('book_form.html', title=title, book=book)
    
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


@app.route('/book/edit/<int:id>', methods=['GET', 'POST'])
def book_edit(id):
    book = Book.query.get_or_404(id)
    if request.method == 'GET':
        title = 'Editar Livro'
        return render_template('book_form.html', title=title, book=book)
    
    book.title=request.form.get('title')
    book.author=request.form.get('author')
    book.publisher=request.form.get('publisher')
    book.edition = request.form.get('edition')
    book.pages_number = request.form.get('pages_number')
    book.img_url = request.form.get('img_url')

    db.session.commit()

    return redirect(url_for('home'))


@app.route('/book/remove/<int:id>')
def book_delete(id):
    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('home'))
