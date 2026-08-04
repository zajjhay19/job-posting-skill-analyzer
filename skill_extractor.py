import re #Imports tools for matching complete words and technical skill names.


SKILLS = [ #Creates the master list of skills the application knows how to recognize.

    # Programming languages
    "Python",
    "SQL",
    "R",
    "Java",
    "JavaScript",
    "TypeScript",
    "C#",
    "C++",
    "Go",
    "PHP",
    "Ruby",
    "Kotlin",
    "Swift",
    "Scala",

    # Backend frameworks and tools
    "Flask",
    "Django",
    "FastAPI",
    "Spring Boot",
    "Node.js",
    "Express.js",
    ".NET",
    "Laravel",
    "Ruby on Rails",

    # Frontend technologies
    "HTML",
    "CSS",
    "React",
    "Angular",
    "Vue.js",
    "Bootstrap",
    "Tailwind CSS",

    # Databases
    "SQLite",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Microsoft SQL Server",
    "Oracle",
    "Redis",

    # Cloud platforms
    "AWS",
    "Azure",
    "Google Cloud",
    "Firebase",

    # DevOps and deployment
    "Docker",
    "Kubernetes",
    "Git",
    "GitHub",
    "GitLab",
    "Jenkins",
    "Terraform",
    "Linux",
    "Nginx",

    # Data and analytics
    "Excel",
    "Power BI",
    "Tableau",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Apache Spark",

    # Artificial intelligence and machine learning
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "Machine Learning",
    "Natural Language Processing",

    # Testing and development tools
    "Selenium",
    "Pytest",
    "JUnit",
    "Postman",
    "Jira",

    # APIs and software architecture
    "REST API",
    "GraphQL",
    "Microservices",
    "JSON",
    "XML"
]


def extract_skills(description): #Creates a function that finds recognized skills inside text.

    found_skills = [] #Creates an empty list to store detected skills.

    for skill in SKILLS: #Loops through every recognized skill.

        escaped_skill = re.escape(
            skill
        ) #Protects special characters such as +, #, and periods.

        pattern = rf"(?<!\w){escaped_skill}(?!\w)" #Requires the complete skill name instead of part of another word.

        if re.search(
            pattern,
            description,
            re.IGNORECASE
        ): #Checks for the skill without caring about uppercase or lowercase letters.

            found_skills.append(
                skill
            ) #Adds the complete recognized skill to the results.

    return found_skills #Returns all detected skills.


# Testing

if __name__ == "__main__": #Checks if this file is being run directly for testing.

    description = """
    Looking for Python, Flask, SQL, Docker, PowerPoint,
    JavaScript, GitHub, Google Cloud and R.
    """

    skills = extract_skills(
        description
    ) #Runs the extractor on the sample text.

    print(
        skills
    ) #Displays the detected skills.