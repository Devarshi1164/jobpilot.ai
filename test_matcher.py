
from job_matcher import calculate_match

my_skills = [
    "Python",
    "SQL",
    "MongoDB",
]

job = {
    "title": "Junior AI Engineer",
    "skills": [
        "Python",
        "SQL",
        "Machine Learning",
        "Docker",
    ],
}

score, matched, missing = calculate_match(
    job,
    my_skills
)

print("Job:", job["title"])
print("Match score:", score, "%")
print("Matched skills:", matched)
print("Missing skills:", missing)
