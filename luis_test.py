import csv
import json
import requests

testCSV = 'capital_test_0425.csv'

columnName = 'question'

endpointURL = '{endpoint}'
appID = '{app_id}'
apiType = '{slots_or_versions}' # slots or versions    @pwcasdf
apiTpye2 = '{slot_or_version_name}' # slot name or version name    @pwcasdf
key = '{key}'

def luis_predict(csvPath, endpointURL, appID, apiType, apiTpye2):
    predict_url = endpointURL + "luis/" + "prediction/" + "v3.0/" \
        + "apps/" + appID + "/" + apiType + "/" + apiTpye2 + "/" + "predict"

    dict_key = {}
    dict_key['Ocp-Apim-Subscription-Key'] = key

    i = 0

    with open(csvPath, 'r', encoding = "utf-8-sig") as csvFile:
        csvReader = csv.DictReader(csvFile)
        
        with open('test_result_luis.csv','w',newline='',encoding = 'utf-8-sig') as csvf:
            csvWriter = csv.writer(csvf)
            firstRow = ['utterances','predictedIntent','score']
            csvWriter.writerow(firstRow)

            for row in csvReader:

                dict_temp = {}
                csv_array = []

                utterance = row[columnName]
                dict_temp['query'] = utterance
                
                print('processing \"' + utterance + '\"')
                
                luis_response = requests.post(predict_url, data = dict_temp, headers = dict_key)

                dict_response = json.loads(luis_response.text)

                topIntent = dict_response['prediction']['topIntent']
                score = dict_response['prediction']['intents'][topIntent]['score']

                csv_array.append(utterance)
                csv_array.append(topIntent)
                csv_array.append(score)

                csvWriter.writerow(csv_array)

                i += 1
    
    print('work is done!!! total {} utterances!!'.format(i))


luis_predict(testCSV, endpointURL, appID, apiType, apiTpye2)