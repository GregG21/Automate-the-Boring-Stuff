import re


search = re.compile(r"(ADJECTIVE)|(NOUN)|(VERB)")

file = open("panda.txt")
text = file.read()
file.close()

for i in search.findall(text):
    for j in i:
        if j != "":
            if j == "ADJECTIVE":
                reg = re.compile(r"{}".format(j))
                replace = input("Enter an %s: " % j)
                text = reg.sub(replace,text,1)
            else:
                reg = re.compile(r"{}".format(j))
                replace = input("Enter a %s: " % j)
                text = reg.sub(replace,text,1)

print(text)
file = open("panda.txt","w")
file.write(text)
file.close()