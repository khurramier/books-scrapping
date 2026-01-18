#Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv
import time
import random
from urllib.parse import urljoin
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_session():
    """
    Creates a requests Session with automatic retry logic.
    If the server blocks us (10054 error), this will wait and try again.
    """
    session = requests.Session()
    retry = Retry(
        total= 3,               # Try 3 times
        backoff_factor=1,       # Wait 1s, then 2s, then 4s
        status_forcelist=[500, 502, 503, 504] # Retry on server errors

    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('http://', adapter)
    return session

def book_scraper():
    # Website to scrape
    current_url = "https://books.toscrape.com/index.html"
    
# User-Agent header to identify our scraper
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    # Open file to write data
    with open('books.csv', 'w', newline='', encoding='utf-8') as f:
        writer= csv.writer(f)
        writer.writerow(['Title', 'Price', 'Star Rating'])
        # Loop through the whole website
        while True:
            print (f"Scraping {current_url}")
            
            try:
                response = requests.get(current_url, headers=headers, timeout=10)
                response.raise_for_status() # check for 404/500 errors

                soup = BeautifulSoup(response.text, "html.parser")
                books = soup.find_all(class_="product_pod")
                if not books:
                    print('No books found. Ending')
                    break
                
                    # scrape the required data from page
                for book in books:
                    title = book.find('h3').find('a')['title']
                    price = book.find(class_='price_color').text
                    rating = book.find('p', class_='star-rating')['class'][1]
                    print (f"Title: {title} Price: {price} Star rating: {rating} ")
                    writer.writerow([title, price, rating]) # Writing data to file
                # Pagination: Find the next button
                next_button = soup.find(class_='next')
                # 
                if next_button:
                    next_url = next_button.find('a')['href']
                    current_url = urljoin(current_url, next_url)
                    time.sleep(random.uniform(2,5))
                else:
                    print('Scraping completed')
                    break
            except Exception as e:
                print(f"Error scraping {current_url}: {e}")
                break
if __name__ == "__main__":
    book_scraper()