from flask import Flask
from HTML_DESIGN import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('<h1 color= "red" style="text-align: center">Hello, World!</h1>'
            '<p>This is my Paragraph.</p>'
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjIyc21kM3J0YWIzaHdvMzM2cjY0ZDdrdmR5YWdjNnNqZXp2NG41diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/65J8Dy5Y41AKvnkEkr/giphy-downsized-large.gif" width=200 height=200>')

@app.route('/Bye')
@make_emphasis
@make_bold
@make_underlined
def Bye():
    return 'Bye'
@app.route('/USERNAME/<username>/<int:number>')
def greeting(username, number):
    return f'Hello there {username} !, you are {number} years old!'

if __name__=="__main__":
    app.run(debug=True)