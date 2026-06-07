from flask import Flask, request , Response , url_for , redirect , session 

app = Flask(__name__) 
app.secret_key = "supersecret"

@app.route("/")
def home():
    return "hello user, this is my first flask app!"

@app.route("/submit" , methods=["GET","POST"])
def submit():
    if request.method  == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username=="admin" and password=="123":
            session["user"]=username
            return redirect(url_for("welcome"))
        else:
            return Response("invalid credentials. try again.", mimetype="text/plain")
        
    return '''
            <h2>login form</h2>
            <form method="POST">
            username: <input type="text" name="username"><br>
            password: <input type="text" name="password"><br>
            <input type="submit" value="login"> 
            </form>
'''


@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>welcome, {session["user"]}</h2>
        <a href={url_for('logout')}></a>
        '''
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("submit"))