import re

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

mo = phoneNumRegex.search('My number is asdasdsssssssssssad asd asdasd asdas 21312 wqeqwe 123123 415-555-4242.')
print(mo.group())
