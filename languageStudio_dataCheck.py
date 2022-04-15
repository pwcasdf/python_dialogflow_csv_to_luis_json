import csv
import json

intentCSV = 'capital_tagging.csv'

entity_list = ['address_qna', \
                'car_installment_qna', \
                'certificate_delinquency', \
                'certificate_deposit', \
                'certificate_financial_dealings', \
                'certificate_full_payment', \
                'certificate_loan_termination', \
                'channel', \
                'credit_mortgage_qna', \
                'delinquency_sharing_qna', \
                'issued_documents', \
                'lease_qna', \
                'loan_amount', \
                'mobile_number_qna', \
                'mortgage_qna', \
                'mortgage_setting', \
                'mortgage_termination_qna', \
                'mpoint_qna', \
                'non-consult', \
                'partial_repayment', \
                'partial_repayment_amount', \
                'payment_account', \
                'payment_amount', \
                'payment_date', \
                'payment_option_immediate', \
                'payment_option_virtual', \
                'remaining_amount', \
                'remaining_period', \
                'rent_qna', \
                'repayment', \
                'repayment_amount', \
                'statement_qna', \
                'total_repayment', \
                'total_repayment_amount', \
                'unpaid_amount']


def to_languageStudio_tagging(csvPath):
    with open(csvPath,'r',encoding = "utf-8-sig") as csvFile:
        csvReader = csv.DictReader(csvFile)

        i = 2
        for row in csvReader:
            
            intent = row['intent'].strip()
            utterance = row['utterance'].strip()
            entity = row['entity'].strip()

            tag_list = entity.split('#')

            if entity != '':
                for tag_row in tag_list:
                    tag_list2 = tag_row.split('@')
                    tag_words, tag_entityName = tag_list2[0].strip(), tag_list2[1].strip()
                    
                    try:
                        tag_index = utterance.index(tag_words)
                    except:
                        print('tag not matched: {}'.format(i))
                    
                    j = 0
                    for list_item in entity_list:
                        if tag_entityName == list_item:
                            j += 1
                    
                    if j == 0:
                        print('entity name is wrong: {}'.format(i))
            
            i += 1

            #test = row['entity'].split("#")
            #print(test)

            #print("@@@@@@@@@@@@@@@@@@")
            #test2 = test[0].split("@")
            #print(test2)

            #test3 = row['utterance']

            #p = test3.index(test2[0])

            #print(test3)
            #print(test2[0])
            #print(len(test2[0]))
            #print(p)

            # strip to remove spaces at the first char end the last
            #a = "aa aa "
            #c = a.strip()
            #b = " bbbb"
            #d = b.strip()

            #print(c+d)

to_languageStudio_tagging(intentCSV)
