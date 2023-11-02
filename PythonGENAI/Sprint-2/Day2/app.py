from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, Welcome!"

@app.route('/greet/<username>')
def greet(username):
    greeting = f'Hello, {username}!'
    return greeting

@app.route('/farewell/<username>')
def farewell(username):
    return f'Goodbye, {username}!'

if __name__ == '__main__':
    app.run(debug=True)
