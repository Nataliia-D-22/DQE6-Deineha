import re

a = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
# task 1
# split at punctuation characters using regular expressions
punct_signs = re.compile('([.!?]\s*)')
split_with_punct = punct_signs.split(a)
# Join everything back with capitalized letters at the start of the sentences.
final = ''.join ([i.capitalize() for i in split_with_punct])
print ('Task 1 result:','\n', final)


#task2
# Also, create one more sentence with last words of each existing sentence and add it to the end of this paragraph

# 	\S Returns a match where the string DOES NOT contain a white space character
end_words = '(\S*)[.]'
data = re.findall(end_words, final)
string_2 = ' '.join (data)
print('Task 2 result: ', a, '\n',string_2.capitalize())



#task3
# it iZ misspeLLing here.fix“iZ” with correct “ is ”, but ONLY when it Iz a mistAKE.

task_3 = final.replace (" iz ", " is ")
print ('Task 3: ', task_3)


# task4
# last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87
# count whitespaces using isspace method
space=0
for k in a:
    if(k.isspace()):
        space=space+1
print ('Whitespaces total:', space)