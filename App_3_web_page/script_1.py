from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Website content goes here!"  #Para ver la pagina buscamos "localhost:5000"

if __name__ == "__main__":
    app.run(debug= True)