from difflib import get_close_matches
import json
data = json.load(open("data.json"))

def translate(word): 
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead of" %get_close_matches(word, data.keys())[0])
        decide = input("Type y for yes or n for no")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("Word not found")
    else:
        print("Word not found")



word = input("Enter the search word")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
