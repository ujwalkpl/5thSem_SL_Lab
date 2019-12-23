from flask import Flask,request,redirect,url_for,render_template,session
app = Flask(__name__)
app.secret_key="ujwal"
@app.route('/',methods = ["POST","GET"])
def index():
    if request.method =="GET":
        return render_template('index.html')
    if request.method == "POST":
        for item in ["shirt","pant","socks"]:
            if item not in session:
                session[item] = int(request.form[item])
            else:
                session[item]=int(session[item])+int(request.form[item])

        return redirect(url_for('cart'))
@app.route('/cart')
def cart():
    cart = []
    total = 0
    for item in [("shirt",100),("pants",150),("socks",200)] :
        cart.append({"name":item[0],"amount":item[1]*session[item[0]],"quantity":session[item[0]]})
        total = total + item[1]*session[item[0]]
    return render_template('cart.html',total = total)

if __name__=='__main__':
    app.run(debug=True)
