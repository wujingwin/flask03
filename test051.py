# -*- coding:utf-8 -*-
from flask import Flask, render_template, request,flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '234YUJFTUILMVCFGK'

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
