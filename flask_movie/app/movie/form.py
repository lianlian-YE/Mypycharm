from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField,FileField,TextAreaField,SelectField
from wtforms.validators import DataRequired

from models import Tag


class movieForm(FlaskForm):
    title=StringField(
        '电影名',
        validators=[DataRequired()]
    )
    url=FileField(
        '文件',
        validators=[FileAllowed(['mp4','avi'])]
    )
    info=TextAreaField(
        '简介',
        validators=[DataRequired()]
    )
    logo=FileField(
        '封面',
        validators=[FileAllowed(['png','jpg'])]
    )
    star = SelectField(
        '星级',
        validators=[DataRequired()],
        coerce=int,
        choices=[(1, '1星'), (2, '2星'), (3, '3星'), (4, '4星'), (5, '5星')]
    )
    tag_id=SelectField(
        '标签',
        validators=[DataRequired()],
        coerce=int
    )
    area=StringField(
        '地区',
        validators=[DataRequired()]
    )
    length=StringField(
        '时长'
    )
    release_time=StringField(
        '上映时间'
    )
    def __init__(self,*args,**kwargs):
        super(movieForm,self).__init__(*args,**kwargs)
        self.tag_id.choices=[(tag.id,tag.name) for tag in Tag.query.all()]
