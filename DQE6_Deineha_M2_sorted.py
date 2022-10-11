from random import randint, choice
from string import ascii_lowercase
from collections import OrderedDict
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

final_dict, tmp_dict = {},  {}

# Modify the list of dicts into dict of lists.
for dictionary in dictList:
  for k, v in dictionary.items():
    tmp_dict.setdefault(k, []).append(v)

# Choose the max
for k, v in tmp_dict.items():
  if len(v) > 1:
    final_dict[k+"_"+str(v.index(max(v))+1)] = max(v)
  else: final_dict[k] = v[0]

sorted_dict = {i: final_dict[i] for i in sorted(final_dict.keys())}

print(dictList)
print(tmp_dict)
print(final_dict)
print(sorted_dict)
