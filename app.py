import os #Imports tools that let Python read information stored in the computer's environment.
from flask import Flask, render_template, request, redirect, session #Imports the tools Flask needs to build webpages, receive form data, and move users between pages.   including session for remembering temporary user data between requests.
from resume_parser import extract_resume_text #Imports the machine that converts an uploaded resume file into readable text.

from database import (
    get_jobs, #Imports the machine that retrieves saved jobs from the database.
    add_job, #Imports the machine that saves a new job into the database.
    add_skill, #Imports the machine that saves an extracted skill into the skills table.
    get_skill_counts #Imports the machine that counts how many times each skill appears.
)

from skill_extractor import extract_skills #Imports the machine that finds skills inside text.

app = Flask(__name__) #Creates the Flask application that runs the website.
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key") #Gets the session secret key from the computer and uses a temporary development key if one has not been set.

@app.route("/") #Connects the home page URL to the function below.
def home(): #Builds everything needed for the main page.

    jobs = get_jobs() #Gets all saved jobs from the database.

    skill_counts = get_skill_counts() #Gets the number of times each skill appears.

    missing_skills = session.get("missing_skills", [])  #Gets the missing skills from the session or creates an empty list if no resume has been analyzed yet.

    match_percentage = session.get("match_percentage", 0)  #Gets the resume match percentage from the session or sets it to 0 if no resume has been analyzed yet.

    matched_skills = session.get("matched_skills", []) #Gets the matched skills from the session or creates an empty list if no resume has been analyzed yet.

    prioritized_missing_skills = session.get("prioritized_missing_skills", []) #Gets the prioritized missing skills from the session or creates an empty list if no resume has been analyzed yet.

    skill_labels = [ #Creates a list that stores only the skill names for Chart.js.

        skill["skill"] #Takes the skill name from each database row.

        for skill in skill_counts #Repeats for every skill count row returned from the database.
    ]

    skill_data = [ #Creates a list that stores only the skill counts for Chart.js.

        skill["count"] #Takes the number associated with each skill.

        for skill in skill_counts #Repeats for every skill count row returned from the database.
    ]

    return render_template( #Sends data to the HTML page so Jinja can build the webpage.

        "index.html", #Tells Flask which HTML file to build.

        jobs=jobs, #Makes the jobs list available inside the HTML template.

        skill_counts=skill_counts, #Makes the raw skill statistics available inside the HTML template.

        skill_labels=skill_labels, #Makes the chart labels available to JavaScript.

        skill_data=skill_data,  #Makes the chart values available to JavaScript.

        missing_skills=missing_skills, #Makes the missing resume skills available inside the HTML template.

        match_percentage=match_percentage, #Makes the resume match percentage available inside the HTML template.

        matched_skills=matched_skills, #Makes the matched resume skills available inside the HTML template.
        
        prioritized_missing_skills=prioritized_missing_skills #Makes the prioritized missing skills and their market counts available inside the HTML template.
        )


@app.route("/add", methods=["POST"]) #Connects form submissions to the function below.
def add(): #Processes new job submissions.

    company = request.form["company"] #Gets the company entered by the user.

    job_title = request.form["job_title"] #Gets the job title entered by the user.

    salary = request.form["salary"] #Gets the salary entered by the user.

    description = request.form["description"] #Gets the job description entered by the user.

    if not company or not job_title  or not description:#Checks if any required job information is missing.
        return redirect("/") #Sends the user back to the home page instead of saving an incomplete job.

    
    job_id = add_job( #Saves the job and receives the database ID that was assigned to it.

        company,
        job_title,
        salary,
        description,
        "2026-07-01"
    )

    skills = extract_skills(description) #Finds all recognized skills inside the job description.

    for skill in skills: #Repeats once for every skill that was found.

        add_skill(job_id, skill) #Connects each skill to the job that it came from.

    return redirect("/") #Sends the user back to the home page after processing is complete.

@app.route("/upload_resume", methods=["POST"]) #Connects resume form submissions to the function below.
def upload_resume(): #Processes the resume uploaded by the user.

    if "resume" not in request.files:#Checks if the resume file was included in the form submission.

        return redirect("/")#Sends the user back to the home page if no resume file was submitted.

    resume_file = request.files["resume"] #Gets the resume file that the user uploaded through the HTML form.

    if resume_file.filename == "":#Checks if the user submitted the form without selecting a resume file.

        return redirect("/")#Sends the user back to the home page if no resume file was selected.
    
    allowed_extensions =(".pdf",".docx")#Creates a group containing the resume file types that the application accepts.

    if not resume_file.filename.lower().endswith(allowed_extensions):

        return redirect("/")
    
    resume_text = extract_resume_text(resume_file) #Converts the uploaded PDF or DOCX resume into plain text.

    resume_skills = extract_skills(resume_text) #Finds all recognized skills inside the extracted resume text.

    skill_counts = get_skill_counts() #Gets all skills found in the saved job postings and how many times each one appears.

    market_skills = set() #Creates an empty box to store unique skills found in the job market.

    for skill in skill_counts: #Loops through every skill returned by the database.

        market_skills.add(skill["skill"]) #Adds only the skill name into the market skills set.

    resume_skills = set(resume_skills) #Converts the resume skills list into a set so it can be compared with another set.

    missing_skills = market_skills - resume_skills #Finds the skills that employers want that are missing from the resume.

    prioritized_missing_skills = []#Creates an empty list to store missing skills together with how often employers request them.

    for skill in skill_counts:#Loops through every skill and its count returned from the database.

        if skill["skill"] in missing_skills:#Checks if the current skill from the database is one of the skills missing from the resume.
                prioritized_missing_skills.append(
                        {
                            "skill": skill["skill"],
                            "count": skill["count"]
                        }
                ) #Adds the missing skill and its market count as a normal dictionary that Flask can store in the session.

    matched_skills = market_skills & resume_skills #Finds the skills that appear in both the job market and the resume.

    if len(market_skills) > 0: #Checks if there are any skills in the job market.

        match_percentage = round((len(matched_skills) / len(market_skills)) * 100) #Calculates the percentage of market skills that are already on the resume.

    else:

        match_percentage = 0

    session["missing_skills"] = list(missing_skills) #Stores the missing skills in the session so Flask can remember them after the redirect.

    session["match_percentage"] = match_percentage #Stores the resume match percentage in the session so Flask can remember it after the redirect.

    session["matched_skills"] = list(matched_skills) #Stores the matched skills in the session so Flask can remember them after the redirect.

    session["prioritized_missing_skills"] = prioritized_missing_skills #Stores the prioritized missing skills in the session so Flask can remember them after the redirect.

    print(missing_skills) #Displays the missing skills in the terminal so we can test the comparison.

    print(resume_skills) #Displays the detected resume skills in the terminal so we can test that everything works.

    print(match_percentage) #Displays the resume match percentage in the terminal so we can test the calculation.

    return redirect("/") #Sends the user back to the home page after the resume analysis is complete.

if __name__ == "__main__": #Checks if this file is being run directly.

    app.run(debug=True) #Starts the Flask development server.