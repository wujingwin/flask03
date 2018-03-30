# -*- coding:utf-8 -*-
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():

    my_list = [1,2,3,4,5,6,7,8]

    context = {
        'my_list':my_list,
    }

    return render_template('template01_for_if.html',**context )


if __name__ == '__main__':

    app.run(debug=True)