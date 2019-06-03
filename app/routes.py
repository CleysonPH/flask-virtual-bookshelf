from flask import render_template, request, redirect, url_for, flash

from app import app, db
from app.models import Book, Author


@app.errorhandler(404)
def error_404(e):
    title = '404 Página Não Encontrada'
    
    return render_template('404.html', title=title), 404


@app.route('/')
def home():
    title = 'Lista de Livros'
    books = Book.query.order_by(Book.title).all()

    return render_template('book/book_list.html', title=title, books=books)


@app.route('/book/search')
def book_search():
    title = 'Resultado da Busca'
    search = request.args.get('search')

    books = Book.query.filter(Book.title.contains(search)).all()

    return render_template('book/book_list.html', title=title, books=books)


@app.route('/book/detail/<int:id>')
def book_detail(id):
    book = Book.query.get_or_404(id)
    title = 'Detalhes do Livro'

    return render_template('book/book_detail.html', title=title, book=book)


@app.route('/book/add', methods=['GET', 'POST'])
def book_add():
    book = 0
    authors = Author.query.order_by(Author.name).all()
    if request.method == 'GET':
        title = 'Cadastrar Livro'
        return render_template('book/book_form.html', title=title, book=book, authors=authors)
    
    print(request.form.get('author'))

    author = Author.query.get(
        request.form.get('author')
    )
    book = Book(
        title=request.form.get('title'),
        author=author,
        publisher=request.form.get('publisher'),
        edition=request.form.get('edition'),
        pages_number=request.form.get('pages_number'),
        img_url=request.form.get('img_url'),
        isbn=request.form.get('isbn'),
        description=request.form.get('description'),
    )

    db.session.add(book)
    db.session.commit()

    flash("Livro cadastrado com sucesso!")
    return redirect(url_for('book_add'))


@app.route('/book/edit/<int:id>', methods=['GET', 'POST'])
def book_edit(id):
    book = Book.query.get_or_404(id)
    authors = Author.query.order_by(Author.name).all()
    if request.method == 'GET':
        title = 'Editar Livro'
        return render_template('book/book_form.html', title=title, book=book, authors=authors)
    
    author = Author.query.get(request.form.get('author'))

    book.title = request.form.get('title')
    book.author = author
    book.publisher = request.form.get('publisher')
    book.edition = request.form.get('edition')
    book.pages_number = request.form.get('pages_number')
    book.img_url = request.form.get('img_url')
    book.isbn = request.form.get('isbn')
    book.description = request.form.get('description')

    db.session.commit()

    flash('Livro editado com sucesso!')
    return redirect(url_for('book_detail', id=book.id))


@app.route('/book/remove/<int:id>')
def book_delete(id):
    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    flash('Livro deletado com sucesso!')
    return redirect(url_for('home'))


@app.route('/author/add', methods=['GET', 'POST'])
def author_add():
    author = 0
    if request.method == 'GET':
        title = 'Cadastrar Autor'
        return render_template('author/author_form.html', title=title, author=author)
    
    author = Author(
        name=request.form.get('name'),
        img_url=request.form.get('img_url'),
        description=request.form.get('description'),
    )

    db.session.add(author)
    db.session.commit()

    flash("Autor cadastrado com sucesso!")
    return redirect(url_for('author_add'))
