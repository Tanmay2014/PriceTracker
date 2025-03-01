# Web Scraper for Product Price Tracking
This repository contains a Python script for scraping product prices from Amazon.in.

# Requirements
To run this script, you need to have the following Python libraries installed:

* `requests`: Install using `pip install requests`
* `beautifulsoup4`: Install using `pip install beautifulsoup4`
* `lxml`: Install using `pip install lxml` (recommended for faster parsing)

## Usage
1.  Clone this repository to your local machine.
2.  Install the required libraries using the commands above.
3.  Modify the `url` variable in the script to the URL of the Amazon.in product you want to scrape.
4.  Run the script using `python your_script_name.py`.
5.  The script will print the product name and price to the console.

## Working in Progress (TODO)

* **Expand to other e-commerce platforms:**
    * Implement scraping functionality for Flipkart.
    * Add support for other e-commerce websites.
* **Error Handling:**
    * Add robust error handling to handle cases like network issues, invalid URLs, and changes in website structure.
* **Scheduler:**
    * Implement a scheduler (e.g., using `schedule` library or cron jobs) to run the script at regular intervals for automated price tracking.
* **Price Comparison:**
    * Implement functionality to compare prices of the same product across different platforms (Amazon, Flipkart, etc.).
* **GUI Implementation:**
    * Create a graphical user interface (GUI) using libraries like Tkinter, PyQt, or Kivy to provide a user-friendly experience.

## Contributing
Contributions are welcome! If you have any improvements or bug fixes, feel free to submit a pull request.
