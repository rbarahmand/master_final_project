# Crawling National Formulary of Iran

**https://irc.fda.gov.ir/nfi**

This projects done by **Reza Barahmand** for research purposes.\
This project fully coded in python.

## Files

This project consists of 3 main files:\

- Experiment file that conclude all my trials and errors (extensive).
- Selenium file, that uses selenium library in python and google chrome webdriver (full solution).
- The combination of BeautifulSoup and requests libraries of python (full solution).

## Approach

1. the main domain to crawl is:
   - https://irc.fda.gov.ir/nfi/Detail/{number}
   - The {number} range is [0,45433] (it is constantly changing)
2. The crawling page is static so we can use both:
   - Selenium + webdriver
   - requests + BeautifulSoup
3. The data will automatically save in dataset folder that will be create automatically as well.
4. Data saver has a mechanism to save data incrementally (due to the network loss).
5. At the end the data can be integrated using pandas library.
6. A mechanism for automatically finding the last index added.

## Features that are collected

- name
- general_name
- drug_type
- consumption
- license
- brand
- country
- producer
- license_exp
- price_per_pack
- unit_price
- GTIN
- IRC
- number_per_pack
- ingredients
- ATC_code

## Coming soon

- Add functionality to the program not to crash after a broken internet connection occurs.
