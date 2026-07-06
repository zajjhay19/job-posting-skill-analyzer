SKILLS = [ 
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


def extract_skills(description):

    found_skills = []

    description = description.lower() ## changes whatever we write to lowercase

    for skill in SKILLS:
        print(skill)

        if skill.lower() in description:
                       
            found_skills.append(skill)
                                      
    return found_skills
    

    #testing

if __name__ == "__main__":
            
    description = "Looking for python, Flask, SQL and Docker."

    skills = extract_skills(description)

    print(skills)