import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

## url comes next
my_url = 'http://www.sec.gov/Archives/edgar/data/1278752/0001278752-17-000030.txt'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.find("results")

print(containers)