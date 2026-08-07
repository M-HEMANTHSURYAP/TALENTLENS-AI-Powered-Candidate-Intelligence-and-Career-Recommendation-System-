LEARNING_RECOMMENDATIONS = {

    "Python": {
        "priority": "High",
        "reason": "Python is a core programming skill required for many software and AI roles.",
        "action": "Practice Python fundamentals, OOP, functions, modules and problem solving."
    },

    "Java": {
        "priority": "High",
        "reason": "Java is widely used in enterprise software development.",
        "action": "Learn Java OOP, collections, exception handling and basic application development."
    },

    "SQL": {
        "priority": "High",
        "reason": "SQL is essential for working with relational databases.",
        "action": "Practice SELECT, JOIN, GROUP BY, subqueries and database design."
    },

    "Data Structures": {
        "priority": "High",
        "reason": "Data structures are fundamental for technical interviews and efficient software.",
        "action": "Study arrays, strings, linked lists, stacks, queues, trees and hash tables."
    },

    "Algorithms": {
        "priority": "High",
        "reason": "Algorithms improve problem-solving and coding interview performance.",
        "action": "Practice searching, sorting, recursion, greedy algorithms and complexity analysis."
    },

    "OOP": {
        "priority": "Medium",
        "reason": "Object-oriented programming is important for designing maintainable applications.",
        "action": "Practice classes, objects, inheritance, polymorphism and encapsulation."
    },

    "Git": {
        "priority": "Medium",
        "reason": "Git is an important development and collaboration tool.",
        "action": "Practice commits, branches, merging, pull requests and GitHub workflows."
    },

    "REST APIs": {
        "priority": "High",
        "reason": "APIs allow applications and services to communicate with each other.",
        "action": "Learn HTTP methods, JSON, endpoints, status codes and Flask/FastAPI APIs."
    },

    "Flask": {
        "priority": "Medium",
        "reason": "Flask is useful for building lightweight Python web applications and APIs.",
        "action": "Build routes, templates, forms, APIs and database-connected applications."
    },

    "Machine Learning": {
        "priority": "High",
        "reason": "Machine learning is a core skill for AI-focused roles.",
        "action": "Learn supervised learning, preprocessing, model evaluation and scikit-learn."
    },

    "Deep Learning": {
        "priority": "High",
        "reason": "Deep learning is important for advanced AI applications.",
        "action": "Learn neural networks, training, loss functions and modern deep-learning architectures."
    },

    "Statistics": {
        "priority": "Medium",
        "reason": "Statistics provides the mathematical foundation for data analysis and machine learning.",
        "action": "Study probability, distributions, mean, variance, correlation and hypothesis testing."
    },

    "NumPy": {
        "priority": "Medium",
        "reason": "NumPy is widely used for numerical computing in Python.",
        "action": "Practice arrays, vectorization, indexing and numerical operations."
    },

    "Pandas": {
        "priority": "Medium",
        "reason": "Pandas is essential for practical data manipulation and analysis.",
        "action": "Practice DataFrames, filtering, grouping, merging and data cleaning."
    },

    "TensorFlow": {
        "priority": "Medium",
        "reason": "TensorFlow is a major framework for developing machine-learning and deep-learning models.",
        "action": "Build basic neural networks and experiment with model training."
    },

    "PyTorch": {
        "priority": "Medium",
        "reason": "PyTorch is widely used for modern deep-learning research and applications.",
        "action": "Learn tensors, datasets, neural networks and model training."
    }
}


def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        if skill in LEARNING_RECOMMENDATIONS:

            recommendation = LEARNING_RECOMMENDATIONS[skill].copy()

            recommendation["skill"] = skill

            recommendations.append(recommendation)

        else:

            recommendations.append({
                "skill": skill,
                "priority": "Medium",
                "reason": "This skill is relevant to your selected target role.",
                "action": f"Build practical knowledge and complete a small project using {skill}."
            })

    return recommendations