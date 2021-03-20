"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    # return f"{github} is the GitHub account for {first} {last}"
    # after updating thae function
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html



@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student_infor_form")    
def student_infor_form():
    """Form to fill out new student."""
    return render_template("student_infor_form.html")

@app.route("/student-add", methods=['GET','POST'])
def student_add():
    """Add a student."""

    github = request.form.get('github')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')


    # return f"{github} is the GitHub account for {first} {last}"
    # after updating thae function
    html = render_template("create_student.html",
                           first_name=first_name,
                           last_name=last_name,
                           github=github)
                           
    first_name, last_name, github = hackbright.make_new_student(first_name, last_name, github)

    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
