from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("/list")

@app.route("/list")
def list():
    return render_template("top.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/edit")
def edit():
    return render_template("edit.html")

app.run(host="0.0.0.0", port=8080)
