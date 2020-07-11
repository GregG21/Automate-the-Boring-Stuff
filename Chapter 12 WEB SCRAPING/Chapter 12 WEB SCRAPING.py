# import requests
#
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#
# print(type(res))
#
# print(res.status_code == requests.codes.ok)
#
#
# print(res.text)
#
#
import requests
#
# res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
# res.raise_for_status()
# playFile = open("RomeoAndJuliet.txt", "wb")
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)
# playFile.close()

import bs4

res = requests.get("https://nostarch.com")
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))

example