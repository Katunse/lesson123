import cgi
import sqlite3
from hashlib import sha256

form = cgi.FieldStorage()


username = form.getvalue('username')
password = form.getvalue('password')


hashed_password = sha256(password.encode()).hexdigest()


conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Проверяем, есть ли пользователь с таким именем и паролем
cursor.execute('SELECT * FROM users WHERE username=? AND password_hash=?', (username, hashed_password))
user = cursor.fetchone()

if user:
    
    print("Location: /messager.html\r\n\r\n")
else:
    print("Content-type:text/html\r\n\r\n")
    print("<h1>Неверное имя пользователя или пароль.</h1>")


conn.close()