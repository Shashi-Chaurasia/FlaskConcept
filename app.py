import re
from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    ename = db.Column(db.String(255), nullable = False)
    eemail = db.Column(db.String(255), nullable = False)
    designation = db.Column(db.String(255), nullable = False)
    salary = db.Column(db.Integer, nullable = False)
    address = db.Column(db.String(255), nullable = False)
    mobile = db.Column(db.String(255), nullable = False)
    # eemail = db.Column(db.String(255), nullable = False)
    date_created = db.Column(db.DateTime(),default=datetime.utcnow)

    def __repr__(self):
        return f'{self.sno} - {self.ename}'

@app.route("/" , methods = ['GET' , 'POST'])
def helloWorld():
    if request.method == 'POST':
        ename = request.form['ename']
        eemail = request.form['eemail']
        designation = request.form['designation']
        salary = request.form['salary']
        address = request.form['address']
        mobile = request.form['mobile']
        todo = Todo(ename = ename , eemail = eemail , designation = designation , salary = salary , address = address , mobile = mobile)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()  
    return render_template('index.html' , allTodo = allTodo)


@app.route("/show")
def products():
    
    return "<p> This is my first products </p>"

@app.route("/update/<int:sno>" , methods = ['GET' , 'POST'])
def update(sno):
    if request.method == 'POST':
        ename = request.form['ename']
        eemail = request.form['eemail']
        designation = request.form['designation']
        salary = request.form['salary']
        address = request.form['address']
        mobile = request.form['mobile']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.ename = ename
        todo.eemail = eemail
        todo.designation = designation
        todo.salary = salary
        todo.address = address
        todo.mobile = mobile
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html' , todo=todo)
    

    
  

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True ,port=8000)
