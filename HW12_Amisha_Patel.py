""" Author  :: Amisha Patel 
    Created :: 12/01/2020 """
import sqlite3
from flask import Flask, render_template, redirect
from typing import Dict, List, Tuple
app:Flask = Flask(__name__)
sqlite_file: str = "R:/Steven Institute/SSW -810-B/HW12/810_startup.db"
@app.route('/')
def index() -> str:
    return redirect('/student')
@app.route('/student')
def student_summary() -> str:
    """This function converts the query results into a list of dictionaries to the HTML template """
    query: str = "select students.Name,students.CWID,grades.Course,grades.Grade,instructors.Name from students,grades,instructors where students.CWID = StudentCWID and InstructorCWID = instructors.CWID order by students.Name;"
    db: sqlite3.Connection = sqlite3.connect(sqlite_file)
    student_data :Dict[str,str] = [{'Name': name, 'CWID': cwid, 'Course': course, 'Grade': grade,
                                 'Instructor': instructor} for name, cwid, course, grade, instructor in db.execute(query)]
    db.close() 
    return render_template('student.html',
        title='Stevens Repository',
        table_title='Student, Course, Grade, and Instructor',
        students=student_data)
app.run(debug=True)