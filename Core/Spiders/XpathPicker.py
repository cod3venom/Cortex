from lxml import etree, html

from Core.DataOperations.Strings import EMPTY
from Logger.Logger import Logger
import Core.Security.Global as Global
from Core.Security.Global import JSON_DUMP
from Core.Spiders.Export.Json import Json

artificial_indexer = 0


class XpathPicker:

    def __init__(self):
        self.source = EMPTY
        self.indexed = False
        self.identifier = EMPTY
        self.data = EMPTY
        self.parsed_data: dict = {}
        self.dyn_list: list = []
        self.logger = Logger()
        self.jsonExport = Json('Kategorie')

    def start(self, source, indexed: bool = False, identifier: str = EMPTY):
        global JSON_DUMP
        self.source = html.fromstring(source)
        if self.source is not None:
            self.indexed = indexed
            self.identifier = identifier
            self.extract()

            JSON_DUMP.append(self.parsed_data)
            self.jsonExport.data = str(JSON_DUMP)
            self.jsonExport.export(append_mode=True, duplicates=True)
            print(self.__repr__())
            self.restore_parsedData()
            self.restore_dynList()

    def restore_parsedData(self):
        self.parsed_data: dict = {}

    def restore_dynList(self):
        self.dyn_list: list = []

    def extract(self):
        try:
            if self.source is not None:
                if self.indexed:
                    if self.identifier == EMPTY:
                        global artificial_indexer
                        self.identifier = str(artificial_indexer + 1)

                    self.parsed_data[self.identifier] = {}
                for selector in Global.__SELECTORS__:
                    self.data = self.source.xpath(selector.SELECTOR_VALUE)
                    if type(self.data) == list:
                        if len(self.data) == 1:
                            for first in self.data:
                                self.parsed_data[self.identifier][selector.SELECTOR_KEY] = first
                        else:
                            for sublist in self.data:
                                if type(sublist) == str:
                                    sublist = sublist.strip()
                                self.dyn_list.append(sublist)
                            self.parsed_data[self.identifier][selector.SELECTOR_KEY] = self.dyn_list
                            self.restore_dynList()
                    else:

                        self.parsed_data[self.identifier][selector.SELECTOR_KEY] = str(self.data).strip()

                # exit()
        except etree.ParseError as ParseError:
            self.logger.Print(9, Global.levels.Error, bundler=True)

        except etree.XPathEvalError as XpathEvalError:
            self.logger.Print(10, Global.levels.Error, bundler=True)

    def __repr__(self):
        return str(JSON_DUMP)
