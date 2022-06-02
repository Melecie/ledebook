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
catList = []
titleList = []
articleNo = 0

# initialize all categories with note counterparts
noteList = {
"Category:All Wikipedia level-1 vital articles": "Vital articles: I",
"Category:All Wikipedia level-2 vital articles": "Vital articles: II",
"Category:All Wikipedia level-3 vital articles": "Vital articles: III",
"Category:All Wikipedia level-4 vital articles": "Vital articles: IV",
"Category:All Wikipedia level-5 vital articles": "Vital articles: V",
"Category:Biography articles of living people": "Living person",
}

noteFilter = ["Version 1.0"]

print('Hello world! Input article names below. Separate articles using pipes [ | ]')
allPages = input()

allPages = allPages.split("|")

for page in allPages:
	
	# getting enwiki article info
	infourl = "https://en.wikipedia.org/w/rest.php/v1/search/page?q=" + page + "&limit=1"
	pageinfo = requests.get(infourl, headers=headers)
	pageinfo = pageinfo.json()
	pageinfo = pageinfo["pages"]
	pageinfo = pageinfo[0]
	
	page = (pageinfo["title"])
	pageid = (pageinfo["id"])
	#image = (pageinfo["thumbnail"])
	pageid = str(pageid)
	
	# getting article lede
	articleurl = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&titles=' + page + '&format=json' # rm explaintext
	response = requests.get(articleurl, headers=headers)
	data = response.json()
	data = (data["query"]["pages"][pageid])
	title = (data["title"])
	extract = (data["extract"])
	
	# getting article categories from Talk
	catsurl = 'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=categories&cllimit=150&titles=Talk:' + page
	response = requests.get(catsurl, headers=headers)
	cats = response.json()
	cats = cats["query"]["pages"]
	allcats = []
	for id, datas in cats.items():
		for catname in datas['categories']:
			allcats = allcats + [catname["title"]]
	
	articleNo = articleNo + 1
	articleList.append(extract)
	infoList.append(pageinfo)
	#linkList.append(pageinfo["html_url"])
	titleList.append(title)
	catList.append(allcats)
	
	#imgList.append(image) # COMMENTED OUT - Need a more graceful way to do this that'd include copyright notices
	print('Article "' + title + '" added')
	
	continue
	
print(str(articleNo) + " articles detected, output has been printed onto output.html")

# initialize outputHTML
outputFile = open('output.html', 'w', encoding="utf-8")

outputHTML = """<html>
<style>
body { background-color: #eef; font-family:"Arial"; color: black; font-size: 16px}
.notes {border-style: solid; border-color: #aaf; background-color:#ddf; padding: 2px 20px 2px 20px}
</style><br><title>Ledebook</title><h1><center>Ledebook</center></h1><hr>"""

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
	#	outputHTML += "<img src='https:" + img["url"] + "' alt='" + titleList[x] + "' style='float:right'>"

	outputHTML += "<h2>" + titleList[x] + "</h2>" + articleList[x] + ""

	notes = catList[x]
	allNotes = []
	
	# add note counterpart per category with note
	for note in notes:
	
	# remove the WikiProject tags then pass it along
		if note.startswith("Category:WikiProject") or note.startswith("Category:Top-importance") or note.startswith("Category:High-importance") or note.startswith("Category:Med-importance"):
			note = note.replace("Category:WikiProject ","")
			note = note.replace("Category:Top-importance ","")
			note = note.replace("Category:High-importance ","")
			note = note.replace("Category:Mid-importance ","")
			note = note.replace(" articles","")
			if note not in noteFilter: # throw notes in Filter out
				allNotes += [note.lower()]
			
	# not a WikiProject? check special notes, replace it with note name, pass it along. else throw it into the trash
		else:
			note = noteList.get(note, "none")
			if note != "none":
				allNotes += [note.lower()]
	
	if len(allNotes) > 0:
		allNotes = list(dict.fromkeys(allNotes)) # remove duplicates
		outputHTML += "<div class = 'notes'>" + " &#8226; ".join(allNotes) + "</div>"

	outputHTML += "<hr>"

	continue
	
outputHTML += "<br><i>Ledebook generator by Melecie, contributions by various users from various English Wikipedia pages licensed under Creative Commons Attribution-ShareAlike License 3.0</i><br><ul>"
for x in range(0, articleNo): # writing links to full articles
	outputHTML += "<li><a href='https://en.wikipedia.org/wiki/" + titleList[x].replace(' ',"_") + "'>" + titleList[x] +"</a></li>"
	continue

outputHTML += "</ul><i>Created on " + timestamp + " (UTC)</i></html>"

outputFile.write(outputHTML)
outputFile.close()

#print('Would you like to create a PDF file? Input [y]')
#answer = input()
#
#if answer == "y":
#	pdfkit.from_string(outputHTML, "output.pdf")
#	print("PDF file created")
