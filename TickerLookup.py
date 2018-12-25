import requests
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

co = str(input('Company Search:  '))
co = co.replace(" ","+")
co = co.replace("&","%26")

url = 'https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup='+co+'&Country=All&Type=All'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup.findAll("tr")
for thing in tags:
    table = thing.findAll("td", {"class":"bottomborder"})
    thingst = str(thing)
    #if thingst.find('<td class="bottomborder"><'):
    #    print(thingst)

forticker = str(tags[1])
forticker = forticker.rstrip()
forticker = forticker.split('\n')

forticker1 = str(forticker[1])

#print(forticker)

newurl = forticker1.split(">")

url = str(newurl[1].split("="""))
url1 = url.split(" ")
url2 = str(url1[2])
financials = str('https://www.marketwatch.com'+str(url2[2:len(url2)-1]) + '/financials')

exchange = str(forticker[3])
exchange1 = exchange[1:]
exchange2 = exchange1.split('<')
exchange3 = str(exchange2[0])
exchange4 = exchange3.split('>')
exchange5 = str(exchange4[1])

exchange = exchange5

tick = str(financials.split('/')[5])

print('Ticker      ',tick.upper())
print('Exchange    ',exchange)
print('Financials  ',financials)
