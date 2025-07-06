from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def fetch_linkedin_job_ids(url):
    """
    Uses headless Chrome to open a LinkedIn jobs page and extract job IDs.
    Returns a dictionary: {job_id1: {}, job_id2: {}, ...}
    """

    # Set up headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--log-level=3")  # suppress logs

    print("Debugging 1")
    driver = webdriver.Chrome(options=chrome_options)
    print("Debugging 2")
    try:
        print("Debugging 3")
        driver.get(url)

        print("Debugging 4")
        # Wait for page to load
        time.sleep(5)  # Use explicit waits in production

        print("Debugging 5")
        # Locate job cards by the specific UI class if needed (optional)
        # This class is for UI section, not job ID — job ID is in <li>
        job_elements = driver.find_elements(By.XPATH, "//li[@data-occludable-job-id]")


        print("Debugging 6")
        job_dict = {}

        for elem in job_elements:
            print("Debugging 7")
            job_id = elem.get_attribute("data-occludable-job-id")
            if job_id:
                print(f"Found job ID: {job_id}")

                job_dict[job_id] = {}

        print("Debugging 8")
        return job_dict

    except Exception as e:
        print(f"Error: {e}")
        return {}

    finally:
        driver.quit()
