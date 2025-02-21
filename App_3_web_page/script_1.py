from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  #Para ver la pagina buscamos "localhost:5000/"
def home():
    return "Home page here!"

@app.route("/about")  #Para ver la pagina buscamos "localhost:5000/about"
def about():
    return "About content goes here!"  

if __name__ == "__main__":
    app.run(debug= True)