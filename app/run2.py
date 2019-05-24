from flask import Flask, render_template, redirect, url_for, request
import pymysql

global key
<<<<<<< HEAD
=======
key = 0
>>>>>>> 95d664aacc4328407b1731722072996c66f54ccb
global sid
global Cname
global Clength
key = 1
Clength = 0
sid = 0

app = Flask(__name__)

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
        sql = """SELECT Csn, Cname FROM CLUB;"""
        # Execute SQL
        cursor.execute(sql)
        # Fetch the result
        # result is dictionary type
        result = cursor.fetchall()
finally:
    db.close()
print("DB retrieve ends...")
Csn = []
Cname = ["" for x in range(len(result))]
Cname_temp = []
for row in result:
    Csn.append(row[0])
    Cname_temp.append(str(row[1]))
i = 0
for csn in Csn:
    Cname[csn-1] = Cname_temp[i]
    i += 1
Clength = i
print("Cname is " + str(Cname))


@app.route("/")
def index1():
    print("Application starts...")
    print("initialized key is " + str(key))
    return render_template('index.html', club_name=Cname, club_length=Clength)

@app.route("/index")
def index2():
    return render_template('index.html', club_name=Cname, club_length=Clength)

@app.route("/club_info", methods = ['POST'])
def club_info():
    if request.method == 'POST':
        print("method starts...")
        club_name = request.form['club_name']
        print(str(club_name) + " : the club info we want to retrieve")
        # retrieve the club info from db
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
                sql = """SELECT * FROM CLUB NATURAL JOIN STUDENT;"""
                # Execute SQL
                cursor.execute(sql)
                # Fetch the result
                # result is dictionary type
                result = cursor.fetchall()
        finally:
            db.close()
        print("DB retrieve ends...")
        print(result)

    return render_template('generic.html')

@app.route("/aboutus")
def aboutus():
    print("aboutus here!!")
    return render_template('aboutus.html', key=key)

@app.route("/redirect_bookmark")
def redirect_bookmark():
    global key
    global sid
    if key == 0:
        # alert
        print("need to login")
        return render_template('Log_in.html', key=key, club_name = ["SEED KAIST"], club_detail = ["Seed..."])
    else:
        return render_template('bookmark.html', key=key)

@app.route("/bookmark")
def bookmark():
    print("bookmark here!!")
    return render_template('bookmark.html', key=key)

@app.route("/interested")
def interested():
    print("interest here!!")
    return render_template('interested.html')

@app.route("/redirect_login")
def redirect_login():
    print("login here!!")
    return render_template('Log_in.html', key=key)

@app.route("/login", methods = ['POST'])
def login():
    global key # will use global key variable
    global sid
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
                sql = """SELECT Sid, ID, Password FROM STUDENT WHERE ID = '""" + id + """';"""
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
            for row in result:  # should be only one ((Sid, id, pw),)
                real_id = row[1]
                real_pw = row[2]
                print(row[0], row[1], row[2])
            if (id == real_id) and (pw == real_pw):
                print("key is now " + str(key))
                key = 1
                sid = row[0]
                print("key is now " + str(key))
                print(str(sid) + " is using the service")
<<<<<<< HEAD
                return render_template('index.html', club_name=Cname, club_length=Clength)
=======
                return render_template('index.html', key=key, club_name = ["SEED KAIST"], club_detail = ["Seed..."])
>>>>>>> 95d664aacc4328407b1731722072996c66f54ccb
            else:
                print("password mismatch")
                return render_template('Log_in.html', key=key)




@app.route("/redirect_logout")
def redirect_logout():
    print("logout starts...")
    global key
    key = 0
    print("key is now " + str(key))
    print("logout ends...")
<<<<<<< HEAD
    return render_template('index.html', club_name=Cname, club_length=Clength)
=======
    return render_template('index.html', key=key, club_name = ["SEED KAIST"], club_detail = ["Seed..."])
>>>>>>> 95d664aacc4328407b1731722072996c66f54ccb


@app.route("/redirect_signup")
def redirect_signup():
    print("signup here!!")
    return render_template('Sign_up.html', key=key)


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

<<<<<<< HEAD
    return render_template('index.html', club_name=Cname, club_length=Clength)
=======
    return render_template('index.html', key=key, club_name=["SEED KAIST"], club_detail=["Seed..."])
>>>>>>> 95d664aacc4328407b1731722072996c66f54ccb


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
