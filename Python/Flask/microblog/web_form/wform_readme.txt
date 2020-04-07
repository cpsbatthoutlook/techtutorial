
Reference: https://hackersandslackers.com/flask-wtforms-forms/
    https://flask-wtf.readthedocs.io/en/stable/
    

you need flask_wtf:
  Create a <form.py> with data points [ TextField, TextArea, Password, Booleadn etc]
  Create a Jinja html in the templates/sdfsd.html with correct fields {flash_messages(), errors etc}
  Edit route to import form.py, add URI [GeT, PosT ] with validated form. 

get_flashed_messages()  #https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/#simple-flashing
    To display the message back at the page


 redirect(url_for('success')) instead of redirect('/') is better for externalizing the links
 secret_key is most important for wtforms
 Forms options to consider:
     [VARIABLE] = [FIELD TYPE]('[LABEL]', [ validators=[VALIDATOR TYPE](message=('[ERROR MESSAGE')) ])
     name = StringField('Name', [ DataRequired()])
    email = StringField('Email', [ Email(message=('Not a valid email address.')), DataRequired()])
    body = TextField('Message', [ DataRequired(), Length(min=4, message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
