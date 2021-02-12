from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"
db = SQLAlchemy(app)

# db models here



@app.route('/')
def homePage():
    return render_template('index.html')


@app.route('/success')
def success():
    return render_template()


@app.route('/contact-us')
def contactUs():
    return render_template()


@app.route('/about-us')
def aboutUs():
    return render_template()


@app.route('/account')
def account():
    return render_template()


@app.route('/auth-page')
def authPage():
    return render_template()


@app.route('/wish-list')
def wishList():
    return render_template()


@app.route('/shopping-lists')
def shoppingLists():
    return render_template()


@app.route('/shopping-list/<id>', method=['GET'])
def shoppingList(id):
    return render_template()


@app.route('/edit-list/<id>', method=['GET', 'POST'])
def editList(id):
    return render_template()


@app.route('/create-list', method=['GET', 'POST'])
def createList():
    return render_template()


@app.route('/delete-list', method=['POST'])
def deleteList():
    return render_template()


@app.route('/edit-item', method=['GET', 'POST'])
def editItem():
    return render_template()


@app.route('/delete-item', method=['POST'])
def deleteItem():
    return render_template()