from os import path

from flask import Blueprint, render_template, flash, redirect, url_for, request
from config import app, db

from app.movie.form import movieForm
from models import Movies, opLog

moviebp=Blueprint('movie','__name__')

@moviebp.route('/add/',methods=['GET','POST'])
def add():
    form=movieForm()
    if form.validate_on_submit():
        file_url=form.url.data.filename
        file_logo=form.logo.data.filename
        form.url.data.save(path.join(app.config['MOVIE_UP_DIR'],file_url))
        form.logo.data.save(path.join(app.config['LOGO_UP_DIR'],file_logo))
        movie = Movies(
            title=form.data['title'],
            url=file_url,
            info=form.data['info'],
            logo=file_logo,
            star=int(form.data["star"]),
            tag_id=int(form.data["tag_id"]),
            area=form.data["area"],
            release_time=form.data["release_time"],
            length=form.data["length"]
        )
        db.session.add(movie)
        db.session.commit()
        flash('添加电影成功')
        oplog = opLog(user_id=1,
                      ip=request.remote_addr,
                      reason='添加电影%s信息' % (movie.title)
                      )
        db.session.add(oplog)
        db.session.commit()
        return redirect(url_for('movie.add'))
    return render_template('movie/movie_add.html',form=form)

@moviebp.route('/list/')
@moviebp.route('/list/<int:page>/')
def list(page=1):
    movies=Movies.query.order_by(Movies.add_time).paginate(page,5)
    return render_template('movie/movie_list.html',movies=movies)
@moviebp.route('/delete/<int:id>/')
def delete(id):
    movie=Movies.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    flash('电影%s删除成功'%movie.title)
    oplog = opLog(user_id=1,
                  ip=request.remote_addr,
                  reason='删除电影%s信息' % (movie.title)
                  )
    db.session.add(oplog)
    db.session.commit()
    return redirect(url_for('movie.list'))
@moviebp.route('/edit/<int:id>/',methods=['GET','POST'])
def edit(id):
    form=movieForm()
    movie=Movies.query.get_or_404(id)
    if request.method=='GET':
        form.title.data = movie.title
        form.info.data = movie.info
        form.tag_id.data = movie.tag_id
        form.star.data = movie.star
        form.area.data = movie.area
        form.length.data = movie.length
        form.release_time.data = movie.release_time
    if form.validate_on_submit():
        movie_count=Movies.query.filter_by(title=form.title.data).count()
        if movie_count>=1:
            flash('电影%s已存在'%movie.title.data)
            return redirect(url_for('movie.edit',id=id))
        movie.title = form.title.data
        movie.info = form.info.data
        movie.tag_id = form.tag_id.data
        movie.star = form.star.data
        movie.area = form.area.data
        movie.length = form.length.data
        movie.release_time = form.release_time.data
        db.session.add(movie)
        db.session.commit()
        flash('电影修改成功')
        oplog = opLog(user_id=1,
                      ip=request.remote_addr,
                      reason='修改电影%s信息' % (form.title.data)
                      )
        db.session.add(oplog)
        db.session.commit()
        return redirect(url_for('movie.list'))
    else:
        return render_template('movie/movie_edit.html',form=form)
