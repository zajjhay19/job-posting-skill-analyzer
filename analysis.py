def find_matched_skills(
    market_skills,
    resume_skills
): #Creates a function that finds skills shared by the job market and the resume.

    matched_skills = market_skills & resume_skills #Finds the skills that appear in both sets.

    return matched_skills #Sends the matched skills back to the part of the application that requested them.


def find_missing_skills(
    market_skills,
    resume_skills
): #Creates a function that finds market skills that are missing from the resume.

    missing_skills = market_skills - resume_skills #Finds skills that appear in the job market but not on the resume.

    return missing_skills #Sends the missing skills back to the part of the application that requested them.


def calculate_match_percentage(
    market_skills,
    matched_skills
): #Creates a function that calculates how much the resume matches the job market.

    if len(market_skills) > 0: #Checks that market skills exist so Python does not divide by zero.

        match_percentage = round(
            (
                len(matched_skills)
                /
                len(market_skills)
            )
            * 100
        ) #Calculates the percentage of job-market skills found on the resume.

    else:

        match_percentage = 0 #Uses 0 when there are no market skills to compare.

    return match_percentage #Sends the calculated percentage back to the application.


def prioritize_missing_skills(
    skill_counts,
    missing_skills
): #Creates a function that combines missing skills with their market demand counts.

    prioritized_missing_skills = [] #Creates an empty list to store the missing skills and their counts.

    for skill in skill_counts: #Loops through every market skill and its count.

        if skill["skill"] in missing_skills: #Checks if the current market skill is missing from the resume.

            prioritized_missing_skills.append(
                {
                    "skill": skill["skill"],
                    "count": skill["count"]
                }
            ) #Adds the missing skill and its job-posting count to the list.

    return prioritized_missing_skills #Sends the prioritized missing skills back to the application.