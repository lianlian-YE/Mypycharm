from app.tag.view import tagbp
from config import app
from app.movie.view import moviebp
app.register_blueprint(moviebp,url_prefix='/movie')
app.register_blueprint(tagbp,url_prefix='/tag')

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
