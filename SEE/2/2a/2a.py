from flask import Flask,request,redirect,render_template,session

app = Flask(__name__)
@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        