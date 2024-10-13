import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    isbn TEXT,
    published_year INTEGER,
    category TEXT,
    available_copies INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone_number TEXT,
    membership_date DATE)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Borrowing (
    borrowing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    member_id INTEGER,
    borrow_date DATE,
    due_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    staff_name TEXT,
    role TEXT,
    email TEXT,
    phone_number TEXT)''')

conn.commit()
conn.close()
