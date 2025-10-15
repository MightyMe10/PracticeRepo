from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  description TEXT,
                  status TEXT DEFAULT 'pending')''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    # SQL Injection vulnerability
    query = f"INSERT INTO tasks (title, description) VALUES ('{title}', '{description}')"
    c.execute(query)
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        # SQL Injection vulnerability
        query = f"UPDATE tasks SET title='{title}', description='{description}', status='{status}' WHERE id={task_id}"
        c.execute(query)
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = c.fetchone()
    conn.close()
    
    if not task:
        return "Task not found", 404
    
    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)