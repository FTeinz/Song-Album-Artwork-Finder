from bs4 import BeautifulSoup as bs
import urllib
import requests



while True:
    song = raw_input("Enter Song: ")
    r = requests.get("https://play.google.com/store/search?q=" + song +"&c=music&hl=en")
    page = r .text
    soup = bs(page)

    list = []


    for img in soup.find_all("img"):
        if img["alt"].lower() == song.lower():
            list.append(img["src"])

    print "Found Image at", list[0]
    urllib.urlretrieve(list[0], (song + ".jpg"))


