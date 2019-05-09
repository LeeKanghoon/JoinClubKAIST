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

@app.route("/redirect_signup")
def redirect_signup():
    print("signup here!!")
    return render_template('Sign_up.html')

@app.route("/signup", methods = ['POST'])
def signup():
    print("signup start")
    if request.method == 'POST':
        print("method starts...")
        sid = request.form['Sid']
        sname = request.form['Sname']
        major = request.form['major']
        minor = request.form['minor']
        nationality = request.form['nationality']
        gender = request.form['gender']
        id = request.form['ID']
        pw = request.form['PW']
        print("method ends...")
        return redirect(url_for('signup_sent', Sid=sid, Sname=sname, Major=major, Minor=minor, Nationality=nationality, Gender=gender, ID=id, PW=pw))

@app.route("/signup_sent/<Sid>/<Sname>/<Major>/<Minor>/<Nationality>/<Gender>/<ID>/<PW>")
def signup_sent(Sid, Sname, Major, Minor, Nationality, Gender, ID, PW):
    # Connect to database
    print("signup_sent start ..")
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='junmo12345',
                         db='joinclubkaist',
                         charset='utf8')
    try:
        # Set cursor to the database
        with db.cursor() as cursor:
            # Write SQL query
            print("SQL student insert begins")
            sql = """INSERT INTO STUDENT
                     VALUES('""" + Sname + """', """ + Sid + """, '""" + Major + """', '""" + Minor + """', '""" + Nationality + """', '""" + Gender + """', '""" + ID + """', '""" + PW + """');"""
            # Execute SQL
            cursor.execute(sql)
            print("SQL student insert ends")
        # You must manually commit after every DML methods.
        db.commit()
    finally:
        db.close()

    return redirect("/")


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
