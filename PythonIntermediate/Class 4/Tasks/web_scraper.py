import threading
import requests


# Function to scrape data from a single URL
def scrape_url(url):
    response = requests.get(url)
    # Process the response data as needed
    print(f"Scraped data from {url}: {response.text[:50]}")


# List of URLs to scrape
urls = ['https://www.delfi.ee', 'https://www.google.com', 'https://doodles.google']

# Create a thread for each URL
threads = []
for url in urls:
    thread = threading.Thread(target=scrape_url, args=(url,))
    threads.append(thread)

# Start all the threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Any further processing of the scraped data can be done here
