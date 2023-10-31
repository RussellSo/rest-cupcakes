from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired

class addCupcake(FlaskForm):
    flavor = StringField('Flavor')
    size = IntegerField('Size')
    rating = IntegerField('rating')