
# # A very simple Flask Hello World app for you to get started with...

# from flask import Flask
# from flask import Flask, request, render_template
# from datetime import datetime

# from flask.ext.wtf.html5 import NumberInput


# # from flask_sqlalchemy import SQLAlchemy

# import random


# app = Flask(__name__)

# # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
# #     username="fturci",
# #     password="era1nottebuiaetempestosa",
# #     hostname="fturci.mysql.eu.pythonanywhere-services.com",
# #     databasename="fturci$cadavrexq",
# # )
# # app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# # app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
# # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# # db = SQLAlchemy(app)

# # class Phrase(db.Model):
# #     __tablename__ = "Frasi"
# #     id = db.Column(db.Integer, primary_key=True)
# #     num = db.Column(db.Integer)
# #     content = db.Column(db.String(4096))

# # r = 1

# @app.route('/')
# def my_form(text=None):
#     value = NumberInput( [Required()])
#     submit = SubmitField('Next')
#     # global r
#     # data = Phrase.query.all()
#     # num = len(data)

#     # if num>2:
#     #     r = random.randint(1,num-1)
#     # else:
#     #     r = 1

#     # sel=db.session.query(Phrase).filter(Phrase.num==r).first()
#     # first = sel.content
#     # sel=db.session.query(Phrase).filter(Phrase.num==r+1).first()
#     # second = sel.content
#     # if r != 1:
#     #     first = "(...) "+first
#     # if r+1 != num:
#     #     second = second+f"(...)"
    
#     # if text==None:
#     #     return render_template("index.html",first=first, second=second)
#     # else:
#     #     return render_template("text.html",first=first,second=second, text=text)

# # @app.route('/',methods=['POST', 'GET'])
# # def interact():
# #     print("Interact!")
# #     global r

# #     if request.form['action']=='Invia':
# #         phrase = request.form["content"]
# #         if len(phrase)>1:
# #             db.session.query(Phrase).filter(Phrase.num>r).update({"num": (Phrase.num+1) })
# #             db.session.commit()

<<<<<<< HEAD
            if phrase.strip()[-1] in '.?!':
                pass
            else:
                phrase += '.'
            #insert new phrase
            p = Phrase(content=phrase, num=r+1)
            db.session.add(p)
            db.session.commit()
=======
# #             #insert new phrase
# #             p = Phrase(content=phrase, num=r+1)
# #             db.session.add(p)
# #             db.session.commit()
>>>>>>> fca6fdeacd756b5e27bcc7a657bad0a407f3056b

# #         return render_template("thanks.html")

# #     elif request.form['action']=='Leggi tutto':
# #         print("Reading")
# #         text = [p.content for p in db.session.query(Phrase).order_by(Phrase.num).all()]
# #         cadavre = " ".join(text)
# #         print(cadavre)

# #         return render_template("text.html",text=cadavre)


# #     elif request.form['action']=='Indietro':
# #         return my_form()

#     #render_template("index.html",n="bibi")
#     #return render_template(phrase)

#     # return """
#         #  <html><body>
#             #  <h1>Hello, world</h1>
#             #  The time is {}.
#         #  </body></html>
#         #  """.format(phrase)



from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'top-secret!'
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')
