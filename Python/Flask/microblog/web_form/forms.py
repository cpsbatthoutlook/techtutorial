from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField,DateField,DateTimeField,RadioField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()] )
    password = StringField('Password', validators=[DataRequired()] )
    remember = BooleanField('Remember me')
    submit = SubmitField('Go for it')
    # 
    #   to address null pointers
    # 
    # # textarea = TextAreaField('Test TextArea')
    # radio = RadioField('Test RadioField')
    # datef = DateField('Test DateField')
    # dtime  = DateTimeField('test DateTimeField ')
