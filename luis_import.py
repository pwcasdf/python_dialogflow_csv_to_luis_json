import csv
import json

intentCSV = 'capital_intent_0411.csv'
entityCSV = 'capital_entity_0411.csv'

dict = {
    "luis_schema_version": "7.0.0",
    "intents": [],
    "entities": [],
    "hierarchicals": [],
    "composites": [],
    "closedLists": [],
    "prebuiltEntities": [],
    "utterances": [],
    "versionId": "0.0.1",
    "name": "capital_luis",
    "desc": "",
    "culture": "ko-kr",
    "tokenizerVersion": "1.0.0",
    "patternAnyEntities": [],
    "regex_entities": [],
    "phraselists": [],
    "regex_features": [],
    "patterns": [],
    "settings": []
}

# coginsight intent to luis intent    @pwcasdf
def to_luis_intent(csvPath):
    with open(csvPath,'r',encoding = "utf-8-sig") as csvFile:
        csvReader = csv.DictReader(csvFile) 
        
        for row in csvReader:
            dict_temp = {}

            # for the 1st entity    @pwcasdf
            if len(dict['intents']) == 0:
                dict_temp['name'] = row['intent']
                dict_temp['features'] = []
                dict['intents'].append(dict_temp)
            else:
                # flag for checking duplicated entity name    @pwcasdf
                flag = 0
                # for duplicated entities    @pwcasdf
                for x in range(len(dict['intents'])):
                    if dict['intents'][x]['name'] == row['intent']:
                        flag = 1
                        break
                
                # for not duplicated entities    @pwcasdf
                if flag == 0:
                    dict_temp['name'] = row['intent']
                    dict_temp['features'] = []
                    dict['intents'].append(dict_temp)

# coginsight example to luis utterance    @pwcasdf
def to_luis_utterance(csvPath):
    with open(csvPath,'r',encoding = "utf-8-sig") as csvFile:
        csvReader = csv.DictReader(csvFile)

        for row in csvReader:
            dict_temp = {
                            'text': row['example'],
                            'intent': row['intent'],
                            'entities': []
                        }
            dict['utterances'].append(dict_temp)


# coginsight entity to luis entity    @pwcasdf
def to_luis_entity(csvPath):
    with open(csvPath,'r',encoding = "utf-8-sig") as csvFile:
        csvReader = csv.reader(csvFile)

        # when the entity type is list    @pwcasdf
        for row in csvReader:
            if row[2] == 'synonyms':
                dict_temp = {
                                'name': row[0],
                                'subLists': [
                                    {
                                        'canonicalForm': row[1],
                                        'list': []
                                    }
                                ]
                            }
                
                dict_temp2 = {
                                'canonicalForm': row[1],
                                'list': []
                            }
                
                # for the 1st entity    @pwcasdf
                if len(dict['closedLists']) == 0:
                    for param in row[3:]:
                        if param != '':
                            dict_temp['subLists'][0]['list'].append(param)
                    dict['closedLists'].append(dict_temp)
                else:
                    # flag for checking duplicated entity name    @pwcasdf
                    flag = 0
                    # for duplicated entities    @pwcasdf
                    for x in range(len(dict['closedLists'])):
                        if dict['closedLists'][x]['name'] == row[0]:
                            for param in row[3:]:
                                if param != '':
                                    dict_temp2['list'].append(param)
                            dict['closedLists'][x]['subLists'].append(dict_temp2)
                            flag = 1

                    # for not duplicated entities    @pwcasdf
                    if flag == 0:
                        for param in row[3:]:
                            if param != '':
                                dict_temp['subLists'][0]['list'].append(param)
                        dict['closedLists'].append(dict_temp)
                
                
to_luis_intent(intentCSV)
to_luis_utterance(intentCSV)
to_luis_entity(entityCSV)

with open('import_result_luis.json','w', encoding = 'utf-8') as jsonf:
    jsonf.write(json.dumps(dict, indent = 4, ensure_ascii=False))

