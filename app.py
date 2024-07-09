from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route('/login')
def login_page():
  return "welcome to the login page"


@app.route('/signup')
def signup_page():
  return "welcome to the Signup page"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
