# <code>📔</code> ledebook
an HTML generator for MediaWiki articles with the [TextExtracts](https://www.mediawiki.org/wiki/Extension:TextExtracts) extension that combines the lead paragraphs of multiple articles into a single page, and a semi-substitute for the disabled [book rendering service](https://en.wikipedia.org/wiki/Wikipedia:Books). by default it uses English Wikipedia articles with images from Wikimedia Commons, however you can easily repurpose it for other wikis by changing the relevant links.

made with love, by [Melecie](https://en.wikipedia.org/wiki/User:Melecie)

## how-to
when launching up the program, you can input articles. you can separate articles through pipe characters <code>|</code>, such as <code>Science|Technology</code> to input [Science](https://en.wikipedia.org/wiki/Science) and [Technology](https://en.wikipedia.org/wiki/Technology). when you're ready, input it and the program will do its magic, taking about two to four seconds per article. once it's done, the file will be outputed at <code>output.html</code> at the same folder ledebook is in. 

if you want to mod ledebook to output another wiki, change <code>articleURL</code>, both instances of <code>imageURL</code>, <code>infoURL</code>, <code>catsURL</code>,  <code>outputHTML</code>, and the link in line 204 to use your desired wiki instead of enwiki and commons. note that <code>catsurl</code> picks up categories from the article's talk page by default (as it picks up what WikiProjects a given page is in through the categories), which you might want to replace to the article itself by removing <code>Talk:</code>.

## dependencies
you'll need to install the following module to run ledebook:
* <code>pytz</code> - converts your local timestamp to UTC

additionally, if modding ledebook, the following extension need to be installed into the wiki:
* <code>TextExtracts</code> - API for getting clean ledes from articles
