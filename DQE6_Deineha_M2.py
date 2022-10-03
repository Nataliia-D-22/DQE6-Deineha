# Task1
# create a list of random number of dicts (from 2 to 10)

import copy
import itertools


dict1 = {'a': 2, 'b': 55, 'd': 67,  'j': 10}
dict2 = {'b': 72, 'd': 67, 'k': 10, 'p': 35}
dict3 = {'d': 67, 'k': 19, 's': 56, 'q': 78}


def main():
    dict1 = dict (a=[2], b=[55], d=[67], j=[10])
    dict2 = dict (b=[72], d=[67], k=[10], p=[35])
    complete_merge = merge_dicts(dict1, dict2, True)
    print('complete_merge', complete_merge)
    resolved_merge = merge_dicts(dict1, dict2, False)
    print('resolved_merge', resolved_merge)



def merge_dicts(a, b, complete):
    new_dict = copy.deepcopy(a)
    if complete:
        for key, value in b.items():
            new_dict.setdefault(key, []).extend(value)
    else:
        for key, value in b.items():
            if key in new_dict:
                # rename first key
                counter = itertools.count(1)
                while True:
                    new_key = f'{key}_{next(counter)}'
                    if new_key not in new_dict:
                        new_dict[new_key] = new_dict.pop(key)
                        break
                # create second key
                while True:
                    new_key = f'{key}_{next(counter)}'
                    if new_key not in new_dict:
                        new_dict[new_key] = value
                        break
            else:
                new_dict[key] = value
    return new_dict


if __name__ == '__main__':
    main()

# for key1, value1 in dict1.items():
#    for key2, value2 in dict2.items():
#        for key3, value3 in dict3.items():

#           print ('Key', key1, key2, key3)
#            print ('value', value1, value2, value3)