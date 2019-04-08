import sqlite3

conn = sqlite3.connect('canucks.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE canucks
          ''')

conn.commit()
conn.close()
