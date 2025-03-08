from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/933ba4d4fc69416f37a8").json()

app = Flask(__name__)



@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route('/login', methods=['POST'])
def login():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    mail_sender(name, email, phone, message)
    # Process or display form data
    return render_template("login.html", name=name, email=email, phone=phone, message=message)


@app.route("/about")
def about():
    return render_template("about.html")

def mail_sender(name:str, email:str, phone:str, message:str):
    my_email = "hackersiva847@gmail.com"
    password = "gaodoysneeotaxmz"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        print("connected")
        connection.sendmail(from_addr=my_email,
                            to_addrs="sivam4266@gmail.com",
                            msg=f"subject:Msg from Client\n\n Name:{name}\nEmail:{email}\nPhone:{phone}\nmessage:{message}")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
