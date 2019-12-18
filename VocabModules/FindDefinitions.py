# Harrison Kim
# This program finds all of the definitions of the words in a csv list and provides defintions for each
# output in a seperate txt file.  This utilizes the Oxford Dictionaries API to find definitions

__all__ = ['findDefinitions']

import csv
import urllib3
import requests
import json
import concurrent.futures

fields = 'definitions'
strictMatch = 'false'


#request from API definitions for word
def findDefinition(input):
    app_id = input[0]
    app_key = input[1]
    word = input[2]
    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/en-us/' + word.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch
    r = requests.get(url, headers={'Accept': 'application/json',
                                   'app_id': app_id,
                                   'app_key': app_key})
    print("Retrieving Definition: ", word)
    if str(r) == '<Response [200]>':
        r = requests.get(url, headers={'Accept': 'application/json',
                                       'app_id': app_id,
                                       'app_key': app_key})
        try:
            data = r.json()
            definition = data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
            print("Retrieved Definition: ", word)
        except:
            definition = 'No Definition Found'

    elif str(r) == '<Response [403]>':
        print("Failure to Retrieve Definition from Oxford Dictionaries")
    else:
        definition = 'No Definition Found'
    return definition

#write the words with definitions to a new file
def writeDefinitions(words, definitions):
    with open('Words with Definitions.txt', mode='w', newline='') as out_f:
        defined_list = csv.writer(out_f, delimiter='\t', quotechar='|')
        for i in range(0, len(words)):
            defined_list.writerow([words[i], definitions[i]])

#pass API ID and Key to retreive definitions through threading
def findDefinitions(app_id, app_key, file):
    with open(file) as in_f:
        contents = csv.reader(in_f, delimiter="\t")
        list_contents = list(contents)
        words = []
        package = []
        definitions = []
        for i in list_contents:
            words.append(i[0])
            package.append([app_id, app_key, i[0]])
        with concurrent.futures.ThreadPoolExecutor(10) as executor:
            future_defs = executor.map(findDefinition, package)
            for future in future_defs:
                definitions.append(str(future))
        writeDefinitions(words, definitions)

