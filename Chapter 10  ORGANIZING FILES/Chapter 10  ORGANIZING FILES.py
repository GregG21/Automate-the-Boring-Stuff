# import os
# from pathlib import Path
#
# for folderName, subFolders, filenames in os.walk(Path.home()):
#     print('The current folder is ' + folderName)
#
#     for subfolder in subFolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
#
#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': ' + filename)
#
#     print('')

import zipfile, os
from pathlib import Path

# p = Path.home()
#
# exampleZip = zipfile.ZipFile(p / "example.zip")
# # exampleZip.namelist()
# # print(exampleZip.namelist())
# #
# # spamInfo = exampleZip.getinfo("spam.txt")
# # print(spamInfo.file_size)
# #
# # print(f"Compressed file is {round(spamInfo.file_size / spamInfo.compress_size,2)}x smaller!")
#
# # exampleZip.extractall("C:\\Users\\WORK\\test")
#
#
# exampleZip.close()

# newZip = zipfile.ZipFile("new.zip", "w")
# newZip.write("spam.txt", compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()



import shutil, os, re

datePattern = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)


for amerFilename in os.listdir("."):
    mo = datePattern.search(amerFilename)

    if mo == None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath(".")
    amerFilename = os.path.join(absWorkingDir,amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.move(amerFilename, euroFilename)   # uncomment after testing