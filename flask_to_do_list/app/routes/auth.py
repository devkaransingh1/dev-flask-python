from flask import redirect , url_for , flash , Blueprint , render_template , request , session
from app import db
from app.models import Users

auth_bp = Blueprint('auth',__name__)


@auth_bp.route('/register',methods=["GET","POST"])
def register():
    if request.method=="POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            new_user=Users(username=username,password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("user registered successfully, Login now.","success")
            return redirect(url_for('auth.login'))
    return render_template("register.html")


@auth_bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print("Entered username:", username)
        print("Entered password:", password)
        users = Users.query.all()
        for u in users:
            print("DB:", u.username, u.password)
            
        user = Users.query.filter_by(username=username,password=password).first()
        if user:
            session['user'] = user.username
            flash('login successful', 'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('invalid username or password', 'danger')

    # If already logged in, redirect to tasks
    if 'user' in session:
        return redirect(url_for('tasks.view_tasks'))

    return render_template('login.html')



@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash('logged out','info')
    return redirect(url_for('auth.login'))
         