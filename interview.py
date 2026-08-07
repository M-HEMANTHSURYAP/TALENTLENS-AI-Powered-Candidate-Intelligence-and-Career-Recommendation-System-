# ==========================================
# TALENTLENS INTERVIEW INTELLIGENCE ENGINE
# ==========================================

QUESTION_BANK = {

    "Python Developer": [
        {
            "question": "What is the difference between a list and a tuple in Python?",
            "keywords": ["list", "tuple", "mutable", "immutable"]
        },
        {
            "question": "What is object-oriented programming in Python?",
            "keywords": ["class", "object", "inheritance", "encapsulation"]
        },
        {
            "question": "What is Flask and why is it used?",
            "keywords": ["web", "framework", "python", "api"]
        },
        {
            "question": "What is the purpose of SQL in a Python application?",
            "keywords": ["database", "query", "data", "sql"]
        },
        {
            "question": "What is a REST API?",
            "keywords": ["api", "http", "get", "post", "request", "response"]
        }
    ],

    "Software Developer": [
        {
            "question": "What is object-oriented programming?",
            "keywords": ["class", "object", "inheritance", "encapsulation", "polymorphism"]
        },
        {
            "question": "What is the difference between an array and a linked list?",
            "keywords": ["array", "linked", "memory", "node"]
        },
        {
            "question": "What is the purpose of Git?",
            "keywords": ["version", "control", "repository", "commit", "branch"]
        },
        {
            "question": "What is a REST API?",
            "keywords": ["api", "http", "request", "response", "get", "post"]
        },
        {
            "question": "What is the difference between SQL and NoSQL databases?",
            "keywords": ["sql", "nosql", "relational", "document", "database"]
        }
    ],

    "Java Developer": [
        {
            "question": "What is the difference between JDK, JRE and JVM?",
            "keywords": ["jdk", "jre", "jvm", "java", "runtime"]
        },
        {
            "question": "Explain inheritance in Java.",
            "keywords": ["inheritance", "class", "parent", "child", "extends"]
        },
        {
            "question": "What is Spring Boot?",
            "keywords": ["spring", "boot", "framework", "java", "application"]
        },
        {
            "question": "What is an interface in Java?",
            "keywords": ["interface", "abstract", "class", "method"]
        },
        {
            "question": "What is a REST API?",
            "keywords": ["api", "http", "get", "post", "request", "response"]
        }
    ],

    "Data Analyst": [
        {
            "question": "What is the difference between mean, median and mode?",
            "keywords": ["mean", "median", "mode", "average", "statistics"]
        },
        {
            "question": "Why is SQL important for a Data Analyst?",
            "keywords": ["sql", "database", "query", "data"]
        },
        {
            "question": "What is data visualization?",
            "keywords": ["visual", "chart", "graph", "dashboard", "data"]
        },
        {
            "question": "What is Pandas used for?",
            "keywords": ["pandas", "python", "dataframe", "data", "analysis"]
        },
        {
            "question": "What is the purpose of Power BI?",
            "keywords": ["power bi", "dashboard", "visualization", "report"]
        }
    ],

    "AI/ML Engineer": [
        {
            "question": "What is machine learning?",
            "keywords": ["machine", "learning", "model", "data", "prediction"]
        },
        {
            "question": "What is the difference between supervised and unsupervised learning?",
            "keywords": ["supervised", "unsupervised", "labeled", "unlabeled"]
        },
        {
            "question": "What is overfitting?",
            "keywords": ["overfitting", "training", "generalization", "model"]
        },
        {
            "question": "Why is Python widely used in machine learning?",
            "keywords": ["python", "library", "numpy", "pandas", "tensorflow"]
        },
        {
            "question": "What is the purpose of a neural network?",
            "keywords": ["neural", "network", "deep", "learning", "model"]
        }
    ],

    "Full Stack Developer": [
        {
            "question": "What is the difference between frontend and backend development?",
            "keywords": ["frontend", "backend", "client", "server"]
        },
        {
            "question": "What is JavaScript used for in web development?",
            "keywords": ["javascript", "web", "frontend", "interaction"]
        },
        {
            "question": "What is React?",
            "keywords": ["react", "javascript", "component", "frontend"]
        },
        {
            "question": "What is Node.js?",
            "keywords": ["node", "javascript", "server", "backend"]
        },
        {
            "question": "What is a REST API?",
            "keywords": ["api", "http", "request", "response", "backend"]
        }
    ],

    "Cybersecurity Analyst": [
        {
            "question": "What is the CIA triad in cybersecurity?",
            "keywords": ["confidentiality", "integrity", "availability"]
        },
        {
            "question": "What is a firewall?",
            "keywords": ["firewall", "network", "traffic", "security"]
        },
        {
            "question": "What is phishing?",
            "keywords": ["phishing", "email", "attack", "credential", "social"]
        },
        {
            "question": "What is SIEM?",
            "keywords": ["siem", "security", "logs", "events", "monitoring"]
        },
        {
            "question": "What is incident response?",
            "keywords": ["incident", "response", "attack", "security", "recovery"]
        }
    ]
}


def get_interview_questions(target_role):

    """
    Return interview questions for the selected role.
    """

    return QUESTION_BANK.get(
        target_role,
        QUESTION_BANK["Software Developer"]
    )


def evaluate_answer(answer, keywords):

    """
    Evaluate an interview answer using
    keyword-based intelligence.
    """

    if not answer:
        return 0

    answer_lower = answer.lower()

    matched_keywords = 0

    for keyword in keywords:

        if keyword.lower() in answer_lower:
            matched_keywords += 1

    total_keywords = len(keywords)

    if total_keywords == 0:
        return 0

    score = round(
        (matched_keywords / total_keywords) * 100
    )

    return min(score, 100)


def get_interview_feedback(score):

    """
    Convert interview score into
    meaningful candidate feedback.
    """

    if score >= 80:

        return (
            "Excellent technical understanding. "
            "Your answers demonstrate strong role readiness."
        )

    elif score >= 60:

        return (
            "Good technical foundation. "
            "Strengthening a few concepts can improve your interview performance."
        )

    elif score >= 40:

        return (
            "Moderate technical readiness. "
            "Focus on the core concepts identified during the interview."
        )

    else:

        return (
            "Your technical foundation needs improvement. "
            "Use the recommended learning areas before attempting another interview."
        )