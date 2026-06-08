from flask import Flask , request , Response ,session, url_for, redirect , render_template, flash
from form import RegistrationForm

app = Flask(__name__)
app.secret_key="my-secret-key"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
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
    if username in valid_users and password==valid_users[username]:
        session["username"]=username;
        
    else:
        return "wrong credentials try again!"
    return redirect(url_for("welcome"))
    

    
@app.route("/feedback",methods=["GET","POST"])
def feedback():
    if request.method=="POST":
        name=request.form.get("name")
        opinion=request.form.get("feedback")
        if not name:
            flash("name can not be empty")
            return redirect(url_for("feedback"))
        if not opinion:
            flash("feedback can not be empty")
            return redirect(url_for("feedback"))
        return render_template("thankyou.html",name=name,feedback=opinion )
    
    return render_template("feedback.html")  


@app.route("/welcome")
def welcome():
    return render_template("welcome.html",is_topper=False,subjects=["maths",'history','english'])


@app.route("/wtf", methods=["GET", "POST"])
def form():
    form = RegistrationForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        flash(f"welcome, {name}! you registered successfully","success")
        return redirect(url_for("success"))
    return render_template("login.html",form=form )
     

@app.route("/success")
def success():
    return render_template("success.html")