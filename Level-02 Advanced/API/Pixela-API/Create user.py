from selenium import webdriver

# Specify the path to the EdgeDriver
driver_path = "C:/WebDrivers/EdgeDriver/msedgedriver.exe"

# Launch Microsoft Edge using the driver
driver = webdriver.Edge(executable_path=driver_path)

# Example usage
driver.get("https://www.google.com")
