import unicodecsv as csv

def extractFandom(inputFile, fandom):
    filetype = ".csv"
    outputFilename = "FFArchive" + fandom
    with open(outputFilename + filetype, 'wb') as f:
        w = csv.writer(f, delimiter=',', escapechar=' ', quoting=csv.QUOTE_MINIMAL)
        with open(inputFile + filetype, "rb") as csvfile:
            csvreader = csv.reader(csvfile, encoding='utf-8-sig')
            for row in csvreader:
                for item in row:
                    if fandom in item:
                        w.writerow(row)


fandoms = ["Supernatural", "Avatar: Last Airbender", "Naruto", "Wrestling", "Twilight", "Star Wars", "Pokémon", "Pokemon", "NCIS", "Harry Potter", "My Little Pony"]
for fandom in fandoms:
    extractFandom("FFArchiveMerged_cleansed", fandom)
