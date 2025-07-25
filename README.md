# TGE_scrape

This Python script scrapes hourly electricity contract prices from the Polish Power Exchange (TGE) and saves them to an XML file named with the current date (e.g. `20250101-120000.xml`). Useful for managing solar (PV) installations and analyzing market prices.

## Requirements

- Python 3
- `beautifulsoup4`
- `requests`
- `datetime`

Install dependencies:

'''bash
pip install beautifulsoup4 requests

# Usage
'''bash
python tge.py

