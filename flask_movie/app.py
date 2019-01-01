from flask import request, render_template

from app.tag.view import tagbp
from config import app, db
from app.movie.view import moviebp
from models import Tag, Movies

app.register_blueprint(moviebp,url_prefix='/movie')
app.register_blueprint(tagbp,url_prefix='/tag')


@app.route('/')
@app.route('/<int:page>/')
def index(page=1):
    # 查询所有的标签
    tags = Tag.query.all()
    # http://127.0.0.1:5002/1/?tid=2&star=0
    # 获取用户需要查找的标签
    tid = int(request.args.get('tid', 0))
    star = int(request.args.get('star', 0))
    movies = Movies.query
    if tid != 0:
        movies = movies.filter_by(tag_id=tid)
    if star != 0:
        movies = movies.filter_by(star=star)
    return  render_template('index.html',
                            tags = tags,
                            movies = movies.paginate(page, 5),
                            p = dict(tid=tid, star=star))

@app.route('/play/<int:id>/')
def play(id):
    movie = Movies.query.get_or_404(id)
    if not movie.play_num:
        movie.play_num = 0
    movie.play_num += 1
    db.session.add(movie)
    db.session.commit()
    return  render_template('play.html', movie=movie)
if __name__ == '__main__':
    app.run()
