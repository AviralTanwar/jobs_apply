from Automation.surf_for_jobs import surf_for_jobs

# ---- JOB URLS ----
urls = [
    "https://www.linkedin.com/jobs/collections/recommended/",
    "https://www.naukri.com/mnjuser/recommendedjobs"
]

if __name__ == "__main__":
    surf_for_jobs(urls)
