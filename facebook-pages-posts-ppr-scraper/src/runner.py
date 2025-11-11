thonimport json
import os
from extractors.facebook_parser import FacebookParser
from extractors.utils_time import DateFilter
from outputs.exporters import Exporter

def main():
    page_url = input("Enter the Facebook page URL to scrape: ")
    start_date = input("Enter start date (YYYY-MM-DD) or press Enter to skip: ")
    end_date = input("Enter end date (YYYY-MM-DD) or press Enter to skip: ")

    # Initialize the date filter if dates are provided
    date_filter = DateFilter(start_date, end_date) if start_date and end_date else None

    # Scrape Facebook posts
    scraper = FacebookParser(page_url, date_filter)
    posts = scraper.scrape_posts()

    # Export the results
    exporter = Exporter(posts)
    exporter.export_to_json()

if __name__ == "__main__":
    main()