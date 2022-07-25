import unicodecsv as csv
import re

filenameAdd = "_Processed"
filetype = ".csv"
folder = "RawExtracts"
finalFilename = "FFArchiveMerged.csv"
monthList = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

with open(finalFilename, 'wb') as f:
    w = csv.writer(f, delimiter=',', escapechar=' ', quoting=csv.QUOTE_MINIMAL)
    for y in range(2000,2023):
        for m in monthList:
            pageNumber = str(y) + m + "00000000"
            filename = "FFArchive" + pageNumber + "_Processed"
            with open(folder + "/" + filename + filetype, "rb") as csvfile:
                csvreader = csv.reader(csvfile, encoding='utf-8-sig')
                for row in csvreader:
                    w.writerow(row)



