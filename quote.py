
import random
import requests
from bs4 import BeautifulSoup
import re
import json

LINE_LENGTH = 15
SCRPE_URL = "https://www.invajy.com/bible-verses/"
Quotes = {}
class WebScrapper:

    def getquote():
        dicti = {}
        page = requests.get(SCRPE_URL, headers={"User-Agent": "XY"})
        soup = BeautifulSoup(page.content, "html.parser")
        print(page)
        for li in soup.find_all("li"):
            li = str(li)
            numbers = bool(re.findall('[0-9]+', li))
            if "</strong>" in li:
                cleaned_txt = WebScrapper.cleanupquote_v2(li)
                dicti[WebScrapper.key(cleaned_txt)] = WebScrapper.value(cleaned_txt)

        with open(r"C:\Users\birdl\Desktop\Year 2\Programming\Python\Praise God\quotes\quotes.txt", 'a') as f:
            f.write(json.dumps(dicti))

    def cleanupquote_v2(text):

        full_quote = ""
        list_of_tag = [i for i, ltr in enumerate(text) if (ltr == ">" or ltr == "<")]
        for index in range(1,len(list_of_tag) - 1, 2):
            full_quote+=text[list_of_tag[index] + 1:list_of_tag[index+1]]

        return full_quote


    def key(text):
        text = str(text)
        index = text.rfind("~")
        return text[index+2:len(text)]

    def value(text):
        text = str(text)
        index = text.rfind("~")
        return text[1:index-2]

    def readrandom():
        with open(r'C:\Users\birdl\Desktop\Year 2\Programming\Python\Praise God\quotes\quotes.txt') as f:
            data = f.read()
        
        js = json.loads(data)
        return js

def load():

    with open (r"C:\Users\birdl\Desktop\Year_2\Programming\Python\Praise_God\quotes\quotes.txt") as f:
        data = f.read()
        
    dictionary = json.loads(data)
    return dictionary

def get_chapter_from_dictionary(dictionary):
    return random.choice(list(dictionary))

def spliceloadedquote(chapter, dictionary):
    '''Get text for key in dicitionary'''
    quote = dictionary[chapter]
    
    char_since_break = 0
    for index in range(len(quote) - 1):
        if quote[index] == " " and char_since_break > LINE_LENGTH:
            '''Add a line break in text quote if it gets longer than LINE_LENGTH'''
            quote=quote[:index]+ "\n" +quote[index:]
            char_since_break = 0
            
        char_since_break+=1

    return quote