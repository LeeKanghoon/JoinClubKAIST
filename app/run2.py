from flask import Flask, render_template, redirect, url_for, request
import pymysql

app = Flask(__name__)

@app.route("/")
def index1():
    print("here!!")
    return render_template('index.html')

@app.route("/index")
def index2():
    return render_template('index.html')

@app.route("/generic")
def generic():
    print("generic here!!")
    return render_template('generic.html')

@app.route("/elements")
def elements():
    print("elements here!!")
    return render_template('elements.html')

@app.route("/login")
def login():
    print("login here!!")
    return render_template('Log_in.html')



if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
