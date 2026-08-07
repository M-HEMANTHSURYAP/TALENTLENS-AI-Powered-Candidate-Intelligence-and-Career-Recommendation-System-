SKILL_LIBRARY = [

    # Programming
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",

    # Web
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "Flask",
    "Spring Boot",
    "REST APIs",

    # Database
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "DBMS",

    # Computer Science
    "Data Structures",
    "Algorithms",
    "OOP",
    "Operating Systems",
    "Computer Networks",

    # Data / AI
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "NumPy",
    "Pandas",
    "TensorFlow",
    "PyTorch",
    "Statistics",

    # Cybersecurity
    "Cybersecurity",
    "Cryptography",
    "Networking",
    "Linux",
    "SIEM",
    "Firewalls",

    # Tools
    "Git",
    "GitHub",
    "Docker",
    "VS Code",
    "Kali Linux",

    # Cloud
    "Cloud Computing",
    "AWS",
    "Azure",
    "Google Cloud"
]


def extract_skills_from_resume(resume_text):

    detected_skills = []

    resume_text_lower = resume_text.lower()

    for skill in SKILL_LIBRARY:

        if skill.lower() in resume_text_lower:

            detected_skills.append(skill)

    return detected_skills