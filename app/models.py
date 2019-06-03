from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    publisher = db.Column(db.String(80), nullable=True)
    edition = db.Column(db.Integer, nullable=True)
    pages_number = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(250), nullable=False, default='https://via.placeholder.com/350x500')
    isbn = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False, default='Nenhuma descrição foi dada')

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', backref=db.backref('books', lazy=True))


    def __init__(self, title, author, publisher, edition, pages_number, img_url, isbn, description):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.edition = edition or None
        self.pages_number = pages_number
        self.img_url = img_url or None
        self.isbn = isbn
        self.description = description or None


    def __repr__(self):
        return f'<Book {self.title}>'



class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    img_url = db.Column(db.String(250), nullable=False, default='https://via.placeholder.com/300x300')
    description = db.Column(db.Text, nullable=False, default='Nenhuma descrição foi dada')


    def __init__(self, name, img_url, description):
        self.name = name
        self.img_url = img_url or None
        self.description = description or None


    def __repr__(self):
        return f'<Author {self.name}>'
