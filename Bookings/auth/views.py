from . import auth

from flask import render_template, flash, redirect, url_for, request, session
from flask_login import login_user, logout_user, login_required

from .forms import LoginForm, SignupForm

@auth.route('/login', methods=["GET","POST"])
def login():
    #TODO valication logic 
    form = LoginForm()

    if form.validate_on_submit():
        
        # fake user - this is for now
        fake_user = {'username': 'tester123', 'password':'test123', 'is_active':True }

        if fake_user['username'] is not None and fake_user['password'] == form.password.data.strip():
            #this stores the user in session
            #login_user(True, form.remember_me.data)
            #flash message back to user
            flash("You are logged in as: {}.".format(fake_user['username']))
            #next is the userpage that the user wanted to visit
            return redirect(request.args.get('next')) or url_for('main.index')
        flash('Incorrect username or password.')

    return render_template("login.html", form=form)



@auth.route('/signup', methods=["GET", "POST"])
def signup():
    
    form = SignupForm()
    
    if form.validate_on_submit():

        try:
            user = {'username': form.username.date, 'email' : form.email.data, 
                    'password' : form.password.data}
            
            session['username'] = user['username'] 
            
            #login_user(user, True)
            flash(format("Welcome {} to Acme app.", session['username']))
            return redirect(url_for('main.index'))
            
        except RuntimeError as e:
            flash("There were error signing you up" + str(e))
            return render_template("signup.html", form=form)
              
    return render_template("signup.html", form=form)


@auth.route("/logout")
def logout():
    #logout_user()
    return redirect(url_for('main.index'))