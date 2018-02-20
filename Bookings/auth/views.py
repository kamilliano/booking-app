from . import auth

from flask import render_template, flash, redirect, url_for, session
#from flask_login import login_user, logout_user, login_required

from .forms import LoginForm, SignupForm



@auth.route('/login', methods=["GET","POST"])
def login():
    #TODO valication logic 
    form = LoginForm()

    if form.validate_on_submit():
        
        # fake user - this is for now
        fake_user = {'username': 'tester123', 'password':'test123', 'user_id' : 1}

        if fake_user['username'] is not None and fake_user['password'] == form.password.data.strip():
            #flash message back to user
            session['user_id'] = fake_user['user_id']
            flash("You are logged in as: {}.".format(fake_user['username']))
            #next is the userpage that the user wanted to visit
            return redirect(url_for('main.index'))
        flash('Incorrect username or password.')

    return render_template("login.html", form=form)



@auth.route('/signup', methods=["GET", "POST"])
def signup():
    
    form = SignupForm()
    
    if form.validate_on_submit():

        try:
            #at the moment use a fake to test signing and redirecting
            fake_user = {'username': form.username.data, 'email' : form.email.data, 
                    'password' : form.password.data, 'user_id' : 2}
            
            session['username'] = fake_user['username'] 
            session['user_id'] = fake_user['user_id']
            #login_user(user, True)
            flash("Welcome {} to Acme app.".format(session['username']))
            return redirect(url_for('main.index'))
            
        except RuntimeError as e:
            flash("Upps, can't sign you in. Error message: " + str(e))
            return render_template("signup.html", form=form)
              
    return render_template("signup.html", form=form)


@auth.route("/logout")
def logout():
    #logout_user()
    return redirect(url_for('main.index'))