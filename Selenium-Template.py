from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

# Start virtual display
display = Display(visible=0, size=(1200, 1200))  
display.start()

# Install and setup ChromeDriver
chromedriver_autoinstaller.install()

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1200x1200")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get('http://github.com')
    print(driver.title)
    with open('./GitHub_Action_Results.txt', 'w') as f:
        f.write(f"This was written with a GitHub action. Page title: {driver.title}")
finally:
    driver.quit()
    display.stop()
