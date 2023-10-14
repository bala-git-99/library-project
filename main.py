from flask import render_template, request, redirect

from db_operations import *


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', books=read_all())


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        temp_dict = {
            'title': request.form['name'],
            'author': request.form['author'],
            'rating': request.form['rating'],
        }

        new_book = Books(title=temp_dict['title'], author=temp_dict['author'], rating=temp_dict['rating'])
        new_book.create()

        return redirect("/")
    return render_template('add.html')


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        update_rating(id, request.form['rating'])
        return redirect("/")
    return render_template('edit.html', book=read(id))


@app.route("/delete")
def delete():
    id = request.args.get('id')
    delete_book(id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
