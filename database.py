import psycopg2,os
 
from dotenv import load_dotenv
load_dotenv() 
def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv('DB_PORT'),
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        sslmode=os.getenv('DB_SSLMODE'),

    )
def init_db():
    conn =get_connection()
    cur =conn.cursor()
    cur.execute('''
            CREATE TABLE IF NOT EXISTS students(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                grade VARCHAR(5) NOT NULL,
                age INT

                    
                )   
                    
                  '''  )
    conn.commit()
    cur.close()
    conn.close()
    print('Database ready!')
