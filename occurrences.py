"""
Make a program that has some sentence (a string) on input and returns a dict containing 
all unique words as keys and the number of occurrences as values. 
"""
sentence = input("Please provide your sentence: ")

result = {}
# or
# result = dict()

for word in sentence.split():
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print("Words:", result)

# or
# import pprint
# print("Words:")
# pprint.pprint(result)
