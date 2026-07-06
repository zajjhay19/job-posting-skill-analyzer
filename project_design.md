# Job Posting Skill Gap Analyzer


## Problem


People applying to jobs don't know which skills are most requested.


---

## Users


Job Seekers

Students

Career Changers

Recruiters


---

## Use Cases


Paste Job Posting


Save Job Posting


View Saved Jobs


Analyze Skills


View Dashboard


Identify Missing Skills


---

## Tech Stack


Python


Flask


SQLite


Pandas


HTML


CSS


Chart.js


Git


GitHub


---

## Architecture


Flask

↓

SQLite

↓

Skill Extractor

↓

Analysis Engine


---

## Database Tables


jobs


skills


---

## Pages


Home


Add Job


Jobs


Dashboard


---

## Features


Store Job Postings


Extract Skills


Count Skills


Calculate Average Salaries


Find Skill Gaps


Display Charts


Export Reports
## </>Markdown 

## Table 1 -Jobs
Stores Infromation about job postings

Id 
Company
Job_Title
Salary
Description
Date_added

## Database Tables

### jobs

id

company

job_title

salary

description

date_added


### skills

id

job_id

skill


## Relationships

One Job

↓

Can Have

↓

Many Skills


jobs.id

connects to


skills.job_id


+----------------+
| jobs           |
+----------------+
| id (PK)        |
| company        |
| job_title      |
| salary         |
| description    |
| date_added     |
+----------------+
         │
         │ One-to-Many
         ▼
+----------------+
| skills         |
+----------------+
| id (PK)        |
| job_id (FK)    |
| skill          |
+----------------+



# Lesson 2 – Primary Keys

## What is a Primary Key?

A primary key is a column that uniquely identifies each row in a table.

## Why do we need it?

Without a primary key, we couldn't reliably update, delete, or relate a specific row to data in another table.

## AUTOINCREMENT

AUTOINCREMENT tells SQLite to automatically assign the next available ID whenever a new row is inserted.

Example:

1
2
3
4
5
...

## Interview Answer

"I used an INTEGER PRIMARY KEY AUTOINCREMENT so every job posting receives a unique identifier automatically. This makes it easy to reference jobs from other tables and prevents duplicate IDs."


## NOT NULL

What is it?

A database constraint that requires a column to have a value.

Why use it?

To prevent incomplete or invalid records from being stored.

Example

company TEXT NOT NULL

If someone tries to save a job without a company name, SQLite rejects the insert and returns an error.

Interview Answer

NOT NULL is used to enforce required fields and maintain data integrity by preventing missing values in important columns.