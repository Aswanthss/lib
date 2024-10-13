from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books')
def books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
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

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Books (title, author, isbn, published_year, category, available_copies) VALUES (?, ?, ?, ?, ?, ?)",
                       (title, author, isbn, published_year, category, available_copies))
        conn.commit()
        conn.close()

        return redirect(url_for('books'))

    return render_template('add_book.html')

@app.route('/members')
def members():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
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

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Members (first_name, last_name, email, phone_number, membership_date) VALUES (?, ?, ?, ?, ?)",
                       (first_name, last_name, email, phone_number, membership_date))
        conn.commit()
        conn.close()

        return redirect(url_for('members'))

    return render_template('add_member.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
