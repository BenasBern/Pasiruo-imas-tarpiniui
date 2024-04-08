from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Global list to store notes
notes = []

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
    print(f"Creating user: {username} with email: {email}")
    return redirect(url_for('get_users'))

@app.route('/notes', methods=['GET', 'POST'])
def notes_route():
    if request.method == 'POST':
        note = request.form['note']
        notes.append(note)
        return redirect(url_for('notes_route'))
    else:
        return render_template('notes.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
