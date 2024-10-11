import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''CREATE  TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

"""КОД ИЗ ПРЕДЫДУЩЕГО ЗАДАНИЯ"""
# # Заполните её 10 записями:
# for i in range(1, 11):
#     cursor.execute('INSERT INTO  Users(username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

# # Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))

# Удалите каждую 3ую запись в таблице начиная с 1ой:
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')


"""Удаление пользователя с id=6"""
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

'''Подсчёт кол-ва всех пользователей'''
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print(total_users)

'''Посчитать сумму всех балансов'''

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(all_balances)

print(all_balances / total_users)
# cursor.execute('SELECT AVG(balance) FROM Users')
# avg_balance = cursor.fetchone()[0]
# print(avg_balance)


connection.commit()
connection.close()
