# YouTube Web Scraping Tool
## YouTube Video Information Scraper

This project is a web scraping tool designed to extract video information from YouTube and save it as a CSV file. The tool utilizes libraries like Selenium for browser automation and various other Python libraries for data manipulation and storage.

Users can input a search keyword, and the program will scrape all relevant videos while ignoring ads and shorts videos. The tool also supports resuming from where it left off and performing detailed searches.

## Features
- Extracts video metadata from YouTube based on user-provided search keywords.
- Saves extracted data into CSV files.
- Ignores ads and shorts videos.
- Supports resuming from where it left off.
- Allows detailed searches for more specific results.

## Requirements

The following requirements must be met for this project:

### 1. Python Version
- **Python 3.x** is required. Make sure you have the latest 3.x version installed.

### 2. Google Chrome Browser and ChromeDriver
- **Google Chrome browser** is used in this project.
- **ChromeDriver** is required to perform browser automation.

#### Important Information:
- **Current ChromeDriver version: 114.0.5735.16**
- **This version is only compatible with Chrome 114.**
- **Therefore, your system must have Google Chrome version 114.x installed.**
- **Google Chrome usually updates automatically to the latest version, so if you are using a different version, you may encounter errors.**
- **If you encounter errors, you need to download and use the older Chrome 114.x version.**

### 3. Considerations for Future Updates
- When Chrome updates, the ChromeDriver version also changes.
- **The program automatically downloads the latest ChromeDriver version. Users only need to ensure that their Chrome browser version is compatible.**
- **Incorrect version combinations can lead to errors in the automation process.**
- **When new Chrome versions are released, you can check compatibility using the command below.**

#### Checking Chrome Version
To check the installed Chrome version, run the following command in the terminal or command prompt:
```sh
chrome --version  # Or for Windows: "chrome.exe --version"
```

If your Chrome version is not compatible with the current ChromeDriver version, **you need to install the appropriate Chrome version.**

### 4. Updating Libraries
It is important to work with the latest versions of the libraries used in this project. Updated versions include bug fixes and new features, so to avoid compatibility issues, make sure the libraries are up to date.

The installation steps already include **commands for installing and updating the required libraries**. **If the libraries are already installed, do not skip the update commands mentioned.** Otherwise, you may experience unexpected errors due to outdated versions.

For detailed installation steps, refer to the section below.

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/kasimblc/youtube-bot
    cd youtube-bot
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. If the necessary libraries are already installed, update them to the latest version:
- **yt-dlp**: For scraping video information from YouTube.
- **selenium**: For browser automation.
- **webdriver-manager**: For managing ChromeDriver versions.

Update commands:
```sh
pip install --upgrade yt-dlp
pip install --upgrade selenium
pip install --upgrade webdriver-manager
```

## Usage Steps
1. **Run the Script**:
    ```sh
    python YoutubeBot.py
    or
    python3 YoutubeBot.py
    ```

2. **Choose the Search Method**:
   - When the script is run, you will be prompted to choose one of the following search methods:
     - **1: Standard Search**:  
       - Enter a search term to fetch videos.  
       - By default, a global search is performed without language or country restrictions.  
       - All videos matching the search term are retrieved.  
     - **2: Advanced Search**:  
       - Allows for advanced search options. You can specify:  
         - **Number of Videos**: Define how many videos to fetch. Enter `0` to fetch all videos.  
         - **Search Language**: Specify the language (e.g., `en` for English, `tr` for Turkish). If left blank, no language filter will be applied.  
         - **Search Country**: Specify the country (e.g., `US` for the United States, `TR` for Turkey). If left blank, no country filter will be applied.  
       - These options allow you to make your search more specific.  
     - **3: Resume Previous Search**:  
       - If a search was previously initiated, enter the search term to continue from where it left off.  
       - If no saved data is found, you will be prompted to start a new search.  
     - **4: Single URL Search**:  
       - Enter a specific YouTube video URL to fetch its metadata.  
       - This method only processes one video and displays its metadata on the screen.  
       - The metadata is not saved to the database, allowing for quick viewing.

---

## Additional Information
### Background Process:
   - The script operates entirely in the background. It does not open a browser window or graphical interface. All processes are performed programmatically.

### Data Output:
   - Retrieved video metadata is saved as a **CSV file** in the directory where the script is run. Each row contains video titles, URLs, and other available metadata.

### Error Handling:
   - If certain video data is hidden (e.g., due to channel restrictions), missing values are displayed as `Null`.  
   - Any errors encountered during the process are displayed in the terminal and marked as `Error` in the output file.

### Resume Functionality:
   - If the script is interrupted, it can resume the scraping process from where it left off without losing previously collected data.

## Contributing
Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

