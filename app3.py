# Session 5 - Integrating HTML With FLASK Web Framework With HTTP VERBS(Get And POST)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    return render_template('result1.html', result='PASS & marks is '+str(score))


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result1.html', result="FAIL & marks is "+str(score))


@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        total_score = 0
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+c+datascience)/4
        res = ""
        if total_score >= 50:
            res = "success"
        else:
            res = "fail"
        return redirect(url_for(res, score=total_score))


if __name__ == '__main__':
    app.run(debug=True)
