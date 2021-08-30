from flask import Flask
app =Flask(__name__)



@app.route('/greeting')
def Welcome():
    return "<h1>Hello Every One Good Morning Have a Nice Day </h1>"

@app.route('/intro')
def hello():
    return  "<h2>Hello This is Ravi kiran i was learing  Data Science and creating Meachine Learnign Pipelines using python </h2>"


if __name__ == "__main__":
    app.run(debug= False)