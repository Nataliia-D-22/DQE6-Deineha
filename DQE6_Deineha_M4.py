# Task2
from random import randint, choice
from string import ascii_lowercase

import string
import random
from collections import defaultdict

dictList = []
for _ in range(random.randint(2,10)): #  number of dictionaries
    size = 4   #  dictionary size
    keys = random.sample(string.ascii_lowercase,size)  # random letters
    values = (random.randint(2,10) for _ in range(size)) # random numbers
    oneDict = dict(zip(keys,values))                      # assemble dict.
    dictList.append(oneDict)

    final_dict, tmp_dict = {}, {}

def dict_modify (final_dict):
# Modify the list of dicts into dict of lists.
    for dictionary in dictList:
      for k, v in dictionary.items():
        tmp_dict.setdefault(k, []).append(v)

    # Choose the max
    for k, v in tmp_dict.items():
      if len(v) > 1:
        final_dict[k+"_"+str(v.index(max(v))+1)] = max(v)
      else: final_dict[k] = v[0]
    return final_dict

final_dict = dict_modify (final_dict)

print(dictList)
print(final_dict)



#task 3

import re


# task 1
a = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

punct_signs = re.compile('([.!?]\s*)')
split_with_punct = punct_signs.split(a)

def task_1 (split_with_punct):

    task_1 = ''.join([i.capitalize() for i in split_with_punct])
    print('Task 1 result:', task_1)
    return task_1
task_1 (split_with_punct)


#task2
# Also, create one more sentence with last words of each existing sentence and add it to the end of this paragraph
# 	\S Returns a match where the string DOES NOT contain a white space character

end_words = '(\S*)[.]'
pre_Cond : string = task_1 (split_with_punct)
data = re.findall(end_words, pre_Cond)

def task_2 (data):
    string_2 = ' '.join (data)
    print('Task 2 result: ', a, '\n',string_2.capitalize())
    return task_2
task_2 (data)

#
# #task3
# # it iZ misspeLLing here.fix“iZ” with correct “ is ”, but ONLY when it Iz a mistAKE.

pre_Cond : string = task_1 (split_with_punct)

def task_3 (pre_Cond):

    task_3 = pre_Cond.replace (" iz ", " is ")

    print ('Task 3: ', task_3)

    return task_3
task_3 (pre_Cond)

# task4
# last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87
# count whitespaces using isspace method

def task_4 (a):
    space = 0
    for k in a:
        if(k.isspace()):
            space=space+1
    print ('Whitespaces total:', space)
    return task_4
task_4 (a)
