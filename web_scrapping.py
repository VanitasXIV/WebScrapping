import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import os

def validate_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def fetch_url(url):
    try:
        html = urllib.request.urlopen(url).read()
        return html
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")
        return None

def extract_links(soup):
    links = []
    tags = soup('a')
    for tag in tags:
        href = tag.get('href', None)
        if href:
            links.append(href)
    return links

def extract_headers(soup):
    headers = []
    for i in range(1, 7):
        tags = soup(f'h{i}')
        for tag in tags:
            headers.append(tag.text.strip())
    return headers

def extract_paragraphs(soup):
    paragraphs = []
    tags = soup('p')
    for tag in tags:
        paragraphs.append(tag.text.strip())
    return paragraphs

def extract_images(soup):
    images = []
    tags = soup('img')
    for tag in tags:
        src = tag.get('src', None)
        if src:
            images.append(src)
    return images

def save_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"{item}\n")
    print(f"Data saved to {filename}")

def main():
    url = input('Enter URL: ')
    if not validate_url(url):
        print("Invalid URL. Please enter a valid URL.")
        return

    html = fetch_url(url)
    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')

    while True:
        print("\nChoose what to extract:")
        print("1. Links")
        print("2. Headers")
        print("3. Paragraphs")
        print("4. Images")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            links = extract_links(soup)
            print("\nLinks:")
            for link in links:
                print(link)
            save_to_file('links.txt', links)
        elif choice == '2':
            headers = extract_headers(soup)
            print("\nHeaders:")
            for header in headers:
                print(header)
            save_to_file('headers.txt', headers)
        elif choice == '3':
            paragraphs = extract_paragraphs(soup)
            print("\nParagraphs:")
            for paragraph in paragraphs:
                print(paragraph)
            save_to_file('paragraphs.txt', paragraphs)
        elif choice == '4':
            images = extract_images(soup)
            print("\nImages:")
            for image in images:
                print(image)
            save_to_file('images.txt', images)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
