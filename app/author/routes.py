from flask import render_template, request, redirect, url_for, flash

from app import app, db
from app.models import Book, Author


@app.route('/author/list')
def author_list():
    title = 'Lista de Autores'
    authors = Author.query.order_by(Author.name).all()

    return render_template('author/author_list.html', title=title, authors=authors)


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


@app.route('/author/edit/<int:id>', methods=['GET', 'POST'])
def author_edit(id):
    author = Author.query.get_or_404(id)
    if request.method == 'GET':
        title = 'Editar Autor'
        return render_template('author/author_form.html', title=title, author=author)
     
    author.name=request.form.get('name')
    author.img_url=request.form.get('img_url')
    author.description=request.form.get('description')

    db.session.commit()

    flash("Autor editado com sucesso!")
    return redirect(url_for('author_detail', id=author.id))


@app.route('/author/remove/<int:id>')
def author_remove(id):
    author = Author.query.get_or_404(id)

    db.session.delete(author)
    db.session.commit()

    flash("Autor deletado com sucesso!")
    return redirect(url_for('author_list'))


@app.route('/author/detail/<int:id>')
def author_detail(id):
    author = Author.query.get_or_404(id)
    title = 'Detalhes do Autor'

    return render_template('author/author_detail.html', title=title, author=author)
