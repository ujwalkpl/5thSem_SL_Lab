from flask import Flask,request,render_template
import time
import re

app = Flask(__name__)
app.secret_key = "ujwal"
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=="GET":
       
        return render_template('index.html',msg = "")
    if request.method=="POST":

        date = request.form["date"]
        usn = request.form["usn"]
        marks1 = int(request.form["marks1"])
        marks2 = int(request.form["marks2"])
        marks3 = int(request.form["marks3"])

    

        try:
     
            time.strptime(date,"%Y-%m-%d")
        except ValueError:
            msg = "Date format is incorrect"
            return render_template('index.html',msg = msg)
        pattern = "^[0-9][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"
        if not re.match(pattern,usn):
            msg = "USN is invalid"
            return render_template('index.html',msg = msg)
        total = marks1+marks2+marks3
        msg = "Average marks is "+ str(total/3.0)
        return render_template('index.html',msg=msg)

if __name__=='__main__':
    app.run(debug=True)
    
