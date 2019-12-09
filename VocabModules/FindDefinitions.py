# Harrison Kim
# This program finds all of the definitions of the words in a csv list and provides defintions for each
# output in a seperate txt file.  This utilizes the Oxford Dictionaries API to find definitions

__all__ = ['findDefinitions']

import csv
import urllib3
import requests
import json
import multiprocessing
from time import sleep
import queue as q

app_id = '' #Enter API ID
app_key = '' #Enter API Key
word_id = 'presage'
fields = 'definitions'
strictMatch = 'false'


def findDefinitions(app_id, app_key, file):
    with open(file) as in_f:
        contents = csv.reader(in_f, delimiter="\t")
        list_contents = list(contents)
        words = []
        definitions = []
        for index in range(0, len(list_contents)):
            words.append(list_contents[index][0])
            word_id = words[index]
            url = 'https://od-api.oxforddictionaries.com/api/v2/entries/en-us/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch
            r = requests.get(url, headers={'Accept': 'application/json',
                                           'app_id': app_id,
                                           'app_key': app_key})
            print("Retrieving Definition: ", words[index])
            if str(r) == '<Response [200]>':
                r = requests.get(url, headers={'Accept': 'application/json',
                                               'app_id': app_id,
                                               'app_key': app_key})
                try:
                    data = r.json()
                    definitions.append(data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
                    print("Retrieved Definition: ", words[index])
                except:
                    definitions.append('No Definition Found')
            elif str(r) == '<Response [403]>':
                print("Failure to Retrieve Definition from Oxford Dictionaries")
            else:
                definitions.append('No Definition Found')

    writeDefinitions(words, definitions)

def writeDefinitions(words, definitions):
    with open('Words with Definitions.txt', mode='w', newline='') as out_f:
        defined_list = csv.writer(out_f, delimiter='\t', quotechar='|')
        for i in range(0, len(words)):
            defined_list.writerow([words[i], definitions[i]])

