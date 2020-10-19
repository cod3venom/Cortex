
from Spider.Browser.__Chormium__ import __Chromium__
from Spider.Extractor.PyDict import PyDict
from Spider.Extractor.PyPath import *
from Spider.Network.PHP import PHP
from Hacker.ClusterClient import send
from Hacker.CsvHandler import CsvHandler
from Hacker.FileSystem import FileSystem


class Categories:
    FS = FileSystem()
    CATEEGORIES_DE = 'aws_categories_silicon_de'
    Countries = {
        'DE':'https://www.amazon.de/gp/site-directory/ref=topnav_sad',
        'UK': 'https://www.amazon.co.uk/gp/site-directory/ref=topnav_sad',
        'USA':'https://www.amazon.com/gp/site-directory/ref=topnav_sad'
    }
    PREFIX = {
        'DE':'https://www.amazon.de',
        'UK': 'https://www.amazon.co.uk',
        'USA':'https://www.amazon.com'
    }

    STACK = {
        "Prime_Video":{}, "Amazon_Music":{}
    }

    CPYCOLUMNS = []
    def __init__(self,Country):
        if Country == 'DE' or Country == 'UK' or Country == 'USA':
            self.Csv = CsvHandler()
            self.Country = Country
            self.FULL = ''
            self.Chrome = __Chromium__(True,False,"",False,True,True)
            if Country == 'DE':
                self.Format = PyDict(self.CATEEGORIES_DE)


    def getCountry(self, key:str) -> str:
        if self.Countries != None and key != None and key in self.Countries:
            try:
                return self.Countries[key]
            except KeyError:
                Logging(3, Bundle().getString(61),Bundle().getString(62))




    def GenerateSiliconELEMENTS(self) -> int:
        self.Chrome.address = self.getCountry(self.Country)
        self.pref = self.PREFIX[self.Country]
        self.Chrome.Navigate()
        self.Chrome.Scroll_V_V()
        pyPath = PyPath(self.Chrome)
        pyPath.Start(self.Chrome.Source())
        KV = self.Format.Load()
        self.Format.__xpath__ = pyPath
        for i in range(len(KV["Keys"])):
            _key_ = KV['Keys'][i]
            _val_ = KV['Values'][i]
            try:
                self.STACK[_key_] = pyPath.Stacked_extraction(_val_)
            except IndexError:
                pass
        self.CreateColumns()

    def CreateColumns(self) ->int:
        if self.STACK != None:
            SYNTAX = ""
            for table in self.STACK.keys():
                table = table.replace("&","").replace(" ","_").replace("-","").replace("__","").replace(",","")
                SYNTAX += "\nCREATE TABLE IF NOT EXISTS AWS_CATEGORY_{} (\nID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,\nLink VARCHAR(1000) NOT NUll);".format(table)
                self.CPYCOLUMNS.append(table)
            self.FS.Write("DB/AWS_CATEGORIES_TABLES.sql",SYNTAX)
            print(SYNTAX)
        self.GenerateRows()



    def GenerateRows(self) ->int:
        if self.STACK!=None:
            KV = self.Format.Load()
            QUERY = ""
            for i in range(len(KV["Keys"])):
                _key_ = KV['Keys'][i]
                for link in self.STACK[_key_]:
                    QUERY += 'INSERT INTO  AWS_CATEGORY_{}(`Link`) VALUES ("{}"); \n'.format(_key_, self.pref+link)
            print(QUERY)
            self.FS.Append('DB/AWS_CATEGORIES_TABLE_INSERTS.sql', QUERY)

    ACT_SILICON = 0

    def c_main(self, action:int) -> int:
         if action == self.ACT_SILICON:
             self.GenerateSiliconELEMENTS()














