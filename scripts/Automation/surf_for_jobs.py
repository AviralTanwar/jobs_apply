import subprocess                           # Used to run system commands (like opening Chrome)
import time                                 # Used to add delays between opening URLs
from dotenv import load_dotenv              # Loads environment variables from a .env file
import os                                   # Used to interact with the operating system
import threading                            # Used to run multiple tasks in parallel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urlparse

# ---- BROWSER CONFIG ----

# Load environment variables from the given .env file path
# This file should contain:
# chrome_path=<path to Chrome.exe>
# chrome_profile_name=<name of your Chrome profile directory>
load_dotenv(r'C:\Users\avira\Documents\Restart_Skills_v2025\GitHub\jobs_apply\config\credentials.env')

# Get the Chrome executable path from environment variables
chrome_path = os.getenv('chrome_path')

# Get the Chrome profile directory name from environment variables
chrome_profile_name = os.getenv('chrome_profile_name')

# --- Global dict ---
job_data = {}

def scrape_linkedin(driver):
    """Scrape LinkedIn page"""
    try:
        description_element = driver.find_element(By.CSS_SELECTOR, 'div.jobs-box__html-content')
        about_job = description_element.text.strip()
    except NoSuchElementException:
        about_job = "Not Found"

    try:
        easy_apply_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label*="Easy Apply"]')
        easy_apply = "yes" if easy_apply_btn else "no"
    except NoSuchElementException:
        easy_apply = "no"

    try:
        company = driver.find_element(By.CSS_SELECTOR, 'a.topcard__org-name-link').text.strip()
    except NoSuchElementException:
        company = "UnknownCompany"

    try:
        job_title = driver.find_element(By.CSS_SELECTOR, 'h1.topcard__title').text.strip()
    except NoSuchElementException:
        job_title = "UnknownJob"

    return company, job_title, about_job, easy_apply

def scrape_naukri(driver):
    """Scrape Naukri page"""
    try:
        description_element = driver.find_element(By.CSS_SELECTOR, 'div.jd-container')  # adjust if needed
        about_job = description_element.text.strip()
    except NoSuchElementException:
        about_job = "Not Found"

    try:
        easy_apply_btn = driver.find_element(By.XPATH, '//button[contains(text(), "Apply")]')
        easy_apply = "yes" if easy_apply_btn else "no"
    except NoSuchElementException:
        easy_apply = "no"

    try:
        company = driver.find_element(By.CSS_SELECTOR, 'a.jd-header-comp-name').text.strip()
    except NoSuchElementException:
        company = "UnknownCompany"

    try:
        job_title = driver.find_element(By.CSS_SELECTOR, 'h1.jd-header-title').text.strip()
    except NoSuchElementException:
        job_title = "UnknownJob"

    return company, job_title, about_job, easy_apply


def scrape_job_data(url):
    try:
        # Setup Chrome options
        options = Options()
        options.add_argument(f"user-data-dir={os.path.dirname(chrome_path)}/User Data")
        options.add_argument(f"profile-directory={chrome_profile_name}")
        options.add_argument("--start-maximized")

        # Setup driver
        service = Service(executable_path=chrome_path)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        time.sleep(5)

        # Detect domain
        domain = urlparse(url).netloc

        if 'linkedin.com' in domain:
            company, job_title, about_job, easy_apply = scrape_linkedin(driver)
        elif 'naukri.com' in domain:
            company, job_title, about_job, easy_apply = scrape_naukri(driver)
        else:
            print(f"Unsupported site: {domain}")
            driver.quit()
            return

        key = f"{company}_{job_title}"
        job_data[key] = {
            'About the job': about_job,
            'Easy Apply': easy_apply
        }

        print(f"✅ Done: {key}")
        driver.quit()

    except Exception as e:
        print(f"Error scraping {url}: {e}")

def surf_for_jobs(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=scrape_job_data, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nAll jobs scraped ✅")
    print(job_data)


if __name__ == "__main__":
    # Example list: mix of LinkedIn + Naukri
    urls = [
        "https://www.linkedin.com/jobs/view/123456789/",
        "https://www.naukri.com/job-listings-example"
    ]
    surf_for_jobs(urls)
