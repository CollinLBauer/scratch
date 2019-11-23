import requests
import re

class ExchangeItem:
    
    def __init__(self,url):
        self.url = url
        self.refreshName()
        self.refreshExchangePrice()

    def refreshName(self):
        content = requests.get(self.url).content
        pattern = re.compile('.*data-item=\"(.*)\" data-data')

        self.name = pattern.findall(str(content))[0]

    def refreshExchangePrice(self):
        content = requests.get(self.url).content
        pattern = re.compile('.*id="GEPrice">(.*)</span><span class=\"gemw-change')

        valStr = pattern.findall(str(content))[0] 
        self.price = int(valStr.replace(",",""))


class SyntheticItem:
    # Used for compatibility between the cost of an item and indirect costs, such as teleport spells
    def __init__(self, name="null", price=0):
        self.name = name
        self.price = price
