import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas
import argparse
import csv
import connect

bay_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=converses&_sacat=0&_pgn="
parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the number of pages to parse", type=int)
parser.add_argument("--dbname", help="Enter the number of pages to parse", type=str)
args = parser.parse_args()
page_num_max = args.page_num_max
dbname = args.dbname
scraped_info_list = []
connect.connect(dbname)


for page in range(1, page_num_max+1):
    url = bay_url + str(page)
    print("GET REQUEST FOR >> " + url)
    req = requests.get(url)
    content = req.content
    print("Success")
    soup = BeautifulSoup(content, "html.parser")

    all_shoes = soup.find_all("li", {"class": "s-item s-item--watch-at-corner"})

    for shoes in all_shoes:
        item_dict = {}
        item_dict["name"] = shoes.find("h3", {"class": "s-item__title"}).text
        item_dict["subtitle"] = shoes.find("span", {"class": "SECONDARY_INFO"}).text
        item_dict["price"] = shoes.find("span", {"class": "s-item__price"}).text
        item_dict["shipping"] = shoes.find("span", {"class": "s-item__shipping s-item__logisticsCost"}).text
        scraped_info_list.append(item_dict)
        connect.insert_in_table(dbname, tuple(item_dict.values()))


dataframe = pandas.DataFrame(scraped_info_list)
print("Creating csv file...")
dataframe.to_csv("Converse.csv")
connect.get_info(dbname)
