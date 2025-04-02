from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

# Start virtual display
print("Starting virtual display...")
display = Display(visible=0, size=(1200, 1200))
display.start()

# Install and setup ChromeDriver
print("Installing ChromeDriver...")
chromedriver_autoinstaller.install()

# Setup Chrome options
print("Setting up Chrome options...")
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1200x1200")

# Initialize WebDriver
print("Initializing WebDriver...")
driver = webdriver.Chrome(options=chrome_options)

try:
    print("Navigating to GitHub...")
    driver.get('http://github.com')
    page_title = driver.title
    print("Page title:", page_title)
    
    print("Writing to file...")
    with open('./GitHub_Action_Results.txt', 'w') as f:
        f.write(f"This was written with a GitHub action. Page title: {page_title}")
    print("File written successfully.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Quitting WebDriver and stopping display...")
    driver.quit()
    display.stop()