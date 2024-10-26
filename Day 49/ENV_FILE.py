from dotenv import load_dotenv
import os

# Load .env file
load_dotenv("MY_CREDENTIALS.env")
MY_EMAIL = os.getenv("E-MAIL")
MY_PASSWORD = os.getenv("PASSWORD")
MY_PHONE_NUMBER = os.getenv("MOBILE_NO")

print(MY_EMAIL, MY_PASSWORD, MY_PHONE_NUMBER)
