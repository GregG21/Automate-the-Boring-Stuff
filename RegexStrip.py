import re

def RegexStrip(string, char=" "):
    if char == "":
        find = re.compile(r'^(\s*)|(\s)*$')
        stripped = find.sub("", string)
        return stripped
    else:
        replace = re.sub("^%s+|%s+|%s+$" % (char, char, char), "", string)
        return replace

