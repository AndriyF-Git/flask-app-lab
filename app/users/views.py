from . import user_bp
from flask import request, redirect, url_for, render_template, session, flash

credentials = {
    "user1": "password123",
    "user2": "mySecurePassword",
    "admin": "adminPass",
    "guest": "guest1234",
    "testUser": "testPass456"
}


@user_bp.route('/')
def main():
    return render_template("base.html")


#users

@user_bp.route("/hi/<string:name>")   #/hi/ivan?age=45
def greetings(name):
    name = name.upper()
    age = request.args.get("age", None, int)   

    return render_template("hi.html", 
                           name=name, age=age)

@user_bp.route("/admin")
def admin():
    to_url = url_for("users.greetings", name="administrator", age=45, _external=True)     # "http://localhost:8080/hi/administrator?age=45"
    print(to_url)
    return redirect(to_url)

@user_bp.route('/homepage')
def home():
    """View for the Home page of your website."""
    agent = request.user_agent

    return render_template("home.html", agent=agent)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["login"]
        password = request.form['password']
        # додати пароль в форму і виправити цей код, зробити функцію автентифікації
        if username in credentials:
            if credentials[username] == password:
                session['username'] = username
                flash("Success: session added successfully.", "success")
                return redirect(url_for('users.profile'))

    return render_template("login.html")

@user_bp.route('/profile')
def profile():
    if "username" in session:
        username_value = session["username"]
        return render_template("profile.html", username=username_value)
    flash("Invalid: Session.", "danger")
    return redirect(url_for("user_name.login"))


@user_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('users.login'))