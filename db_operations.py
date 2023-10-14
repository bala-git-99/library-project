from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-library.db"
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def create(self):
        with app.app_context():
            db.session.add(self)
            db.session.commit()


with app.app_context():
    db.create_all()


def read_all():
    with app.app_context():
        all_books = db.session.execute(db.select(Books)).scalars()
        books_list = []
        for book in all_books:
            books_list.append(book)
            # print(book.title)
        return books_list


def read(id):
    with app.app_context():
        book = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
        return book


def update_rating(id, rating):
    with app.app_context():
        book_to_update = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
        book_to_update.rating = rating
        db.session.commit()


def delete_book(id):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
