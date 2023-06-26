import xml.etree.ElementTree as ET

tree = ET.parse('C:/Users/anato/OneDrive/Desktop/Python/Dictionary/es-en.xml')
myroot = tree.getroot()

def translate(inp):
    inp = inp.lower()
    for child in myroot.findall('l'):
        for x in child:
            word = x.find('c').text
            desc = x.find('d').text
            if inp == word:
                
                return(["word: ", word, "Description: ", desc])
    else:
        print("Not Found")

inp = input("Enter a word to translate")
output = translate(inp)


#print(output)
   
  


