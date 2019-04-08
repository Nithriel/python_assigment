import sqlite3

conn = sqlite3.connect('canucks.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE canucks
          (id INTEGER PRIMARY KEY ASC, 
           first_name VARCHAR(250) NOT NULL,
           last_name VARCHAR(250) NOT NULL,
           date_of_birth VARCHAR(10) NOT NULL,
           position VARCHAR(100) NOT NULL,
           type VARCHAR(10) NOT NULL,
           height FLOAT,
           weight FLOAT,
           player_number INTEGER,
           shoot VARCHAR(1),
           hire_date VARCHAR(10),
           previous_team VARCHAR(250)
           )
          ''')

conn.commit()
conn.close()
