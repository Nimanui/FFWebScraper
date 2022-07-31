import requests
from bs4 import BeautifulSoup as bs
import unicodecsv as csv
import re

#r = requests.get("https://web.archive.org/web/19990508063956/http://www.fanfiction.net:80/text/browse-listcategories.cfm")
#r = requests.get("https://web.archive.org/web/"+ pageNumber + "/http://www.fanfiction.net/master.cfm?action=story-categories&categoryID=20" + str(i))
# if i == 3:
#     r = requests.get(
#         "https://web.archive.org/web/" + pageNumber + "/http://www.fanfiction.net/sections/cartoons/index.fic?action=story-categories&categoryID=20" + str(
#             i))
# el
# cat/ 2004 - 2006
# "" 2007 - 2022
# index.fic?action=story-categories&categoryID= 1999-2000
# master.cfm?action=story-categories&categoryID= 2000-2001
# subcats.php?categoryid= 2002 - 2004
pageNumber = "20010516200302"
month = "May"
year = "2001"
folder = "Raw2ndScrape073022/"

found = False
def findPage(baseURL, bigCategory):
    urlMidList = [""]
    # , "cat/", "subcats.php?categoryid=", "index.fic?action=story-categories&categoryID="]
    for urlMid in urlMidList:
        r = requests.get(baseURL + urlMid + str(bigCategory))
        if r.status_code == 200:
            return r

def scrapeFFNetOld(baseURL, pageNumber, bigCategoryList):
    number = re.compile('\([0-9k]')
    categoriesList = []
    for i in bigCategoryList:
        r = findPage(baseURL, i)

        if r is not None:
            soup = bs(r.content, 'html.parser')

            for font in soup.find_all('td'):
               if(number.search(font.text) != None):
                  categoriesList.append({"text": font.text})

                  filename = folder + "FFArchive" + str(pageNumber) + "#" + i.replace("/", "") + ".csv"
                  with open(filename, 'wb') as f:
                      w = csv.DictWriter(f, ['text'], encoding='utf-8-sig')
                      w.writeheader()

                      w.writerows(categoriesList)

            # for font in soup.find_all('td'):
            #     if(number.search(font.text) != None):
            #         categoriesList.append({"text": font.text})




monthList = ["01","02","03","04","05","06","07","08","09","10","11","12"]
bigCategoryList1 = ["201","202","203","204","205","206","207","208",
                   "209","210","211","212","217","329","214","314",
                   "919","633","250","277","216"]
bigCategoryList2 = ["anime/","book/","cartoon/",
                   "comic/","game/","misc/","movie/","play/","tv/",
                   "crossovers/anime/","crossovers/book/","crossovers/cartoon/",
                   "crossovers/comic/","crossovers/game/","crossovers/misc/",
                   "crossovers/movie/","crossovers/play/","crossovers/tv/"]

for y in range(2022,2023):
    for m in monthList:
        pageNumber = str(y) + m + "00000000"
        r = requests.get("https://web.archive.org/web/" + pageNumber + "/http://fanfiction.net/")
        if r.status_code == 200:
            found = True
            print(pageNumber)
            scrapeFFNetOld(r.url, pageNumber, bigCategoryList2)

# s = soup.find_all('table')
# s2 = soup.find('table')
# print(s2)
# content = s2.find('font')
# print(content)