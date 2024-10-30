from . import app
from flask import request, redirect, url_for, render_template


@app.context_processor
def some_processor():
    def full_name(product):
        return '{0} / {1}'.format(product['category'], product['name'])
    return {'full_name': full_name}

@app.context_processor
def some_processor_static():
    return {'utc': "18:14"}


@app.route('/ctx')   # URL '/' to be handled by main() route handler
def ctx():
    return render_template("base.html", product=dict(category="cat", name="flask"))

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    return f'Hello, world!   {app.config["SECRET_KEY"]=} {app.instance_path=} {app.template_folder=}'

@app.route('/homepage') 
def home():
    """View for the Home page of your website."""
    return f"This is your homepage :) \n Your IP is {request.remote_addr} and you are using {request.user_agent}"

@app.route("/hi/<string:name>") # URL rule must start with a slash.
def greetings(name):
    """View function to greet the user by name."""
    name = name.upper()
    age = request.args.get("age")
    return f"Welcome {name=} {age=}!"


@app.route("/admin")
def admin():
    to_url = url_for("greetings", name="administrator") # return "/administrator"
    to_url = url_for("greetings", name="administrator", surname = "unknow") # return "/administrator?surname=unknow"
    print(to_url)
    return redirect(to_url)


