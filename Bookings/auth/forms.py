from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo




class LoginForm(FlaskForm):
    username = StringField("Your Username: ", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Stay logged in') #sets a cookie
    submit = SubmitField('Log me in')
    #recaptcha = RecaptchaField()  

class SignupForm(FlaskForm):
    username = StringField('Username',
                            description = "Combination of lower or uppercase 'a-z' characters, \
                                            numbers '0-9' and underscores '_' ",
                            validators=[
                                DataRequired(), Length(4, 80),
                                Regexp('^[A-Za-z0-9_]{3,}$',
                                    message="Usernames consist of numbers, letters, "
                                    "and underscores.")])
    
    password = PasswordField('Password',
                            description = "Add description",                                       
                            validators=[DataRequired(),
                            EqualTo('password2', message='Passwords must match.')])
    
    password2 = PasswordField('Confirm password',
                                description = "Add description",    
                                validators=[DataRequired()])
    
    email = StringField('Email', 
                        description = "Add description",   
                        validators=[DataRequired(), Length(1, 120), Email()])
    submit = SubmitField("Register me")
    #recaptcha = RecaptchaField()
    #TODO query database to validate if username OR email if already there