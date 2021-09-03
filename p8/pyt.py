from flask import Flask,redirect,url_for,render_template,request
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Ak0906sa@'
app.config['MYSQL_DB']='pro'
mysql=MySQL(app)
@app.route('/')
def home():
	return render_template('home.html')
@app.route('/creat.html')

@app.route('/creat.html')
def cr():
	return render_template('creat.html')	 
@app.route('/creat.html',methods=['GET','POST'])
def creat():
	cur=mysql.connection.cursor()

	text=request.form['qu']
	cur.execute(text)
	#print(text)
	return render_template('creat.html',data='DONE')
	print(text)	
@app.route('/read.html')
def re():
	return render_template('read.html')	
@app.route('/read.html',methods=['GET','POST'])
def rea():
	cur=mysql.connection.cursor()
	text=request.form['rqu']
	cur.execute(text)
	fet=cur.fetchall()
	fet = str(fet).replace('('," ")
	fet=str(fet).replace(')'," ")
	fet=str(fet).replace('['," ")
	fet=str(fet).replace(']'," ")
	fet=str(fet).replace(','," ")
	fet=str(fet).replace('"'," ")
	fet=str(fet).replace("'"," ")
	#self.number.setPlainText(fet)

	cur.close()

	return render_template('read.html',data=fet)	
@app.route('/update.html')
def up():
	return render_template('update.html')	
@app.route('/update.html',methods=['GET','POST'])
def upd():
	cur=mysql.connection.cursor()
	text=request.form['urq']
	cur.execute(text)
	fet=cur.fetchall()
	fet = str(fet).replace('('," ")
	fet=str(fet).replace(')'," ")
	fet=str(fet).replace('['," ")
	fet=str(fet).replace(']'," ")
	fet=str(fet).replace(','," ")
	fet=str(fet).replace('"'," ")
	fet=str(fet).replace("'"," ")
	#self.number.setPlainText(fet)

	cur.close()

	return render_template('update.html',data=fet)
@app.route('/delect.html')
def de():
	return render_template('delect.html')	
@app.route('/delect.html',methods=['GET','POST'])
def det():
	cur=mysql.connection.cursor()
	text=request.form['drq']
	cur.execute(text)
	fet=cur.fetchall()
	fet = str(fet).replace('('," ")
	fet=str(fet).replace(')'," ")
	fet=str(fet).replace('['," ")
	fet=str(fet).replace(']'," ")
	fet=str(fet).replace(','," ")
	fet=str(fet).replace('"'," ")
	fet=str(fet).replace("'"," ")
	#self.number.setPlainText(fet)

	cur.close()

	return render_template('delect.html',data=fet)	

if __name__=='__main__':
	app.debug=True
	app.run()	