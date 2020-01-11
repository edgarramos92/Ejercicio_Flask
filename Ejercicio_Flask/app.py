#!/usr/bin/env python
from flask import Flask, render_template, json,  jsonify, request, url_for, redirect, session
from werkzeug import generate_password_hash, check_password_hash
import numpy as np
import mysql.connector
from datetime import datetime
import os
import uuid


#mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'
conn = mysql.connector.connect(host="localhost",user="root",passwd="Ganjahman92", database = "BucketList")
cursor = conn.cursor()
# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'Ganjahman92'
#app.config['MYSQL_DATABASE_DB'] = 'mydatabase'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#app.config['MYSQL_DATABASE_PORT'] = 5050
#mysql.init_app(app)

# Default setting
pagelimit = 4


@app.route('/')
def main():
	return render_template('index.html')

@app.route('/Home')
def Home():
	print (session.get('id') )
	if session.get('id'):
		return render_template('home.html', bienvenido = 'Has iniciado sesion en IoTSol')
	else:
		return render_template('errorLog.html',error = 'Acceso no autorizado')

@app.route('/logout')
def logout():
	session.pop('id',None) 
	return redirect('/')

@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')

@app.route('/dash')
def dash():
	if session.get('id'):
		return render_template('dash.html')
	else:
		return render_template('errorLog.html',error = 'Acceso no autorizado')

@app.route('/AddWish')
def AddWish():
	if session.get('id'):
		return render_template('wishpage.html')
	else:
		return render_template('errorLog.html',error = 'Acceso no autorizado')

@app.route('/showLogging')
def showLogging():
	return render_template('logging.html')

@app.route('/Term')
def Term():
	return render_template('Term.html')

@app.route('/Priv')
def Priv():
	return render_template('Priv.html')

@app.route('/addlike',methods=['POST'])
def addlike():
	try:
		if session.get('id'):
			_user = session.get('id')
			_like = request.form['like']
			_wishid = request.form['wish']
			sql = "select 1 from tbl_likes where (wish_id, user_id) = (%s,%s)"
			val = (_wishid,_user)
			cursor.execute(sql,val)
			res = cursor.fetchall()
			print (res)
			if len(res) == 1:
				sql = "update tbl_likes set wish_like = %s where (wish_id, user_id) = (%s,%s)"
				val =(_like,_wishid,_user)
				cursor.execute(sql,val)
				conn.commit()
				return json.dumps({'status':'Like Guardado'})
			else:
				val = (_wishid,_user,_like)
				sql = "INSERT INTO tbl_likes (wish_id,user_id,wish_like) VALUES (%s, %s, %s)"
				cursor.execute(sql, val)
				conn.commit()
				return json.dumps({'status':'Like Guardado 2'})
	except Exception as e:
		return json.dumps({'status':str(e)} )

@app.route('/getallwish', methods=['GET'])
def getallwish():
	try:
		if session.get('id'):
			_user = session.get('id')
			sql = "SELECT  wish_id, wish_title, wish_description, wish_file_path, wish_user_id, wish_date FROM tbl_wish WHERE  wish_private = 0"
			cursor.execute(sql)
			res = cursor.fetchall()

			res2 = []
			wdict = []
			_likes = []
			#print (res)
			for i in res:
				res2.append(i[0])
			for i,j,k in zip(res2,res, range(len(res))):
				sql = "SELECT  wish_like FROM tbl_likes WHERE  wish_id = %s"

				val = (i,)
				cursor.execute(sql,val)
				res3 = cursor.fetchall()
				sql = "SELECT  wish_like FROM tbl_likes WHERE  (wish_id, user_id) = (%s,%s)"
				val = (i,_user)
				cursor.execute(sql,val)
				res4 = cursor.fetchall()
				val = (j[4],)
				sql = "SELECT  user_name FROM tbl_user WHERE  user_id = %s"
				cursor.execute(sql,val)
				res5 = cursor.fetchall()
				#print ('El post ',j[0],' del usuario',res5,' le gusto al usuario: ',res4)
				print('res4  : ',res4, ' res3 (con np): ',np.sum(res3) )
				var = np.sum(res3)
				_likes.append((j[0], int(var), res4, res5))
				#_likes.append((j[0], 0, 0, res5))	
			print(' _likes : : ',_likes)
			for i,j in zip(res,_likes):
				print ('id', i[0],' likes',j[1], 'usuario ', j[3])
				wish_dict = {'Id': i[0],'Titulo': i[1],'Descripcion': i[2],'Path': i[3], 'Likes': j[1], 'Liked': j[2], 'Usuario':  j[3], 'Fecha': i[5] }
				wdict.append(wish_dict)
			#print (np.size(wdict))
			return json.dumps(wdict)
		else:
			print (np.size(wdict))
			return json.dumps({'status':'Acceso no autorizado'})
	except Exception as e:
		
		return json.dumps({'status':str(e)} )


@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		extension = os.path.splitext(file.filename)[1]
		f_name = str(uuid.uuid4()) + extension
		app.config['UPLOAD_FOLDER'] = 'static/uploads'
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
		return json.dumps({'filename':f_name})

@app.route('/updatewish', methods=['POST'])
def updatewish():

	try:
		if session.get('id') :
			_id = request.form['id']
			_user = session.get('id')
			_desc = request.form['desc']
			_tit = request.form['tit']
			_filepath = request.form['filePath']
			_private = request.form['private']
			_done = request.form['done']
			#			print ('Este deberia ser el path de la imagen :',_filepath)
			#		print ('file path: ',_filepath)
			sql = "UPDATE tbl_wish SET wish_title = %s, wish_description = %s, wish_file_path = %s, wish_private = %s, wish_accomplished = %s WHERE  (wish_user_id, wish_id)  = (%s,%s)"
			val =(_tit,_desc,_filepath,_private,_done, _user,_id)
			cursor.execute(sql,val)
			conn.commit()
			return json.dumps({'status':'OK', 'off':pagelimit})
		else:
			return json.dumps({'status':'Acceso no autorizado'})
	except Exception as e:
		return render_template('errorLog.html',error = str(e))

@app.route('/delwish', methods=['POST'])
def delwish():
	try:
		if session.get('id') :
			_id = request.form['id']
			_user = session.get('id')

			sql = "DELETE FROM tbl_wish WHERE  (wish_user_id, wish_id)  = (%s,%s)"
			val =(_user,_id)
			cursor.execute(sql,val)
			conn.commit()

			return json.dumps({'status':'OK', 'off':pagelimit})
		else:
			return json.dumps({'status':'Acceso no autorizado'})
	except Exception as e:
		return render_template('errorLog.html',error = str(e))



@app.route('/getwishbyID',methods=['POST'])
def getwishbyID():
	try:

		if session.get('id'):
			_id = request.form['id']
			_user = session.get('id')

			sql = "SELECT  wish_id, wish_title, wish_description, wish_file_path, wish_private, wish_accomplished FROM tbl_wish WHERE  (wish_user_id,wish_id) = (%s,%s)"
			val = (_user,_id)
			cursor.execute(sql,val)
			res = cursor.fetchall()

			wish = []
			wish.append({'Id':res[0][0],'Titulo':res[0][1],'Descripcion':res[0][2], 'ruta':res[0][3], 'Privacidad':res[0][4], 'Completado':res[0][5]})
			return json.dumps(wish)
		else:
			return render_template('errorLog.html', error = 'Acceso no autorizado')
	except Exception as e:
		return render_template('errorLog.html',error = str(e))

@app.route('/addwish',methods=['POST'])
def addwish():
	
	try:
		if session.get('id'):
			_title = request.form['inputTitle']
			_desc = request.form['inputDesc']
			_user = session.get('id')

			if request.form.get('filePath') is None:
				_filepath = ''
			else:
				_filepath = request.form.get('filePath')
			if request.form.get('private') is None:
				_private = 0
			else:
				_private = 1
			if request.form.get('done') is None:
				_done = 0
			else:
				_done = 1
			print(_filepath,' el path del archivo')
			val = (_title,_desc,_user,datetime.now(),_filepath, _done,_private,)
			if len(val) == 7 and val[0] != '' and val[1] != '':
				sql = "INSERT INTO tbl_wish (wish_title,wish_description, wish_user_id, wish_date, wish_file_path, wish_accomplished , wish_private ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
				cursor.execute(sql, val)
				conn.commit()
				last_id = cursor.lastrowid
				print (last_id)
				sql = "INSERT INTO tbl_likes (wish_id, user_id, wish_like ) VALUES (%s, %s, %s)"
				val = (last_id, _user,0)
				cursor.execute(sql, val)
				conn.commit()
				return render_template('home.html', bienvenido = 'Agregaste un deseo nuevo!')
			else:
				return render_template('errorLog.html',error = 'Error ingresa todos los campos')
		else:
			return render_template('errorLog.html',error = 'error 1')
	except Exception as e:
		return render_template('errorLog.html',error = str(e))

@app.route('/getwish', methods = ['POST'])
def getwish():
#	print (session.get('id'), 'blabla ')
	try:
		if session.get('id'):
			_limit = pagelimit
			_off = request.form['offset']
			sql = "SELECT * FROM tbl_wish WHERE wish_user_id = %s ORDER BY wish_date DESC LIMIT %s OFFSET %s"
			val = (session.get('id'),_limit,int(_off))
			cursor.execute(sql,val)
			res = cursor.fetchall()

			sql2 = "SELECT * FROM tbl_wish WHERE wish_user_id = %s"
			val2 = (session.get('id'),)
			cursor.execute(sql2,val2)

			counter = len(cursor.fetchall())



			wdict = []
			response = []
			for i in res:
				wish_dict = {'Id': i[0],'Titulo': i[1],'Descripcion': i[2],'Fecha': i[4]}
				wdict.append(wish_dict)
			response.append(wdict)
			response.append({'total':counter, 'item' : pagelimit})
			return json.dumps(response)

		else:
			return render_template('errorLog.html',error = 'Acceso no autorizado')
	except Exception as e:
		return json.dumps({'status':str(e)})
	

@app.route('/Contact',methods=['POST','GET'])
def Contact():
	_name = request.form['inputname']
	_email = request.form['inputmail']
	_text = request.form['inputtext']
	

	sql = "INSERT INTO contact2 (user_name,user_email,user_comment) VALUES (%s, %s, %s)"
	val = (_name, _email, _text)
	cursor.execute(sql, val)
#	   print(cursor.rowcount, " bla bla ")
	conn.commit()
	return 0
	

@app.route('/Logging',methods=['POST'])
def Logging():
	try:
		_email = request.form['inputemail']
		_password = request.form['inputpassword']
		sql = "SELECT * FROM tbl_user WHERE (user_username, user_password) = (%s,%s)"
		val = (_email,_password)
		cursor.execute(sql, val)
		res = cursor.fetchall()

		if len(res) > 0:
			session['id']= res[0][0]
# 		print (session['id'])
			return redirect('/dash')
		else:
		   	return render_template('errorLog.html',error = 'Usuario o contrasena incorrectos')
	except:
		return render_template('errorLog.html',error = 'Introduce todos los campos')



@app.route('/signUp',methods=['POST','GET'])
def signUp():
	_name = request.form['inputName']
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']
#	_term = request.form['Aceptar']
	

	sql = "SELECT * FROM tbl_user WHERE user_username = %s"
	val = (_email,)
	cursor.execute(sql, val)
	res = cursor.fetchall()
	if len(res) == 0:
		sql = "INSERT INTO tbl_user (user_name,user_username,user_password) VALUES (%s, %s, %s)"
		val = (_name, _email, _password)
		cursor.execute(sql, val)
#	   print(cursor.rowcount, " bla bla ")
		conn.commit()
		return redirect('/showLogging')
	elif len(res) > 0:
		return jsonify({'message':'Email ya fue registrado'})

   

if __name__ == "__main__":
	app.run(debug = True,  port = 5003)
