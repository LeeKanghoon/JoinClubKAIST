from flask import Flask, render_template, redirect, url_for, request
import pymysql

global key
global sid
global Cname
global Clength

key = 0
Clength = 0
sid = 0


app = Flask(__name__)
# retrieve the Cname, Csn  from db

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
        sql = """SELECT Cname, Csn FROM CLUB;"""
        # Execute SQL
        cursor.execute(sql)
        # Fetch the result
        # result is dictionary type
        result_ = cursor.fetchall()
finally:
    db.close()
print("DB retrieve ends...")

Csn = []
Cname_temp = []
Clength = len(result_)
print("the number of club is " + str(Clength))
Cname = ['' for x in range(Clength)]
for row__ in result_:
    Cname_temp.append(row__[0])
    Csn.append(row__[1])
for ind, csn in enumerate(Csn):
    Cname[csn-1] = Cname_temp[ind]
print(Cname)

@app.route("/")
def index1():
    print("Application starts...")
    print("initialized key is " + str(key))
    #return render_template('index.html', club_name = ["SEED KAIST", "hihi", "...........!!"], club_length = 79)
    return render_template('index.html', club_name=Cname, club_length=Clength, key = key)

@app.route("/index")
def index2():
    return render_template('index.html', club_name=Cname, club_length=Clength)

@app.route("/club_info", methods = ['POST'])
def club_info():
    global key
    global sid
    print("club_info start")
    if request.method == 'POST':
        print("method starts...")
        club_name = request.form['club_name']
        club_num = request.form['club_num']
        # retrieve the club_info from db
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
                sql = """SELECT Cname, Class, District, Department, Establish, Num_member, Num_recruit, Activity_time, Phone, Room, Homepage, Csn, Intro
                FROM STUDENT INNER JOIN CLUB ON STUDENT.Sid = CLUB.Csid WHERE CLUB.Csn='"""+str(club_num)+"""';"""
                # Execute SQL
                cursor.execute(sql)
                # Fetch the result
                # result is dictionary type
                result = cursor.fetchall()
        finally:
            db.close()
        print("DB retrieve ends...")
    row = result[0]
    print("club_info finish")

    print("bookmark_info start")
    if (key == 0):
        print("user is not logged in")
        bookmark_v = 0
    else:
        # retrieve the club_info from db
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
                sql = """SELECT BCsn FROM BOOKMARK WHERE BOOKMARK.BSid='""" + str(sid) + """';"""
                # Execute SQL
                cursor.execute(sql)
                # Fetch the result
                # result is dictionary type
                result = cursor.fetchall()
        finally:
            db.close()
        print("DB retrieve ends...")
        bookmark_list = []
        for row_ in result:
            bookmark_list.append(row_[0])
        print(bookmark_list)
        if row[11] in bookmark_list:
            print("the club is already in bookmark list")
            bookmark_v = 1
        else:
            print("the club is not in bookmark list")
            bookmark_v = 0
    print("bookmark_info finish")

    return render_template('generic.html', club_name=row[0], class_=row[1], district=row[2], department=row[3], establish=row[4],
                           club_member=row[5], recruit_member=row[6], activity_time=row[7], phone=row[8], location=row[9], homepage=row[10], cnum=row[11], cinfo=row[12],
                           key=key, bookmark_v=bookmark_v)

@app.route("/bookmark_insert", methods = ['POST'])
def bookmark_insert():
    global sid;
    print("bookmark_insert start")
    if request.method == 'POST':
        print("method starts...")

        csn = request.form['csn']
        club_name = request.form['club_name']
        class_ = request.form['class_']
        district = request.form['district']
        department = request.form['department']
        establish = request.form['establish']
        club_member = request.form['club_member']
        recruit_member = request.form['recruit_member']
        activity_time = request.form['activity_time']
        phone = request.form['phone']
        location = request.form['location']
        homepage = request.form['homepage']
        cnum = request.form['cnum']
        cinfo = request.form['cinfo']
        # retrieve the club_info from db
        print("DB update starts...")
        db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             passwd='junmo12345',
                             db='joinclubkaist',
                             charset='utf8')
        try:
            # Set cursor to the database
            with db.cursor() as cursor:
                sql = """INSERT INTO BOOKMARK VALUES('""" + str(csn) + """', '""" + str(sid) + """');"""
                cursor.execute(sql)
            db.commit()
        finally:
            db.close()
        print("DB update ends...")
    print("bookmark_insert finish")
    return render_template('generic.html', club_name=club_name, class_=class_, district=district, department=department, establish=establish,
                           club_member=club_member, recruit_member=recruit_member, activity_time=activity_time, phone=phone, location=location, homepage=homepage,
                            cnum=cnum, cinfo=cinfo,
                           key=key, bookmark_v=1)

@app.route("/bookmark_delete", methods = ['POST'])
def bookmark_delete():
    global sid;
    print("bookmark_delete start")
    if request.method == 'POST':
        print("method starts...")
        csn = request.form['csn']
        club_name = request.form['club_name']
        class_ = request.form['class_']
        district = request.form['district']
        department = request.form['department']
        establish = request.form['establish']
        club_member = request.form['club_member']
        recruit_member = request.form['recruit_member']
        activity_time = request.form['activity_time']
        phone = request.form['phone']
        location = request.form['location']
        homepage = request.form['homepage']
        cnum = request.form['cnum']
        cinfo = request.form['cinfo']
        # retrieve the club_info from db
        print("DB update starts...")
        db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             passwd='junmo12345',
                             db='joinclubkaist',
                             charset='utf8')
        try:
            # Set cursor to the database
            with db.cursor() as cursor:
                sql = """DELETE FROM BOOKMARK WHERE BOOKMARK.BCsn='"""+str(csn)+"""' AND BOOKMARK.BSid='"""+str(sid)+"""';"""
                cursor.execute(sql)
            db.commit()
        finally:
            db.close()
        print("DB update ends...")
    print("bookmark_delete finish")
    return render_template('generic.html', club_name=club_name, class_=class_, district=district, department=department, establish=establish,
                           club_member=club_member, recruit_member=recruit_member, activity_time=activity_time, phone=phone, location=location, homepage=homepage,
                            cnum=cnum, cinfo=cinfo, key=key, bookmark_v=0)

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
        return render_template('Log_in.html', key=key)
    else:
        print("redirect_bookmark start")
        # retrieve the club_info from db
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
                sql = """SELECT Cname, BCsn FROM BOOKMARK INNER JOIN CLUB ON BOOKMARK.BCsn = CLUB.Csn WHERE BOOKMARK.BSid='""" + str(sid) + """';"""
                # Execute SQL
                cursor.execute(sql)
                # Fetch the result
                # result is dictionary type
                result = cursor.fetchall()
        finally:
            db.close()
        print("DB retrieve ends...")
        print(result)
        print("redirect_bookmark finish")
        club_name = []
        club_idx = ""
        club_length = len(result)
        for row in result:
            club_name.append(row[0])
            club_idx = club_idx + str(row[1]) + ","
        club_idx = club_idx[:-1]
        print(club_name)
        print(club_idx)
        return render_template('bookmark.html', key=key, club_name=club_name, club_idx=club_idx, club_length=club_length)

@app.route("/interest_insert", methods = ['POST'])
def interest_insert():
    global sid;
    global key;
    print("interest_insert start")
    if request.method == 'POST':
        print("method starts...")
        event_v = request.form['event_v']
        event_num = request.form['event_num']
        club_name = request.form['club_name']
        event_name = request.form['event_name']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        length = request.form['length']
        index = request.form['index']
        print(event_v)
        print(event_num)
        print(club_name)
        print(event_name)
        print(date)
        print(time)
        print(location)

        event_v = event_v[1:-1].split(",")
        event_num = event_num[1:-1].split(",")
        club_name = club_name[1:-1].split(",")
        event_name = event_name[1:-1].split(",")
        date = date[1:-1].split(",")
        time = time[1:-1].split(",")
        location = location[1:-1].split(",")

        for i in range(len(event_v)):
            event_v[i] = event_v[i][1:-1]
            event_num[i] = event_num[i][1:-1]
            club_name[i] = club_name[i][1:-1]
            event_name[i] = event_name[i][1:-1]
            date[i] = date[i][1:-1]
            time[i] = time[i][1:-1]
            location[i] = location[i][1:-1]


        index = int(index)
        event_v[index] = '1'
        eno = event_num[index]

        # retrieve the club_info from db
        print("DB update starts...")
        db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             passwd='junmo12345',
                             db='joinclubkaist',
                             charset='utf8')
        try:
            # Set cursor to the database
            with db.cursor() as cursor:
                sql = """INSERT INTO INTEREST VALUES('""" + str(eno) + """', '""" + str(sid) + """');"""
                cursor.execute(sql)
            db.commit()
        finally:
            db.close()
        print("DB update ends...")
        print("interest_insert finish")
        return render_template('event.html#'+str(index), key=key, event_v=event_v, event_num=event_num, club_name=club_name,
                               event_name=event_name, date=date, time=time, location=location, length=length)


@app.route("/interest_delete", methods = ['POST'])
def interest_delete():
    global sid;
    global key;
    print("interest_delete start")
    if request.method == 'POST':
        print("method starts...")
        event_v = request.form['event_v']
        event_num = request.form['event_num']
        club_name = request.form['club_name']
        event_name = request.form['event_name']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        length = request.form['length']
        index = request.form['index']
        print(event_v)
        print(type(event_v))

        event_v = event_v[1:-1].split(",")
        event_num = event_num[1:-1].split(",")
        club_name = club_name[1:-1].split(",")
        event_name = event_name[1:-1].split(",")
        date = date[1:-1].split(",")
        time = time[1:-1].split(",")
        location = location[1:-1].split(",")

        for i in range(len(event_v)):
            event_v[i] = event_v[i][1:-1]
            event_num[i] = event_num[i][1:-1]
            club_name[i] = club_name[i][1:-1]
            event_name[i] = event_name[i][1:-1]
            date[i] = date[i][1:-1]
            time[i] = time[i][1:-1]
            location[i] = location[i][1:-1]


        index = int(index)
        event_v[index] = '0'
        eno = event_num[index]

        # retrieve the club_info from db
        print("DB update starts...")
        db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             passwd='junmo12345',
                             db='joinclubkaist',
                             charset='utf8')
        try:
            # Set cursor to the database
            with db.cursor() as cursor:
                sql = """DELETE FROM INTEREST WHERE INTEREST.IEno = '""" + str(eno) + """' AND INTEREST.ISid='""" + str(sid) + """';"""
                cursor.execute(sql)
            db.commit()
        finally:
            db.close()
        print("DB update ends...")
        print("interest_delete finish")
        return render_template('event.html#'+str(index), key=key, event_v=event_v, event_num=event_num, club_name=club_name,
                               event_name=event_name, date=date, time=time, location=location, length=length)


@app.route("/redirect_event")
def redirect_event():
    global key
    global sid
    if key == 0:
        # alert
        print("need to login")
        return render_template('Log_in.html', key=key)
    else:
        print("redirect_event start")
        # retrieve the club_info from db
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
                sql = """SELECT Eno, Ename, Edate, Stime, Etime, Loc, Cname FROM EVENT INNER JOIN CLUB ON EVENT.ECsn = CLUB.Csn;"""
                # Execute SQL
                cursor.execute(sql)
                # Fetch the result
                # result is dictionary type
                result = cursor.fetchall()
        finally:
            db.close()
        print("DB retrieve ends...")
        print("redirect_event finish")
        event_time = []
        for row in result:
            event_time.append(int(row[2]+row[3]))
        event_sort = [i[0] for i in sorted(enumerate(event_time), key=lambda x:x[1])] #event time sorted index
        length = len(result)
        Eno = []
        Ename = []
        Edate = []
        Time = []
        Loc = []
        Cname = []
        for i in event_sort:
            row = result[i]
            Eno.append(str(row[0]))
            Ename.append(row[1])
            edate = row[2]
            edate = edate[:4] + ' / ' + edate[4:6] + ' / ' + edate[6:8]
            Edate.append(edate)
            stime = row[3]
            etime = row[4]
            stime = stime[:2] + ':' + stime[2:4]
            etime = etime[:2] + ':' + etime[2:4]
            Time.append(stime + ' ~ ' + etime)
            Loc.append(row[5])
            Cname.append(row[6])
        print("retrieve interested start")
        # retrieve the club_info from db
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
                sql = """SELECT IEno, ISid FROM INTEREST WHERE INTEREST.ISid='""" + str(sid) + """';"""
                # Execute SQL
                cursor.execute(sql)
                # Fetch the result
                # result is dictionary type
                result = cursor.fetchall()
        finally:
            db.close()
        print("DB retrieve ends...")
        print(result)
        print("retrieve interested finish")
        event_v = ['0' for x in range(length)]
        for row in result:
            event_v[row[0]] = '1'
        return render_template('event.html', key=key, event_v=event_v, event_num=Eno, club_name=Cname,
                               event_name=Ename, date=Edate, time=Time, location=Loc, length=length)

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
                sql = """SELECT Sid, ID, PW FROM STUDENT WHERE ID = '""" + id + """';"""
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
            row = result[0]
            pw_ = row[2]
            pw_ = pw_[:-1]
            if (id == row[1]) and (pw == pw_):
                print("key is now " + str(key))
                key = 1
                sid = row[0]
                print("key is now " + str(key))
                print(str(sid) + " is using the service")
                return render_template('index.html', club_name=Cname, club_length=Clength, key=key)

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
    return render_template('index.html', club_name=Cname, club_length=Clength)


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
        phone = request.form['phone']
        id = request.form['ID']
        pw = request.form['PW']

        print("method ends...")
        return redirect(url_for('signup_sent', Sid=sid, Sname=sname, Major=major, Minor=minor, Nationality=nationality,
                                Gender=gender, Phone=phone, ID=id, PW=pw))

@app.route("/signup_sent/<Sid>/<Sname>/<Major>/<Minor>/<Nationality>/<Gender>/<Phone>/<ID>/<PW>")
def signup_sent(Sid, Sname, Major, Minor, Nationality, Gender, Phone, ID, PW):
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
                     VALUES('""" + Sname + """', """ + Sid + """, '""" + Major + """', '""" + Minor + """', '""" + Nationality + """', '""" + Gender + """', '""" + Phone + """', '""" + ID + """', '""" + PW + """');"""
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
