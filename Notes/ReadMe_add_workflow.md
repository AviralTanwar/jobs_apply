
# ✅ 📌 **Job Application Automation Workflow**

This workflow describes the **end-to-end steps** for the AI Job Application & Tracking System.

---

## 🚀 **Workflow Steps**

1️⃣ **Start**  
   - Launch the automation scripts. (For me, my linedin page is on a different chrome page)

2️⃣ **Open LinkedIn & Naukri**  
   - Use Playwright/Selenium to open job portals.

3️⃣ **Search for Jobs**  
   - Filter jobs matching your **dream goal** and aligning with your **resume**.

4️⃣ **Categorize Jobs:**  
   - **80%**: Directly auto-apply.
   - **20%**: Jobs needing manual apply (e.g., redirect to company website) — **store for manual tracking** (prefer LinkedIn for this).

5️⃣ **Apply & Store:**  
   - Auto-apply to easy apply jobs.
   - Store all job info in:
     - ✅ **Notion Database**
     - ✅ **Excel file**

6️⃣ **Check Gmail for Updates:**  
   - Use IMAP/Gmail API to check emails for replies.
   - Update **Excel** and **Notion** statuses accordingly.

7️⃣ **Analyze & Dashboard:**  
   - Generate KPIs and performance insights:
     - Where you are lagging
     - Calculate **OE (Overall Efficiency)** score
     - Store analysis in a separate **Excel Dashboard**.

8️⃣ **Excel To-Do:**  
   - Show:
     - Jobs you still need to apply for.
     - The **20% stored jobs** for which you must **connect with someone on LinkedIn for a referral**.

9️⃣ **Repeat daily/weekly:**  
   - Schedule automation via `schedule` or cron.

---

## ✅ **How to use**

- Automate start via `main.py`
- Keep secrets in `.env` or `config/`
- Version control with Git
- Store logs in `logs.md`

---

**📌 Add this workflow in your main README later as `workflow.md`.**  
