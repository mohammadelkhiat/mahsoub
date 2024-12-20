from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = "mahsoub.db"

# Initialize the database
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS exercises (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT NOT NULL,
                exercise_name TEXT NOT NULL,
                counts INTEGER,
                weight REAL,
                duration TEXT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    print("Database initialized!")

# Add an exercise
@app.route("/add", methods=["POST"])
def add_exercise():
    data = request.get_json()
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO exercises (user, exercise_name, counts, weight, duration)
            VALUES (?, ?, ?, ?, ?)
        """, (data['user'], data['exercise_name'], data['counts'], data['weight'], data['duration']))
        conn.commit()
    return jsonify({"message": "Exercise added successfully!"}), 201

# View all exercises
@app.route("/history/<string:user>", methods=["GET"])
def view_history(user):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM exercises WHERE user = ? ORDER BY date DESC
        """, (user,))
        exercises = cursor.fetchall()
    return jsonify({"history": exercises})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
