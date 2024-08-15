import sqlite3

DATABASE_FILE = 'passwords.db'

def connect():
    return sqlite3.connect(DATABASE_FILE)

def initialize_database():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
                   id INTEGER PRIMARY KEY,
                   site TEXT NOT NULL,
                   username TEXT NOT NULL,
                   encrypted_password TEXT NOT NULL
                   )
                ''')
    conn.commit()
    conn.close()

def add_password(site, username, encrypted_password):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
            INSERT INTO passwords (site, username, encrypted_password)
            VALUES (?, ?, ?)
    ''', (site, username, encrypted_password))
    conn.commit()
    conn.close()

def delete_password(password_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(' DELETE from passwords where id=? ', (password_id,))
    conn.commit()
    conn.close()

def get_passwords(site):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT id, site, username, encrypted_password FROM passwords WHERE site=?', (site,))
    rows = cursor.fetchall()
    conn.close()
    return rows