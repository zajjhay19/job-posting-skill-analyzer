import os #Imports tools that let Python read information stored in the computer's environment.
from datetime import date #Imports date tools so the application can use the current date.
from flask import Flask, render_template, request, redirect, session, flash #Imports the Flask tools used for webpages, forms, redirects, sessions, and temporary feedback messages.

from resume_parser import extract_resume_text #Imports the machine that converts an uploaded resume file into readable text.

from database import (
    get_jobs, #Imports the machine that retrieves saved jobs from the database.
    add_job, #Imports the machine that saves a new job into the database.
    add_skill, #Imports the machine that saves an extracted skill into the skills table.
    get_skill_counts #Imports the machine that counts how many times each skill appears.
)

from skill_extractor import extract_skills #Imports the machine that finds recognized skills inside text.

from analysis import (
    find_matched_skills, #Imports the machine that finds skills shared by the job market and resume.
    find_missing_skills, #Imports the machine that finds market skills missing from the resume.
    calculate_match_percentage, #Imports the machine that calculates the resume match percentage.
    prioritize_missing_skills #Imports the machine that prioritizes missing skills using market demand.
)


app = Flask(__name__) #Creates the Flask application that runs the website.

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "dev-secret-key"
) #Gets the session secret key from the computer or uses a temporary development key if one has not been set.



@app.route("/") #Connects the home page URL to the function below.
def home(): #Builds everything needed for the main page.

    jobs = get_jobs() #Gets all saved jobs from the database.

    skill_counts = get_skill_counts() #Gets each skill and the number of times it appears in saved job postings.

    missing_skills = session.get(
        "missing_skills",
        []
    ) #Gets the missing skills from the session or uses an empty list if no resume has been analyzed yet.

    match_percentage = session.get(
        "match_percentage",
        0
    ) #Gets the resume match percentage from the session or uses 0 if no resume has been analyzed yet.

    matched_skills = session.get(
        "matched_skills",
        []
    ) #Gets the matched resume skills from the session or uses an empty list if no resume has been analyzed yet.

    prioritized_missing_skills = session.get(
        "prioritized_missing_skills",
        []
    ) #Gets the missing skills and their market demand counts from the session.

    skill_labels = [ #Creates a list containing only the skill names for Chart.js.

        skill["skill"] #Takes the skill name from the current database row.

        for skill in skill_counts #Repeats for every skill returned from the database.
    ]

    skill_data = [ #Creates a list containing only the skill counts for Chart.js.

        skill["count"] #Takes the count from the current database row.

        for skill in skill_counts #Repeats for every skill returned from the database.
    ]

    return render_template( #Sends all the information needed to build the home page.

        "index.html", #Tells Flask which HTML template to use.

        jobs=jobs, #Makes the saved jobs available inside the HTML template.

        skill_counts=skill_counts, #Makes the skill statistics available inside the HTML template.

        skill_labels=skill_labels, #Makes the chart labels available to JavaScript.

        skill_data=skill_data, #Makes the chart values available to JavaScript.

        missing_skills=missing_skills, #Makes the missing resume skills available inside the HTML template.

        match_percentage=match_percentage, #Makes the resume match percentage available inside the HTML template.

        matched_skills=matched_skills, #Makes the matched resume skills available inside the HTML template.

        prioritized_missing_skills=prioritized_missing_skills #Makes the prioritized missing skills and their demand counts available inside the HTML template.
    )



@app.route("/add", methods=["POST"]) #Connects job form submissions to the function below.
def add(): #Processes a new job posting submitted by the user.

    company = request.form["company"] #Gets the company entered by the user.

    job_title = request.form["job_title"] #Gets the job title entered by the user.

    salary = request.form["salary"] #Gets the salary entered by the user.

    description = request.form["description"] #Gets the job description entered by the user.

    if not company or not job_title or not description: #Checks if any required job information is missing.
            
        flash(
           "Please enter the company, job title, and description."
       ) #Stores a temporary message explaining which job information is required.

        return redirect("/")

    job_id = add_job( #Saves the job and stores the database ID assigned to the new job.

        company,
        job_title,
        salary,
        description,
        date.today().isoformat()
    )

    skills = extract_skills(description) #Finds all recognized skills inside the job description.

    if not skills: #Checks if the job description contained any skills the application recognizes.

        flash(
            "Job saved, but no recognized skills were found in the description."
        ) #Tells the user that the job was saved even though no skills were detected.


    for skill in skills: #Loops through every skill that was found.

        add_skill(
            job_id,
            skill
        ) #Connects each detected skill to the job it came from.

    return redirect("/") #Sends the user back to the home page after the job is saved.



@app.route("/upload_resume", methods=["POST"]) #Connects resume form submissions to the function below.
def upload_resume(): #Processes the resume uploaded by the user.

    if "resume" not in request.files: #Checks if the resume field was included in the form submission.

        flash(
             "No resume was submitted."
        ) #Stores a temporary message explaining that the resume was missing from the submission.
            
        return redirect("/")

    resume_file = request.files["resume"] #Gets the uploaded resume and stores it so the application can inspect and process it.

    if resume_file.filename == "": #Checks if the user submitted the form without selecting a file.

        flash(
            "Please select a resume before uploading."
        ) #Stores a temporary message explaining that a resume must be selected.
            
        return redirect("/")

    allowed_extensions = (
        ".pdf",
        ".docx"
    ) #Creates a group containing the resume file types that the application accepts.

    if not resume_file.filename.lower().endswith(allowed_extensions): #Checks if the uploaded resume is not a PDF or DOCX file.

        flash(
            "Only PDF and DOCX resumes are supported."
        ) #Stores a temporary message explaining why the uploaded file was rejected.

        return redirect("/")

    resume_text = extract_resume_text(
        resume_file
    ) #Converts the uploaded PDF or DOCX resume into plain text.

    resume_skills = extract_skills(
        resume_text
    ) #Finds all recognized skills inside the extracted resume text.

    skill_counts = get_skill_counts() #Gets each market skill and how many times it appears in saved job postings.

    market_skills = set() #Creates an empty set to store the unique skills found in the job market.

    for skill in skill_counts: #Loops through every skill returned from the database.

        market_skills.add(
            skill["skill"]
        ) #Adds only the skill name to the market skills set.

    resume_skills = set(
        resume_skills
    ) #Converts the resume skills list into a set so it can be compared with the market skills set.

    missing_skills = find_missing_skills(
        market_skills,
        resume_skills
    ) #Uses analysis.py to find market skills that are missing from the resume.

    matched_skills = find_matched_skills(
        market_skills,
        resume_skills
    ) #Uses analysis.py to find skills shared by the job market and the resume.

    prioritized_missing_skills = prioritize_missing_skills(
        skill_counts,
        missing_skills
    ) #Uses analysis.py to organize missing skills by their job market demand.

    match_percentage = calculate_match_percentage(
        market_skills,
        matched_skills
    ) #Uses analysis.py to calculate what percentage of market skills are already found on the resume.

    session["missing_skills"] = list(
        missing_skills
    ) #Stores the missing skills in the session so Flask remembers them after the redirect.

    session["match_percentage"] = match_percentage #Stores the resume match percentage in the session.

    session["matched_skills"] = list(
        matched_skills
    ) #Stores the matched resume skills in the session.

    session["prioritized_missing_skills"] = prioritized_missing_skills #Stores the prioritized missing skills and demand counts in the session.

    return redirect("/") #Sends the user back to the home page after the resume analysis is complete.

if __name__ == "__main__": #Checks if this file is being run directly.

    app.run(debug=True) #Starts the Flask development server.
    #