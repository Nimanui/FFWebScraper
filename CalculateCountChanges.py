import unicodecsv as csv

# this function finds velocity for the 2nd column in the input file noted by this index
index = 1
monthInd = 3
yearInd = 2
inputFilename = ""
filetype = ".csv"


def findVelocity(row, previousCount, curVel):
    newRow = row.copy()
    if row[index].isdigit() is False or previousCount[index].isdigit() is False:
        return row
    elif row[index] == previousCount[index]:
        newRow[index] = curVel
        return row
    else:
        newRow[index] = str(int(row[index]) - int(previousCount[index]))
        return newRow


def findVelocityRaw(row, previousCount):
    newRow = row.copy()
    if row[index].isdigit() is False or previousCount[index].isdigit() is False:
        return newRow
    elif row[index] == previousCount[index]:
        return None
    else:
        newRow[index] = str(int(row[index]) - int(previousCount[index]))
        return newRow


def calculateAllVelocities(inputFile):
    outputFilename = inputFile + "_velocities"
    with open(outputFilename + filetype, 'wb') as f:
        w = csv.writer(f, delimiter=',', escapechar=' ', quoting=csv.QUOTE_MINIMAL)
        with open(inputFile + filetype, "rb") as csvfile:
            csvreader = csv.reader(csvfile, encoding='utf-8-sig')
            previousRow = ['0','0','0','0','0']
            rowStorage = []
            curVel = 0
            curRow = 0
            for row in csvreader:
                foundRow = findVelocity(row, previousRow, curVel)
                if foundRow[index] == previousRow[index]: #missing data?
                    rowStorage.append(foundRow)
                else:
                    curVel = int(foundRow[index])
                    if curRow == 0:
                        monthCount = 1
                    else:
                        monthCount = int(int(foundRow[monthInd]) - int(previousRow[monthInd]) + 12 * (int(foundRow[yearInd]) - int(previousRow[yearInd])))
                    previousRow = row.copy()
                    for adjustRow in rowStorage:
                        adjustRow[index] = str(curVel/monthCount)
                        w.writerow(adjustRow)
                    rowStorage = []
                    rowStorage.append(row)
                    curRow +=1


def calculateAllVelocitiesRaw(inputFile):
    outputFilename = inputFile + "_velocitiesRaw"
    with open(outputFilename + filetype, 'wb') as f:
        w = csv.writer(f, delimiter=',', escapechar=' ', quoting=csv.QUOTE_MINIMAL)
        with open(inputFile + filetype, "rb") as csvfile:
            csvreader = csv.reader(csvfile, encoding='utf-8-sig')
            previousRow = ['0','0','0','0','0']
            for row in csvreader:
                foundRow = findVelocityRaw(row, previousRow)
                if foundRow is not None:
                    w.writerow(foundRow)
                    previousRow = row



calculateAllVelocities("FFArchiveHarryPotter")
calculateAllVelocitiesRaw("FFArchiveHarryPotter")
