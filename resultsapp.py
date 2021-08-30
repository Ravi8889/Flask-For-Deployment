from flask import Flask, redirect, url_for,render_template
from flask.globals import request
app =Flask(__name__)


@app.route('/')
def Home():
    return render_template("form.html")

@app.route('/pass/<int:score>')
def Pass(score):
    res =" "
    if score >= 50:
        res ="PASS" 
    else:
        res ="FAIL"
    return render_template("results.html",results =res)
@app.route('/fail/<int:score>')
def fail(score):
    
@app.route('/result/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result= "fail"
    elif marks > 50:
        result = "Pass"
    else:
        result ="I Don't Know "
    return redirect(url_for(result, score =marks))
@app.route('/submit',methods =['POST','GET'])
def submit():
    tota_score= 0
    if request.method =="POST":
        science =float(request.form['science'])
        maths = float(request.form['maths'])
        data_science =float(request.form['data_science'])
        statistics =float(request.form['statistics'])
        tota_score =(science+maths+data_science+statistics)/4;
    res =" "
    if tota_score >= 50:
        res ="pass"
    else:
        res ="fail"
    return redirect(url_for(res,score =tota_score))




if __name__ == "__main__":
    app.run(debug=True)