import sqlite3

conn = sqlite3.connect("birthdays.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS birthdays (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    birthday TEXT,
    image TEXT
)
""")

cursor.execute("""
INSERT INTO birthdays (name, birthday, image)
VALUES
('Maryline', '06-01', 'maryline.jpg'),
('anaya', '06-01', 'anaya.jpg'),
('Taylor', '12-13', 'taylor.jpg'),
('Priyanka', '07-18', 'priyanka.jpg')
""")

conn.commit()

conn.close()

print("Database created")