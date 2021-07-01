import scrapy
from scrapy.exceptions import CloseSpider
from helpers import (yesno_prompt,
                     colors,
                     yesno_isvalid,
                     is_valid_list,
                     loopbreak,
                     eyerelief)


class SpanishSpider(scrapy.Spider):
    name = "spanishspider"
    faillist = []

    def start_requests(self):
        with open('toscrape.txt') as f:
            words = f.readlines()
        urls = ['https://www.spanishdict.com/translate/' +
                word[:-1] for word in words]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        satisfied = False
        exitvalve = 0
        while not satisfied:
            exitvalve += 1
            if exitvalve > 1000:
                raise CloseSpider(loopbreak)
                break
            n = 0
            exlist = response.css('span._1vjZoH4D::text').getall()
            trlist = response.css('span._3nHbP_Tm::text').getall()
            eyerelief()
            if len(exlist) == 0:
                print(f'{colors.warning("ERROR - NO RESULTS RETURNED; SKIPPING " + response.url[38:])}')
                self.faillist.append(response.url[38:])
                break
            for ex, tr in zip(exlist, trlist):
                print(f'{n}\n{colors.bluetext(ex)}\n{colors.information(tr)}')
                n += 1
            eyerelief()
            userchoice = input(
                colors.prompt(
                    'Enter the numbers of the examples above you would like'
                    'to save, separated by commas:\n'
                )
            )
            exitvalve2 = 0
            while not is_valid_list(userchoice,
                                    exlist) or not is_valid_list(userchoice,
                                                                 trlist):
                exitvalve2 += 1
                if exitvalve2 > 1000:
                    raise CloseSpider(loopbreak)
                    break
                userchoice = input(
                    colors.warning(
                        'Invalid choice. Please enter the numbers of the '
                        'examples you would like to save separated by '
                        'commas:\n'
                    )
                )
            userchoice = userchoice.split(',')
            userchoice = [int(s) for s in userchoice]
            userchoice = set(userchoice)
            print(colors.prompt("you selected:"))
            for num in userchoice:
                print(colors.parrot(f'{num}\n') +
                      colors.bluetext(f'{exlist[num]}\n') +
                      colors.information(f'{trlist[num]}\n'))
            if yesno_prompt(
                colors.prompt('Is that correct? y/n:\n'),
                colors.warning('Invalid entry. Please enter y or n:\n')
            ):
                satisfied = True
            with open('examples.txt', 'a') as output:
                for num in userchoice:
                    output.write(f'{exlist[num]}|{trlist[num]}\n')

            # for num in userchoice:
            #     yield {
            #         'example': exlist[num],
            #         'translation': trlist[num]
            #     }
