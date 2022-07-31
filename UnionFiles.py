import unicodecsv as csv
from os.path import exists

filenameAdd = "_Processed"
filetype = ".csv"
folder = "RawScrape073022"
finalFilename = "FFArchiveMerged.csv"
finalFilenameCross = "FFArchiveMergedCrossover.csv"
monthList = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
primeCategory = ["211", "tv"]
crossCategoryList = ["crossoverstv"]
bigCategoryList = ["201", "202", "203", "204", "205", "206", "207", "208",
                   "209", "210", "211", "212", "217", "329", "214", "314",
                   "919", "633", "250", "277", "216", "anime", "book", "cartoon",
                   "comic", "game", "misc", "movie", "play", "tv"]
crossCategoryList = ["crossoversanime", "crossoversbook", "crossoverscartoon",
                   "crossoverscomic", "crossoversgame", "crossoversmisc",
                   "crossoversmovie", "crossoversplay", "crossoverstv"]

with open(finalFilename, 'wb') as f:
    w = csv.writer(f, delimiter=',', escapechar=' ', quoting=csv.QUOTE_MINIMAL)
    for y in range(2000,2023):
        for m in monthList:
            for cat in primeCategory:
                pageNumber = str(y) + m + "00000000"
                filename = "FFArchive" + pageNumber + "#" + cat + "_Processed"
                fileExists = exists(folder + "/" + filename + filetype)
                if fileExists:
                    with open(folder + "/" + filename + filetype, "rb") as csvfile:
                        csvreader = csv.reader(csvfile, encoding='utf-8-sig')
                        for row in csvreader:
                            w.writerow(row)



