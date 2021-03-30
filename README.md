# spanishscraper - generate Spanish example sentence flashcards for Anki from a Spanish dictionary
Takes a list of Spanish words and outputs a text file of user selected scraped example sentences and translations that can be uploaded as flashcards in Anki

## DISCLAIMER: This repository is meant to serve merely as an example of how one might use Scrapy to automate the generation of Anki flashcards.
By uploading this project, I do not intend to advocate or encourage the scraping any website. Before scraping any website, you should review that website's terms of service to make sure you do not violate them. 

* User places a list of Spanish words on newlines in 'toscrape.txt'
* User runs getwords.py in an environment where requirements.txt has been installed
* User is prompted to select example sentences/translations pulled from spanishdict.com
* Selected examples are saved in examples.txt - each example appears on its own line separated from its translation by a |
* The resultant examples.txt file can be imported into Anki to generate flashcards of each example/translation combination.
