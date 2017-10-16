from flask.ext.wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import PasswordField
from wtforms import TextAreaField
from wtforms.validators import Required
from wtforms.validators import EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('用户名:', validators=[Required()])
    password = PasswordField('密码:', validators=[Required()])
    password2 = PasswordField('确认密码', validators=
                              [Required(), EqualTo('password', message='两次密码不一致')])
    submit = SubmitField('确认,提交')

class LoginForm(FlaskForm):
    username = StringField('用户名:', validators=[Required()])
    password = PasswordField('密码:', validators=[Required()])
    submit = SubmitField('确认,提交')

class PostForm(FlaskForm):
    title = StringField('文章标题:', validators=[Required()])
    content = TextAreaField('文章内容', validators=[Required()])
    submit = SubmitField('发布')