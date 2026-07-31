# Job Posting Skill Analyzer

A Flask web application that analyzes job postings, extracts technical skills, compares them with an uploaded résumé, and identifies the most important skill gaps based on job-market demand.

This project was built as part of my backend software development portfolio to demonstrate practical experience with Python, Flask, SQLite, SQL, HTML, CSS, Bootstrap, Jinja2, Chart.js, file processing, and Git.

---

## Features

- Add and save job postings
- Store job data in a SQLite database
- Automatically extract recognized skills from job descriptions
- Store extracted skills in a separate database table
- Count how often each skill appears across saved job postings
- Display skill-frequency data in a Chart.js bar chart
- Upload PDF and DOCX résumés
- Extract text from uploaded résumés
- Detect recognized skills in résumé text
- Compare résumé skills with current job-market skills
- Calculate a résumé-to-market match percentage
- Display matched résumé skills
- Display missing résumé skills
- Prioritize missing skills by how often employers request them
- Validate required job-posting fields
- Reject unsupported résumé file types
- Display user-facing validation messages
- Use Flask sessions to preserve analysis results after redirects
- Automatically save the current date when a job is added
- Responsive Bootstrap dashboard layout
- Custom CSS cards, spacing, shadows, and page styling
- Git and GitHub version control

---

## Technologies Used

### Backend

- Python 3
- Flask
- SQLite3

### Résumé Processing

- pypdf
- python-docx

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- Jinja2
- Chart.js

### Database

- SQLite

### Version Control

- Git
- GitHub

---

## Project Structure

```text
job-posting-skill-analyzer/
│
├── app.py                 # Flask routes, request handling, sessions, and validation
├── analysis.py            # Skill comparison and analysis functions
├── database.py            # Database creation and query functions
├── resume_parser.py       # PDF and DOCX text extraction
├── skill_extractor.py     # Skill detection logic
├── jobs.db                # Local SQLite database ignored by Git
│
├── templates/
│   └── index.html         # Main Jinja2 template
│
├── static/
│   └── style.css          # Custom application styling
│
├── .gitignore
└── README.md
```

---

## Application Architecture

The application separates its responsibilities across multiple files:

```text
app.py
│
├── Handles Flask routes
├── Receives form submissions
├── Validates user input
├── Manages sessions
└── Sends data to the HTML template

analysis.py
│
├── Finds matched skills
├── Finds missing skills
├── Calculates the match percentage
└── Prioritizes missing skills by market demand

database.py
│
├── Creates database tables
├── Saves jobs
├── Saves extracted skills
├── Retrieves saved jobs
└── Calculates skill-frequency counts

resume_parser.py
│
└── Converts PDF and DOCX résumés into plain text

skill_extractor.py
│
└── Detects recognized skills inside job descriptions and résumés
```

---

## Database Design

### `jobs` table

| Column | Description |
|---|---|
| `id` | Primary key |
| `company` | Company name |
| `job_title` | Job title |
| `salary` | Salary information |
| `description` | Full job description |
| `date_added` | Date the job was added |

### `skills` table

| Column | Description |
|---|---|
| `id` | Primary key |
| `job_id` | ID of the related job posting |
| `skill` | Extracted skill name |

The `job_id` column connects each extracted skill to the job posting where it was found.

---

## Current Skill List

The application currently recognizes skills across several categories.

### Programming Languages

- Python
- SQL
- Java
- JavaScript
- TypeScript
- C#
- C++
- Go
- PHP
- Ruby
- Kotlin
- Swift
- Scala

### Backend Frameworks and Tools

- Flask
- Django
- FastAPI
- Spring Boot
- Node.js
- Express.js
- .NET
- Laravel
- Ruby on Rails

### Frontend Technologies

- HTML
- CSS
- React
- Angular
- Vue.js
- Bootstrap
- Tailwind CSS

### Databases

- SQLite
- MySQL
- PostgreSQL
- MongoDB
- Microsoft SQL Server
- Oracle
- Redis

### Cloud Platforms

- AWS
- Azure
- Google Cloud
- Firebase

### DevOps and Deployment

- Docker
- Kubernetes
- Git
- GitHub
- GitLab
- Jenkins
- Terraform
- Linux
- Nginx

### Data and Analytics

- Excel
- Power BI
- Tableau
- Pandas
- NumPy
- Matplotlib
- Apache Spark

### Artificial Intelligence and Machine Learning

- TensorFlow
- PyTorch
- Scikit-learn
- Machine Learning
- Natural Language Processing

### Testing and Development Tools

- Selenium
- Pytest
- JUnit
- Postman
- Jira

### APIs and Architecture

- REST API
- GraphQL
- Microservices
- JSON
- XML

Skill detection is case-insensitive.

### Example

Input:

```text
Looking for python, Flask, SQL and Docker experience.
```

Detected skills:

```text
Python
SQL
Flask
Docker
```

---

## How the Application Works

### Job-posting analysis

1. The user enters a company, job title, salary, and job description.
2. Flask validates the required information.
3. The job is saved in the `jobs` table.
4. The skill extractor checks the description against the recognized skill list.
5. Each detected skill is saved in the `skills` table.
6. SQLite groups matching skills and calculates how often each skill appears.
7. Chart.js displays the current skill-frequency results.

### Résumé analysis

1. The user uploads a PDF or DOCX résumé.
2. Flask validates that a supported file was submitted.
3. The résumé parser extracts plain text from the file.
4. The skill extractor identifies recognized résumé skills.
5. The application compares résumé skills with skills from saved job postings.
6. The analysis layer calculates:
   - matched skills
   - missing skills
   - match percentage
   - missing-skill demand counts
7. Flask stores the results in the session.
8. The dashboard displays the completed résumé analysis.

---

## Match Percentage

The match percentage represents how many unique job-market skills were found on the uploaded résumé.

```text
matched market skills
--------------------- × 100
total market skills
```

Example:

```text
Matched skills: 6
Market skills: 8

6 ÷ 8 × 100 = 75%
```

If there are no market skills available, the application returns `0%` instead of attempting to divide by zero.

---

## Missing-Skill Prioritization

Missing skills are displayed with the number of saved job postings in which they appeared.

Example:

```text
Docker - 5 job postings
AWS - 3 job postings
Azure - 1 job posting
```

This helps the user decide which missing skills may be most valuable to learn first.

---

## Validation and Error Handling

The application handles several common edge cases:

- Missing company, job title, or job description
- Missing résumé field
- No résumé file selected
- Unsupported résumé file type
- Job descriptions containing no recognized skills
- Résumés containing no recognized skills
- No market skills available for comparison
- Empty sets during percentage calculations

Only PDF and DOCX résumés are accepted.

---

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/zajjhay19/job-posting-skill-analyzer.git
```

### 2. Move into the project folder

```bash
cd job-posting-skill-analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, temporarily allow it for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then run:

```powershell
venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install flask pypdf python-docx
```

These packages are used for:

- **Flask** — runs the web application
- **pypdf** — reads PDF résumés
- **python-docx** — reads Microsoft Word `.docx` résumés

### 6. Create the database

```bash
python database.py
```

This creates the required `jobs` and `skills` tables.

### 7. Run the application

```bash
python app.py
```

### 8. Open the application

Open a browser and visit:

```text
http://127.0.0.1:5000
```

---

## Testing Completed

The following workflows and edge cases have been tested:

- Add a normal job posting
- Add a job containing recognized skills
- Add a job containing no recognized skills
- Upload a valid PDF résumé
- Upload a valid DOCX résumé
- Upload an unsupported TXT file
- Submit a résumé form without a file
- Analyze a résumé containing no recognized skills
- Calculate a match percentage with no market skills
- Confirm matched skills appear correctly
- Confirm missing skills appear correctly
- Confirm missing-skill demand counts appear correctly
- Confirm the chart updates after adding new jobs
- Confirm the application loads when the database is empty
- Confirm the app works after cloning it onto another computer

---

## What I Learned

Through this project, I practiced:

- Python programming
- Flask web development
- Flask routing
- Request and form handling
- Flask sessions
- User-input validation
- Flash messages
- File uploads
- PDF processing
- DOCX processing
- SQLite database design
- SQL queries
- Primary and foreign-key relationships
- CRUD-style database operations
- Python functions
- Lists, sets, tuples, and dictionaries
- Set difference and intersection
- Defensive programming
- Division-by-zero protection
- Business-logic separation
- Jinja2 templating
- HTML forms
- CSS styling
- Bootstrap responsive layouts
- Chart.js data visualization
- Git commits
- GitHub pushes and pulls
- Rebase conflict resolution
- Virtual environments
- Debugging Python and Flask errors

---

## Future Improvements

Possible future improvements include:

- Deploy the application online
- Add PostgreSQL support
- Add user accounts and authentication
- Add job deletion and editing
- Search and filter saved job postings
- Export analysis results
- Add salary analytics
- Add company analytics
- Expand the recognized skill library
- Replace substring matching with NLP-based skill extraction
- Add weighted résumé matching using skill demand
- Add automated tests
- Add a REST API
- Add Docker deployment support

---

## Author

**Zajae Hayles**

GitHub:

```text
https://github.com/zajjhay19
```

---

## License

This project was created for educational and portfolio purposes.
