from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class tagForm(FlaskForm):
    name=StringField('标签名称',
                     validators=[DataRequired('请输入标签名称！')])
    submit=SubmitField('提交')