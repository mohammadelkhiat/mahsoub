from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mahsoub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
from flask import request, jsonify

@app.route('/add-exercise', methods=['POST'])
def add_exercise():
    data = request.json
    exercise = Exercise(
        name=data['name'],
        repetitions=data['repetitions'],
        weight=data.get('weight'),
        duration=data.get('duration')
    )
    db.session.add(exercise)
    db.session.commit()
    return jsonify({'message': 'Exercise added!'}), 201

@app.route('/exercises', methods=['GET'])
def get_exercises():
    # Query all exercise records from the database
    exercises = Exercise.query.all()
    # Transform the data into a list of dictionaries for easy JSON conversion
    exercises_data = [
        {
            'id': exercise.id,
            'name': exercise.name,
            'repetitions': exercise.repetitions,
            'weight': exercise.weight,
            'duration': exercise.duration,
            'created_at': exercise.created_at
        }
        for exercise in exercises
    ]
    return jsonify(exercises_data)

@app.route('/edit-exercise/<int:id>', methods=['PUT'])
def edit_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return jsonify({'error': 'Exercise not found'}), 404

    data = request.json
    exercise.name = data.get('name', exercise.name)
    exercise.repetitions = data.get('repetitions', exercise.repetitions)
    exercise.weight = data.get('weight', exercise.weight)
    exercise.duration = data.get('duration', exercise.duration)

    db.session.commit()
    return jsonify({'message': 'Exercise updated!'})

from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"  # Redirects to login page if not logged in

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # Hash passwords in a real app!
            login_user(user)
            return redirect(url_for('index'))
        flash("Invalid credentials!")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user is None:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful!")
            return redirect(url_for('login'))
        flash("Username already exists!")
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)

if __name__ == '__main__':
    db.create_all()  # Creates tables (users.db)
    app.run(debug=True)
