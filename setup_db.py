from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Get the absolute path of the database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'library.db')

def get_db_connection():
    conn = sqlite3.connect(db_path)
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        isbn TEXT,
        published_year INTEGER,
        category TEXT,
        available_copies INTEGER
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Members (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        phone_number TEXT,
        membership_date DATE
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Borrowing (
        borrowing_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        member_id INTEGER,
        borrow_date DATE,
        due_date DATE,
        return_date DATE,
        FOREIGN KEY (book_id) REFERENCES Books(book_id),
        FOREIGN KEY (member_id) REFERENCES Members(member_id)
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categories (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Staff (
        staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
        staff_name TEXT,
        role TEXT,
        email TEXT,
        phone_number TEXT
    )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized and tables created.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books')
def books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Books';")
    if cursor.fetchone() is None:
        print("Books table does not exist.")
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    conn.close()
    return render_template('books.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        published_year = request.form['published_year']
        category = request.form['category']
        available_copies = request.form['available_copies']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Books (title, author, isbn, published_year, category, available_copies) VALUES (?, ?, ?, ?, ?, ?)",
                       (title, author, isbn, published_year, category, available_copies))
        conn.commit()
        conn.close()

        return redirect(url_for('books'))

    return render_template('add_book.html')

@app.route('/members')
def members():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Members';")
    if cursor.fetchone() is None:
        print("Members table does not exist.")
    cursor.execute("SELECT * FROM Members")
    members = cursor.fetchall()
    conn.close()
    return render_template('members.html', members=members)

@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        membership_date = request.form['membership_date']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Members (first_name, last_name, email, phone_number, membership_date) VALUES (?, ?, ?, ?, ?)",
                       (first_name, last_name, email, phone_number, membership_date))
        conn.commit()
        conn.close()

        return redirect(url_for('members'))

    return render_template('add_member.html')

if __name__ == '__main__':
    init_db()
    app.run(host='127.0.0.1', port=5000)
