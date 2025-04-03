# YouTube Web Scraping Tool
## YouTube Video Metadata Scraper

---

This project is designed to scrape video metadata from YouTube and store the data in CSV format. It leverages Selenium for browser automation and various Python libraries for data processing and storage. The tool filters out advertisements and short videos, supports resuming from previous sessions, and offers advanced search options.

### Features
- **Video Metadata Scraping:** Retrieves video details based on user-defined search queries.
- **CSV Output:** Saves the scraped data into CSV files.
- **Ad and Short Video Filtering:** Automatically excludes unwanted content.
- **Resume Functionality:** Continues scraping from where it left off if interrupted.
- **Advanced Search Options:** Enables more targeted searches through criteria like language, country, and video count.

---

## Requirements

### 1. Python Version
- **Python 3.x:** Ensure you have the latest version of Python 3.x installed.

### 2. Google Chrome and ChromeDriver
- **Google Chrome:** This is the browser used by the project.
- **ChromeDriver:** Necessary for Selenium to execute browser automation.
  - **Important:**
    - The program automatically downloads the latest version of ChromeDriver.
    - Ensure that your installed Google Chrome version is compatible with the downloaded ChromeDriver.
    - Mismatched versions may lead to automation errors.
    - Check your Chrome version with:
      ```sh
      chrome --version  # or "chrome.exe --version" on Windows
      ```
  - If your Chrome version is not compatible with the current ChromeDriver, install the appropriate version.

### 3. Library Updates
- The project requires the latest versions of several libraries to function correctly, which helps resolve bugs and access new features.
- **Required Libraries:**
  - **yt-dlp:** For scraping video information from YouTube.
  - **selenium:** For browser automation.
  - **webdriver-manager:** For managing ChromeDriver versions.
- To install or update the libraries, run:
    ```sh
    pip install -r requirements.txt
    pip install --upgrade yt-dlp selenium webdriver-manager
    ```

---

## Installation Steps

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/kasimblc/youtube-bot
    cd youtube-bot
    ```

2. **Install the Required Libraries:**
    ```sh
    pip install -r requirements.txt
    ```

3. **(Optional) Update Installed Libraries:**
    If the libraries are already installed, update them with:
    ```sh
    pip install --upgrade yt-dlp
    pip install --upgrade selenium
    pip install --upgrade webdriver-manager
    ```

---

## Usage

### Running the Script

1. **Start the Script:**
    ```sh
    python YoutubeBot.py
    ```
    or
    ```sh
    python3 YoutubeBot.py
    ```

2. **Choose the Search Method:**
   When the script runs, you will be prompted to select one of the following options:
   - **1: Standard Search**  
     - Enter a search term to perform a global search (without language or country restrictions).
     - All videos matching the search term are scraped.
   
   - **2: Advanced Search**  
     - Offers extended search options:
       - **Video Count:** Specify the number of videos to retrieve (enter `0` for all videos).
       - **Search Language:** For example, enter `en` for English or `tr` for Turkish (leave blank to disable language filtering).
       - **Search Country:** For example, enter `US` for the United States or `TR` for Turkey (leave blank to disable country filtering).
   
   - **3: Resume Previous Search**  
     - If a previous search session exists, input the search term to continue where you left off.
     - If no saved data is found, a new search session is initiated.
   
   - **4: Single URL Search**  
     - Enter a specific YouTube video URL to display its metadata.
     - This option processes only one video, and its metadata is only displayed on-screen.
     - Note that the metadata is not saved to the database.

---

## Additional Information

### Background Process
- The script runs entirely in the background. It does not open a browser window or graphical interface, and all operations are executed programmatically.

### Data Output
- Once the scraping process is complete, the video metadata is saved as a CSV file in the directory where the script is run.
- Each row in the CSV file contains the video title, URL, and other available metadata.

### Error Handling
- If certain video details are hidden (e.g., due to channel restrictions), missing values are displayed as `Null`.
- Any errors encountered during the process are logged to the terminal and marked as `Error` in the output file.

### Resume Functionality
- If the script is interrupted, it can resume from where it left off without losing any previously collected data.

---

## Contributing
If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue.

---

## License
This project is licensed under the GNU General Public License v3.0. For further details, see the LICENSE file.
