import unicodecsv as csv
import re

def removeKDecimal(matchedObject):
    return matchedObject.group(1) + matchedObject.group(3) + "00"

def removeK(matchedObject):
    return matchedObject.group(1) + "000"

def cleanseRow(row):
    thousandsDecimal = re.compile('([0-9]+)([.]+)([0-9])K')
    thousands = re.compile('([0-9]+)K')
    newRow = []
    for item in row:
        item = item.replace("[\'", "")
        item = item.replace("[\"", "")
        item = item.replace("\\xa0", "")
        item = re.sub(thousandsDecimal, removeKDecimal, item)
        item = re.sub(thousands, removeK, item)
        newRow.append(item)
    return newRow

def cleanseFile(inputFile):
    filetype = ".csv"
    outputFilename = inputFile + "_cleansed"
    with open(outputFilename + filetype, 'wb') as f:
        w = csv.writer(f, delimiter=',', escapechar=' ', quoting=csv.QUOTE_MINIMAL)
        with open(inputFile + filetype, "rb") as csvfile:
            csvreader = csv.reader(csvfile, encoding='utf-8-sig')
            for row in csvreader:
                newRow = cleanseRow(row)
                w.writerow(newRow)

cleanseFile("FFArchiveMerged")