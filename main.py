from flask import Flask,request,render_template,url_for,redirect,jsonify
app = Flask(__name__)


@app.route('/')
def msg ():
    return("Hello World")

@app.route('/success/<int:score>')
def  success(score):
    return("Your registration process has been success and your Token number is :") + str(score)

@app.route('/fail/<int:score>')
def  fail(score):
    return("Your registration process has been failed and and your number is :") + str(score)

@app.route("/form",methods=["GET","POST"])
def  form():
    if request.method=="GET":
        return render_template("index.html")
    else:
        maths= float(request.form["maths"])
        science= float(request.form["science"])
        history= float(request.form["history"]) 
    Total_marks = (maths + science + history) / 3 
    return render_template("index.html",hello = Total_marks)


@app.route('/api',methods=["POST"])
def  calculate():
    data = request.test.json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val + b_val)










    # # Redirect into success or fail page as per user marks
    # res = ""
    # if Total_marks < 35:
    #     res = "fail"
    # else:
    #     res = "success"
    # return redirect(url_for(res,score  = Total_marks))





    


    









if __name__=="__main__":
    app.run(debug=True)