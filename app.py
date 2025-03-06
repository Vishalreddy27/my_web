from flask import Flask,render_template

app=Flask(__name__)
'''actually in default flask serches for a folder name Templates and there it will search for the html file 
to search in the same dir as app.py use 
Flask(__name__,template_folder=".")
'''
#add by 
@app.route("/")
def hello_world():
    return render_template("home.html")

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
