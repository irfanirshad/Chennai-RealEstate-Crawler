# ChennaiRealEstateCrawler

This is a Python-based web scraper that extracts information on commercial properties from Magicbricks.com and 99acres.com for SNE, a real estate company based in Chennai, Tamil Nadu, India. The scraper is designed to collect data on properties that match the profile of the target clients to whom SNE leases commercial properties, such as IT offices, factories, showrooms etc.

This project follows the Strategy Design Pattern, where the strategies followed in this case involve scraping either MagicBricks.com or 99Acres.com. The corresponding service is then called to perform the required scraping task for you.

## Requirements

To run this web scraper, you'll need:

- Python 3.x
- Selenium
- ChromeDriver
- ExcelWriter
- Pandas

# Installation

* Clone this repository to your local machine:
```
git clone https://github.com/irfanirshad/selenium_scraper.git

```

* Install the required Python packages:
```
pip install -r requirements.txt

```

* Download and install ChromeDriver for your operating system. You can find the latest version of ChromeDriver [here](https://sites.google.com/chromium.org/driver/) .


# Usage

To run the scraper, simply navigate into the driver folder and run the driver.py file:
```
python driver.py
```

The script will then start scraping commercial property data from Magicbricks.com  and save the results to a Excel file in the current directory.


## Contributing

If you'd like to contribute to this project, please open an issue or pull request on this repository.


## License

This project is licensed under the MIT License. See the LICENSE file for details.
