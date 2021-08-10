print('Day 27: Reading & Writing JSON')

import json

print("\n------------Writing JSON data into file------------")

dictionary = {'Name':'Moneesh','Status':'Open to work','Position':'Python Developer'}
#opening file in write mode & convering dictionary to JSON
with open('test.json','w') as file:
    json.dump(dictionary,file, indent=2)
print("Successfully written JSON data into test.json")

print("\n------------Reading JSON data from a file------------")
#opening file in read mode & printing the json file
f = open('test.json','r')
print(f.read())
#closing file
f.close()