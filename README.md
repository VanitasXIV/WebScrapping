# Web Scraping Tool

This Python script allows you to scrape web pages for various types of content such as links, headers, paragraphs, and images. It uses the `BeautifulSoup` library to parse HTML and extract the desired data, which can then be saved to text files.

## Features

- **Input Validation**: Ensures the URL provided is valid.
- **Exception Handling**: Catches errors during URL fetching.
- **Extracting Other Tags**: Retrieves and prints other HTML elements like headers, paragraphs, and images.
- **Exporting Data**: Saves the retrieved links and other extracted data to a file.
- **Improved User Interface**: Provides a menu for the user to choose what to extract.

## Prerequisites

- Python 3.x
- `BeautifulSoup` library
- `urllib` module

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/your-username/web-scraping-tool.git
    cd web-scraping-tool
    ```

2. Install the required packages:
    ```sh
    pip install beautifulsoup4
    ```

## Usage

1. Run the script:
    ```sh
    python web_scraping_tool.py
    ```

2. Enter the URL you want to scrape when prompted.

3. Choose what type of content you want to extract by selecting the corresponding option:
    - Links
    - Headers
    - Paragraphs
    - Images
    - Exit

4. The extracted data will be printed on the screen and saved to a corresponding text file (`links.txt`, `headers.txt`, `paragraphs.txt`, or `images.txt`).

## Example

```sh
Enter URL: https://www.example.com
Choose what to extract:
1. Links
2. Headers
3. Paragraphs
4. Images
5. Exit
Enter your choice: 1

Links:
https://www.example.com/page1
https://www.example.com/page2
...
Data saved to links.txt
