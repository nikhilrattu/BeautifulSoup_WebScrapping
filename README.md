# BeautifulSoup Web Scraping

A collection of web scraping projects built using Python and BeautifulSoup.  
This repository documents practical implementations of web scraping techniques.

---

## About This Repository

This repository contains multiple mini-projects that demonstrate how to extract, process, and analyze data from websites.

Each project is organized independently for clarity and scalability.

---

## Project 1: Basic Web Scraper

### Overview
This project demonstrates the fundamentals of web scraping using BeautifulSoup. It focuses on fetching webpage content and extracting specific data elements in a structured format.

### Features
- Sends HTTP requests to a target website  
- Parses HTML content using BeautifulSoup  
- Extracts relevant data (e.g., headings, links, or other elements depending on the script)  
- Outputs clean and structured results  

### Key Learnings
- Understanding HTML structure for scraping  
- Using BeautifulSoup methods such as `find()` and `find_all()`  
- Handling HTTP requests and responses  
- Debugging basic scraping scripts  

### Tech Stack
- Python  
- BeautifulSoup  
- requests  

## Project 2: Books Website Scraper (Books to Scrape)

### Overview
This project involves scraping book data from a demo e-commerce website. It extracts key information such as book titles, product links, and prices across multiple pages and stores the data in a structured CSV file.

### Purpose
The goal of this project is to practice large-scale data extraction using pagination. It demonstrates how to systematically scrape multiple pages of a website and organize the collected data for further use, such as analysis or reporting.

### Features
- Scrapes data from 50 pages of a website  
- Extracts book titles, links, and prices  
- Handles structured HTML elements efficiently  
- Stores extracted data into a CSV file using pandas  

### Key Concepts and Logic Used
- **HTTP Requests**: Used the `requests` library to fetch webpage content  
- **HTML Parsing**: Utilized BeautifulSoup to navigate and extract data from HTML  
- **Pagination Handling**: Iterated through multiple pages using a loop (`range(1,51)`)  
- **Tag Navigation**: Accessed nested tags (`h3 > a`) to extract book names and links  
- **Data Extraction**: Retrieved attributes such as text and `href` values  
- **Data Aggregation**: Stored extracted data in a list of dictionaries  
- **Data Export**: Converted the collected data into a pandas DataFrame and exported it as a CSV file  

### Tech Stack
- Python  
- BeautifulSoup  
- requests  
- pandas  

### Output
The final output is a CSV file (`Books_info.csv`) containing details of books including name, link, and price.

## Project 3: E-commerce Product Scraper (Love & Flair)

### Overview
This project focuses on scraping product data from an e-commerce website. It extracts structured information such as product name, price, stock availability, color, and available sizes across multiple pages and stores the data in a CSV file for further analysis.

### Purpose
The primary objective of this project is to demonstrate end-to-end web scraping, including pagination handling, product link extraction, detailed page scraping, and data storage. It simulates a real-world use case of collecting product data for analysis or automation.

### Features
- Scrapes multiple pages using pagination  
- Collects unique product links from listing pages  
- Extracts detailed product information from individual product pages  
- Handles missing data gracefully  
- Stores structured data into a CSV file using pandas  

### Key Concepts and Logic Used
- **HTTP Requests**: Used the `requests` library with custom headers to mimic a browser request  
- **HTML Parsing**: Parsed web pages using BeautifulSoup  
- **Pagination Handling**: Iterated through multiple pages using a loop (`range(1,11)`)  
- **URL Handling**: Used `urljoin` to construct complete product URLs  
- **Data Deduplication**: Used a `set` to store unique product links  
- **Conditional Extraction**: Checked for missing HTML elements to avoid errors  
- **List Handling**: Extracted available sizes dynamically while filtering out disabled options  
- **Data Structuring**: Stored extracted data in dictionaries and appended to a list  
- **Data Export**: Converted data into a pandas DataFrame and exported it as a CSV file  

### Tech Stack
- Python  
- BeautifulSoup  
- requests  
- pandas  

### Output
The final output is a CSV file (`products.csv`) containing structured product data.
