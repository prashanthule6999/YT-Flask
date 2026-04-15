# Building Url Dynamically In Flask Web Framework
# Variable rules & URL Building
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my YOUTUBE Channel.'

@app.route('/success/<int:score>')
def success(score):
    return 'The person is pass and has scored '+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person is fail and has scored '+str(score)

@app.route('/on_boder/<int:score>')
def on_boder(score):
    return "<html><body><h1>Passed on boder</h1></body></html>"

# Result Checker
@app.route('/results/<int:marks>')
def result(marks):
    result = ""
    if marks < 50:
        result = 'fail'    
    elif marks == 50:
        result = 'on_boder'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))

if __name__ == "__main__":
    app.run(debug=True)
