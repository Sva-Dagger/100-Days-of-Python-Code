from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv("MY_CREDENTIALS.env")
MY_EMAIL = os.getenv("E-MAIL")
MY_PASSWORD = os.getenv("PASSWORD")
PROMISED_DOWN = 1000
PROMISED_UP = 30

Edge_options =webdriver.EdgeOptions()
Edge_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Edge(options=Edge_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(4)
        self.driver.find_element(By.XPATH,
                            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        sleep(40)
        self.down = self.driver.find_element(By.XPATH,
                                   value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                 value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text



        print(f"Download = {self.down} Mbps")
        print(f"Upload = {self.up} Mbps")
        sleep(2)

    def tweet_at_provider(self):
        self.driver.maximize_window()
        self.driver.get("https://x.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJteCI6IjIifQ%3D%3D%22%7D")
        sleep(5)
        email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email.send_keys(MY_EMAIL)
        sleep(2)
        email.send_keys(Keys.ENTER)
        sleep(2)
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(MY_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(25)
        sleep(5)
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        sleep(2)
        tweet = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} Mbps Down/{self.up} Mbps Up when I pay for {PROMISED_DOWN} Mbps Down/{PROMISED_UP} Mbps Up?")
        sleep(5)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]').click()
        sleep(2)
        self.driver.quit()


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.tweet_at_provider()
