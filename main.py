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
