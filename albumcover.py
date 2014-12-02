from bs4 import BeautifulSoup as bs
import urllib
import requests
import easygui
import os



while True:
    song = raw_input("Enter Song: ")
    r = requests.get("https://play.google.com/store/search?q=" + song +"&c=music&hl=en")
    page = r.text
    soup = bs(page)

    list = []


    for img in soup.find_all("img"):
        if img["alt"].lower() == song.lower():
            list.append(img["src"])
    
    for i in list:
        
        print "Found Image at", i
        urllib.urlretrieve(i, (song + ".jpg"))
        image = song +".jpg"
        msg   = "Do you like this picture?"
        choices = ["Yes","No","Cancel"]
        reply=easygui.buttonbox(msg,image=image,choices=choices)
        if reply == "Cancel":
            os.remove(song+".jpg")
            break
        if reply == "Yes":
            break
            


