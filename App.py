from flask import Flask, jsonify,request
from psycopg2.extras import RealDictCursor
import database
app=Flask(__name__)
database.init_db()
@app.route('/')
def home():
    return jsonify({'message':'API running!'} )
@app.route('/students')
def get_students():
    conn= database.get_connection()
    cur= conn.cursor()
    cur.execute('SELECT * FROM students')
    rows=cur.fetchall()
    cur.close();  conn.close()
    return jsonify(rows)
@app.route('/students',methods=['POST'])
def create_student():
    data=request.get_json()
    conn= database.get_connection()
    cur=conn.cursor()
    cur.execute('''
        `INSERT INTO students(name,grade,age)`
                VALUES(%s,%s,%s),
                (data['name'],data['grade'],data['age'])

    ''')
    conn.commit(); cur.close(); conn.close(); 
    return jsonify({"message":'person created'}), 201
                   