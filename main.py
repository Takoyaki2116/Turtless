from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from peewee import Delete


from datebase import Turtle

app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("/list")

@app.route("/list")
def list():
  turtles = Turtle.select()
  return render_template("top.html", turtles=turtles)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/edit/<id>")
def edit(id):
      turtle = Turtle.get(id=id)
      return render_template("edit.html", turtle=turtle)

@app.route("/update/<id>", methods=["POST"])
def update(id):
      turtle = Turtle.get(id=id)
      Turtlenamee = request.form["Turtlename"]
      turtle.name = Turtlenamee
      turtle.save()
      return redirect("/list")

@app.route("/delete/<id>", methods=["POST"])
def delete(id):
      turtle = Turtle.get(id=id)
      turtle.delete_instance()
      return redirect("/list")

@app.route("/new", methods=["POST"])
def new():
  Turtlename = request.form["Turtlename"]
  Turtle.create(name=Turtlename)
  return redirect("/list")

app.run(host="0.0.0.0", port=8080)
