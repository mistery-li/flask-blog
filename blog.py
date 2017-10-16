from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy



# 当下文件夹绝对路径

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)


class NameForm(FlaskForm):
    name = StringField('你叫什么名字', validators=[Required()])
    submit = SubmitField('提交')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data)
        if user is None:
            user = User(name=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))

@app.route('/<username>')
def user(username):
    return render_template('user.html', name=username)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    manager.run()