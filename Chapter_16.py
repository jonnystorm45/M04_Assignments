# 16.1
import csv

text = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''

with open('books2.csv', 'wt') as fout:
    fout.write(text)

# 16.2
with open("books2.csv", 'rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

print(books)

# 16.3
text = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mieville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''

with open('books2.csv', 'wt') as fout:
    fout.write(text)

# 16.4
import sqlite3

try:
    conn = sqlite3.connect('books.db')
    curs = conn.cursor()
    curs.execute('''CREATE TABLE books
    (title VARCHAR(20),
    author VARCHAR(20),
    year INT)''')
except:
    pass

# 16.5
with open("books2.csv", 'rt') as fin:
    cin = csv.reader(fin)
    books = [row for row in cin]

del books[0]

ins = 'INSERT INTO books (title, author, year) VALUES(?, ?, ?)'
for book in books:
    curs.execute(ins, book)

# 16.6
curs.execute('SELECT * from books ORDER BY title')

for book in curs.fetchall():
    print(*book, sep=', ')

print()
# 16.7
curs.execute('SELECT * from books ORDER BY year')

for book in curs.fetchall():
    print(*book, sep=', ')

curs.close()
conn.close()

print()
# 16.8
import sqlalchemy as sa

conns = sa.create_engine('sqlite:///books.db')

rows = conns.execute('select title from books order by title asc')

for row in rows:
    print(row)
