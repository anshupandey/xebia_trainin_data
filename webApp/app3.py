from flask import Flask, render_template, request
import joblib

model = joblib.load("model.pkl")
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def main():
    return render_template("index.html")


@app.route("/predict",methods=["GET","POST"])
def main2():
    data = dict(request.form)
    print(data)
    data = [data['at'],data['v'],data['ap'],data['rh']]
    
    pred = model.predict([data])[0]
    return "The prediction is "+str(pred)

if __name__=="__main__":
    app.run(debug=True)

