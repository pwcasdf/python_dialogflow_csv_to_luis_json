import csv
import json
import requests

testCSV = 'capital_test_0425.csv'

columnName = 'question'

endpointURL = '{endpoint}'
projectName = '{project_name}'
deploymentName = '{deployment_name}'
key = '{key}'

def luis_predict(csvPath, endpointURL, projectName, deploymentName):
    predict_url = endpointURL + "language/:analyze-conversations?api-version=2021-11-01-preview" \
        + "&projectName=" + projectName + "&deploymentName=" + deploymentName

    dict_header = {}
    dict_header['Ocp-Apim-Subscription-Key'] = key
    dict_header['Content-Type'] = 'application/json'

    i = 0

    with open(csvPath, 'r', encoding = "utf-8-sig") as csvFile:
        csvReader = csv.DictReader(csvFile)
        
        with open('test_result_languageStudio.csv','w',newline='',encoding = 'utf-8-sig') as csvf:
            csvWriter = csv.writer(csvf)
            firstRow = ['utterances','predictedIntent','score']
            csvWriter.writerow(firstRow)

            for row in csvReader:

                dict_temp = {}
                csv_array = []

                utterance = row[columnName]
                dict_temp['query'] = utterance

                print('processing \"' + utterance + '\"')

                body = "{\"query\":\"" + utterance + "\"}"

                luis_response = requests.post(predict_url, data = body.encode('utf-8'), headers = dict_header)

                dict_response = json.loads(luis_response.text)

                topIntent = dict_response['prediction']['topIntent']
                score = dict_response['prediction']['intents'][0]['confidenceScore']

                csv_array.append(utterance)
                csv_array.append(topIntent)
                csv_array.append(score)

                csvWriter.writerow(csv_array)

                i += 1
   
    print('work is done!!! total {} utterances!!'.format(i))


luis_predict(testCSV, endpointURL, projectName, deploymentName)