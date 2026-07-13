from flask import Flask, render_template, request, redirect
from database import (
    get_jobs,
    add_job,
    add_skill,
    get_skill_counts
    )

from skill_extractor import extract_skills

app = Flask(__name__)

@app.route("/")
def home():

    jobs = get_jobs()

    skill_counts = get_skill_counts()

    skill_labels = [
        skill["skill"]
        for skill in skill_counts
    ]

    skill_data = [
        skill["count"]
        for skill in skill_counts
    ]

    return render_template(
        "index.html",
        jobs=jobs,
        skill_counts=skill_counts,
        skill_labels=skill_labels,
        skill_data=skill_data
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

    skills = extract_skills(description)

    for skill in skills:
        add_skill(job_id, skill)

    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)