from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def login():
    return render_template('content/login.html', title='Login')

@auth.route('/login', methods=['GET', 'POST'])
def login_post():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        """
        b = check_password_hash(user.password, password)
        a1 = generate_password_hash('1', method='sha256')
        a2 = generate_password_hash('1')
        a3 = generate_password_hash('1', method='sha512')
        a4 = generate_password_hash('1', method='pbkdf2:sha256')
        a5 = generate_password_hash('1', method='pbkdf2:sha256')
        a6 = generate_password_hash(password, method='pbkdf2:sha256')
        b2 = check_password_hash(a6, password)
        b3 = user.check_password(password)
"""

        # check if user actually exists
        # take the user supplied password, hash it, and compare it to the hashed password in database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))   # if user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember) # User 인스턴스를 current_user에 등록한다는 것입니다.
        return redirect(url_for('main.index'))

@auth.route('/signup')
def signup():
    """사용자 가입"""
    #return render_template('signup.html')
    return render_template('content/register.html', title='Sign-up')

@auth.route('/signup', methods=['POST'])
def signup_post():
    """사용자 가입"""
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()  # if this returns a user, then the email already exists in database

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    try:
        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = User(email=email, name=name, password=password)

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
    except Exception as msg:
        print("Exception : %s" % msg)
    finally:
        db.session.close()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required   #인증하기를 원하는 함수
def logout():
    logout_user() #logout_user() 라고 호출하여 login_manager에게 해당 세션의 사용자를 로그아웃하겠다고 알려줍니다.
    return redirect(url_for('main.index'))

@auth.route('/profile')
@login_required   #인증하기를 원하는 함수
def profile():
    #return render_template('content/profile.html', name=current_user.name)
    return render_template('content/profile.html', title='Profile')