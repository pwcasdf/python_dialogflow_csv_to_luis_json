import csv
import json
import requests

testCSV = 'capital_test.csv'

columnName = 'question'

endpointURL = 'endpoint'
appID = 'app_id'
apiType = 'slots or versions' # slots or versions    @pwcasdf
apiTpye2 = 'production or version no' # slot name or version name    @pwcasdf
key = 'luis_key'

def luis_predict(csvPath, endpointURL, appID, apiType, apiTpye2):
    predict_url = endpointURL + "luis/" + "prediction/" + "v3.0/" \
        + "apps/" + appID + "/" + apiType + "/" + apiTpye2 + "/" + "predict"

    dict_key = {}
    dict_key['Ocp-Apim-Subscription-Key'] = key

    i = 0

    with open(csvPath, 'r', encoding = "utf-8-sig") as csvFile:
        csvReader = csv.DictReader(csvFile)
        
        with open('test_result.csv','w',newline='',encoding = 'utf-8-sig') as csvf:
            csvWriter = csv.writer(csvf)
            firstRow = ['utterances','predictedIntent','score']
            csvWriter.writerow(firstRow)

            for row in csvReader:

                dict_temp = {}
                csv_array = []

                utterance = row[columnName]
                dict_temp['query'] = utterance

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