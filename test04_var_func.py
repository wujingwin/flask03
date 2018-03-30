# -*- coding:utf-8 -*-
from flask import Flask,render_template,g,flash




app = Flask(__name__)
app.config['SECRET_KEY'] = '234YUJFTUILMVCFGK'

@app.route('/')
def index():
    g.name= 'lailaialia'
    print  g.name

    # 向flash消息队列中添加一条测试消息，将来在模板中取出来
    flash(u'这是测试消息')

    return render_template('template04_var_func.html')






@app.route('/order/<order_id>')
def order(order_id):
    return 'order %s' %order_id

if __name__ == '__main__':
    app.run(debug=True)