from flask import Blueprint

userbp=Blueprint('user',__name__)

@userbp.route('/')
def index():
    return 'this is user index'

