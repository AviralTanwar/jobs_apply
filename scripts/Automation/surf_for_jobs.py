import time
import os
import threading
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Automation.linkedIn.surf_linkedin import fetch_linkedin_job_ids

# ---- ENVIRONMENT CONFIG ----
load_dotenv(r'C:\Users\avira\Documents\Restart_Skills_v2025\GitHub\jobs_apply\config\credentials.env')
chrome_path = os.getenv('chrome_path')  # Not required for Selenium unless custom
chrome_profile_name = os.getenv('chrome_profile_name')  # Not used here unless you want to persist session

# ---- HEADLESS BROWSER FUNCTION ----
def open_url_with_selenium(url):
    """
    Opens a URL in headless Chrome using Selenium and scrapes job data if it's a LinkedIn URL.
    """
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(5)  # Give time for page to load (you can improve this with WebDriverWait)

        if "linkedin" in url.lower():
            exit
            job_data = fetch_linkedin_job_ids(driver.page_source)
            print(f"[LinkedIn Job Data] {len(job_data)} jobs found:")
            for job_id in job_data:
                print(f" - Job ID: {job_id}")

        driver.quit()

    except Exception as e:
        print(f"Error in open_url_with_selenium for URL {url}: {e}")
        raise

# ---- PARALLEL SURF FUNCTION ----
def surf_for_jobs(urls):
    """
    Opens each URL in parallel using threading and Selenium (headless).
    """
    try:
        threads = []
        for url in urls:
            thread = threading.Thread(target=open_url_with_selenium, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    except Exception as e:
        print(f"An error occurred in surf_for_jobs: {e}")
        raise
