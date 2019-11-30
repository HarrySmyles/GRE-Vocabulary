# Harrison Kim
# This program finds all of the definitions of the words in a csv list and provides defintions for each
# output in a seperate txt file.  This utilizes the Oxford Dictionaries API to find definitions

__all__ = ['findDefinitions']

import csv


app_id = '' #Enter API ID
app_key = '' #Enter API Key
word_id = 'presage'
fields = 'definitions'
strictMatch = 'false'


def findDefinitions():
    with open('GMAT Vocabulary Words.txt', mode='r') as in_f:
        contents = csv.reader(in_f, delimiter="\t")
        list_contents = list(contents)
        words = []
        for index in range(0, len(list_contents)):
            words.append(list_contents[index][0])

        print(words)
        with open('Words with Definitions.txt', mode='w') as out_f:
            #defined_list = csv.writer(out_f, delimiter='', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for i in words:
                out_f.write(i)
                out_f.write('\n')


findDefinitions()