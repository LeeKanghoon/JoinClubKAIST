import pymysql
import csv

# Connect to database
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='junmo12345',
                     db='joinclubkaist',
                     charset='utf8mb4')

try:
    # Set cursor to the database
    with db.cursor() as cursor:
        # Write SQL query
            sql = """LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/event_db.csv' 
                    INTO TABLE EVENT FIELDS TERMINATED BY ','
                    (Eno, @Ename, @Edate, @Stime, @Etime, @Loc, ECsn)
                    SET
                    Ename = nullif(@Ename, ''),
                    Edate = nullif(@Edate, ''),
                    Stime = nullif(@Stime, ''),
                    Etime = nullif(@Etime, ''),
                    Loc = nullif(@Loc, '');
                    """
            # Execute SQL
            cursor.execute(sql)
    # You must manually commit after every DML methods.
    db.commit()
finally:
    db.close()

# Connect to database
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='junmo12345',
                     db='joinclubkaist',
                     charset='utf8mb4')

try:
    # Set cursor to the database
    with db.cursor() as cursor:
        # Write SQL query
            sql = """LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/student_db.csv' 
                    INTO TABLE STUDENT FIELDS TERMINATED BY ','
                    (Sname, Sid, @Major, @Minor, @Nationality, @Gender, @Phone, @ID, @PW)
                    SET
                    Major = nullif(@Major, ''),
                    Minor = nullif(@Minor, ''),
                    Nationality = nullif(@Nationality, ''),
                    Gender = nullif(@Gender, ''),
                    Phone = nullif(@Phone, ''),
                    ID = nullif(@ID, ''),
                    PW = nullif(@PW, '');
                    """
            # Execute SQL
            cursor.execute(sql)
    # You must manually commit after every DML methods.
    db.commit()
finally:
    db.close()

# Connect to database
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='junmo12345',
                     db='joinclubkaist',
                     charset='utf8mb4')

try:
    # Set cursor to the database
    with db.cursor() as cursor:
        # Write SQL query
            sql = """LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/club_db_final.csv' 
                    INTO TABLE CLUB FIELDS TERMINATED BY ','
                    (Cname, Csn, @Class, @District, @Department, @Establish, @Num_member, @Num_recruit, @Activity_time, 
                    @Homepage, @Room, @CSid, @Intro)
                    SET
                    Class = nullif(@Class, ''),
                    District = nullif(@District, ''),
                    Department = nullif(@Department, ''),
                    Establish = nullif(@Establish, ''),
                    Num_member = nullif(@Num_member, ''),
                    Num_recruit = nullif(@Num_recruit, ''),
                    Activity_time = nullif(@Activity_time, ''),
                    Homepage = nullif(@Homepage, ''),
                    Room = nullif(@Room, ''),
                    CSid = nullif(@CSid, ''),
                    Intro = nullif(@Intro, '');
                    """
            # Execute SQL
            cursor.execute(sql)
    # You must manually commit after every DML methods.
    db.commit()
finally:
    db.close()


