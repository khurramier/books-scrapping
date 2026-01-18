# 🛡️ End-to-End E-Commerce Data Pipeline

A robust, fault-tolerant ETL (Extract, Transform, Load) solution designed to scrape, clean, and structure pricing data from e-commerce platforms.

**Target:** [Books to Scrape](http://books.toscrape.com) (Sandbox Environment)  
**Tech Stack:** Python, Pandas, BeautifulSoup4, Requests (with Retry Logic).

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Status](https://img.shields.io/badge/Status-Production%20Ready-green) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-150458)

---

## 📖 Project Overview
This project demonstrates a production-grade **Data Pipeline** that goes beyond simple scraping. It mimics human behavior to navigate paginated content, handles server-side connection drops automatically, and includes a post-processing layer to sanitize currency data for analysis.

### The Business Case
Businesses need real-time competitor pricing intelligence. Manual data entry is slow and prone to error. This tool automates the collection of 1,000+ SKUs, reducing a 10-hour manual task to a **2-minute automated run** with 100% accuracy.

---

## 🚀 Key Engineering Features

### 1. 🛡️ Robust Network Logic (The "Retry" Layer)
* **Automatic Retries:** Implements `urllib3.util.retry` with exponential backoff. If the server drops the connection (Error 10054) or returns a 5xx error, the script waits and retries automatically instead of crashing.
* **Session Management:** Uses a persistent `requests.Session` object to maintain cookies and connection pooling for faster performance.

### 2. 🕵️‍♂️ Anti-Bot Evasion
* **User-Agent Spoofing:** Injects browser-mimicking headers to bypass basic firewall blocks.
* **Randomized Jitter:** Implements `random.uniform(2, 5)` delays between requests to disrupt mechanical scraping patterns.

### 3. 🧹 Automated Data Cleaning (Pandas)
* **Encoding Fixes:** Explicitly handles UTF-8 artifacts (removing `Â£` symbols).
* **Type Conversion:** Automatically converts currency strings into clean `float` or `numeric` types, ensuring the final output is ready for immediate SQL/Excel analysis.

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `scraper.py` | **The Extractor.** Handles HTTP requests, pagination logic, and raw HTML parsing. Includes the Retry Adapter. |
| `clean_data.py` | **The Transformer.** Loads the raw CSV, sanitizes currency symbols, handles missing values, and exports the final dataset. |
| `books.csv` | **Raw Output.** The initial data dump from the scraper. |
| `books_cleaned_data.csv` | **Final Deliverable.** The clean, analysis-ready dataset. |

---

## 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/books-data-pipeline.git](https://github.com/yourusername/books-data-pipeline.git)
    cd books-data-pipeline
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests beautifulsoup4 pandas
    ```

3.  **Step 1: Run the Scraper**
    ```bash
    python scraper.py
    ```
    *Status: This will crawl all 50 pages and generate `books.csv`.*

4.  **Step 2: Clean the Data**
    ```bash
    python clean_data.py
    ```
    *Status: This will remove encoding artifacts and generate `books_cleaned_data.csv`.*

---

## 📊 Sample Data (Before vs. After)

**Raw Data (`books.csv`):**
| Title | Price | Star Rating |
| :--- | :--- | :--- |
| A Light in the Attic | Â£51.77 | Three |

**Cleaned Data (`books_cleaned_data.csv`):**
| Title | Price | Star Rating |
| :--- | :--- | :--- |
| A Light in the Attic | 51.77 | Three |

---

## ⚖️ Disclaimer
This project targets a public sandbox environment specifically designed for testing web scrapers. The techniques used here (User-Agents, Delays, Retries) are for educational demonstration of ethical, robust scraping practices.