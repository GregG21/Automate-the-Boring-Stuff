import requests,os, bs4

def ImageDownloader(site, category):


    res = requests.get(site + "/search?q=" + category)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    imgElement = soup.select("#imagelist img")

    os.makedirs(category, exist_ok=True) #makes folder

    for link in soup.find_all("img"):
        print(link.get("src"))

        imgURL = "https:" + link.get("src")
        res = requests.get(imgURL)
        res.raise_for_status()



        imgFile = open(os.path.join(category, os.path.basename(imgURL)), "wb")

        for chunk in res.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()
    print("I AM DONE")




ImageDownloader("https://imgur.com/","sunset")

