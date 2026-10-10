
def calculate_match(job, candidate_skills):
    required = {
        skill.strip().lower()
        for skill in job["skills"]
    }

    candidate = {
        skill.strip().lower()
        for skill in candidate_skills
    }

    if not required:
        return 0, [], []

    matched = required.intersection(candidate)
    missing = required.difference(candidate)

    score = round(len(matched) / len(required) * 100)

    return score, sorted(matched), sorted(missing)
