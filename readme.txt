for setup migrations file in flask
1. pip install Flask-Migrate

2. 
for example: 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from flask_migrate import Migrate
migrate = Migrate(app, db) --app is main file where you will run the aplicaton

3. flask db init  --this will create a migrations/versions in the versions folder all of of your changes will be there
4. flask db migrate

NOTE: Then each time the database models change repeat the migrate and upgrade commands.