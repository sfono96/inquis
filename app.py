from flask import Flask, render_template
from data import *
 
app = Flask(__name__)
 
# @app.route('/')
# @app.route('/index')
# def index(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
# 	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
# 	series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
# 	title = {"text": 'My Title'}
# 	xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
# 	yAxis = {"title": {"text": 'yAxis Label'}}
# 	return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
 
@app.route('/')
@app.route('/index')
def index(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Overall Scores', "data": overall_scores}]
	title = {"text": 'Weekly Assessment Tracking - Overall'}
	xAxis = {"categories": overall_dates, "title":{"text":'Week'}}
	yAxis = {"title": {"text": 'Score %'}}
	return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

@app.route('/grade')
def grade(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Kindergarten', "data": kindergarten_scores},{"name": '1st Grade', "data": first_scores},{"name": '2nd Grade', "data": second_scores},
	{"name": '3rd Grade', "data": third_scores},{"name": '4th Grade', "data": fourth_scores},{"name": '5th Grade', "data": fifth_scores},
	{"name": '6th Grade', "data": sixth_scores}]
	title = {"text": 'Weekly Assessment Tracking - By Grade'}
	xAxis = {"categories": overall_dates, "title":{"text":'Week'}}
	yAxis = {"title": {"text": 'Score %'}}
	return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

@app.route('/teacher/all')
def allTeachers(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}
	series = all_teachers
	title = {"text": 'Weekly Assessment Tracking - By Teacher - All Grades'}
	xAxis = {"categories": overall_dates, "title":{"text":'Week'}}
	yAxis = {"title": {"text": 'Score %'}}
	return render_template('teacher.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

@app.route('/teacher/kindergarten')
def kindergartenTeachers(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}
	series = kindergarten_teachers
	title = {"text": 'Weekly Assessment Tracking - By Teacher - Kindergarten'}
	xAxis = {"categories": overall_dates, "title":{"text":'Week'}}
	yAxis = {"title": {"text": 'Score %'}}
	return render_template('teacher.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

@app.route('/teacher/first')
def firstTeachers(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}
	series = first_grade_teachers
	title = {"text": 'Weekly Assessment Tracking - By Teacher - 1st Grade'}
	xAxis = {"categories": overall_dates, "title":{"text":'Week'}}
	yAxis = {"title": {"text": 'Score %'}}
	return render_template('teacher.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

@app.route('/teacher/second')
def secondTeachers(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}
	series = second_grade_teachers
	title = {"text": 'Weekly Assessment Tracking - By Teacher - 2nd Grade'}
	xAxis = {"categories": overall_dates, "title":{"text":'Week'}}
	yAxis = {"title": {"text": 'Score %'}}
	return render_template('teacher.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

@app.route('/teacher/third')
def thirdTeachers(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}
	series = third_grade_teachers
	title = {"text": 'Weekly Assessment Tracking - By Teacher - 3rd Grade'}
	xAxis = {"categories": overall_dates, "title":{"text":'Week'}}
	yAxis = {"title": {"text": 'Score %'}}
	return render_template('teacher.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

@app.route('/teacher/fourth')
def fourthTeachers(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}
	series = fourth_grade_teachers
	title = {"text": 'Weekly Assessment Tracking - By Teacher - 4th Grade'}
	xAxis = {"categories": overall_dates, "title":{"text":'Week'}}
	yAxis = {"title": {"text": 'Score %'}}
	return render_template('teacher.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

@app.route('/teacher/fifth')
def fifthTeachers(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}
	series = fifth_grade_teachers
	title = {"text": 'Weekly Assessment Tracking - By Teacher - 5th Grade'}
	xAxis = {"categories": overall_dates, "title":{"text":'Week'}}
	yAxis = {"title": {"text": 'Score %'}}
	return render_template('teacher.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

@app.route('/teacher/sixth')
def sixthTeachers(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}
	series = sixth_grade_teachers
	title = {"text": 'Weekly Assessment Tracking - By Teacher - 6th Grade'}
	xAxis = {"categories": overall_dates, "title":{"text":'Week'}}
	yAxis = {"title": {"text": 'Score %'}}
	return render_template('teacher.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)


if __name__ == "__main__":
	#app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
	app.run(debug = True)