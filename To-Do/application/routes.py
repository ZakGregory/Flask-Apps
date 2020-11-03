from application import app, db
from application.models import Tasks

@app.route('/')
def home():
    all_tasks=Tasks.query.all()
    all_tasks_list=""
    for tasks in all_tasks:
        all_tasks_list+="<br>" + tasks.name
    return all_tasks_list   


@app.route('/add/<newtask>')
def add(newtask):
    new_task= Tasks(name=newtask)
    db.session.add(new_task)
    db.session.commit()
    return "New task added"

'''
@app.route('/complete')
def complete():
   #

@app.route('/incomplete')
def incomplete():
    #
 
@app.route('/update')
def update():
    #

@app.route('/delete')
def delete():
    #
'''
