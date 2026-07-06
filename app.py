from flask import Flask, render_template, request, redirect
from database import get_jobs, add_job, add_skill
from skill_extractor import extract_skills

app = Flask(__name__)

@app.route("/")
def home():

    jobs = get_jobs()

    return render_template(
        "index.html",
        jobs=jobs
        )

@app.route("/add", methods=["POST"])
def add():

    company = request.form["company"]
    job_title = request.form["job_title"]
    salary = request.form["salary"]
    description = request.form["description"]

    job_id = add_job(
        company,
        job_title,
        salary,
        description,
        "2026-07-01"
    )
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)