# Session 7 - Creating API

from flask import Flask, render_template, request, redirect, url_for,jsonify

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    c_val = float(dict(data)['c'])
    
    return jsonify(a_val+b_val+c_val)


if __name__ == '__main__':
    app.run(debug=True)