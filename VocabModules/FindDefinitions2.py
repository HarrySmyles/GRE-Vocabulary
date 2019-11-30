# Harrison Kim
# This program finds all of the definitions of the words in a csv list and provides defintions for each
# output in a seperate txt file.  This utilizes the Oxford Dictionaries API to find definitions

__all__ = ['findDefinitions']

import csv
import urllib3
import requests
import json
import concurrent.futures

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
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_def = [executor.submit(getDefinitions, list_contents[i], app_id, app_key)
                         for i in range(0, len(list_contents)-1)]
            definitions = [future.result() for future in
                           concurrent.futures.as_completed(future_def)]

#To Do: Create a class that is defined by a word and its definition so that words and definitions can be grouped together after multithreading

        #for index in range(0, len(list_contents)):
        #    words.append(list_contents[index][0])
        #    word_id = words[index]

                
        with open('Words with Definitions.txt', mode='w') as out_f:
            #defined_list = csv.writer(out_f, delimiter='', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in words:
                out_f.write(i + '\t' + definitions[i] + '\n')
        #for i in range(0, len(list_contents)):
        #    print(words[i], ":  ", definitions[i])
        #f = open('Words With Definitions.txt', 'w')
        #for i in range(0, len(list(contents))):
        #    f.write(words[i], ':  ', definitions[i])
        #f.close()
        """
        with open('Words with Definitions.txt', mode='wb') as out_f:
            defined_list = csv.writer(out_f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(0, len(list(contents))):
                defined_list.writerow(words[i], definitions[i])
                """


def getDefinitions(word_id, app_id, app_key):
    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/en-us/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch
    r = requests.get(url, headers={'Accept': 'application/json',
                                   'app_id': app_id,
                                   'app_key': app_key})
    print(r)
    if str(r) == '<Response [200]>':
        r = requests.get(url, headers={'Accept': 'application/json',
                                       'app_id': app_id,
                                       'app_key': app_key})
        try:
            data = r.json()
            return (word_id, data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
        except:
            return (word_id, 'No Definition Found')
    if str(r) == '<Response [403]>':
        return (word_id, "Failure to Retrieve Definition from Oxford Dictionaries")
    else:
        return (word_id, 'No Definition Found')

def loadWithThread():
    with concurrent.futures.ThreadPoolExecutor(10) as executor:
        future_db = [executor.submit(findDefinitions, i, people_db_file) for i in range(max_people)]
        person_list = [future.result() for future in concurrent.futures.as_completed(future_db)]
    person_list.sort(key=lambda row:(row[2], row[1]))  #Sorting the list by last name, first name
    print(person_list)