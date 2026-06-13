from flask import redirect , url_for , flash , Blueprint , render_template , request , session
from app import db
from app.models import Task, Users


tasks_bp = Blueprint('tasks',__name__)

@tasks_bp.route('/')
def view_tasks():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user_id = session['user_id']
    tasks = Task.query.filter_by(user_id=user_id).all()
    if session.get('user_id'):
                passeduser = Users.query.get(session['user_id'])
    return render_template('tasks.html',tasks=tasks,passedusername=passeduser.username)


@tasks_bp.route('/add',methods=["GET","POST"])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
     
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status='pending',user_id=session['user_id'])
        db.session.add(new_task)
        db.session.commit()
        flash('task added successfully','success')
    
    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/toggle/<int:task_id>',methods=["GET","POST"])
def toggle_status(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status=="pending":
            task.status="working"
        elif task.status=="working":
            task.status="done"
        else:
            task.status="pending"
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/clear',methods=["POST"])
def clear_tasks():
    
    Task.query.filter_by(user_id=session['user_id']).delete()
    db.session.commit()
    flash("all tasks cleared","info")
    return redirect(url_for('tasks.view_tasks')  )

