from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
import time

# Set the URL of the Bhuvan website
url = 'https://bhuvan-app1.nrsc.gov.in/bhuvan2d/bhuvan/bhuvan2d.php#'

# Set the path to the ChromeDriver executable
driver_path = '/Users/keshavsharma/Desktop/chromedriver'

# Create a ChromeOptions instance
options = ChromeOptions()
options.add_argument('--no-sandbox')

# Create a ChromeDriver instance
driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path), options=options)

# Navigate to the Bhuvan website
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)

# Take the coordinates as input
coordinates = input("Enter the coordinates (latitude, longitude): ")

# Find the search input element and enter the coordinates
search_input = driver.find_element(by='id', value='Val')
search_input.clear()
search_input.send_keys(coordinates)
search_input.send_keys(Keys.RETURN)

driver.execute_script("AddLayer('Corono_Sat_Data','Corono_Sat_Data',urlArray1)")
driver.execute_script("map.zoomTo(8)")
time.sleep(8)
# Wait for the map to load
driver.implicitly_wait(10)

# Take a snapshot of the map
driver.save_screenshot('map_snapshot.png')

# Close the ChromeDriver instance
driver.quit()
