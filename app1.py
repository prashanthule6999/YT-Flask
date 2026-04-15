# Sample Flask Web Application Skeleton
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome To Home Page & My Channel.'

@app.route('/member')
def member():
    return 'Welcome to my youtube'


if __name__ == '__main__':
    app.run(debug=True)