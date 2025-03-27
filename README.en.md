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
- Python 3.x
- Google Chrome browser

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

## Usage
1. **Run the script**:
    ```sh
    python YoutubeBot.py
    or
    python3 YoutubeBot.py
    ```

2. **Choose Search Method**:
   - When the script is executed, you will be prompted to choose one of the following search methods:
     - **1: Standard Search**:  
       - Enter a search term to fetch videos.  
       - Global search is performed by default, as no language or country restrictions are set.  
       - All videos matching the search term will be retrieved.  
     - **2: Custom Search**:  
       - Allows for advanced search options. You can specify:  
         - **Number of Videos**: Define how many videos to fetch. Enter `0` to retrieve all videos.  
         - **Search Language**: Specify the language (e.g., `en` for English or `tr` for Turkish). If left empty, no language filter will be applied.  
         - **Search Country**: Specify the country (e.g., `US` for the United States or `TR` for Turkey). If left empty, no country filter will be applied.  
       - These options enable you to customize your search for more specific results.  
     - **3: Resume Previous Search**:  
       - If a previous search exists, enter its search term to continue scraping from where it was last interrupted.  
       - If no saved data is found, you will be prompted to start a new search.

3. **Background Operation**:
   - The script operates entirely in the background. It does not open a browser window or graphical interface. All actions are handled programmatically.

4. **Data Output**:
   - Extracted video metadata will be saved in a CSV file in the current directory. Each row will include video titles, URLs, and any additional available metadata.

5. **Error Handling**:
   - If certain video data is hidden (e.g., due to channel restrictions), the missing values will be displayed as `Null`.  
   - Errors encountered during processing will be logged in the terminal and flagged as `Error` in the output file.

6. **Resume Functionality**:
   - If the script is interrupted, it can resume scraping from where it left off without losing previously collected data.

## Contributing
Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

