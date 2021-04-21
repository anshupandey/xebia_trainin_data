from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def maain():
    return "Hello world from Python"

@app.route("/contact",methods=['POST','GET'])
def maain2():
    return "Hello world please call me"

@app.route("/predict",methods=['POST','GET'])
def maain3():
    return "hiiiiiiiiiiiiiiiiiiiiiiiiiiiii"

@app.route("/aboutus",methods=['POST','GET'])
def maain4():
    return "Python coders"


if __name__=="__main__":
    app.run(debug=True)
