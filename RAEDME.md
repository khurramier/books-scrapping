# 📚 Books To Scrape - E-Commerce Data Pipeline

A full-stack web scraping project that extracts, processes, and structures product data from [Books to Scrape](http://books.toscrape.com). This tool autonomously navigates through 50 pages of pagination to collect data on 1,000 books, mimicking human behavior to ensure reliability.

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `scraper.py` | **The Core Engine.** Navigates pages, handles pagination logic, and extracts raw data (Title, Price, Rating). Includes anti-bot delays. |
| `check_data.py` | **The Auditor.** A Pandas-based script that loads the raw CSV, performs quality checks, cleans currency symbols (UTF-8 issues), and exports the final dataset. |
| `books.csv` | The **Raw** output from the scraper (contains uncleaned symbols like `Â£`). |
| `books_cleaned_data.csv` | The **Final** deliverable. Cleaned, numeric price columns, ready for analysis. |

## 🚀 Key Features

* **Automated Pagination:** Logic to handle `next` buttons and relative URL joining across 50+ pages.
* **Robust Extraction:** Uses `BeautifulSoup4` to parse complex HTML tags (extracting ratings from class names, e.g., `class="star-rating Three"`).
* **Anti-Blocking:** Implements random time delays (`jitter`) and User-Agent headers to bypass basic scraping protections.
* **Data Pipeline:** Separate logic for extraction (Requests) and transformation (Pandas), ensuring data safety if the network fails.

## 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/khurramier/books-scraping.git
    cd books-scraping
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests beautifulsoup4 pandas
    ```

3.  **Run the Scraper:**
    ```bash
    python scraper.py
    ```
4.  **Clean the Data:**
    ```bash
    python check_data.py
    ```
    *This will generate `books_cleaned_data.csv`.*

## 📊 Sample Data (Cleaned)

| Title | Price | Star Rating |
| :--- | :--- | :--- |
| A Light in the Attic | 51.77 | Three |
| Tipping the Velvet | 53.74 | One |
| Soumission | 50.10 | One |

## 🛡️ Disclaimer
This project is for educational purposes only. The target website `books.toscrape.com` is a sandbox environment specifically designed for testing web scrapers.