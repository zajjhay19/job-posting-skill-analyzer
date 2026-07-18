## comments

import sqlite3 #Imports the tool that allows Python to communicate with SQLite databases.


def create_database(): #Creates the database structure if it does not already exist.

    connection = sqlite3.connect("jobs.db") #Opens a connection to the project's database file.

    cursor = connection.cursor() #Creates the worker responsible for sending SQL commands to the database.

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS jobs
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        job_title TEXT NOT NULL,
        salary TEXT,
        description TEXT,
        date_added TEXT
    )
    """
    ) #Creates the jobs table used to store job posting information.

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS skills
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER NOT NULL,
        skill TEXT NOT NULL
    )
    """
    ) #Creates the skills table used to store extracted skills separately from jobs.

    connection.commit() #Permanently saves all database changes.

    connection.close() #Closes the connection to free resources and prevent database locks.



def add_job(company, job_title, salary, description, date_added): #Creates a machine that saves a job posting into the database.

    connection = sqlite3.connect("jobs.db") #Opens a connection to the database.

    connection.row_factory = sqlite3.Row #Allows rows to behave like dictionaries instead of numbered lists.

    cursor = connection.cursor() #Creates the SQL worker for this database session.

    cursor.execute(
        """
        INSERT INTO jobs
        (
            company,
            job_title,
            salary,
            description,
            date_added
        )
        VALUES (?,?,?,?,?)
        """,
        (
            company,
            job_title,
            salary,
            description,
            date_added
        )
    ) #Inserts the new job information into the jobs table.

    job_id = cursor.lastrowid #Stores the database ID that was assigned to the newly created job.

    connection.commit() #Permanently saves the new job.

    connection.close() #Closes the database connection.

    return job_id



def add_skill(job_id, skill): #Creates a machine that connects a skill to a specific job posting.

    connection = sqlite3.connect("jobs.db") #Opens a connection to the database.

    cursor = connection.cursor() #Creates the SQL worker for this database session.

    cursor.execute(
        """
        INSERT INTO skills
        (
            job_id,
            skill
        )
        VALUES (?, ?)
        """,
        (
            job_id,
            skill
        )
    ) #Stores the relationship between the job and the detected skill.

    connection.commit() #Permanently saves the skill record.

    connection.close() #Closes the database connection.



def get_jobs(): #Creates a machine that retrieves all saved jobs.

    connection = sqlite3.connect("jobs.db") #Opens a connection to the database.

    connection.row_factory = sqlite3.Row #Allows rows to be accessed using column names.

    cursor = connection.cursor() #Creates the SQL worker for this database session.

    cursor.execute(
    """
    SELECT * FROM jobs
    """
    ) #Requests every job stored in the jobs table.

    jobs = cursor.fetchall() #Collects all returned rows into a Python list.

    connection.close() #Closes the database connection.

    return jobs



def get_skill_counts(): #Creates a machine that calculates skill popularity across all jobs.

    connection = sqlite3.connect("jobs.db") #Opens a connection to the database.

    connection.row_factory = sqlite3.Row #Allows rows to be accessed using column names.

    cursor = connection.cursor() #Creates the SQL worker for this database session.

    cursor.execute(
    """
    SELECT skill, COUNT(*) AS count
    FROM skills
    GROUP BY skill
    ORDER BY count DESC
    """
    ) #Groups matching skills together and counts how often each one appears.

    skill_counts = cursor.fetchall() #Collects the completed skill statistics report.

    connection.close() #Closes the database connection.

    return skill_counts



if __name__ == "__main__": #Checks if this file is being run directly for testing purposes.

    create_database() #Ensures the database structure exists before testing.

    skill_counts = get_skill_counts() #Retrieves the current skill statistics.

    for skill in skill_counts: #Loops through every skill summary returned by the database.

        print(skill["skill"], skill["count"]) #Displays the skill name and its frequency.