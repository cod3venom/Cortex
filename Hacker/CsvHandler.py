import datetime, os, csv

class CsvHandler:
    def randomFile(self) -> str:
        return 'export_{}.csv'.format(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def CreateHeaders(self,headers:dict) -> str:
        if headers!=None:
            export = self.randomFile()
            if os.path.isfile(export) == False:
                with open(export,'a', encoding="utf-8") as cswriter:
                    writer = csv.DictWriter(cswriter, headers.keys(), delimiter=";", quoting=csv.QUOTE_NONE)
                    writer.writeheader()
                    return export

    def AppendData(self, data:dict, path:str) -> int:
        if os.path.isfile(path):
            with open(path, 'a', newline='', encoding="utf-8") as writer:
                cswriter = csv.writer(writer, delimiter=";")
                cswriter.writerows(data.items())