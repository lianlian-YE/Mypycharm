from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, current_user
from auth import authbp
from auth.form import LoginForm,RegistrationForm
from configs import db, send_email
from models import User

@authbp.route('/login/',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('index'))
        flash('invalid username or password')
    return render_template('auth/login.html',form=form)
@authbp.route('/register/',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        # user=User(email=form.data.email,
        #           uname=form.data.username,
        #           password=form.data.password)
        user=User(email=form.email.data,
                  uname=form.username.data,
                  password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token=user.generate_confirmation_token()
        send_email(user.email,'Confirm your account',
                   'auth/email/confirm',user=user,token=token)
        flash('A confirmnation email has been sent to you by email')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form=form)

@authbp.route('/logout/')
@login_required
def logout():
    login_user()    #删除并重设用户会话
    flash('you have been logout')
    redirect(url_for('index'))      #重定向至首页

@authbp.route('/confirm/<token>/')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('index'))
    if current_user.confirm(token):
        flash('you can confirm your account. thanks!')
    else:
        flash('the confirmation link is invalid or has expired.')
    return redirect(url_for('index'))
@authbp.route('/confirm/')
@login_required
def resend_confirmation():
    token=current_user.generate_confirmation_token()
    send_email(current_user.email,'Confirm your account',
               '/auth/email/confirm',user=current_user,token=token)
    flash('A new confirmation eamil has been sent to you by email')
    return redirect(url_for('index'))
@authbp.before_app_request
def before_request():
    if current_user.is_authenticated \
        and not current_user.confirmed \
        and request.endpoint[:5]!='auth,' \
        and request.endpoint!='static':
        return redirect(url_for('auth.unconfirmed'))
@authbp.route('/unconfirmed/')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('index'))
    return render_template('auth/unconfirmed.html')
