🧠 TalentLens
AI-powered candidate intelligence and career recommendation system.
TalentLens helps users understand where they stand technically — what skills they already have, what's missing for a target role, how their resume reads, and whether they're ready for a technical interview. It brings skill analysis, resume parsing, career recommendations, and interview practice into a single platform.
🚧 Status: actively in development. Core features are working; more are planned below.
---
🎯 What it does
🧩 Analyzes a user's technical skills against a chosen career role
📊 Calculates a career readiness score
📄 Extracts skills automatically from an uploaded PDF resume
🔍 Compares resume-detected skills against target roles
🚀 Recommends the skills a candidate should learn next
💬 Runs practice technical interviews and scores the answers
📈 Returns an interview readiness score with feedback
The idea is to answer four questions in order: where am I now, what am I missing, which role fits me, and am I ready for the interview.
---
⚙️ How it works
🎯 Skill Analysis
A user submits their name, target role, and current skills. TalentLens compares those skills against what the role requires and returns matches, gaps, a readiness score, and suggested areas to learn.
📄 Resume Intelligence
A user uploads a resume as a PDF. The text is extracted and scanned for technical skills, which then feed into the same analysis and recommendation pipeline used above.
```
📄 resume upload → 🔤 text extraction → 🔍 skill detection → 🧩 career comparison → 📊 gap report → 🚀 recommendations
```
💬 Interview Practice
Based on a chosen role, the user is given technical interview questions, submits answers, and receives an evaluation along with an overall readiness score.
---
📁 Project structure
```
TALENTLENS/
├── main.py                 # app entry point / routes
├── analyzer.py              # skill analysis logic
├── resume_analyzer.py       # resume text extraction & skill detection
├── recommender.py           # career / skill-gap recommendations
├── interview.py              # interview question & answer evaluation
├── database.py                # database models & queries
├── uploads.py                 # resume upload handling
├── talentlens.db               # SQLite database
├── templates/                  # HTML pages (Flask/Jinja)
└── static/                     # CSS, JS, assets
```
---
🛠️ Tech stack
🐍 Python / Flask
🗄️ SQLite
🎨 HTML, CSS, Jinja templates
📄 PDF text extraction for resume parsing
---
▶️ Running it locally
```bash
git clone https://github.com/<your-username>/talentlens.git
cd talentlens
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
python main.py
```
Then open `http://127.0.0.1:5000` in your browser.
---
🔮 Roadmap
🤖 More advanced resume parsing and skill extraction
💼 A larger library of career roles and interview questions
📈 More detailed answer evaluation and candidate analytics
🧠 ML-based career prediction and candidate scoring
🎙️ Voice-based interview simulation
🔗 Job description ↔ resume matching
📚 Personalized learning path recommendations
👤 User accounts, profiles, and dashboards
☁️ Production database and cloud deployment
---
👨‍💻 Author
M Hemanth Surya Prasad
Cyber Security Analyst · Full-Stack Engineer
TalentLens was built as a project combining software development, resume intelligence, career guidance, and technical interview evaluation into one platform.
