from flask import Flask, Response , request , url_for , redirect , session

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/login",methods=["GET","POST"])
def login():

    if request.method=="POST":
        userchoice = request.form.get("choice")
        if userchoice=="login":
            return redirect(url_for("loginpage"))
        else:
            return "invalid choice try again"
    return '''
          <form method="POST">
    <h2>Selection for login or just view</h2>

    <input
        type="text"
        placeholder="Enter here"
        name="choice"
    >

    <button type="submit">Submit</button>
</form>

'''


@app.route("/loginpage")
def loginpage():
    return "this is the login page"