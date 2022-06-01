# ledebook
an HTML generator for MediaWiki articles with the [TextExtracts](https://www.mediawiki.org/wiki/Extension:TextExtracts) extension that combines the lead paragraphs of multiple articles into a single page. by default it uses English Wikipedia articles with images from Wikimedia Commons, however you can easily repurpose it for other wikis by changing the relevant links.

made with love, by [Melecie](https://en.wikipedia.org/wiki/User:Melecie)

## how-to
when launching up the program, you can input articles. you can separate articles through pipe characters <code>|</code>, such as <code>Science|Technology</code> to input [Science](https://en.wikipedia.org/wiki/Science) and [Technology](https://en.wikipedia.org/wiki/Technology). when you're ready, input it and the program will do its magic. once it's done, the file will be outputed at <code>output.html</code> at the same folder ledebook is in. 

if you want to mod ledebook to output another wiki, change <code>infourl</code>, <code>articleurl</code>, <code>catsurl</code>, and <code>outputHTML</code> to use your desired wiki instead of enwiki. note that <code>catsurl</code> picks up categories from the article's talk page by default (as it picks up what WikiProjects a given page is in through the categories), which you might want to replace to the article itself by removing <code>Talk:</code>.

## dependencies
you'll need to install the following module to run ledebook:
* <code>pytz</code> - converts your local timestamp to UTC
