from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField("Pitch Title",validators=[Required()])
    pitch = TextAreaField('Write your pitch here')
    category = SelectField("Pitch category",choices=[('Pickup Lines','Pickup Lines'),('Interview Pitch','Interview Pitch'),('Product Pitch','Promotion Pitch')],validators=[Required()])
    submit = SubmitField('Submit')