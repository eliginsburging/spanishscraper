# spanishscraper - generate Spanish example sentence flashcards for Anki from Spanishdict.com
Takes a list of Spanish words and outputs a text file of user selected scraped example sentences and translations that can be uploaded as flashcards in Anki

* User places a list of Spanish words on newlines in 'toscrape.txt'
* User runs getwords.py in an environment where requirements.txt has been installed
* User is prompted to select example sentences/translations pulled from spanishdict.com
* Selected examples are saved in examples.txt - each example appears on its own line separated from its translation by a |
* The resultant examples.txt file can be imported into Anki to generate flashcards of each example/translation combination.
