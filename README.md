# README.md

## Overview

This Python script, `proto.py`, automates the process of extracting publication information of professors from the Ministry of Science and Technology (MOST) website in Taiwan. The script utilizes Selenium for web scraping and BeautifulSoup for parsing the HTML content.

## Prerequisites

Before running the script, ensure you have the following installed:
- Python 3.x
- Selenium
- BeautifulSoup
- Chrome WebDriver (compatible with your Chrome browser version)

## Setting Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies. Follow these steps to set up and activate a virtual environment:

1. **Create a Virtual Environment**:
   ```sh
   python -m venv myenv
    ```
2. **Activate the Virtual Environment**
    - on Windows
    ```sh
    myenv\Scripts\activate
    ```
    - on Mac
    ```sh
    source myenv/bin/activate
    ```
3. **Install Dependencies**
    ```sh
    pip install selenium beautifulsoup4
    ```
## Script Description
Functions
download_publications(professor): This function takes the name of a professor as input, navigates the MOST website, and extracts publication information for that professor. The function returns two lists:
articles: All articles by the professor.
articles_2011: Articles published by the professor after the year 2010.
Main Program
The script defines a list of professor names (profs). For each professor, it calls the download_publications function and prints the publication information categorized into:

Journal Articles
Book Chapters
Books
Others

## How to Use

    ```sh
    python proto.py
    ```