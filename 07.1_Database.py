# import psycopg2 as pg
# import csv
# try:
#     con=pg.connect(
#         host='localhost',
#         database='Test',
#         user='postgres',
#         password='Admin@123',
#         port='5432')
#     cur=con.cursor()
#     with open(r'C:\Users\ppras\OneDrive\Desktop\Student_deails_new.csv')as f:
#         read=csv.reader(f)
#         data=list(read)[1:]
#         # print(data)
#         for record in data:
#             print(record)
#             insert=f'''Insert into student_details(roll_no,student_name,class,mark,grade)
#             values({record[0]},'{record[1]}','{record[2]}',{record[3]},'{record[4]}')'''
#             cur.execute(insert)
#
#
#     con.commit()
# finally:
#     cur.close()
#     con.close()

# import psycopg2 as pg
# import csv
# try:
#     con=pg.connect(
#         host='localhost',
#         database='Test',
#         user='postgres',
#         password='Admin@123',
#         port='5432'
#     )
#     cur=con.cursor()
#     with open(r'C:\Users\ppras\OneDrive\Desktop\Student_deails_new.csv') as f:
#         read=csv.reader(f)
#         data=list(read) [1:]
#         # print(data)
#         for record in data:
#             print(record)
#             insert=f'''Insert into student_details(roll_no,student_name,class,mark,grade)
#             values({record[0]},'{record[1]}','{record[2]}',{record[3]},'{record[4]}') '''
#             cur.execute(insert)
#     con.commit()
# finally:
#     cur.close()
#     con.close()
# import logging
# logging.basicConfig(filename='looging Text',level=logging.DEBUG)
# message='Logging module demo'
# logging.debug(message)

import psycopg2 as pg
import csv

# import os
# host=os.environ['ht']
# database=os.environ['db']
# user=os.environ['us']
# password=os.environ['pass']
#
# try:
#     con=pg.connect(
#         host='ht',
#         database='db',
#         user='us',
#         password='pass',
#         port='5432'
#     )
#     cur=con.cursor()
#     with open(r'C:\Users\ppras\OneDrive\Desktop\student_details_1.csv','r') as f:
#         read=csv.reader(f)
#         data=list(read) [1:]
#         # print(data [1:])
#         for record in data:
#             print(record)
#     insert=f'''Insert into student_details_1 (roll_no,student_name,class,mark,grade) values ({record[0]},'{record[1]}','{record[2]}',{record[3]},'{record[4]}')'''
#     cur.execute(insert)
#     con.commit()
# finally:
#     cur.close()
#     con.close()

# import psycopg2 as pg
# import csv
# try:
#     con=pg.connect(
#             host='localhost',
#             database='Test',
#             user='postgres',
#             password='Admin@123',
#             port='5432'
#         )
#     cur=con.cursor()
#     # with open(r'C:\Users\ppras\OneDrive\Desktop\Employee_3.csv','r') as f:
#     #     read=csv.reader(f)
#     #     data=list(read) [1:]
#     #     # print(data)
#     #     for record in data:
#             # print(record)
#             # insert=f'''Insert Into employee.Employee_3 values ({record[0]},'{record[1]}',{record[2]},'{record[3]}') '''
#             # cur.execute(insert)
#     insert = '''Insert Into employee.Employee_3 values (9,'F',35000,'testing',15)'''
#     cur.execute(insert)
#
#     con.commit()
# finally:
#     cur.close()
#     con.close()










