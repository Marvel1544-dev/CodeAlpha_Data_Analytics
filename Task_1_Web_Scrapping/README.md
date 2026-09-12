# Web Scraping Task - Books Dataset

## Overview
This project demonstrates web scraping techniques using Python to extract book data from **books.toscrape.com**. The scraped data includes book titles, prices, ratings, and availability information, which is then analyzed and stored in a CSV file.

## Project Structure
```
Task_1_Web_Scrapping/
├── web_scraping.py          # Main web scraping script
├── books_dataset.csv        # Output dataset with scraped book data
└── README.md               # This file
```

## Features
- **Web Scraping**: Extracts book information from [books.toscrape.com](https://books.toscrape.com/)
- **Data Extraction**: Collects:
  - Book titles
  - Prices (in GBP)
  - Star ratings (One to Five)
  - Availability status
- **Data Analysis**: Performs statistical analysis on the scraped dataset
- **Data Export**: Saves collected data to CSV format

## Requirements
Install the required dependencies:

```bash
pip install requests beautifulsoup4 pandas
```

### Dependencies
- **requests** - HTTP library for fetching web pages
- **beautifulsoup4** - HTML/XML parsing library
- **pandas** - Data manipulation and analysis

## Usage

### Running the Scraper
```bash
python web_scraping.py
```

The script will:
1. Fetch data from books.toscrape.com
2. Parse HTML content using BeautifulSoup
3. Extract book information from product pods
4. Print detailed information for each book
5. Display statistical summaries

### Output
The script generates:
- **Console Output**: Details for each book scraped
- **Statistical Analysis**: 
  - Dataset information (dtypes, memory usage)
  - Missing values count
  - Duplicate values count
  - Summary statistics
  - Price-specific statistics

## Dataset Details

The `books_dataset.csv` contains the following columns:

| Column | Description | Type |
|--------|-------------|------|
| title | Book title | String |
| price | Book price in GBP | Float |
| rating | Star rating (One-Five) | String |
| availability | Stock status | String |

### Sample Data
```csv
title,price,rating,availability
A Light in the Attic,51.77,Three,In stock
Tipping the Velvet,53.74,One,In stock
Sapiens: A Brief History of Humankind,54.23,Five,In stock
```

## Code Highlights

### Key Extraction Methods
```python
# Extract book title
title = book.h3.a["title"]

# Extract price and clean it
price = book.find("p", class_="price_color").text.replace("£", "").strip()

# Extract rating
rating = book.find("p", class_="star-rating")["class"][1]

# Extract availability
availability = book.find("p", class_="instock availability").text.strip()
```

### Data Analysis
The script performs:
- Data type verification and conversion
- Descriptive statistics calculation
- Missing value detection
- Duplicate record identification

## Learning Objectives
This task demonstrates:
✅ Web scraping with Python  
✅ HTML parsing and element extraction  
✅ Data cleaning and transformation  
✅ Pandas DataFrame manipulation  
✅ Statistical analysis on raw data  
✅ Data export to CSV format  

## Notes
- The scraper is designed for educational purposes
- Ensure you have proper permissions before scraping any website
- Respect the website's `robots.txt` and terms of service
- The target website (books.toscrape.com) is specifically designed for learning web scraping

## Future Enhancements
- Add error handling for network failures
- Implement pagination to scrape multiple pages
- Add database storage option (SQLite/PostgreSQL)
- Create data visualization charts
- Optimize DataFrame creation (currently recreates on each iteration)
- Add logging functionality

## Author
Marvel1544-dev

## License
This is an educational project for CodeAlpha Data Analytics Internship.
