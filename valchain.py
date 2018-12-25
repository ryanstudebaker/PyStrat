from wikipedia import wikipedia
import sys
import requests
import lxml
from lxml import etree
import beautifulsoup
from wikipedia.wikipedia import WikipediaPage

print('-------------------------------------')
print('|      Strategy Value Chain Tool     |')
print('-------------------------------------')
query = input("Company Search: ")
iters = int(20)
searchresult = wikipedia.search(query, 10)

resultlist = []
resultlist = searchresult
a = len(resultlist)

narrowlist = []

b = 0

print("Crawling for companies...")

for thing in resultlist:
    b = b + 1
    sys.stdout.write('\r')
    sys.stdout.write('%.0f%% complete' % (b / a * 100,))
    sys.stdout.flush()
    try:
        summary = wikipedia.summary(thing, 1)
        if summary.find('company'):
            narrowlist.append(thing)
        elif summary.find('corporation'):
            narrowlist.append(thing)
        else: continue
    except: continue

print('\n')
print(narrowlist)
print("Scoring search results...")

a = len(narrowlist)

dive = []
consolation = []

b = 0

for thing in narrowlist: #ranks based on likelihood of it being a company
    b = b + 1
    sys.stdout.write('\r')
    sys.stdout.write('%.0f%% complete' % (b / a * 100,))
    sys.stdout.flush()
    if thing.find('Inc.'):
        dive.append(thing)
    elif thing.find('Company'):
        dive.append(thing)
    elif thing.find('Corporation'):
        dive.append(thing)
    elif thing.find('Co.'):
        dive.append(thing)
    elif thing.find('Group'):
        dive.append(thing)
    else :
        consolation.append(thing)

print('\n')
print("Digging for company info...")

a = len(dive)
b = 0
c = []

for thing in dive:
    b = b + 1
    sys.stdout.write('\r')
    sys.stdout.write('%.0f%% complete' % (b / a * 100,))
    sys.stdout.flush()
    thing = str(thing)
    # manually storing desired URL
    url1 = wikipedia.page(thing)
    url2 = url1.url
    c.append(url2)
    req = requests.get(url2)
    store = etree.fromstring(req.text)
    output = store.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[11]')
    #print(output)

print('\n')
for thing in c:
    print(thing)

#'//*[@id="mw-content-text"]/div/table[1]/tbody/tr[17]/th'
#'//*[@id="mw-content-text"]/div/table[1]/tbody/tr[17]/td'
#'//*[@id="mw-content-text"]/div/table[1]/tbody/tr[11]/td/span/text()'
#//*[@id="mw-content-text"]/div/table[1]/tbody/tr[16]/td/span/text()
#type = str() #Public
#traded_as = str()
#traded_as_exchange = str() #NYSE, split at ':'
#traded_as_ticker = str() #EMN
#industry = str()
#revenue =
