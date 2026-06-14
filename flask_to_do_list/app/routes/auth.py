from flask import redirect , url_for , flash , Blueprint , render_template , request , session
from app import db
from app.models import Users
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth',__name__)




@auth_bp.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('tasks.view_tasks'))
    return render_template('home.html')



@auth_bp.route('/register',methods=["GET","POST"])
def register():
    if request.method=="POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            existing_user=Users.query.filter_by(username=username).first()
            if existing_user:
                flash('username already exist','danger')
                return redirect(url_for('auth.login'))
            new_user = Users(username=username)
            new_user.set_password(password)
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
        user = Users.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('login successful', 'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('invalid username or password', 'danger')

    # If already logged in, redirect to tasks
    if 'user_id' in session:
        return redirect(url_for('tasks.view_tasks'))

    return render_template('login.html')





@auth_bp.route('/logout')
def logout():
    session.pop('user_id',None)
    flash('logged out','info')
    return redirect(url_for('auth.login'))


