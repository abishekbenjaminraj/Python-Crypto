from flask import Flask,render_template,request
import requests

app=Flask(__name__)

url="http://api.coinlayer.com/live?access_key=9680b09f33c5b5ef8e1c36a9971ff13e"


@app.route('/')
def login():
    return render_template("index.html")
@app.route('/bitcoin',methods=["GET","POST"])
def home():
    if request.method=="POST":
        complete_url=requests.get(url)
        data=complete_url.json()
        rate=request.form.get("rate")
        success=data.get("success")
        target=data.get("target")
        rates=data.get("rates")
        if rate in rates:
            result=rates[rate]
        return render_template("login.html",result=result,success=success,target=target,rate=rate)
    return render_template("login.html")




if __name__ == "__main__":
    app.run(debug=True)