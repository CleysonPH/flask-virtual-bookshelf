from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.Text, nullable=False)
    publisher = db.Column(db.String(80), nullable=True)
    edition = db.Column(db.Integer, nullable=True)
    pages_number = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(250), nullable=False, default='https://via.placeholder.com/350x500')


    def __init__(self, title, author, publisher, edition, pages_number, img_url):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.edition = edition
        self.pages_number = pages_number
        self.img_url = img_url


    def __repr__(self):
        return f'<Book {self.title}>'