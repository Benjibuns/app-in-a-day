from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"
db = SQLAlchemy(app)


class ShoppingList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), unique=False, nullable=False)
    items = db.relationship('Item', backref='shopping_list', lazy=True, cascade="all, delete-orphan")


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(100), unique=False, nullable=True)
    shopping_list_id = db.Column(db.Integer, db.ForeignKey('shopping_list.id'), nullable=False)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/account')
def account():
    return render_template('account.html')


@app.route('/auth_page')
def auth_page():
    return render_template('auth_page.html')


@app.route('/wish_list')
def wish_list():
    return render_template('wish_list.html')


@app.route('/shopping_lists')
def shopping_lists():
    all_lists = ShoppingList.query.all()
    return render_template('shopping_lists.html', all_lists = all_lists)


@app.route('/single_shopping_list/<id>', methods=['GET', 'POST'])
def single_shopping_list(id):
    if request.method == 'POST':
        single_list = ShoppingList.query.get(id)
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        description = request.form.get('description')
        new_item = Item(name=name, quantity=quantity, description=description, shopping_list=single_list)
        db.session.add(new_item)
        db.session.commit()
        return redirect(f'/single_shopping_list/{single_list.id}')
    else:
        single_list = ShoppingList.query.get(id)
        if single_list:
            return render_template('single_shopping_list.html', single_list = single_list)
        else:
            return redirect("/no_match")


@app.route("/no_match")
def no_match():
    return render_template("no_match.html")


@app.route('/edit_list/<id>', methods=['GET', 'POST'])
def edit_list(id):
    if request.method == 'POST':
        single_list = ShoppingList.query.get(id)
        title = request.form.get('title')
        single_list.title = title
        db.session.commit()
        flash('your list was Edited', 'update')
        return redirect(f'/single_shopping_list/{single_list.id}')
    else:
        single_list = ShoppingList.query.get(id)
        return render_template('edit_list.html', single_list = single_list)


@app.route('/create_list', methods=['GET', 'POST'])
def create_list():
        if request.method == "POST":
            title = request.form.get("title")
            new_list = ShoppingList(title=title)
            db.session.add(new_list)
            db.session.commit()
            flash("Your new awesome list was added!!", "success")
            return redirect(f'/single_shopping_list/{new_list.id}')
        else:
            return render_template('create_list.html')


@app.route('/delete_list/<id>', methods=['POST'])
def delete_list(id):
    list = ShoppingList.query.get(id)
    db.session.delete(list)
    db.session.commit()
    flash("Your List was deleted", "danger")

    return redirect('/shopping_lists')


@app.route('/edit_item', methods=['GET', 'POST'])
def edit_item():
    return render_template('edit_item.html')


@app.route('/delete_item', methods=['POST'])
def delete_item():
    return render_template('delete_item.html')


if __name__ == '__main__':
    app.run(debug=True)
