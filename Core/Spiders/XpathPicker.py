import json
from pprint import pprint

from lxml import etree, html

from Core.DataOperations.Logger.Logger import Logger, EMPTY
from Core.Security.Global import __SELECTORS__, levels
from Core.Spiders.Export.Json import Json

artificial_indexer = 0


class XpathPicker:

    def __init__(self: str):
        self.source = EMPTY
        self.indexed = False
        self.identifier = EMPTY
        self.data = EMPTY
        self.parsed_data: dict = {}
        self.dyn_list: list = []
        self.jsonExport = Json('testowy')

    def start(self, source , indexed: bool = False, identifier: str = EMPTY):
        self.source = html.fromstring(source)
        if self.source is not None:
            self.indexed = indexed
            self.identifier = identifier
            self.extract()
            self.jsonExport.data = self.parsed_data
            self.jsonExport.export(append_mode=True, duplicates=True)
            print(self.__repr__())
            self.parsed_data: dict = {}
            self.dyn_list: list = []

    def extract(self):
        try:
            if self.source is not None:
                if self.indexed:
                    if self.identifier == EMPTY:
                        global artificial_indexer
                        self.identifier = str(artificial_indexer + 1)

                    self.parsed_data[self.identifier] = {}
                for selector in __SELECTORS__:
                    self.data = self.source.xpath(selector.SELECTOR_VALUE)
                    if type(self.data) == list:
                        if len(self.data) == 1:
                            for first in self.data:
                                self.parsed_data[self.identifier][selector.SELECTOR_KEY] = first
                        else:
                            for sublist in self.data:
                                self.dyn_list.append(sublist)
                            self.parsed_data[self.identifier][selector.SELECTOR_KEY] = self.dyn_list
                    else:

                        self.parsed_data[self.identifier][selector.SELECTOR_KEY] = str(self.data)


                #exit()
        except etree.ParseError as ParseError:
            Logger(True, 9, levels.Error)
        except etree.XPathEvalError as XpathEvalError:
            Logger(True, 10, levels.Error)

    def __repr__(self):
        return self.parsed_data
