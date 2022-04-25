# LUIS csv to json (for version import from gcp dialogflow)

>_important **use csv file as csv utf-8**_

## how to use?

<ol>
<li>create csv file</li>
<li>change the csv file path in luis_import.py</li>
<li>run the python code</li>
<li>enjoy the luis</li>
</ol>

## luis_import.py csv format


**intent**

|intent|utterance|
|:---:|:---:|
|greeting|how are you?|
|greeting|what's up?|

**list entity**

|parent_name|child_name|type|synonyms|||
|:---:|:---:|:---:|:---:|:---:|:---:|
|device|cell phone|synonyms|mobile|phone|smart phone|
|device|laptop|synonyms|portable computer|


## languageStudio_import.py csv format


**intent**

|intent|utterance|entity|
|:---:|:---:|:---:|
|greeting|hey you, how are you?|how are you@entity_name|
|greeting|hey you, what's up?|what's up@entity_name|
|aks_for_meal|do you want some snacks?|snack@food|
|...|...|...|

**list entity**

|parent_name|child_name|type|synonyms|||
|:---:|:---:|:---:|:---:|:---:|:---:|
|device|cell phone|synonyms|mobile|phone|smart phone|
|device|laptop|synonyms|portable computer|
|...|...|...|...|

types: synonyms(list entity)

## test csv format

|question|
|:---:|
|1st utterance|
|2nd utterance|
|...|