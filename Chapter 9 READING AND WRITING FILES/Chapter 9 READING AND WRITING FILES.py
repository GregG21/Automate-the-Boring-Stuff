from pathlib import Path

# p = Path("spam.txt")

# p.write_text("Hello World")

# p.read_text("spam.txt")

# helloFile = open(Path("hello.txt"))
#
# helloContent = helloFile.read()
#
# print(helloContent)


# sonnetFile = open(Path("sonnet29.txt"))
#
# sonnetContent = sonnetFile.readlines()
#
#
# print(sonnetContent[0])
#
# sonnetFile.close()
#
# sonnetFile = open("sonnet29.txt", "w")
# sonnetFile.write("I wrote this using Pyhon")
#
# sonnetFile.close()
import shelve

# shelfFile = shelve.open("mydata")
# # cats = ['Zophie', 'Pooka', 'Simon']
# # shelfFile["cats"] = cats
# # shelfFile.close()


import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]


fileObj = open("myCats.py","w")
fileObj.write("cats = " + pprint.pformat(cats) + "\n")