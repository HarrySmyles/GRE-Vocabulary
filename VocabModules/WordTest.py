#Harrison Kim
#This program will scramble the GRE words in a list with definitions (tab delimited)
# and provide multiple choice questions for each word.

__all__ = ['wordTest']

import csv
import random


def wordTest():
    with open('Words with Definitions.txt') as in_f:
        contents = csv.reader(in_f, delimiter="\t")
        list_contents = list(contents)
        rand_index = [i for i in range(len(list_contents))]
        random.shuffle(rand_index)
        words = []
        definitions = []
        for index in range(0, len(list_contents)):
            words.append(list_contents[index][0])
            definitions.append(list_contents[index][1])

        for x in rand_index:
            definition = [0, 0, 0, 0]
            check_diff = 5
            while check_diff > 4:
                check_diff = 0
                for index in range(len(list_contents)):
                    if definitions[x] == list_contents[index][1]:
                        definition[0] = list_contents[index][1]
                definition[1] = definitions[
                    random.randint(0, (len(definitions) - 1))]
                definition[2] = definitions[
                    random.randint(0, len(list_contents) - 1)]
                definition[3] = definitions[
                    random.randint(0, len(list_contents) - 1)]
                for i in range(4):
                    if definition[i] == definition[0]:
                        check_diff += 1
                    if definition[i] == definition[1]:
                        check_diff += 1
                    if definition[i] == definition[2]:
                        check_diff += 1
                    if definition[i] == definition[3]:
                        check_diff += 1
                shuffle_index = [0, 1, 2, 3]
                random.shuffle(shuffle_index)
            answer = input("{}:\n1. {}\n2. {}\n3. {}\n4. {}\n".format(words[x],
                                                                      definition[
                                                                          shuffle_index[
                                                                              0]],
                                                                      definition[
                                                                          shuffle_index[
                                                                              1]],
                                                                      definition[
                                                                          shuffle_index[
                                                                              2]],
                                                                      definition[
                                                                          shuffle_index[
                                                                              3]]))
            if shuffle_index[int(answer) - 1] == 0:
                print("\nCorrect!\n")
            else:
                print("\nIncorrect! The Correct Answer is: ", definition[0], "\n")
