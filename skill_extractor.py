SKILLS = [ #Creates the master list of skills the application knows how to recognize.

    # Programming languages
    "Python",
    "SQL",
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


def extract_skills(description): #Creates a machine that takes text and returns any recognized skills.

    found_skills = [] #Creates an empty box to store all detected skills.

    description = description.lower() #Converts the text to lowercase for consistent matching.

    for skill in SKILLS: #Loops through every skill the application knows about.

        if skill.lower() in description: #Checks if the current skill appears anywhere in the text.

            found_skills.append(skill) #Adds the detected skill to the results list.

    return found_skills #Returns the completed list of detected skills.



# Testing

if __name__ == "__main__": #Checks if this file is being run directly instead of being imported.

    description = "Looking for python, Flask, SQL and Docker." #Creates sample text to test the extractor.

    skills = extract_skills(description) #Runs the extractor on the sample text.

   