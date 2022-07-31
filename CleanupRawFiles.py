import unicodecsv as csv
import re
from os.path import exists

def foundCommasInNumbers(matchedObject):
    return str(matchedObject.group(1) + matchedObject.group(3))

def processOneRecord(record):
    closeParenth = re.compile('\)')
    openParenth = re.compile(' \(')
    newLine = re.compile(r'\\n')
    commasNumbers = re.compile('([0-9]+)(,)([0-9]+)')
    foundCommaNumbers = re.search(commasNumbers, str(record))
    if foundCommaNumbers is not None:
        formattedNumbers = re.sub(commasNumbers, foundCommasInNumbers, str(record))
        commaRecord = re.sub(openParenth, '\",', str(formattedNumbers))
    else:
        commaRecord = re.sub(openParenth, '\",', str(record))
    cleanNewLineRecord = re.sub(newLine, '', commaRecord)
    addQuote = re.sub(closeParenth, ')', cleanNewLineRecord)
    splitRows = re.split(closeParenth, addQuote)
    return splitRows

# commasNumbers = re.compile('([0-9]+)(,)([0-9]+)')
#     foundCommaNumbers = re.search(commasNumbers, str(record) )
#     if foundCommaNumbers is not None:
#         formattedNumbers = re.sub(commasNumbers, foundCommaNumbers.group(1) + foundCommaNumbers.group(3), str(record))
#         commaRecord = re.sub(openParenth, formattedNumbers)

def extendRecord(records, stringToAdd):
    recordsFinal = []
    for record in records:
        record = record + ", " + stringToAdd
        recordsFinal.append(record)
    return recordsFinal

def writeFile(filename, folder):
    # filename = "FFArchive20200600000000"
    # folder = ""
    folder = folder + "/"
    filenameAdd = "_Processed"
    filetype = ".csv"
    year = filename[9:13]
    month = filename[13:15]
    category = filename.split("#")[1]
    foundRows = []
    fields = []

    with open(folder + filename + filetype, "rb") as csvfile:
        csvreader = csv.reader(csvfile, encoding='utf-8-sig')
        fields = next(csvreader)

        for row in csvreader:
            processedRows = processOneRecord(row)
            processedRowsYear = extendRecord(processedRows, year)
            processedRowsMonth = extendRecord(processedRowsYear, month)
            processedRowsCategory = extendRecord(processedRowsMonth, bigCategoryMap[category])
            foundRows = list(set(foundRows) | set(processedRowsCategory))

        with open(folder + filename + filenameAdd + filetype, 'wb') as f:
            w = csv.writer(f, delimiter=',', escapechar=' ', quoting=csv.QUOTE_MINIMAL)
            for singleRow in foundRows:
                w.writerow([singleRow])

monthList = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

bigCategoryList = ["201", "202", "203", "204", "205", "206", "207", "208",
                   "209", "210", "211", "212", "217", "329", "214", "314",
                   "919", "633", "250", "277", "216", "anime", "book", "cartoon",
                   "comic", "game", "misc", "movie", "play", "tv",
                   "crossoversanime", "crossoversbook", "crossoverscartoon",
                   "crossoverscomic", "crossoversgame", "crossoversmisc",
                   "crossoversmovie", "crossoversplay", "crossoverstv"]

bigCategoryMap = {"201": "anime", "202": "book", "203": "cartoon", "211": "misc",
                  "209": "game", "204": "comic", "205": "movie" , "208": "tv",
                  "206": "original", "210": "musicGroup", "207": "poetry",
                  "217": "originalFantasy", "329": "originalGeneral",
                  "214": "originalHaiku", "314": "originalHorror",
                  "919": "originalHumor", "633": "originalMystery",
                  "250": "originalPoetry", "277": "originalSong",
                  "216": "originalSciFi", "212": "screenplays",
                  "anime": "anime", "book": "book", "cartoon": "cartoon",
                  "comic": "comic", "game": "game", "misc": "misc",
                  "movie": "movie", "play": "play", "tv": "tv",
                  "crossoversanime": "xoverAnime", "crossoversbook": "xoverBook",
                  "crossoverscartoon": "xoverCartoon", "crossoverscomic": "xoverComic",
                  "crossoversgame": "xoverGame", "crossoversmisc": "xoverMisc",
                  "crossoversmovie": "xoverMovie", "crossoversplay": "xoverPlay",
                  "crossoverstv": "xoverTV"};

for y in range(2000, 2023):
    for m in monthList:
        for cat in bigCategoryList:
            pageNumber = str(y) + m + "00000000"
            filename = "FFArchive" + pageNumber + "#" + cat
            folder = "RawScrape073022"
            fileType = ".csv"
            fileExists = exists(folder + "/" + filename + fileType)
            if fileExists:
                writeFile(filename, folder)

                