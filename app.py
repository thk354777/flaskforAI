from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
       first_name = request.form.get("fname")
       age = int(request.form.get("age"))
       last_name = request.form.get("lname") 
       weight = float(request.form.get("weight"))
       height = float(request.form.get("height"))
       bmi = weight/(height**2)
       return first_name + " " + last_name + " BMI is " + str(bmi) + " and result is " + classified(bmi, age)
    

    return render_template("index.html", message="Calculator")

def classified(bmi, age):
    if age < 65:
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi <= 24.9:
            return "Healthy weight"
        elif 24.9 < bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"
    elif 65 <= age < 75:
        if bmi < 22:
            return "Underweight"
        elif 22 <= bmi <= 26.9:
            return "Healthy weight"
        elif 26.9 < bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"
    else:
        if bmi < 23:
            return "Underweight"
        elif 23.1 <= bmi <= 27.9:
            return "Healthy weight"
        elif 28 < bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"
    
if __name__ == "__main__":
    app.run(debug=True)
