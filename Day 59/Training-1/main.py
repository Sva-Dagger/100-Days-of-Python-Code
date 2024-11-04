from flask import render_template,Flask
import requests


blog_url = "https://api.npoint.io/2b1e1701b179fe512483"
blog_resp = requests.get(blog_url)
all_posts = blog_resp.json()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', posts=all_posts)

if __name__=="__main__":
    app.run(debug=True)