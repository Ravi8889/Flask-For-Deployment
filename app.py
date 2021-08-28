from flask import Flask


app =Flask(__name__)# definig the app

@app.route('/')
def pyhome():
    #return "Hello world"
    return "<h1> KONDA RAVI KIRAN </h1>"
    

if __name__ == "__main__":
    app.run()
