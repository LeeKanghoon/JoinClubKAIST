import pymysql
import csv
import numpy

f1 = open('./club_db.csv','r', encoding='utf-8', errors='ignore')
r1 = csv.reader(f1)
club_db = []
for row in r1:
    club_db.append(row)
f1.close()
club_db = club_db[1:]

# Connect to database
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='rkdgns7549!!',
                     db='joinclubkaist',
                     charset='utf8')

try:
    # Set cursor to the database
    with db.cursor() as cursor:
        # Write SQL query
            sql = """LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/club_db.csv'
                    INTO TABLE CLUB FIELDS TERMINATED BY ','
                    (Cname, Csn, @Class, @District, @Department, @Establish, @Num_member, @Num_recruit, @Activity_time, @Phone, @Homepage, @Room, @CSid)
                    SET
                    Class = nullif(@Class, ''),
                    District = nullif(@District, ''),
                    Department = nullif(@Department, ''),
                    Establish = nullif(@Establish, ''),
                    Num_member = nullif(@Num_member, ''),
                    Num_recruit = nullif(@Num_recruit, ''),
                    Activity_time = nullif(@Activity_time, ''),
                    Phone = nullif(@Phone, ''),
                    Homepage = nullif(@Homepage, ''),
                    Room = nullif(@Room, ''),
                    CSid = nullif(@CSid, '');
                    """
            # Execute SQL
            cursor.execute(sql)
    # You must manually commit after every DML methods.
    db.commit()
finally:
    db.close()
