
# 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

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from wtforms.fields import IntegerField


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'top-secret!'
Bootstrap(app)



class TestForm(FlaskForm):
    number = IntegerField('Number')

@app.route('/',methods=['POST', 'GET'])
def index():
    # level    = IntegerField('User Level', [validators.NumberRange(min=0, max=10)])
     form = TestForm()
    if request.method == 'GET':
        form.number.data = 100
    if request.method == 'POST':
        form.number.data = 200
    return render_template('index.html', form=form)