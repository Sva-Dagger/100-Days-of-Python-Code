import requests
from flask import render_template, Flask

response=requests.get("https://api.npoint.io/c026e44a9def7239eed7")
all_posts=response.json()

app=Flask(__name__)

@app.route("/blog")
def post():
    return render_template("post.html")

if __name__=="__main__":
    app.run(debug=True)
