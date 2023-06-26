import json
data = json.load(open("Dictionary/data.json"))

def translate(word): 
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("Word not found")



word = input("Enter the word")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
#print(output)