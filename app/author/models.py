from app import db


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
