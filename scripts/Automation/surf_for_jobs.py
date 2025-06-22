import subprocess                           # Used to run system commands (like opening Chrome)
import time                                 # Used to add delays between opening URLs
from dotenv import load_dotenv              # Loads environment variables from a .env file
import os                                   # Used to interact with the operating system
import threading                            # Used to run multiple tasks in parallel

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


def open_url_in_chrome(url):
    """
    Helper function:
    Opens a single URL in Chrome with the specified profile.
    """
    subprocess.Popen([
        chrome_path,
        "--new-window",
        f'--profile-directory={chrome_profile_name}',
        url
    ])


def surf_for_jobs(urls):
    """
    Opens each URL from the list in a new Chrome window,
    using the specified Chrome profile.
    Each URL opens in parallel (simultaneously) using threads.
    """
    try:
        threads = []  # List to keep track of threads

        for url in urls:
            # Create a new thread for each URL
            thread = threading.Thread(target=open_url_in_chrome, args=(url,))
            threads.append(thread)
            thread.start()  # Start the thread (runs open_url_in_chrome)

        # Optional: wait for all threads to finish (not strictly needed here)
        for thread in threads:
            thread.join()

    except Exception as e:
        print(f"An error occurred in the function :- surf_for_jobs: {e}")  
        print(os.path.abspath(__file__))
        raise
