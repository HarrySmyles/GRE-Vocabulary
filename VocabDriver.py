# Harrison Kim
# This program finds all of the definitions of the words in a csv list and provides defintions for each
# output in a seperate txt file.  This utilizes the Oxford Dictionaries API to find definitions

from VocabModules import *

choice = input("Please provide an option.\n1. Find definitions of words in a list.\n2. Scramble words and take a multiple choice vocab quiz\nInput: ")

if choice == '1':
    app_id = input('Please provide an API ID for Oxford Dictionaries')
    app_key = input('Please provide the API key')


    #file = input('Please provide the txt/csv file with the list of words')
    file = 'Words.txt'
    FindDefinitions.findDefinitions(app_id, app_key, file)

elif choice == '2':
    WordTest.wordTest()
