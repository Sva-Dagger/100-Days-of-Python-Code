import requests
from flask import Flask, render_template
app=Flask(__name__)
name="siva"
Genderize_response = requests.get(f"https://api.genderize.io?name={name}")
Gender = Genderize_response.json()["gender"]

Agify_response = requests.get(f"https://api.agify.io?name={name}")
Age = Agify_response.json()["age"]
@app.route('/')
def API():
    return render_template("index.html", name=name, gender=Gender, age=Age)

if __name__ == "__main__":
    app.run(debug=True)

