from flask import Flask, render_template, redirect, url_for, request
import pymysql

global key
key = 0
app = Flask(__name__)

@app.route("/")
def index1():
    print("Application starts...")
    print("initialized key is " + str(key))
    return render_template('index.html', key=key)

@app.route("/index")
def index2():
    return render_template('index.html')

@app.route("/generic")
def generic():
    print("generic here!!")
    return render_template('generic.html')

@app.route("/jyprac")
def jyprac():
    print("jyprac here!!")
    return render_template('jyprac.html')

@app.route("/elements")
def elements():
    print("elements here!!")
    return render_template('elements.html')

@app.route("/redirect_login")
def redirect_login():
    print("login here!!")
    return render_template('Log_in.html')

@app.route("/login", methods = ['POST'])
def login():
    global key # will use global key variable
    print("login start")
    if request.method == 'POST':
        print("method starts...")
        id = request.form['ID']
        pw = request.form['PW']
        # retrieve the ID, PW from db
        print("DB retrieve starts...")
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
                sql = """SELECT ID, Password FROM STUDENT WHERE ID = '""" + id + """';"""
                # Execute SQL
                cursor.execute(sql)
                # Fetch the result
                # result is dictionary type
                result = cursor.fetchall()
        finally:
            db.close()
        print("DB retrieve ends...")
        if not result: # dictionary is empty
            print("no matching ID")
        else:
            for row in result:  # should be only one ((id, pw),)
                real_id = row[0]
                real_pw = row[1]
            if (id == real_id) and (pw==real_pw):
                print(key)
                key = 1
                print(key)
                return render_template('index.html', key=key)

@app.route("/redirect_logout")
def redirect_logout():
    print("logout starts...")
    global key
    key = 0
    print("logout ends...")
    return redirect("/index")


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

    return redirect("/index")


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
