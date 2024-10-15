from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello, world!'

@app.route('/homepage')
def home():
    """View for the Home page of your website."""
    return f"<h1>This is your homepage :) </h1>"

@app.route('/hi/<string:name>/<int:age>')
def greetings(name, age):
    name = name.upper()
    year = 2024 - age
    return f"Welcome {name=} {year=}"


if __name__ == '__main__':
    app.run(debug=True)