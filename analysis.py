def find_matched_skills(market_skills, resume_skills):#Creates a function that finds skills shared by the job market and the resume.

    matched_skills = market_skills & resume_skills #Finds the skills that appear in both sets.

    return matched_skills #Sends the matched skills back to the part of the application that requested them.


def find_missing_skills(market_skills,resume_skills):#Creates a function that finds market skills that are missing from the resume.

    missing_skills = market_skills - resume_skills#Finds skills that appear in the job market but not on the resume.

    return missing_skills #Sends the missing skills back to the part of the application that requested them.


def calculate_market_percentage(market_skills, matched_skills):#creates a function that caculate how much the resume matches the job market.

    if len(market_skills) > 0: #checks that market skills exist, so that python does not divide by zero

        match_percentage = round
        (
            ( len(matched_skills) / len(market_skills) * 100 )
        )# callculates the market percentage
    else:

        match_percentage = 0 #Uses 0 when there are no market skills to compare

    return match_percentage #Sends the calculated percentage back to the part of the application that requested it.