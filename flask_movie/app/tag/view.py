from flask import Blueprint, flash, redirect, url_for, render_template, request
from models import Tag
from .form import tagForm
from models import db

tagbp=Blueprint('tag','__name__')

@tagbp.route('/add/',methods=['GET','POST'])
def add():
    form=tagForm()
    if form.validate_on_submit():
        data=form.data
        print(form)
        print(form.data)
        tag=Tag.query.filter_by(name=data['name']).count()
        print(tag)
        if tag>=1:
            flash('标签已存在')
            return redirect(url_for('tag.add'))
        else:
            tag=Tag(name=data['name'])
            db.session.add(tag)
            db.session.commit()
            flash('标签添加成功！')
            return redirect((url_for('tag.add')))
    else:
        return render_template('tag/tag_add.html',form=form)
@tagbp.route('/edit/<int:id>/',methods=['GET','POST'])
def edit(id):
    form=tagForm()
    tag=Tag.query.get_or_404(id)
    if request.method=='GET':
        form.name.data=tag.name
    if form.validate_on_submit():
        data=form.data
        count=Tag.query.filter_by(name=data['name']).count()
        if count>=1:
            flash('名称已存在！')
            return redirect(url_for('tag.add'))
        else:
            tag.name=data['name']
            db.session.add(tag)
            db.session.commit()
            flash('修改标签成功！')
            return redirect(url_for('tag.list',id=id))
    else:
        return render_template('tag/tag_edit.html',form=form,tag=tag)
@tagbp.route('/delete/<int:id>')
def delete(id):
    tag = Tag.query.get_or_404(id)
    db.session.delete(tag)
    db.session.commit()
    flash('删除%s成功'%tag.name)
    return redirect(url_for('tag.list'))
@tagbp.route('/list/')
@tagbp.route('/list/<int:page>/')
def list(page=1):
    tags=Tag.query.paginate(page,5)
    return render_template('tag/tag_list.html',tags=tags)