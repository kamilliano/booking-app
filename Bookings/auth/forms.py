from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo




class LoginForm(FlaskForm):
    username = StringField("Your Username: ", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Stay logged in') #sets a cookie
    submit = SubmitField('Log me in')
    recaptcha = RecaptchaField()  

class SignupForm(FlaskForm):
    username = StringField('Username',
                            validators=[
                                DataRequired(), Length(4, 80),
                                Regexp('^[A-Za-z0-9_]{3,}$',
                                    message="Usernames consist of numbers, letters, "
                                    "and underscores.")])
    
    password = PasswordField('Password',
                            validators=[DataRequired(),
                            EqualTo('password2', message='Passwords must match.')])
    
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    
    email = StringField('Email', 
                        validators=[DataRequired(), Length(1, 120), Email()])
    
    recaptcha = RecaptchaField()
    #TODO query database to validate if username OR email if already there