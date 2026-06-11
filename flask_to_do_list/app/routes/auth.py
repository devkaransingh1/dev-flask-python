from flask import redirect , url_for , flash , Blueprint , render_template , request , session

auth_bp = Blueprint('auth',__name__)

USER_CREDENTIALS = {
    'username':'admin',
    'password':'1234'
}

@auth_bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
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
         