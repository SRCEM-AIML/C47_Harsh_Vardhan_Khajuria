<<<<<<< HEAD
=======
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "<h1>Hello, Flask!</h1>"

# if __name__ == '__main__':
#     app.run(debug=True,port=8000)

>>>>>>> a21132d801b622e55102556c2af9ac93f4eda11c
from flask import Flask, render_template

app = Flask(__name__)

<<<<<<< HEAD
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
=======
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/products")
def products():
    return "<p>Hello, this is the product page.</p>"

@app.route("/home")
def home_page():
    return "<p>Hello, this is the home page. Tell me more about you!</p>"

if __name__ == "__main__":
    app.run(debug=True, port=8000)
>>>>>>> a21132d801b622e55102556c2af9ac93f4eda11c
