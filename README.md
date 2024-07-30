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

## Usage
1. **Run the script**:
    ```sh
    python YoutubeBot.py
    ```

2. **Provide Search Keyword**:
   - When you run the script, it will prompt you in the terminal to enter a search keyword. Type your keyword and press Enter. The script will use this keyword to perform the scraping.

3. **Background Operation**:
   - The script operates entirely in the background. It does not open a browser window or graphical interface. All actions are handled programmatically.

4. **Data Output**:
   - Extracted data will be saved in a CSV file located in the current directory.

5. **Resume Functionality**:
   - If the script is interrupted, it can resume from where it left off.


## Contributing
Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
