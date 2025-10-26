import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import time
import html2text

base_url = "https://www.mql5.com"
docs_url = "https://www.mql5.com/en/docs/python_metatrader5"

# Fetch the main documentation page
response = requests.get(docs_url)
if response.status_code != 200:
    print("Failed to fetch the main page")
    exit(1)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all links to documentation pages
links = soup.find_all('a', href=True)
doc_links = set()

for link in links:
    href = link['href']
    if href.startswith('/en/docs/python_metatrader5/'):
        full_url = urllib.parse.urljoin(base_url, href)
        doc_links.add(full_url)

print(f"Found {len(doc_links)} documentation pages.")

# Create directory to save docs
os.makedirs('docs', exist_ok=True)

# Download each page
for url in doc_links:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Convert HTML to Markdown
            h = html2text.HTML2Text()
            h.ignore_links = False
            markdown_content = h.handle(response.text)
            # Extract filename from URL
            path = urllib.parse.urlparse(url).path
            filename = path.split('/')[-1] + '.md'
            filepath = os.path.join('docs', filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            print(f"Saved {filename}")
        else:
            print(f"Failed to fetch {url} (status {response.status_code})")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    
    # Add delay to avoid overwhelming the server
    time.sleep(1)
