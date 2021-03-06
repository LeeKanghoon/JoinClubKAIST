from flask import Flask, render_template, redirect, url_for, request
import pymysql

global key
global sid
global Cname
global Clength
global bookmark
key = 1
Clength = 0
sid = 0
bookmark_v = 1

app = Flask(__name__)


@app.route("/")
def index1():
    print("Application starts...")
    print("initialized key is " + str(key))
    return render_template('index.html', club_name = ["SEED KAIST", "hihi", "...........!!"], club_length = 79, key = key)
    #return render_template('index.html', club_name=Cname, club_length=Clength)

@app.route("/index")
def index2():
    return render_template('index.html', club_name=Cname, club_length=Clength)

@app.route("/club_info", methods = ['POST'])
def club_info():
    print("club_info start")
    if request.method == 'POST':
        print("method starts...")
        club_name = request.form['club_name']
        club_num = request.form['club_num']
        # retrieve the club_info from db

    return render_template('generic.html', club_name="name", class_="class", district="district", department="dep", establish="est",
                           club_member="c mem", recruit_member="r mem", activity_time="a time", phone="pho", location="lo", homepage="home", cnum="2", cinfo = "....",
                           key = key, bookmark_v = bookmark_v)


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
        return render_template('Log_in.html', key=key, club_name = ["SEED KAIST", "ani", "kaldi"], club_idx = "1,4,6",club_length=3 )
    else:
        return render_template('bookmark.html', key=key, club_name = ["SEED KAIST", "ani", "kaldi"], club_idx = "1,4,6",club_length=3 ,
        event_num = [12, 14, 16], event_name = ["open dongbang", "open coffe"], e_club_name = ["SEED KAIST", "ani", "kaldi"],
        date = ["0304", "0506"], time = ["20:30~22:30", "9:30~11:30"], location = ["N1-102", "E78-204"], length = 3)

@app.route("/bookmark")
def bookmark():
    print("bookmark here!!")
    return render_template('bookmark.html', key=key)

@app.route("/redirect_event")
def redirect_event():
    print("event here!!")
    return render_template('event.html', key=key, event_v = [1, 0, 1], event_num = [12, 14, 16], club_name = ["SEED KAIST", "KALDI"], event_name = ["open dongbang", "open coffe"],
    date = ["0304", "0506"], time = ["20:30~22:30", "9:30~11:30"], location = ["N1-102", "E78-204"], length = 3)

@app.route("/interest_delete", methods = ['POST'])
def interest_delete():
    print("... here!!")
    index = request.form['index']
    print(index)

    if request.method == 'POST':
        return render_template('event.html', key=key, event_v = [1, 0, 1], event_num = [12, 14, 16], club_name = ["SEED KAIST", "KALDI"], event_name = ["open dongbang", "open coffe"],
        date = ["0304", "0506"], time = ["20:30~22:30", "9:30~11:30"], location = ["N1-102", "E78-204"], length = 3)

@app.route("/redirect_login")
def redirect_login():
    print("login here!!")
    return render_template('Log_in.html', key=key)

@app.route("/elements")
def elements():
    print("element here!!")
    return render_template('elements.html', key=key)


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
                return render_template('index.html', club_name=Cname, club_length=Clength)

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
    return render_template('index.html', club_name = ["SEED KAIST", "hihi", "...........!!"], club_length = 79, key = key)


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
    return render_template('index.html', club_name=Cname, club_length=Clength)



if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
