## comments
import sqlite3

def create_database():

    connection = sqlite3.connect("jobs.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs
    (
        id INTEGER  PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        job_title TEXT NOT NULL,
        salary TEXT,
        description TEXT,
        date_added TEXT
)
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skills
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL,
    skill TEXT NOT NULL
    )
    """)
    connection.commit()
    connection.close()




def add_job(company, job_title, salary, description, date_added):

    connection = sqlite3.connect("jobs.db")
    connection.row_factory = sqlite3.Row
    
    cursor = connection.cursor()

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
    )

    job_id = cursor.lastrowid

    connection.commit()
    connection.close()
    
    return job_id


def add_skill(job_id, skill):

    connection = sqlite3.connect("jobs.db")

    cursor = connection.cursor()

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
    )

    connection.commit()
    connection.close()

def get_jobs():

    connection = sqlite3.connect("jobs.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM jobs
    """)

    jobs = cursor.fetchall()

    connection.close()

    return jobs


def get_skill_counts():

    connection = sqlite3.connect("jobs.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""

    SELECT skill, COUNT(*) AS count
    FROM skills
    GROUP BY skill
    ORDER BY count DESC
    """)

    skill_counts = cursor.fetchall()

    connection.close()

    return skill_counts


if __name__ == "__main__":

    create_database()

    skill_counts = get_skill_counts()

    for skill in skill_counts:
        print(skill["skill"], skill["count"])