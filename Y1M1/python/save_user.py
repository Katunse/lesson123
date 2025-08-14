import cgi
import sqlite3
from hashlib import sha256


form = cgi.FieldStorage()


username = form.getvalue('username')
email = form.getvalue('email')
password = form.getvalue('password')


hashed_password = sha256(password.encode()).hexdigest()


conn = sqlite3.connect('users.db')
cursor = conn.cursor()


cursor.execute('SELECT * FROM users WHERE username=? OR email=?', (username, email))
existing_user = cursor.fetchone()

if existing_user:
    print("Content-type:text/html\r\n\r\n")
    print("<h1>Пользователь с таким именем или электронной почтой уже существует!</h1>")
else:
    
    cursor.execute('''
        INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)
    ''', (username, email, hashed_password))
    conn.commit()


    print("Location: /messager.html\r\n\r\n")


conn.close()