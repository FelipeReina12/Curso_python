from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  #Para ver la pagina buscamos "localhost:5000/"
def home():
    return render_template("home.html")

@app.route("/about")  #Para ver la pagina buscamos "localhost:5000/about"
def about():
    return render_template("about.html") 

if __name__ == "__main__":
    app.run(debug= True)