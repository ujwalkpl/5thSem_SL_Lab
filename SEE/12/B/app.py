from flask import Flask,request,render_template,session
app = Flask(__name__)
app.secret_key="ujwal"
@app.route('/',methods= ["POST","GET"])
def index():
    
    print("index")
    try:
        balance = session["balance"]
        count = session["count"]
    except KeyError:
        balance = session["balance"]=8000
        count = session["count"]=0

    if request.method == "GET":
        print('get')
        return render_template('index.html',msg = " ",balance=balance)
    else:
        print("post")
        if(count>5):
            print("ihi")
            msg = "the number of transactions has exceeded the limit"
            return render_template('index.html',msg=msg,balance = balance)
        elif(request.form["action"]=="withdraw"):
            print("withdraw kar bc")
            if(int(request.form["amount"]<balance)):
                msg = "insufficient funds"
                return render_template('index.html',msg = msg,balance=balance)
            balance = balance - int(request.form["amount"])
            session["balance"]=balance
            count = count +1
            session["count"]=count
            msg = "amount withdrawn"
            return render_template('index.html',msg=msg,balance=balance)
        elif(request.form["action"]=="deposit"):
            print("arey deposit")
            balance = balance + int(request.form["amount"])
            session["balance"]=balance
            count = count +1
            session["count"]=count
            msg = "amount deposited"
            return render_template('index.html',msg=msg,balance=balance)
        else:
            return render_template('index.html',msg=msg,balance=balance)
if __name__ =='__main__':
    app.run(debug=True)



        