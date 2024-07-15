import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class WebScrapperApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Web Scrapper")
        self.geometry("500x300")
        self.create_widgets()
    
    def create_widgets(self):
        # URL Input
        self.url_label = ttk.Label(self, text="Enter URL:")
        self.url_label.pack(pady=5)
        self.url_entry = ttk.Entry(self, width=50)
        self.url_entry.pack(pady=5)

        # Option Buttons
        self.option_label = ttk.Label(self, text="Choose what to extract:")
        self.option_label.pack(pady=5)

        self.option_var = tk.StringVar()
        self.option_menu = ttk.Combobox(self, textvariable=self.option_var)
        self.option_menu['values'] = ('Links', 'Headers', 'Paragraphs', 'Images')
        self.option_menu.pack(pady=5)

        # Scrape Button
        self.scrape_button = ttk.Button(self, text="Scrape", command=self.scrape)
        self.scrape_button.pack(pady=20)

    def scrape(self):
        url = self.url_entry.get()
        option = self.option_var.get()

        if not validate_url(url):
            messagebox.showerror("Invalid URL", "Please enter a valid URL.")
            return

        html = fetch_url(url)
        if not html:
            messagebox.showerror("Error", "Failed to fetch URL.")
            return

        soup = BeautifulSoup(html, 'html.parser')

        if option == 'Links':
            data = extract_links(soup)
        elif option == 'Headers':
            data = extract_headers(soup)
        elif option == 'Paragraphs':
            data = extract_paragraphs(soup)
        elif option == 'Images':
            data = extract_images(soup)
        else:
            messagebox.showerror("Invalid Option", "Please select a valid option.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if save_path:
            save_to_file(save_path, data)
            messagebox.showinfo("Success", f"Data saved to {save_path}")    

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

if __name__ == "__main__":
    app = WebScrapperApp()
    app.mainloop()
