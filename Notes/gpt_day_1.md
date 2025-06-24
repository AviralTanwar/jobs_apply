
# 🚀 AI Job Application & Tracking System

A **personal AI-powered automation system** to apply for jobs, request referrals, track emails, and analyze your job hunt — seamlessly integrated with **LinkedIn**, **Notion**, **email**, and an interactive **dashboard**.

---

## ✅ 1️⃣ Core Technologies

| **Part** | **Suggested Tools** |
|----------|---------------------|
| **Automation Scripts** | Python (`requests`, `Selenium`, `BeautifulSoup`, `Playwright`) |
| **LinkedIn & Notion API** | Official REST APIs, OAuth tokens |
| **Email Access** | `imaplib` for reading, `smtplib` for sending |
| **Storage** | Notion API + local SQLite or pandas Excel |
| **Dashboard** | Streamlit / Dash / Power BI |
| **ML/NLP** | `scikit-learn` for predictions, `transformers` for sentiment |
| **Scheduler** | Python `schedule` library or OS cron job |

---

## ✅ 2️⃣ Suggested Folder Structure

```plaintext
job_automation/
│
├── config/
│   ├── secrets.json         # API keys, tokens
│   ├── mail_creds.json      # Email app password
│
├── scripts/
│   ├── linkedin_apply.py       # Phase 1
│   ├── referral_request.py     # Phase 2
│   ├── manual_tracker.py       # Phase 3
│   ├── mail_checker.py         # Phase 4
│   ├── analysis_dashboard.py   # Phase 5
│
├── data/
│   ├── notion_backup.json
│   ├── applications.xlsx
│
├── models/
│   ├── jd_matcher.pkl          # Fit prediction model
│   ├── sentiment.pkl           # Sentiment model
│
├── main.py     # Orchestrator
└── README.md   # Project overview
```

---

## ✅ 3️⃣ Phase-by-Phase Breakdown

### ▶️ Phase 1 — Auto Apply

**Goal:** Automatically apply to all **Easy Apply** jobs on LinkedIn.

**Steps:**
- Use **Selenium** or **Playwright** to log in to LinkedIn.
- Search for jobs with “Easy Apply”.
- Auto-fill forms and click **Apply**.
- Store job info in:
  - **Notion Database** (via Notion REST API)
  - **Excel** (via `pandas.to_excel()`)

**Docs:**
- ✅ [LinkedIn scraping guidelines — respect TOS](https://www.linkedin.com/legal/user-agreement)
- ✅ [Notion Python SDK](https://developers.notion.com/)

---

### ▶️ Phase 2 — Referral Request

**Goal:** Contact employees for referrals.

**Steps:**
- For about 1/3 of companies, find employee profiles using the LinkedIn API or scraping.
- Draft a personalized message:  
  > "Hi [Name], I came across [Role] at [Company]. I’d love to connect and ask for any tips. I believe my background aligns well."
- Send connection requests + message via LinkedIn API.

---

### ▶️ Phase 3 — Manual Tracker

**Goal:** Keep track of jobs needing manual apply (e.g., Naukri, or complex ATS).

**Steps:**
- Record them manually in Notion + Excel.
- Mark them as `MANUAL` → so automation ignores them in auto apply.

---

### ▶️ Phase 4 — Mail Analysis

**Goal:** Auto-check your email for job-related updates.

**Steps:**
- Use `imaplib` to read inbox messages.
- Use NLP (`transformers` or `TextBlob`) for sentiment analysis.
  - If rejection: update Notion + Excel.
  - If interview: highlight + send notification.
- Print **BOLD ALERT** for high-priority messages.

---

### ▶️ Phase 5 — Dashboard & KPI

**Goal:** Visualize job hunt progress and insights.

**Steps:**
- Read data from Excel + Notion.
- Use **Streamlit** or **Dash** to plot:
  - 📊 Applications vs. Responses
  - ✅ Matches vs. Rejections
  - 📈 JD match score (NLP similarity of JD vs. your resume)
  - 🔑 Most common rejection reasons
  - 🎯 Suggested improvements for your resume.

---

## ✅ 4️⃣ Extra: Fit Prediction

**Goal:** Predict how well a job fits you.

**Steps:**
- Build a text similarity model:
  - Your resume (bag of words / embeddings)
  - Job description (same)
  - Calculate **cosine similarity**.
- Train on past data using `scikit-learn` or `transformers`.

---

## ✅ 5️⃣ Deployment

**Develop locally** first.

Use **`schedule`** or **cron** to run tasks automatically, e.g.:

```python
import schedule
import time

def apply_jobs():
    # run your script here

schedule.every().day.at("21:00").do(apply_jobs)

while True:
    schedule.run_pending()
    time.sleep(1)
```

- Store and version your code on **GitHub** (public or private).
- Share progress, insights, and dashboard screenshots on LinkedIn!

---

## ✅ 6️⃣ Tips

✔ Use `.env` or encrypted files for secrets and credentials.  
✔ Test APIs in **Postman** before adding them to code.  
✔ Respect **LinkedIn’s scraping limits** to avoid bans.  
✔ Start small — automate for 1 company, then scale up.

---

## 📌 Ready to start?

✅ Generate a starter Python repo  
✅ Provide a sample Notion database schema  
✅ Draft the Phase 1 LinkedIn script  

✨ **Just say:** “Yes, give me the starter code!”

---

## 📂 LOG

Store all your progress, ideas, and commands here as you build each phase.

**🚀 Let’s automate your job hunt like a pro!**
