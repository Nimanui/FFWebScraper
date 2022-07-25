import unicodecsv as csv
import re

def processOneRecord(record):
    closeParenth = re.compile('\)')
    openParenth = re.compile(' \(')
    newLine = re.compile(r'\\n')
    commasNumbers = re.compile('([0-9]+)(,)([0-9]+)')
    foundCommaNumbers = re.search(commasNumbers, str(record))
    if foundCommaNumbers is not None:
        formattedNumbers = re.sub(commasNumbers, str(foundCommaNumbers.group(1) + foundCommaNumbers.group(3)), str(record))
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
        record = record + "," + stringToAdd
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
    foundRows = []
    fields = []

    with open(folder + filename + filetype, "rb") as csvfile:
        csvreader = csv.reader(csvfile, encoding='utf-8-sig')
        fields = next(csvreader)

        for row in csvreader:
            processedRows = processOneRecord(row)
            processedRowsYear = extendRecord(processedRows, year)
            processedRowsMonth = extendRecord(processedRowsYear, month)
            foundRows = list(set(foundRows) | set(processedRowsMonth))

        with open(folder + filename + filenameAdd + filetype, 'wb') as f:
            w = csv.writer(f, delimiter=',', escapechar=' ', quoting=csv.QUOTE_MINIMAL)
            for singleRow in foundRows:
                w.writerow([singleRow])

monthList = ["01","02","03","04","05","06","07","08","09","10","11","12"]
for y in range(2000,2023):
    for m in monthList:
        pageNumber = str(y) + m + "00000000"
        filename = "FFArchive" + pageNumber
        folder = "RawExtracts"
        writeFile(filename, folder)
