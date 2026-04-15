# Session 6 - Integrating HTML With FLASK Web Framework With HTTP VERBS(Get And POST)
# {%...%} used for writing conditions, loops in .html
# {{...}} experssion to print output in .html
# {#...#} this is used for comments in .html

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/final_result/<int:score>')
def final_result(score):
    return render_template('result2.html', result=score)


@app.route('/submit', methods=['POST'])
def submit():
    total_score = 0

    science = float(request.form['science'])
    maths = float(request.form['maths'])
    c = float(request.form['c'])
    datascience = float(request.form['datascience'])
    total_score = (science+maths+c+datascience)/4

    return redirect(url_for('final_result', score=total_score))


if __name__ == '__main__':
    app.run(debug=True)
