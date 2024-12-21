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
