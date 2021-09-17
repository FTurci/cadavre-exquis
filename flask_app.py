
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import Flask, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, IntegerField, validators
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
    Alice_Box_0_Empty = IntegerField(
        label='', default=0,
        validators=[validators.InputRequired()])
    Alice_Box_1_White = IntegerField(
        label='Box 1: White', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_2_Red = IntegerField(
        label='Box 2: Red', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_2_Yellow = IntegerField(
        label='Box 2: Yellow', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_3_Green = IntegerField(
        label='Box 3: Green', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_3_Cyan = IntegerField(
        label='Box 3: Cyan', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_3_Black = IntegerField(
        label='Box 3: Black', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_4_White = IntegerField(
        label='Box 4: White', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_4_Red = IntegerField(
        label='Box 4: Red', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_4_Yellow = IntegerField(
        label='Box 4: Yellow', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_5_Green = IntegerField(
        label='Box 5: Green', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_5_Cyan = IntegerField(
        label='Box 5: Cyan', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_5_Black = IntegerField(
        label='Box 5: Black', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_5_White = IntegerField(
        label='Box 5: White', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_6_Red = IntegerField(
        label='Box 6: Red', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_6_Yellow = IntegerField(
        label='Box 6: Yellow', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_6_Green = IntegerField(
        label='Box 6: Green', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_6_Cyan = IntegerField(
        label='Box 6: Cyan', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_6_Black = IntegerField(
        label='Box 6: Black', default=5,
        validators=[validators.InputRequired()])

    Alice_Box_7_White = IntegerField(
        label='Box 7: White', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_7_Red = IntegerField(
        label='Box 7: Red', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_7_Yellow = IntegerField(
        label='Box 7: Yellow', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_7_Green = IntegerField(
        label='Box 7: Green', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_7_Cyan = IntegerField(
        label='Box 7: Cyan', default=5,
        validators=[validators.InputRequired()])
    Alice_Box_7_Black = IntegerField(
        label='Box 7: Black', default=5,
        validators=[validators.InputRequired()])


    #  Bob's boxes
    Bob_Box_0_Empty = IntegerField(
        label='', default=0,
        validators=[validators.InputRequired()])
    Bob_Box_1_White = IntegerField(
        label='Box 1: White', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_2_Red = IntegerField(
        label='Box 2: Red', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_2_Yellow = IntegerField(
        label='Box 2: Yellow', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_3_Green = IntegerField(
        label='Box 3: Green', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_3_Cyan = IntegerField(
        label='Box 3: Cyan', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_3_Black = IntegerField(
        label='Box 3: Black', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_4_White = IntegerField(
        label='Box 4: White', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_4_Red = IntegerField(
        label='Box 4: Red', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_4_Yellow = IntegerField(
        label='Box 4: Yellow', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_5_Green = IntegerField(
        label='Box 5: Green', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_5_Cyan = IntegerField(
        label='Box 5: Cyan', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_5_Black = IntegerField(
        label='Box 5: Black', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_5_White = IntegerField(
        label='Box 5: White', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_6_Red = IntegerField(
        label='Box 6: Red', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_6_Yellow = IntegerField(
        label='Box 6: Yellow', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_6_Green = IntegerField(
        label='Box 6: Green', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_6_Cyan = IntegerField(
        label='Box 6: Cyan', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_6_Black = IntegerField(
        label='Box 6: Black', default=5,
        validators=[validators.InputRequired()])

    Bob_Box_7_White = IntegerField(
        label='Box 7: White', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_7_Red = IntegerField(
        label='Box 7: Red', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_7_Yellow = IntegerField(
        label='Box 7: Yellow', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_7_Green = IntegerField(
        label='Box 7: Green', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_7_Cyan = IntegerField(
        label='Box 7: Cyan', default=5,
        validators=[validators.InputRequired()])
    Bob_Box_7_Black = IntegerField(
        label='Box 7: Black', default=5,
        validators=[validators.InputRequired()])


   
@app.route('/',methods=['POST', 'GET'])
def interact():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():

        print("requesting", form.Alice_Box_1_White.data, type(form.Alice_Box_1_White.data) )
        # print(dir(form.Alice_Box_1_White))
        from nimplus import Player, State, Game

        '''For level 3, fast Nim+ game, input Alice's and Bob's boxes content then plays 1 million matches with random starter to decide who is the winner.'''

        matches = 10000

        alice, bob = Player(), Player()
        keys = []
        for i in range(8):
            fromstate = State(i)
            fromstate.set_avail()
            fromstate.reorder()
            for tostate in fromstate.avail:
                keys.append((fromstate, tostate))
        print(len(keys))

        alice.boxes[keys[0]] = form.Alice_Box_1_White.data
        alice.boxes[keys[1]] = form.Alice_Box_2_Red.data
        alice.boxes[keys[2]] = form.Alice_Box_2_Yellow.data
        alice.boxes[keys[3]] = form.Alice_Box_3_Green.data
        alice.boxes[keys[4]] = form.Alice_Box_3_Cyan.data
        alice.boxes[keys[5]] = form.Alice_Box_3_Black.data
        alice.boxes[keys[6]] = form.Alice_Box_4_White.data
        alice.boxes[keys[7]] = form.Alice_Box_4_Red.data
        alice.boxes[keys[8]] = form.Alice_Box_4_Yellow.data
        alice.boxes[keys[9]] = form.Alice_Box_5_Green.data
        alice.boxes[keys[10]] = form.Alice_Box_5_Cyan.data
        alice.boxes[keys[11]] = form.Alice_Box_5_Black.data
        alice.boxes[keys[12]] = form.Alice_Box_5_White.data
        alice.boxes[keys[13]] = form.Alice_Box_6_Red.data
        alice.boxes[keys[14]] = form.Alice_Box_6_Yellow.data
        alice.boxes[keys[15]] = form.Alice_Box_6_Green.data
        alice.boxes[keys[16]] = form.Alice_Box_6_Cyan.data
        alice.boxes[keys[17]] = form.Alice_Box_6_Black.data
        alice.boxes[keys[18]] = form.Alice_Box_7_White.data
        alice.boxes[keys[19]] = form.Alice_Box_7_Red.data
        alice.boxes[keys[20]] = form.Alice_Box_7_Yellow.data
        alice.boxes[keys[21]] = form.Alice_Box_7_Green.data
        alice.boxes[keys[22]] = form.Alice_Box_7_Cyan.data
        alice.boxes[keys[23]] = form.Alice_Box_7_Black.data


        bob.boxes[keys[0]] = form.Bob_Box_1_White.data
        bob.boxes[keys[1]] = form.Bob_Box_2_Red.data
        bob.boxes[keys[2]] = form.Bob_Box_2_Yellow.data
        bob.boxes[keys[3]] = form.Bob_Box_3_Green.data
        bob.boxes[keys[4]] = form.Bob_Box_3_Cyan.data
        bob.boxes[keys[5]] = form.Bob_Box_3_Black.data
        bob.boxes[keys[6]] = form.Bob_Box_4_White.data
        bob.boxes[keys[7]] = form.Bob_Box_4_Red.data
        bob.boxes[keys[8]] = form.Bob_Box_4_Yellow.data
        bob.boxes[keys[9]] = form.Bob_Box_5_Green.data
        bob.boxes[keys[10]] = form.Bob_Box_5_Cyan.data
        bob.boxes[keys[11]] = form.Bob_Box_5_Black.data
        bob.boxes[keys[12]] = form.Bob_Box_5_White.data
        bob.boxes[keys[13]] = form.Bob_Box_6_Red.data
        bob.boxes[keys[14]] = form.Bob_Box_6_Yellow.data
        bob.boxes[keys[15]] = form.Bob_Box_6_Green.data
        bob.boxes[keys[16]] = form.Bob_Box_6_Cyan.data
        bob.boxes[keys[17]] = form.Bob_Box_6_Black.data
        bob.boxes[keys[18]] = form.Bob_Box_7_White.data
        bob.boxes[keys[19]] = form.Bob_Box_7_Red.data
        bob.boxes[keys[20]] = form.Bob_Box_7_Yellow.data
        bob.boxes[keys[21]] = form.Bob_Box_7_Green.data
        bob.boxes[keys[22]] = form.Bob_Box_7_Cyan.data
        bob.boxes[keys[23]] = form.Bob_Box_7_Black.data
        
        print(alice.boxes)

        game = Game(3, matches)
        game.play(alice, bob)

        print("Alice wins", alice.wins/matches * 100 , "% of matches!")
        print("Bob wins", (1-alice.wins/matches) * 100, "% of matches!")

        result = alice.wins/matches * 100
        # return render_template("Alice wins "+str(alice.wins/matches * 100 )+"% of matches!",form=form)
        return render_template("result.html",form=form, result_alice=str(result), result_bob=str(100.0-result))


    else:
        form = InputForm(request.form)
        return render_template("index.html",form=form)

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

# @app.route('/',methods=['POST', 'GET'])
# def interact():
#     print("Interact!")
#     global r

#     if request.form['action']=='Invia':
#         phrase = request.form["content"]

#         # if len(phrase)>1:
#         #     db.session.query(Phrase).filter(Phrase.num>r).update({"num": (Phrase.num+1) })
#         #     db.session.commit()

#         #     #insert new phrase
#         #     p = Phrase(content=phrase, num=r+1)
#         #     db.session.add(p)
#         #     db.session.commit()

#         return render_template("thanks.html")

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

