from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<b><p>Hello this Vishal Reddy  21MID0059</p></b>"

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
