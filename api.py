from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('',methods=["POST"])
def get_data():
    data = request.get_json()

    name = float(dict(data)['a'])
    surname = float(dict(data)['b']) 
    return jsonify(name + surname)   












if __name__=='__main__':
    app.run(debug=True)