import psycopg2

# Connect to the database

def create_table():
  conn = psycopg2.connect(
    dbname='student',
    user='postgres',
    password='admin123',
    host='localhost',
    port='5432'
  ) 

  cur = conn.cursor()
  cur.execute('''CREATE TABLE teacher(
              ID SERIAL,
              NAME TEXT,
              AGE INT,
              ADDRESS TEXT
  )''')
  conn.commit()
  conn.close()

# Insert data into the table

def insert_data():
  conn = psycopg2.connect(
      dbname='student',
      user='postgres',
      password='admin123',
      host='localhost',
      port='5432'
    )

  cur = conn.cursor()
  cur.execute("INSERT INTO teacher (NAME, AGE, ADDRESS) VALUES (%s, %s, %s)", ('Dave', 29, 'Canada'))
  conn.commit()
  conn.close()
  
