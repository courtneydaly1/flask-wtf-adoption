from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form to add pets"""
    
    name= StringField('Pet Name', validators=[InputRequired()])
    species=StringField('Species', choices=[
        ('dog', 'Dog'),
        ('cat','Cat'),
        ('rabbit', 'Rabbit'),
        ('turtle', 'Turtle'),
        ('horse', 'Horse'),
        ('bird', 'Bird'),
        ('hampser','Hampster')
        ])
    photo_url=StringField('Photo URL', validators=[Optional(),URL()])
    age=IntegerField('Age', validators=[Optional(),NumberRange(min=0, max=80)])
    notes= TextAreaField('Comments', validators=[Optional(), Length(min=10, max=30)])
    
    
class EditPetForm(FlaskForm):
    """form to edit pets"""
    
    photo_url= StringField('Photo URL', validators=[Optional(),URL()])
    notes= TextAreaField('Comments', validators=[Optional(), Length(min=10, max=30)])
    available = BooleanField("Still Available?")