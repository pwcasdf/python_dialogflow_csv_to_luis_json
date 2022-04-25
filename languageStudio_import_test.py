import csv
import json

testUtteranceCSV = 'capital_test_0425.csv'

testSet = []

def to_languageStudio_testUtterance(csvPath):
    with open(csvPath,'r',encoding = "utf-8-sig") as csvFile:
        csvReader = csv.DictReader(csvFile)
        
        for row in csvReader:
            dict = {}
            dict['intent'] = row['expected']
            dict['language'] = 'ko-kr'
            dict['text'] = row['question']
            dict['entities'] = []
        
            testSet.append(dict)

to_languageStudio_testUtterance(testUtteranceCSV)

with open('import_testSet_languageStudio.json','w', encoding = 'utf-8') as jsonf:
    jsonf.write(json.dumps(testSet, indent = 4, ensure_ascii=False))