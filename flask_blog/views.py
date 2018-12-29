from config import app
from flask import render_template
from login.views import userbp

from login_form import loginForm
app.register_blueprint(userbp,url_prefix='/user')

@app.route('/login/')
def login():
    form=loginForm()
    return render_template('login.html',form=form)
