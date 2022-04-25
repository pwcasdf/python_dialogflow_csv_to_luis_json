import csv
import json

intentCSV = 'capital_intent_tagging_0411.csv'
entityCSV = 'capital_entity_0411.csv'

dict = {
    "api-version": "2022-03-01-preview",
    "stringIndexType": "Utf16CodeUnit",
    "metadata": {
        "projectKind": "conversation",
        "settings": {
            "confidenceThreshold": 0
        },
        "projectName": "capital_clu",
        "multilingual": 0,
        "description": "",
        "language": "ko"
    },
    "assets": {
        "intents": [],
        "entities": [],
        "utterances": []
    }
}

def to_languageStudio_intent(csvPath):
    with open(csvPath,'r',encoding = "utf-8-sig") as csvFile:
        csvReader = csv.DictReader(csvFile)
        
        for row in csvReader:
            dict_temp = {}

            # for the 1st entity    @pwcasdf
            if len(dict['assets']['intents']) == 0:
                dict_temp['category'] = row['intent']
                dict['assets']['intents'].append(dict_temp)
            else:
                # flag for checking duplicated entity name    @pwcasdf
                flag = 0
                # for duplicated entities    @pwcasdf
                for x in range(len(dict['assets']['intents'])):
                    if dict['assets']['intents'][x]['category'] == row['intent']:
                        flag = 1
                        break
                
                # for not duplicated entities    @pwcasdf
                if flag == 0:
                    dict_temp['category'] = row['intent']
                    dict['assets']['intents'].append(dict_temp)


def to_languageStudio_entity(csvPath):
    with open(csvPath,'r',encoding = "utf-8-sig") as csvFile:
        csvReader = csv.reader(csvFile)

        # when the entity type is list    @pwcasdf
        for row in csvReader:
            if row[2] == 'synonyms':
                dict_temp = {
                                'category': row[0],
                                'compositionSetting': 'returnLongestOverlap',
                                'list': {
                                    'sublists': [
                                        {
                                            'listKey': row[1]
                                        }
                                    ]
                                }
                            }

                dict_temp2 = {        
                                'language': 'ko',
                                'values': []
                            }

                dict_temp3 = {
                                'listKey': row[1],
                                'synonyms': [
                                    {        
                                        'language': 'ko',
                                        'values': []
                                    }
                                ]
                            }
                
                # for the 1st entity    @pwcasdf
                if len(dict['assets']['entities']) == 0:
                    if row[3] != '':
                        for param in row[3:]:
                            if param != '':
                                dict_temp2['values'].append(param)
                        dict_temp['list']['sublists'][0]['synonyms'] = [dict_temp2]
                    dict['assets']['entities'].append(dict_temp)
                else:
                    # flag for checking duplicated entity name    @pwcasdf
                    flag = 0
                    # for duplicated entities    @pwcasdf
                    for x in range(len(dict['assets']['entities'])):
                        if dict['assets']['entities'][x]['category'] == row[0]:
                            for param in row[3:]:
                                if param != '':
                                    dict_temp3['synonyms'][0]['values'].append(param)
                            dict['assets']['entities'][x]['list']['sublists'].append(dict_temp3)
                            flag = 1

                    # for not duplicated entities    @pwcasdf
                    if flag == 0:
                        if row[3] != '':
                            for param in row[3:]:
                                if param != '':
                                    dict_temp2['values'].append(param)
                            dict_temp['list']['sublists'][0]['synonyms'] = [dict_temp2]
                        dict['assets']['entities'].append(dict_temp)


def to_languageStudio_utterance(csvPath):
    with open(csvPath,'r',encoding = "utf-8-sig") as csvFile:
        csvReader = csv.DictReader(csvFile)

        for row in csvReader:
            dict_temp = {
                            'text': row['utterance'],
                            'language': "ko",
                            'intent': row['intent'],
                            'entities': []
                        }

            entity_split = row['entity'].split("#")
            
            if row['entity'] != '':
                for i in range(len(entity_split)):
                    dict_temp2 = {}

                    entity_split2 = entity_split[i].split("@")

                    dict_temp2['category'] = entity_split2[1].strip()
                    dict_temp2['offset'] = row['utterance'].index(entity_split2[0].strip())
                    dict_temp2['length'] = len(entity_split2[0].strip())

                    dict_temp['entities'].append(dict_temp2)
            
            dict['assets']['utterances'].append(dict_temp)


to_languageStudio_intent(intentCSV)
to_languageStudio_utterance(intentCSV)
to_languageStudio_entity(entityCSV)

with open('import_result_languageStudio.json','w', encoding = 'utf-8') as jsonf:
    jsonf.write(json.dumps(dict, indent = 4, ensure_ascii=False))
