from flask import Flask

app=Flask(__name__)
if __name__=='_main_':
    app.run(port=5000,debug=True)
    
@app.route('/')
def home():
    return "Welkom op mijn eerste Flask-website"

