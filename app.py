<<<<<<< HEAD
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def message():
    return "Hello World"

@app.route('/success/<int:score>')
def result(score):
    return "You passed the exam and your score is: " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "You failed the exam and your score is: " + str(score)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET": 
        return render_template('form.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths + science + history) / 3                     
        return render_template('form.html', score=average_marks)

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask,render_template,request,url_for

app = Flask(__name__)

@app.route('/')
def message():
    return("Hello World")

@app.route('/success/<int:score>')
def result(score):
    return "You passed the exam and your score is :" + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "You failed the exam and your score is :" + str(score)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths + science + history) / 3
        return render_template('form.html', score=average_marks)






if __name__=="__main__":
    app.run(debug=True)
>>>>>>> 6869e64748f9b08e314c2ea60ad120d7345e2570
