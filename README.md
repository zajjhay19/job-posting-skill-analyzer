# Job Posting Skill Analyzer

A Flask web application that analyzes job postings, extracts technical skills from job descriptions, compares them with an uploaded résumé, and identifies the most important skill gaps based on current job-market demand.

This project was built as part of my backend software development portfolio to demonstrate practical experience with Python, Flask, SQLite, SQL, HTML, CSS, Bootstrap, Jinja2, Chart.js, file processing, database design, and Git.

---

## Project Status

**Version:** 1.0

**Status:** ✅ Complete

This project is feature-complete as a portfolio application and demonstrates backend software development, relational database design, file processing, server-side rendering, data visualization, and business-logic separation using Python and Flask.

---

## Project Highlights

- Backend web application built with Python and Flask
- SQLite relational database
- PDF and DOCX résumé parsing
- Automatic technical skill extraction
- Resume-to-job-market skill comparison
- Skill gap prioritization based on employer demand
- Live analytics dashboard using Chart.js
- Responsive Bootstrap interface
- Light and Dark Mode support
- Modular project architecture

---

# Screenshots

## Dashboard

### Light Mode

![Dashboard 1](screenshots/dashboard/light-1.png)

![Dashboard 2](screenshots/dashboard/light-2.png)

### Dark Mode

![Dashboard 1](screenshots/dashboard/dark-1.png)

![Dashboard 2](screenshots/dashboard/dark-2.png)

---

## Resume Analysis

### Light Mode

![Analysis 1](screenshots/resume-analysis/light-1.png)

![Analysis 2](screenshots/resume-analysis/light-2.png)

![Analysis 3](screenshots/resume-analysis/light-3.png)

### Dark Mode

![Analysis 1](screenshots/resume-analysis/dark-1.png)

![Analysis 2](screenshots/resume-analysis/dark-2.png)

![Analysis 3](screenshots/resume-analysis/dark-3.png)



## Features

- Add and save job postings
- Store job data in a SQLite database
- Automatically extract recognized skills from job descriptions
- Store extracted skills in a separate database table
- Count how often each skill appears across saved job postings
- Display live skill-frequency analytics using Chart.js
- Upload PDF and DOCX résumés
- Extract text from uploaded résumés
- Detect recognized skills in résumé text
- Compare résumé skills with current job-market skills
- Calculate a résumé-to-market match percentage
- Display matched résumé skills
- Display prioritized missing skills
- Rank missing skills by employer demand
- Validate required job-posting fields
- Reject unsupported résumé file types
- Display user-friendly validation messages
- Preserve analysis results using Flask sessions
- Automatically save the current date
- Responsive Bootstrap dashboard
- Light and Dark Mode theme toggle
- Custom dashboard cards and styling
- Git and GitHub version control

---

## Technologies Used

### Backend

- Python 3
- Flask

### Database

- SQLite

### Resume Processing

- pypdf
- python-docx

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- Jinja2
- Chart.js

### Libraries

- re (Regular Expressions)

### Development Tools

- Git
- GitHub

### Concepts

- CRUD operations
- Session management
- Relational databases
- Business logic separation
- Data visualization
- File processing
- Responsive web design

---

## Project Structure

```text
job-posting-skill-analyzer/
│
├── app.py
├── analysis.py
├── database.py
├── resume_parser.py
├── skill_extractor.py
├── jobs.db
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Application Architecture

```text
                 User

                   │

                   ▼

          Flask Application

                   │

      ┌────────────┼────────────┐

      ▼            ▼            ▼

 Database      Analysis     Resume Parser

(SQLite)         Logic

      │            │            │

      └────────► Skill Extractor

                    │

                    ▼

            Jinja2 Templates

                    │

                    ▼

         Bootstrap Dashboard
```

---

## Database Design

### jobs

| Column | Description |
|---------|-------------|
| id | Primary Key |
| company | Company name |
| job_title | Job title |
| salary | Salary |
| description | Job description |
| date_added | Date added |

### skills

| Column | Description |
|---------|-------------|
| id | Primary Key |
| job_id | Related job |
| skill | Extracted skill |

Each extracted skill is linked back to its originating job posting through the **job_id** foreign key.

---

## Skill Detection

The application currently recognizes technical skills across:

- Programming Languages
- Backend Development
- Frontend Development
- Databases
- Cloud Platforms
- DevOps
- Data Analytics
- Artificial Intelligence
- Testing Tools
- APIs and Software Architecture

Skill detection is case-insensitive and supports dozens of commonly requested technologies.

---

## How the Application Works

### Job Analysis

1. User submits a job posting.
2. Flask validates the input.
3. The job is stored in SQLite.
4. The skill extractor scans the description.
5. Skills are saved in the database.
6. SQL aggregates skill frequencies.
7. Chart.js visualizes the results.

### Resume Analysis

1. User uploads a PDF or DOCX résumé.
2. Flask validates the file.
3. Text is extracted.
4. Skills are detected.
5. Resume skills are compared with market skills.
6. The application calculates:
   - Match percentage
   - Matched skills
   - Missing skills
   - Missing-skill demand
7. Results are displayed on the dashboard.

---

## Resume Match Percentage

The application compares unique résumé skills against unique skills found across saved job postings.

```
Matched Skills
────────────── × 100
Market Skills
```

If there are no market skills available, the application safely returns **0%** instead of dividing by zero.

---

## Missing Skill Prioritization

Missing skills are sorted by employer demand.

Example:

```
Docker      — 5 job postings
AWS         — 3 job postings
Azure       — 1 job posting
```

This helps users identify which missing skills are likely to have the greatest impact on employability.

---

## Validation & Error Handling

The application handles:

- Missing required fields
- Blank résumé uploads
- Unsupported file types
- Empty databases
- Job descriptions with no recognized skills
- Résumés with no recognized skills
- Division-by-zero scenarios
- Empty skill sets
- Missing chart data

---

## Running the Project

```bash
git clone https://github.com/zajjhay19/job-posting-skill-analyzer.git

cd job-posting-skill-analyzer

python -m venv venv

venv\Scripts\Activate.ps1

pip install -r requirements.txt

python database.py

python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## Testing Completed

✔ Normal job posting

✔ Blank salary

✔ Missing required fields

✔ PDF résumé

✔ DOCX résumé

✔ Unsupported file type

✔ Blank résumé

✔ No recognized skills

✔ Partial résumé match

✔ Full résumé match

✔ Empty database

✔ Empty dashboard states

✔ Dark Mode

✔ Light Mode

---

## What I Learned

This project strengthened my understanding of:

- Python programming
- Flask application structure
- SQL and SQLite
- Relational database design
- CRUD operations
- Business-logic separation
- Session management
- PDF and DOCX parsing
- File uploads
- Jinja2 templating
- Bootstrap
- Responsive design
- Chart.js
- Git and GitHub
- Debugging and testing
- Building complete backend applications

---

## Future Improvements

- Deploy to Render
- Docker support
- PostgreSQL support
- User authentication
- Edit/Delete job postings
- Search and filtering
- Export reports
- Salary analytics
- Company analytics
- REST API
- Automated unit tests
- NLP-based skill extraction
- Weighted résumé scoring

---

## Author

**Zajae Hayles**

Aspiring Backend Software Developer

GitHub:

https://github.com/zajjhay19

---

## License

This project was created for educational purposes and as part of my software development portfolio.
