# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = '234YUJFTUILMVCFGK'

class RegisterForm(FlaskForm):
    """自定义表单的类，实现自己的注册的表单验证逻辑"""
    # 数据校验
    user_name = StringField(u'用户名',validators=[DataRequired(u'缺少用户名')] )
    psd1 = PasswordField(u'密码', validators=[DataRequired()])

    psd2 = StringField(u'确认密码',validators=[DataRequired(),EqualTo('psd1',u'密码不一致')] )

    Submit = SubmitField(u'注册' )


@app.route('/demo')
def demo():

    #创建自定义的对象
    register_form = RegisterForm()

    if request.method == 'POST':
        if register_form.validate_on_submit():
            user_name = request.form.get('user_name')
            psd1 = request.form.get('psd1')
            psd2 = request.form.get('psd2')
            return 'success %s-%s-%s' % (user_name, psd1, psd2)
        else:
            flash(u'参数有误')

    return render_template('template05_wtf.html',form=register_form)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        psd1 = request.form.get('psd1')
        psd2 = request.form.get('psd2')
        if not all([user_name,psd1,psd2]):
            flash(u'缺少参数')
        elif psd1 != psd2:
            return '密码不一致'
        else:
            return 'success %s-%s-%s'%(user_name,psd1,psd2)

    return render_template('template05_wtf.html')


if __name__ == '__main__':
    app.run(debug=True)
