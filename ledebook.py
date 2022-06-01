import requests
import codecs
#import pdfkit
import pytz
import datetime

headers = {"User-Agent": "Ledebook, written by Melecie (en:User:Melecie, github Melecie)"}

# initialize vars
articleList = [] 
infoList = []
imgList = []
titleList = []
articleNo = 0

print('Hello world! Input article names below. Separate articles using pipes [ | ]')
allPages = input()

allPages = allPages.split("|")

for page in allPages: # inputing end causes page collection to end

    # getting article info
    infourl = "https://en.wikipedia.org/w/rest.php/v1/search/page?q=" + page + "&limit=1"
    pageinfo = requests.get(infourl, headers=headers)
    pageinfo = pageinfo.json()
    pageinfo = pageinfo["pages"]
    
    pageinfo = pageinfo[0]
    
    page = (pageinfo["title"])
    pageid = (pageinfo["id"])
    image = (pageinfo["thumbnail"])
    pageid = str(pageid)
    
    # getting article lede
    dataurl = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&titles=' + page + '&format=json' # rm explaintext
    response = requests.get(dataurl, headers=headers)
    data = response.json()
    data = (data["query"])
    data = (data["pages"])
    data = (data[pageid])
    title = (data["title"])
    extract = (data["extract"])
    
    articleNo = articleNo + 1
    articleList.append(extract)
    infoList.append(pageinfo)
    #linkList.append(pageinfo["html_url"])
    titleList.append(title)
    #imgList.append(image) # COMMENTED OUT - Need a more graceful way to do this that'd include copyright notices
    print('Article "' + title + '" added')
    
    continue
    
print(str(articleNo) + " articles detected, output has been printed onto output.html")

# initialize outputHTML
outputFile = open('output.html', 'w', encoding="utf-8")

outputHTML = """<html>

<style>
body {
	background-color: #eef;
	font-family:"Arial";
	color: black;
	font-size: 16px
    }
    
body {
	background-color: #eef;
	font-family:"Arial";
	color: #002;
	font-size: 16px
    }
    </style>
    
<br><title>Ledebook</title><h1><center>Ledebook</center></h1><hr>"""

# get current time, convert to UTC
timestamp = datetime.datetime.now(pytz.utc)
timestamp = str(timestamp)
print(timestamp)

if articleNo > 9: # write contents if there are a lot of contents
    outputHTML += "<h2>Ledebook Contents:</h2><ol>"
    for x in range(0, articleNo):
        outputHTML += "<li>" + titleList[x] + "</li>"
        continue
    outputHTML += "</ol><hr>"

for x in range(0, articleNo): # writing lede text

    # if image != null, add the thumbnail to the right before the text
    #img = imgList[x]
    #if isinstance(img, dict):
    #    outputHTML += "<img src='https:" + img["url"] + "' alt='" + titleList[x] + "' style='float:right'>"

    outputHTML += "<h2>" + titleList[x] + "</h2>" + articleList[x] + "<hr>"
    
    continue
    
outputHTML += "<br><i>Ledebook Generator by <b>Melecie</b>, contributions by various users from various English Wikipedia pages licensed under Creative Commons Attribution-ShareAlike License 3.0:</i><br><ul>"
for x in range(0, articleNo): # writing links to full articles
    outputHTML += "<li><a href='https://en.wikipedia.org/wiki/" + titleList[x].replace(' ',"_") + "'>" + titleList[x] +"</a></li>"
    continue

outputHTML += "</ul><br><i>Created on " + timestamp + " (UTC)</i></html>"

outputFile.write(outputHTML)
outputFile.close()

#print('Would you like to create a PDF file? Input [y]')
#answer = input()
#
#if answer == "y":
#    pdfkit.from_string(outputHTML, "output.pdf")
#    print("PDF file created")
