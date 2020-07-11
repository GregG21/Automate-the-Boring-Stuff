
import requests, bs4

def LinkVerification(link):

    res = requests.get(link)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    for link in soup.find_all("a"):
        try:
            possibleLink = requests.get(link.get("href"))

            possibleLink.raise_for_status()
            print(str(link.get("href")) + " --> Good link")
        except Exception as exc:
            print("There was a problem: %s" % (exc))

LinkVerification("https://unsplash.com/s/photos/ducks")