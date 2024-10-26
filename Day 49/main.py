from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time
load_dotenv("MY_CREDENTIALS.env")
MY_EMAIL = os.getenv("E-MAIL")
MY_PASSWORD = os.getenv("PASSWORD")
MY_PHONE_NUMBER = os.getenv("MOBILE_NO")
My_JOB="Python Developer"

Edge_options =webdriver.EdgeOptions()
Edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=Edge_options)
driver.get("https://www.linkedin.com/?original_referer=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3Ff_AL%3Dtrue%26geoId%3D101174742%26keywords%3DAnalytic%2520Recruiting%2520Inc%26location%3DCanada")
time.sleep(8)
driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/div[2]/a').click()
wait = WebDriverWait(driver, 15)


# Wait for email input to be visible and interactable
email_input = driver.find_element(By.ID, "username")
email_input.send_keys(MY_EMAIL)
time.sleep(5)

# Step 4: Insert the password
password_input = driver.find_element(by=By.ID, value="password")
password_input.send_keys(MY_PASSWORD)
time.sleep(2)

signin_button = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[4]/button')
time.sleep(2)
signin_button.click()
time.sleep(8 )
job_button = driver.find_element(by=By.ID, value='searchFilter_timePostedRange')
time.sleep(2)
job_button.click()

"""
# Step 3: Click the "Next" button
next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next_button.click()

# Wait for the password field to load
time.sleep(2)  # You may adjust this based on your connection speed

# Step 4: Insert the password
password_input = driver.find_element(By.NAME, "Passwd")
password_input.send_keys(MY_PASSWORD)

# Step 5: Click the "Next" button
password_next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
password_next_button.click()

# Wait for some time to observe the result (e.g., successful login)
time.sleep(5)

# Sign-in
driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]').click()
time.sleep(2)
email = driver.find_element(by=By.NAME, value="session_key")
email.send_keys(MY_EMAIL)
password = driver.find_element(by=By.NAME, value="session_password")
password.send_keys(MY_PASSWORD)
driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(10)

# Scan available jobs
jobs = driver.find_elements(by=By.CLASS_NAME, value='job-card-list__title')
jobs_available = [job.text for job in jobs]
print(jobs_available)

# Select job posting and click on apply
while jobs_available:
    posting_num = 0
    try:
        driver.find_element(by=By.LINK_TEXT, value=f'{jobs_available[posting_num]}').click()
        time.sleep(2)
        driver.find_element(by=By.CLASS_NAME, value="jobs-s-apply").click()
    except NoSuchElementException:
        posting_num += 1
        driver.find_element(by=By.LINK_TEXT, value=f'{jobs_available[posting_num]}').click()
        time.sleep(2)
        driver.find_element(by=By.CLASS_NAME, value="jobs-s-apply").click()
    finally:
        # Complete application
        jobs_available.remove(jobs_available[posting_num])
        try:
            time.sleep(2)
            phone_num = driver.find_element(by=By.CLASS_NAME, value='fb-single-line-text__input')
            phone_num.clear()
            time.sleep(2)
            phone_num.send_keys(MY_PHONE_NUMBER)
            time.sleep(2)
            driver.find_element(by=By.CSS_SELECTOR, value='footer button').click()
            time.sleep(2)
            driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="Review your application"]').click()
            time.sleep(2)
            driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="Submit application"]').click()
        except NoSuchElementException:
            print('Cannot apply, skipped')
    print("Work complete")"""
