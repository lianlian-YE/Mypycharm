from flask import Blueprint,render_template

moviebp=Blueprint('movie','__name__')

@moviebp.route('/add/')
def add():
    return render_template('movie/movie_add.html')