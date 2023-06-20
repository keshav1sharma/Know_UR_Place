# Know_UR_Place

This is a Python script that utilizes Selenium to interact with the Bhuvan website and capture old satellite imagery snapshot from 1990s of a specified location on the map.

## Prerequisites

- Python 3.x
- Selenium library
- ChromeDriver executable

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/keshav1sharma/Know_UR_Place.git
   ```

2. Install the required dependencies using pip:

   ```shell
   pip install selenium
   ```

3. Download the ChromeDriver executable suitable for your operating system and Chrome browser version. Make sure to note the path where you save the executable.

   ChromeDriver download link: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

## Usage

1. Open the `know_ur_place.py` file in a text editor.

2. Set the URL of the Bhuvan website by modifying the `url` variable. By default, it is set to `'https://bhuvan-app1.nrsc.gov.in/bhuvan2d/bhuvan/bhuvan2d.php#'`.

3. Set the path to the ChromeDriver executable by modifying the `driver_path` variable. Replace `/Users/keshavsharma/Desktop/chromedriver` with the actual path where you saved the ChromeDriver executable.

4. Run the script:

   ```shell
   python know_ur_place.py
   ```

5. Enter the coordinates (latitude, longitude) when prompted.

6. The script will navigate to the Bhuvan website, search for the specified coordinates, wait for the map to load, take a snapshot of the map, and save it as `map_snapshot.png`.

7. The ChromeDriver instance will be closed automatically.

## Notes

- Ensure you have a stable internet connection to access the Bhuvan website and load the map.
- The script uses the Selenium library to automate interactions with the website, specifically with the Chrome browser. Make sure you have Chrome installed on your system.
- The `selenium` and `webdriver` packages must be installed for the script to work correctly. You can install them using the command `pip install selenium`.
- The script assumes that you have downloaded the ChromeDriver executable and provided its path in the `driver_path` variable. If you encounter any issues, please ensure that the ChromeDriver version matches your Chrome browser version.
- The script implicitly waits for certain elements to load on the webpage. However, depending on your internet speed and system performance, you may need to adjust the wait times in the script to ensure proper execution.
- The captured map snapshot will be saved in the same directory as the script with the filename `map_snapshot.png`.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This script utilizes the Selenium library, which is a powerful tool for automating web browsers. For more information, visit [https://www.selenium.dev/](https://www.selenium.dev/).
