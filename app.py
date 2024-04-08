from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Global list to store notes
notes = []

def init_db():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    # Create the users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, email TEXT)''')
    # Create the notes table
    c.execute('''CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY, note TEXT)''')
    conn.commit()
    conn.close()

init_db()  # Call the function to ensure our database and tables are set up


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def get_users():
    return render_template('users.html')

@app.route('/users', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
    conn.commit()
    conn.close()
    return redirect(url_for('get_users'))

@app.route('/notes', methods=['POST'])
def create_note():
    note = request.form['note']
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('INSERT INTO notes (note) VALUES (?)', (note,))
    conn.commit()
    conn.close()
    return redirect(url_for('notes_route'))

@app.route('/notes', methods=['GET', 'POST'])
def notes_route():
    if request.method == 'POST':
        note = request.form['note']
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute('INSERT INTO notes (note) VALUES (?)', (note,))
        conn.commit()
        conn.close()
        return redirect(url_for('notes_route'))
    else:
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute('SELECT note FROM notes')
        notes = c.fetchall()  # Fetch all notes from the database
        conn.close()
        return render_template('notes.html', notes=[note[0] for note in notes])

if __name__ == '__main__':
    app.run(debug=True)
