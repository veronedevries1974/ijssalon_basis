from flask import Flask
from flask import render_template

app=Flask(__name__)
if __name__=='_main_':
    app.run(port=5000,debug=True)
    
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/prijzen')
def prijzen():
    return render_template("prijzen.html")

@app.route('/recepten')
def recepten():
    return render_template("recepten.html")