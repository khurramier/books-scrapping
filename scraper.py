#Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv
import time
import random

def book_scraper():
    # Website to scrape
    base_url = "https://books.toscrape.com/"
    current_url = "catalogue/page-1.html"

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
            if "catalogue" not in current_url:
                full_address = base_url +"catalogue/"+ current_url
            else:
                full_address = base_url + current_url
            response = requests.get(full_address, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.find_all(class_="product_pod")            
            # scrape the required data from page
            for book in books:
                title = book.find('h3').find('a')['title']
                price = book.find(class_='price_color').text
                rating = book.find('p', class_='star-rating')['class'][1]
                print (f"Title: {title} Price: {price} Star rating: {rating} ")
                writer.writerow([title, price, rating]) # Writing data to file
                
            # Find the next button
            next_button = soup.find(class_='next')
            time.sleep(random.uniform(2,5))
            if next_button:
                current_url = next_button.find('a')['href']
            else:
                print('Scraping completed')
                break
if __name__ == "__main__":
    book_scraper()