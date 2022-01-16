from flask import Flask, render_template, request, redirect
#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
from classes.Tasks import Task

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
       task = request.form['new_task']

       try:
           newTask=Task()
           newTask.addTask(task)
           return redirect('/')
       except:
           return 'There was an issue adding your task'

    else:
        data=Task()
        return render_template("index.html", tasks=data.allTasks())


@app.route('/delete/<int:id>')
def delete(id):
    try:
        task_to_delete=Task()
        task_to_delete.deleteTask(id)
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
     
    if request.method == 'POST':
        taskUpdated = request.form['taskUpdated']
        
        try:
            task_to_update=Task()
            task_to_update.updateTask(taskUpdated,id)
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        task=Task() 
        return render_template('update.html', data=task.getTask(id))

@app.route('/alterState')
def alterState():
    id = request.args.get('id')
    state = request.args.get('state')
    if state=='0':
        newstate=1
    else:
        newstate=0
        
    try:
        task_alter_state=Task()
        task_alter_state.alterTask(newstate,id)
        return redirect('/')
    except:
        return 'There was an issue altering your task'


if __name__ == "__main__":
    app.run(debug=True, port=5050)