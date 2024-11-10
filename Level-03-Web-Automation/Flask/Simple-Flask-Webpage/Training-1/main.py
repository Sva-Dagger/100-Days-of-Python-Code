from flask import render_template,Flask
import requests


blog_url = "https://api.npoint.io/c026e44a9def7239eed7"
blog_resp = requests.get(blog_url)
all_posts = blog_resp.json()


app = Flask(__name__)


@app.route('/index.html')
def home():
    return render_template('index.html', posts=all_posts)
@app.route('/about.html')
def about():
    return render_template('about.html', posts=all_posts)
@app.route('/contact.html')
def contact():
    return render_template('contact.html', posts=all_posts)
@app.route('/post.html')
def post():
    return render_template('post.html', posts=all_posts)

if __name__=="__main__":
    app.run(debug=True)