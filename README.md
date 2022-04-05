# LUIS csv to json (for version import from gcp dialogflow)

>_important **use csv file as csv utf-8**_

## how to use?

<ol>
<li>create csv file</li>
<li>change the csv file path in luis_import.py</li>
<li>run the python code</li>
<li>enjoy the luis</li>
</ol>

## csv format


**intent**

|intent|utterances|
|:---:|:---:|
|greeting|how are you?|
|greeting|what's up?|

**list entity**

|parent_name|child_name|type|synonyms|||
|:---:|:---:|:---:|:---:|:---:|:---:|
|device|cell phone|synonyms|mobile|phone|smart phone|
|device|laptop|synonyms|portable computer|


types: synonyms(list entity)
(pattern(regex) will be updated soon)