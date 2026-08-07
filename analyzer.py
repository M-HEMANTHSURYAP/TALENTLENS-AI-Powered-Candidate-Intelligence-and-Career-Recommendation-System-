ROLE_REQUIREMENTS = {

    "Software Developer": [
        "Python",
        "Java",
        "SQL",
        "Data Structures",
        "Algorithms",
        "OOP",
        "Git",
        "REST APIs"
    ],

    "Python Developer": [
        "Python",
        "OOP",
        "SQL",
        "Git",
        "Flask",
        "REST APIs",
        "Data Structures"
    ],

    "Java Developer": [
        "Java",
        "OOP",
        "SQL",
        "Data Structures",
        "Algorithms",
        "Git",
        "Spring Boot",
        "REST APIs"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Statistics",
        "Data Visualization",
        "Pandas",
        "Power BI"
    ],

    "AI/ML Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "Statistics",
        "NumPy",
        "Pandas",
        "TensorFlow",
        "PyTorch"
    ],

    "Full Stack Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "SQL",
        "REST APIs",
        "Git"
    ],

    "Cybersecurity Analyst": [
        "Networking",
        "Linux",
        "Python",
        "Cybersecurity",
        "Cryptography",
        "SIEM",
        "Firewalls",
        "Incident Response"
    ]
}


def analyze_skills(user_skills, target_role):

    required_skills = ROLE_REQUIREMENTS.get(target_role, [])

    user_skill_list = [
        skill.strip().lower()
        for skill in user_skills.split(",")
        if skill.strip()
    ]

    matched = []
    missing = []

    for skill in required_skills:

        if skill.lower() in user_skill_list:
            matched.append(skill)
        else:
            missing.append(skill)

    total = len(required_skills)

    if total > 0:
        score = round((len(matched) / total) * 100)
    else:
        score = 0

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }