from bs4 import BeautifulSoup
import requests
import os
import json

def fetch_linkedin_job_ids(url):
    """
    Given a LinkedIn job URL, fetch the HTML content,
    parse job IDs using BeautifulSoup, and return a
    dictionary where keys are job_ids and values are empty dicts.
    """
    try:
        if "linkedin" not in url:
            raise ValueError("URL is not a LinkedIn job URL")

        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        print("--------------------------------------------------------------------------") 
        print("-----------------------------soup---------------------------------------------")
        print("--------------------------------------------------------------------------") 
        print(soup.prettify())  # Print the HTML content for debugging
        print("--------------------------------------------------------------------------") 

        print("")
        print("")
        print("")
        print("")
        print("")

        # Find the job container using LinkedIn's UI class
        job_elements = soup.find_all("li", attrs={"data-occludable-job-id": True})
        print("--------------------------------------------------------------------------") 
        print("-----------------------------job_elements---------------------------------------------")
        print("--------------------------------------------------------------------------") 
        print(job_elements)  # Print the HTML content for debugging
        print("--------------------------------------------------------------------------") 

        print("")
        print("")
        print("")
        print("")
        print("")

        job_dict = {}
        for job_elem in job_elements:
            job_id = job_elem.get("data-occludable-job-id")
            if job_id:
                job_dict[job_id] = {}  # Empty dictionary for now

        print("The Dictionary of LinkedIn jobs is:")
        print(json.dumps(job_dict, indent=4))

        return job_dict

    except Exception as e:
        print(f"An error occurred in the function fetch_linkedin_job_ids: {e}")
        print(os.path.abspath(__file__))
        raise
