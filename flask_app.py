
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import Flask, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, FloatField, validators
import random


app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="fturci",
    password="era1nottebuiaetempestosa",
    hostname="fturci.mysql.eu.pythonanywhere-services.com",
    databasename="fturci$cadavrexq",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Phrase(db.Model):
    __tablename__ = "Frasi"
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    content = db.Column(db.String(4096))

r = 1


class InputForm(Form):
    Box_1 = FloatField(
        label='', default=5,
        validators=[validators.InputRequired()])
    Box_2 = FloatField(
        label='', default=5,
        validators=[validators.InputRequired()])
    Box_3 = FloatField(
        label='', default=5,
        validators=[validators.InputRequired()])
    Box_4 = FloatField(
        label='', default=5,
        validators=[validators.InputRequired()])
    Box_5 = FloatField(
        label='', default=5,
        validators=[validators.InputRequired()])
    Box_6 = FloatField(
        label='', default=5,
        validators=[validators.InputRequired()])
    Box_7 = FloatField(
        label='', default=5,
        validators=[validators.InputRequired()])
    Box_8 = FloatField(
        label='', default=5,
        validators=[validators.InputRequired()])
@app.route('/')
def my_form( methods=['GET', 'POST']):
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data, form.b.data,
                         form.w.data, form.T.data)
    else:
        result = None

    return render_template("index.html",
                           form=form, result=result)

    # global r
    # data = Phrase.query.all()
    # num = len(data)

    # if num>2:
    #     r = random.randint(1,num-1)
    # else:
    #     r = 1

    # sel=db.session.query(Phrase).filter(Phrase.num==r).first()
    # first = sel.content
    # sel=db.session.query(Phrase).filter(Phrase.num==r+1).first()
    # second = sel.content
    # if r != 1:
    #     first = "(...) "+first
    # if r+1 != num:
    #     second = second+f"(...)"
    
    # if text==None:
    #     return render_template("index.html",first=first, second=second)
    # else:
    #     return render_template("text.html",first=first,second=second, text=text)

@app.route('/',methods=['POST', 'GET'])
def interact():
    print("Interact!")
    global r

    if request.form['action']=='Invia':
        phrase = request.form["content"]

        # if len(phrase)>1:
        #     db.session.query(Phrase).filter(Phrase.num>r).update({"num": (Phrase.num+1) })
        #     db.session.commit()

        #     #insert new phrase
        #     p = Phrase(content=phrase, num=r+1)
        #     db.session.add(p)
        #     db.session.commit()

        return render_template("thanks.html")

    # elif request.form['action']=='Leggi tutto':
    #     print("Reading")
    #     text = [p.content for p in db.session.query(Phrase).order_by(Phrase.num).all()]
    #     cadavre = " ".join(text)
    #     print(cadavre)

    #     return render_template("text.html",text=cadavre)


    # elif request.form['action']=='Indietro':
    #     return my_form()

    #render_template("index.html",n="bibi")
    #return render_template(phrase)

    # return """
        #  <html><body>
            #  <h1>Hello, world</h1>
            #  The time is {}.
        #  </body></html>
        #  """.format(phrase)

