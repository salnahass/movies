from flask import Flask, render_template, request
from projects import Project  # Assuming the Project class is in a file named projects.py

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    projectList = Project.getAllProjects()
    return render_template('index.html', message=projectList)

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "GET":
        projectList = Project.getAllProjects()
        return render_template('delete.html', message=projectList)
    elif request.method == "POST":
        title = request.form.get("projtitle", 0)
        Project.delProjects_Title_DB(title)
        projectList = Project.getAllProjects()
        return render_template('delete.html', message=projectList)
    else:
        return render_template('delete.html', message="Something did not work.")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        projectList = Project.getAllProjects()
        return render_template('add.html', message=projectList)
    elif request.method == "POST":
        title = request.form.get("projtitle", 0)
        description = request.form.get("projdesc", 0)
        imageFileName = request.form.get("ImageFileName", 0)
        Project.saveProjectDB(title, description, imageFileName)
        projectList = Project.getAllProjects()
        return render_template('add.html', message=projectList)
    else:
        return render_template('add.html', message='Something went wrong.')

app.run(debug=True)
