SKILLS = [ #Creates the master list of skills the application knows how to recognize.

    "Python",
    "SQL",
    "Flask",
    "Java",
    "JavaScript",
    "TypeScript",
    "C#",
    "C++",
    "Go",
    "Docker",
    "Git",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "AWS",
    "Azure",
    "Linux",
    "Excel",
    "Power BI"
]


def extract_skills(description): #Creates a machine that takes text and returns any recognized skills.

    found_skills = [] #Creates an empty box to store all detected skills.

    description = description.lower() #Converts the text to lowercase for consistent matching.

    for skill in SKILLS: #Loops through every skill the application knows about.

        print(skill) #Displays the current skill being checked for debugging and learning purposes.

        if skill.lower() in description: #Checks if the current skill appears anywhere in the text.

            found_skills.append(skill) #Adds the detected skill to the results list.

    return found_skills #Returns the completed list of detected skills.



# Testing

if __name__ == "__main__": #Checks if this file is being run directly instead of being imported.

    description = "Looking for python, Flask, SQL and Docker." #Creates sample text to test the extractor.

    skills = extract_skills(description) #Runs the extractor on the sample text.

    print(skills) #Displays the skills that were successfully detected.