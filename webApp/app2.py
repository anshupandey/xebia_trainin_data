from flask import Flask,render_template, request
import joblib

model = joblib.load("model.pkl")
app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def maain():
    return render_template("index.html")



@app.route("/predict",methods=['POST','GET'])
def maain3():
    data = dict(request.form)
    print(data)
    data = [data['at'],data['v'],data['ap'],data['rh']]
    output = model.predict([data])
    
    return "THe electricy producted based on values would be - "+str(output)



if __name__=="__main__":
    app.run(debug=True)
