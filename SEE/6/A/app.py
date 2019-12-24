from flask import Flask,request,redirect,render_template

app = Flask(__name__)
@app.route('/',methods = ["POST","GET"])
def index():
    if(request.method == "GET"):
        print("hi")
        return render_template('index.html',msg = "Welcome")
    elif(request.method == "POST"):
        pant = request.form["pant"]
        shirt = request.form["shirt"]
        trouser = request.form["trouser"]
        if(pant == "" or shirt == "" or trouser == ""):
            msg = "fields cant be empty"
            return render_template('index.html',msg = msg)
        if(int(pant)<0 or int(shirt)<0 or int(trouser)<0):
            msg = "quantity cannot be negative"
            return render_template('index.html',msg = msg)
        total = int(pant)*200+int(shirt)*100+int(trouser)*150
        msg = "Total amount is " + str(total)
        return render_template('index.html',msg = msg)

if __name__ =='__main__':
    app.run(debug=True)