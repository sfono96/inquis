import MySQLdb as mdb
import sys
import re
from datetime import date, timedelta, datetime

con = None

host = '127.0.0.1'
user = 'root'
password = 'password'
database = 'inquis'

con = mdb.connect(host,user,password,database)
cur = con.cursor()

# overall data series
overallSQL = 'Select date, avg(score) from assessment_tracking group by date order by date'
cur.execute(overallSQL)
rs = cur.fetchall()
overall_dates = [date.strftime(x[0],'%m-%d-%Y') for x in rs]
overall_scores = [float(x[1]) for x in rs]

# grade data series
gradeSQL = 'Select date, grade, avg(score) from assessment_tracking group by date, grade order by date'
cur.execute(gradeSQL)
rs1 = cur.fetchall()
grade_dates = [date.strftime(x[0],'%m-%d-%Y') for x in rs1]
kindergarten_scores = [float(x[2]) for x in rs1 if x[1] == 'k']
first_scores = [float(x[2]) for x in rs1 if x[1] == '1']
second_scores = [float(x[2]) for x in rs1 if x[1] == '2']
third_scores = [float(x[2]) for x in rs1 if x[1] == '3']
fourth_scores = [float(x[2]) for x in rs1 if x[1] == '4']
fifth_scores = [float(x[2]) for x in rs1 if x[1] == '5']
sixth_scores = [float(x[2]) for x in rs1 if x[1] == '6']


### teachers ###

# all teachers'
teacherSQL = 'Select date, teacher, avg(score) from assessment_tracking group by date, teacher order by date'
cur.execute(teacherSQL)
rs2 = cur.fetchall()
teachers = []
for row in rs2:
	if row[1] not in teachers:
		teachers.append(row[1])

all_teachers = []
for teacher in teachers:
	dict = {}
	dict['name'] = teacher
	dict['data'] = [float(x[2]) for x in rs2 if x[1] == teacher]
	all_teachers.append(dict)

# kindergarten teachers'
teacherSQL = 'Select date, teacher, avg(score) from assessment_tracking where grade = \'k\' group by date, teacher order by date'
cur.execute(teacherSQL)
rs2 = cur.fetchall()
teachers = []
for row in rs2:
	if row[1] not in teachers:
		teachers.append(row[1])

kindergarten_teachers = []
for teacher in teachers:
	dict = {}
	dict['name'] = teacher
	dict['data'] = [float(x[2]) for x in rs2 if x[1] == teacher]
	kindergarten_teachers.append(dict)

# first grade teachers'
teacherSQL = 'Select date, teacher, avg(score) from assessment_tracking where grade = \'1\' group by date, teacher order by date'
cur.execute(teacherSQL)
rs2 = cur.fetchall()
teachers = []
for row in rs2:
	if row[1] not in teachers:
		teachers.append(row[1])

first_grade_teachers = []
for teacher in teachers:
	dict = {}
	dict['name'] = teacher
	dict['data'] = [float(x[2]) for x in rs2 if x[1] == teacher]
	first_grade_teachers.append(dict)

# second grade teachers'
teacherSQL = 'Select date, teacher, avg(score) from assessment_tracking where grade = \'2\' group by date, teacher order by date'
cur.execute(teacherSQL)
rs2 = cur.fetchall()
teachers = []
for row in rs2:
	if row[1] not in teachers:
		teachers.append(row[1])

second_grade_teachers = []
for teacher in teachers:
	dict = {}
	dict['name'] = teacher
	dict['data'] = [float(x[2]) for x in rs2 if x[1] == teacher]
	second_grade_teachers.append(dict)

# third grade teachers'
teacherSQL = 'Select date, teacher, avg(score) from assessment_tracking where grade = \'3\' group by date, teacher order by date'
cur.execute(teacherSQL)
rs2 = cur.fetchall()
teachers = []
for row in rs2:
	if row[1] not in teachers:
		teachers.append(row[1])

third_grade_teachers = []
for teacher in teachers:
	dict = {}
	dict['name'] = teacher
	dict['data'] = [float(x[2]) for x in rs2 if x[1] == teacher]
	third_grade_teachers.append(dict)

# fourth grade teachers'
teacherSQL = 'Select date, teacher, avg(score) from assessment_tracking where grade = \'4\' group by date, teacher order by date'
cur.execute(teacherSQL)
rs2 = cur.fetchall()
teachers = []
for row in rs2:
	if row[1] not in teachers:
		teachers.append(row[1])

fourth_grade_teachers = []
for teacher in teachers:
	dict = {}
	dict['name'] = teacher
	dict['data'] = [float(x[2]) for x in rs2 if x[1] == teacher]
	fourth_grade_teachers.append(dict)

# fifth grade teachers'
teacherSQL = 'Select date, teacher, avg(score) from assessment_tracking where grade = \'5\' group by date, teacher order by date'
cur.execute(teacherSQL)
rs2 = cur.fetchall()
teachers = []
for row in rs2:
	if row[1] not in teachers:
		teachers.append(row[1])

fifth_grade_teachers = []
for teacher in teachers:
	dict = {}
	dict['name'] = teacher
	dict['data'] = [float(x[2]) for x in rs2 if x[1] == teacher]
	fifth_grade_teachers.append(dict)

# sixth grade teachers'
teacherSQL = 'Select date, teacher, avg(score) from assessment_tracking where grade = \'6\' group by date, teacher order by date'
cur.execute(teacherSQL)
rs2 = cur.fetchall()
teachers = []
for row in rs2:
	if row[1] not in teachers:
		teachers.append(row[1])

sixth_grade_teachers = []
for teacher in teachers:
	dict = {}
	dict['name'] = teacher
	dict['data'] = [float(x[2]) for x in rs2 if x[1] == teacher]
	sixth_grade_teachers.append(dict)

con.close()