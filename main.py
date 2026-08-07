from flask import Flask, render_template, request, session

from database import initialize_database, save_candidate
from analyzer import analyze_skills
from recommender import generate_recommendations
from resume_analyzer import extract_skills_from_resume
from interview import (
    get_interview_questions,
    evaluate_answer,
    get_interview_feedback
)

from pypdf import PdfReader
from werkzeug.utils import secure_filename

import os


# =========================================================
# CREATE FLASK APPLICATION
# =========================================================

app = Flask(__name__)

# Secret key for session storage
app.secret_key = "talentlens_secret_key_2026"


# =========================================================
# INITIALIZE SQLITE DATABASE
# =========================================================

initialize_database()


# =========================================================
# RESUME UPLOAD CONFIGURATION
# =========================================================

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# =========================================================
# MANUAL SKILL ANALYSIS
# =========================================================

@app.route(
    "/analysis",
    methods=["GET", "POST"]
)
def analysis():

    if request.method == "POST":

        # ---------------------------------------------
        # GET FORM DATA
        # ---------------------------------------------

        name = request.form.get(
            "name",
            ""
        )

        email = request.form.get(
            "email",
            ""
        )

        target_role = request.form.get(
            "target_role",
            ""
        )

        skills = request.form.get(
            "skills",
            ""
        )


        # ---------------------------------------------
        # VALIDATION
        # ---------------------------------------------

        if not name:
            return "Please enter your name."

        if not target_role:
            return "Please select a target role."

        if not skills:
            return "Please enter your skills."


        # ---------------------------------------------
        # SAVE CANDIDATE TO SQLITE
        # ---------------------------------------------

        save_candidate(
            name,
            email,
            target_role,
            skills
        )


        # ---------------------------------------------
        # ANALYZE SKILLS
        # ---------------------------------------------

        analysis_result = analyze_skills(
            skills,
            target_role
        )


        # ---------------------------------------------
        # GENERATE RECOMMENDATIONS
        # ---------------------------------------------

        recommendations = generate_recommendations(
            analysis_result["missing"]
        )


        # ---------------------------------------------
        # SHOW RESULT
        # ---------------------------------------------

        return render_template(
            "result.html",

            name=name,

            target_role=target_role,

            skills=skills,

            score=analysis_result["score"],

            matched=analysis_result["matched"],

            missing=analysis_result["missing"],

            recommendations=recommendations
        )


    # ---------------------------------------------
    # GET REQUEST
    # ---------------------------------------------

    return render_template(
        "analysis.html"
    )


# =========================================================
# RESUME INTELLIGENCE ENGINE
# =========================================================

@app.route(
    "/resume",
    methods=["GET", "POST"]
)
def resume():

    if request.method == "POST":

        # ---------------------------------------------
        # GET UPLOADED FILE
        # ---------------------------------------------

        resume_file = request.files.get(
            "resume"
        )


        # ---------------------------------------------
        # CHECK FILE
        # ---------------------------------------------

        if not resume_file:

            return "Please upload a resume."


        if resume_file.filename == "":

            return "Please select a PDF file."


        # ---------------------------------------------
        # CHECK FILE TYPE
        # ---------------------------------------------

        if not resume_file.filename.lower().endswith(".pdf"):

            return "Only PDF resumes are supported."


        # ---------------------------------------------
        # SECURE FILE NAME
        # ---------------------------------------------

        filename = secure_filename(
            resume_file.filename
        )


        if not filename:

            return "Invalid file name."


        # ---------------------------------------------
        # CREATE FILE PATH
        # ---------------------------------------------

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )


        # ---------------------------------------------
        # SAVE RESUME
        # ---------------------------------------------

        resume_file.save(
            file_path
        )


        # =============================================
        # EXTRACT TEXT FROM PDF
        # =============================================

        try:

            reader = PdfReader(
                file_path
            )

            resume_text = ""

            for page in reader.pages:

                text = page.extract_text()

                if text:

                    resume_text += (
                        text + "\n"
                    )


        except Exception as error:

            return (
                f"Could not process the PDF: {error}"
            )


        # =============================================
        # CHECK EXTRACTED TEXT
        # =============================================

        if not resume_text.strip():

            return (
                "The PDF could not be read. "
                "Please upload a text-based PDF resume."
            )


        # =============================================
        # AUTOMATIC SKILL DETECTION
        # =============================================

        detected_skills = extract_skills_from_resume(
            resume_text
        )


        # =============================================
        # STORE RESUME DATA IN SESSION
        # =============================================

        session["resume_text"] = resume_text

        session["detected_skills"] = detected_skills


        # =============================================
        # SHOW RESUME RESULT
        # =============================================

        return render_template(
            "resume_result.html",

            resume_text=resume_text,

            detected_skills=detected_skills
        )


    # ---------------------------------------------
    # GET REQUEST
    # ---------------------------------------------

    return render_template(
        "resume.html"
    )


# =========================================================
# RESUME → CAREER ANALYSIS
# =========================================================

@app.route(
    "/resume-analysis",
    methods=["GET", "POST"]
)
def resume_analysis():

    # ---------------------------------------------
    # GET DETECTED SKILLS FROM SESSION
    # ---------------------------------------------

    detected_skills = session.get(
        "detected_skills",
        []
    )


    # ---------------------------------------------
    # SAFETY CHECK
    # ---------------------------------------------

    if not detected_skills:

        return (
            "No resume skills found. "
            "Please upload your resume first."
        )


    # =============================================
    # POST REQUEST
    # =============================================

    if request.method == "POST":

        # -----------------------------------------
        # GET FORM DATA
        # -----------------------------------------

        name = request.form.get(
            "name",
            "Candidate"
        )

        target_role = request.form.get(
            "target_role",
            ""
        )


        # -----------------------------------------
        # VALIDATE ROLE
        # -----------------------------------------

        if not target_role:

            return (
                "Please select a target career role."
            )


        # -----------------------------------------
        # CONVERT SKILLS TO STRING
        # -----------------------------------------

        skills_string = ", ".join(
            detected_skills
        )


        # -----------------------------------------
        # ANALYZE RESUME SKILLS
        # -----------------------------------------

        analysis_result = analyze_skills(
            skills_string,
            target_role
        )


        # -----------------------------------------
        # GENERATE RECOMMENDATIONS
        # -----------------------------------------

        recommendations = generate_recommendations(
            analysis_result["missing"]
        )


        # -----------------------------------------
        # SAVE CANDIDATE
        # -----------------------------------------

        save_candidate(
            name,
            "",
            target_role,
            skills_string
        )


        # -----------------------------------------
        # SHOW CAREER RESULT
        # -----------------------------------------

        return render_template(
            "resume_career_result.html",

            name=name,

            target_role=target_role,

            skills=skills_string,

            score=analysis_result["score"],

            matched=analysis_result["matched"],

            missing=analysis_result["missing"],

            recommendations=recommendations
        )


    # =============================================
    # GET REQUEST
    # =============================================

    return render_template(
        "resume_analysis.html",

        detected_skills=detected_skills,

        name=""
    )


# =========================================================
# INTERVIEW INTELLIGENCE ENGINE
# =========================================================

@app.route(
    "/interview",
    methods=["GET", "POST"]
)
def interview():

    # =============================================
    # POST REQUEST
    # =============================================

    if request.method == "POST":

        # -----------------------------------------
        # GET CANDIDATE INFORMATION
        # -----------------------------------------

        name = request.form.get(
            "name",
            "Candidate"
        )

        target_role = request.form.get(
            "target_role",
            ""
        )

        answer = request.form.get(
            "answer",
            ""
        )


        # -----------------------------------------
        # VALIDATE TARGET ROLE
        # -----------------------------------------

        if not target_role:

            return (
                "Please select a target interview role."
            )


        # -----------------------------------------
        # VALIDATE ANSWER
        # -----------------------------------------

        if not answer.strip():

            return (
                "Please provide an answer "
                "before submitting the interview."
            )


        # =========================================
        # GET QUESTIONS FOR SELECTED ROLE
        # =========================================

        questions = get_interview_questions(
            target_role
        )


        if not questions:

            return (
                "No interview questions are available "
                "for this role."
            )


        # =========================================
        # USE FIRST QUESTION
        # =========================================

        question_data = questions[0]

        question = question_data["question"]

        keywords = question_data["keywords"]


        # =========================================
        # EVALUATE ANSWER
        # =========================================

        score = evaluate_answer(
            answer,
            keywords
        )


        # =========================================
        # GENERATE FEEDBACK
        # =========================================

        feedback = get_interview_feedback(
            score
        )


        # =========================================
        # STORE INTERVIEW INFORMATION
        # =========================================

        session["interview_role"] = target_role

        session["interview_question"] = question

        session["interview_score"] = score


        # =========================================
        # SHOW INTERVIEW RESULT
        # =========================================

        return render_template(
            "interview_result.html",

            name=name,

            target_role=target_role,

            question=question,

            answer=answer,

            score=score,

            feedback=feedback
        )


    # =============================================
    # GET REQUEST
    # =============================================

    # Default question shown when interview page opens
    default_role = "Software Developer"

    questions = get_interview_questions(
        default_role
    )

    question = ""

    if questions:

        question = questions[0]["question"]


    return render_template(
        "interview.html",

        question=question
    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )