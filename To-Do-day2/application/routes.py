from flask import render_template, redirect, request, url_for
from application import app, db
from application.models import Tasks
from application.forms import InputForm 

@app.route('/')
@app.route('/home')
def home():
    all_tasks=Tasks.query.all()
    return render_template('home.html', all_tasks=all_tasks)

@app.route('/add', methods=['GET','POST'])
def add():
    form = InputForm()

    if form.validate_on_submit():
        new_task = Tasks(name=form.new_task.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/complete/<taskid>')
def complete(taskid):
    task_to_update = Tasks.query.get(taskid)
    task_to_update.complete = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/incomplete/<taskid>')
def incomplete(taskid):
    task_to_update = Tasks.query.get(taskid)
    task_to_update.complete = False
    db.session.commit()
    return redirect(url_for('home'))
''' 
@app.route('/update')
def update():
''' 

@app.route('/delete')
def delete():
    task_to_delete = Tasks.query.first()
    db.sessiom.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
