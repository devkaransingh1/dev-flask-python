from flask import Flask , request , Response ,session, url_for, redirect , render_template

app = Flask(__name__)
app.secret_key="supersecret"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")
    valid_users={
        'rajat':'tonystark',
        'krishna':'098',
        'tisha':'1234'
    }
    if username in valid_users and password==valid_users[username ]:
        return render_template("welcome.html",name=username)
    else:
        return "wrong credentials try again!"
    
