# Job Posting Skill Analyzer

A Flask web application that analyzes job postings, extracts technical skills from job descriptions, and stores the results in a SQLite database.

This project is being built as part of my backend software development portfolio to demonstrate Python, Flask, SQL, SQLite, HTML, and Git development skills.

---

## Current Features

- Store job postings in a SQLite database
- Display saved job postings using Flask templates
- Extract technical skills from job descriptions
- Case-insensitive skill matching
- Separate Jobs and Skills database tables
- Git version control
- Hosted on GitHub

---

## Technologies Used

### Backend

- Python 3
- Flask
- SQLite3

### Frontend

- HTML5
- Jinja2 Templates

### Database

- SQLite

### Version Control

- Git
- GitHub

---

## Project Structure

```
job-posting-skill-analyzer/
│
├── app.py                 # Flask application
├── database.py            # Database functions
├── analysis.py            # Future analysis functions
├── skill_extractor.py     # Skill extraction logic
├── jobs.db                # SQLite database (ignored by Git)
│
├── templates/
│   └── index.html
│
├── static/
│
├── .gitignore
└── README.md
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
| description | Full job description |
| date_added | Date added |

---

### skills

| Column | Description |
|---------|-------------|
| id | Primary Key |
| job_id | Related job |
| skill | Extracted skill |

---

## Current Skill List

The application currently detects technologies including:

- Python
- SQL
- Flask
- Java
- JavaScript
- TypeScript
- C#
- C++
- Go
- Docker
- Git
- HTML
- CSS
- React
- Node.js
- AWS
- Azure
- Linux
- Excel
- Power BI

Skill detection is case-insensitive.

Example:

```
Looking for python, Flask, SQL and Docker.
```

Produces

```
Python
SQL
Flask
Docker
```

---

## How It Works

1. User submits a job posting.
2. The job is saved in the SQLite database.
3. The description is converted to lowercase.
4. Every skill in the predefined skills list is checked.
5. Matching skills are returned.
6. (Upcoming) Matching skills will be stored in the `skills` table.
7. (Upcoming) Analytics will be generated from stored skills.

---

## Running the Project

Clone the repository

```bash
git clone https://github.com/zajjhay19/job-posting-skill-analyzer.git
```

Move into the project

```bash
cd job-posting-skill-analyzer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install Flask

```bash
pip install flask
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## What I've Learned

Through this project I have practiced:

- Python programming
- Flask web development
- HTML templating with Jinja2
- SQLite databases
- SQL CRUD operations
- Database design
- Primary and foreign keys
- Python functions
- Lists and loops
- String processing
- Case-insensitive matching
- Git
- GitHub
- Version control

---

## Planned Features

- Store extracted skills automatically
- Search job postings
- Upload job descriptions
- Skill frequency analysis
- Dashboard with charts
- Bootstrap responsive interface
- REST API
- Export reports
- Authentication
- AI-powered job analysis
- Resume skill matching
- Recruiter dashboard

---

## Future Improvements

- Docker deployment
- PostgreSQL support
- Cloud deployment
- Machine Learning skill prediction
- NLP-based extraction
- Resume parser
- Salary analytics
- Company analytics

---

## Author

**Zajae Hayles**

GitHub

https://github.com/zajjhay19

---

## License

This project is intended for educational and portfolio purposes.
