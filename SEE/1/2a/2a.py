from flask import Flask,render_template,request,session

app = Flask(__name__)
app.secret_key = "ujwal"

@app.route('/',methods= ['POST','GET'])
def index():
	
	try:
		balance = session["balance"]
		count = session["count"]
	except KeyError:
		balance = session["balance"] = 8000
		count = session["count"] = 0
    
	if request.method == "GET" :
		return render_template('index.html',balance= balance,msg = "")
	if request.method == "POST" :
		if request.form["amount"] == "":
			msg= "Amount should not be empty  "
			return render_template('index.html',balance=balance,msg=msg)
		if int(request.form["amount"])<0 :
			msg = "Amount should be positive"
			return render_template('index.html',msg=msg,balance=balance)
		if session["count"]>5 :
			msg = "5 transactions done "
			return render_template('index.html',msg=msg,balance=balance)
		if request.form["action"]=="deposit":
			msg = "Amount deposited"
			count = count + 1
			session["count"]=count
			balance = balance + int(request.form["amount"])
			session["balance"]=balance
			return render_template('index.html',msg=msg,balance=balance)
		if request.form["action"]=="withdraw":
			msg = "Amount withdrawn"
			count = count +1 
			session["count"] = count 
			balance = balance - int(request.form["amount"])
			session["balance"] = balance
			return render_template('index.html',msg=msg,balance=balance)

@app.route('/clear')
def clear():
	session.clear()
	return render_template('index.html',msg="session cleared",balance=8000)

if __name__ == '__main__':
    app.run(debug=True)









    