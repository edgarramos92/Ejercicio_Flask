from flask import Flask, render_template, jsonify, request, redirect
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import numpy as np
import mysql.connector

#mysql = MySQL()
app = Flask(__name__)
conn = mysql.connector.connect(host="localhost",user="root",passwd="Ganjahman92", database = "BucketList")
cursor = conn.cursor()
# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'Ganjahman92'
#app.config['MYSQL_DATABASE_DB'] = 'mydatabase'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#app.config['MYSQL_DATABASE_PORT'] = 5050
#mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/Home')
def Home():
    return render_template('home.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showLogging')
def showLogging():
    return render_template('logging.html')

@app.route('/serv1')
def serv1():
    return render_template('serv1.html')

@app.route('/serv2')
def serv2():
    return render_template('serv2.html')

@app.route('/serv3')
def serv3():
    return render_template('serv3.html')

@app.route('/Term')
def Term():
    return render_template('Term.html')

@app.route('/Priv')
def Priv():
    return render_template('Priv.html')

@app.route('/Contact',methods=['POST','GET'])
def Contact():
    _name = request.form['inputname']
    _email = request.form['inputmail']
    _text = request.form['inputtext']
    print(_name, 'si funiono !!!!!')

    sql = "INSERT INTO contact2 (user_name,user_email,user_comment) VALUES (%s, %s, %s)"
    val = (_name, _email, _text)
    cursor.execute(sql, val)
#       print(cursor.rowcount, " bla bla ")
    conn.commit()
    return jsonify({'message':'Usuario creado correctamente!'})
    

@app.route('/Logging',methods=['POST','GET'])
def Logging():
    _email = request.form['inputemail']
    _password = request.form['inputpassword']
#    _term = request.form['Aceptar']


    sql = "SELECT * FROM tbl_user WHERE (user_username, user_password) = (%s,%s)"
    val = (_email,_password)
    cursor.execute(sql, val)
    res = cursor.fetchall()
    print _email,_password,np.size(res)
    if np.size(res) > 0:
	return redirect('/')
    else:
        return jsonify({'message':'Datos erroneos'})


@app.route('/signUp',methods=['POST','GET'])
def signUp():


    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
#    _term = request.form['Aceptar']
    print(_name)

    sql = "SELECT * FROM tbl_user WHERE user_username = %s"
    val = (_email,)
    cursor.execute(sql, val)
    res = cursor.fetchall()
    if np.size(res) == 0:
        sql = "INSERT INTO tbl_user (user_name,user_username,user_password) VALUES (%s, %s, %s)"
        val = (_name, _email, _password)
        cursor.execute(sql, val)
#       print(cursor.rowcount, " bla bla ")
        conn.commit()
        return jsonify({'message':'Usuario creado correctamente!'})
    elif np.size(res) > 0:
        return jsonify({'message':'Email ya fue registrado'})



    return 0
   

if __name__ == "__main__":
    app.run(debug=True, port = 5055)
