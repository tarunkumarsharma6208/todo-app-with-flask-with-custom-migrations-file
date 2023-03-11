from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)

#here is database configrations
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/flaskdb'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#models
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(1000), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create the table this is for first time it run to create sql table in database
# with app.app_context():
#     db.create_all()

#views
@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    description = request.form.get('description')

    todo = Todo(title=title, description=description)
    db.session.add(todo)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)