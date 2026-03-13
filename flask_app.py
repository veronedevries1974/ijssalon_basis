from flask import Flask
from flask import render_template
    
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/prijzen')
def prijzen():
    items = [
        {"product":"vanille-ijs 1 liter",
         "prijs":"2 euro"
         },
        {"product":"chocolade-ijs 1 liter",
         "prijs": "2 euro"
         }
    ]
    return render_template("prijzen.html", items=items)

@app.route('/recepten')
def recepten():
    items = [
        {   
            "recept": "Tiramisu di nona",
            "img": "tiramisu.png"
        },
        {
            "recept": "IJstaart met chocolade",
            "img": "ijstaart.png"
        } 
    ]
    return render_template("recepten.html", items=items)

app=Flask(__name__)
if __name__=='_main_':
    app.run(port=5000,debug=True)