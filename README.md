## ⚙️ How It Works

### 🎯 Skill Analysis

A user submits their **name, target role, and current skills**. TalentLens compares those skills against the requirements of the selected role and provides:

* ✅ Matching skills
* ⚠️ Skill gaps
* 📊 Readiness score
* 📚 Suggested areas to learn

### 📄 Resume Intelligence

A user can upload their **resume as a PDF**. TalentLens extracts the resume text, detects relevant technical skills, and feeds them into the same **skill analysis and career recommendation pipeline**.

### 🔄 Processing Flow

📄 **Resume Upload**
↓
🔤 **Text Extraction**
↓
🔍 **Skill Detection**
↓
🧩 **Career Comparison**
↓
📊 **Gap Report**
↓
🚀 **Recommendations**

---

## 📁 Project Structure

```text
TALENTLENS/
├── main.py                  # App entry point & Flask routes
├── analyzer.py              # Skill analysis logic
├── resume_analyzer.py       # Resume text extraction & skill detection
├── recommender.py           # Career & skill-gap recommendations
├── interview.py             # Interview question & answer evaluation
├── database.py              # Database models & queries
├── uploads.py               # Resume upload handling
├── talentlens.db            # SQLite database
├── templates/               # HTML pages (Flask/Jinja2)
└── static/                  # CSS, JavaScript & other assets
```

---

## ▶️ Running It Locally

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/talentlens.git
cd talentlens
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the Application

```bash
python main.py
```

### 6. Open in Browser

Go to:

```text
http://127.0.0.1:5000
```

---

## 👨‍💻 Author

**M Hemanth Surya Prasad**

**Cyber Security Analyst · Full-Stack Engineer**

TalentLens was built as a project combining **software development, resume intelligence, career guidance, skill-gap analysis, and technical interview evaluation** into one unified platform.
