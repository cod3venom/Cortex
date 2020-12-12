import mysql.connector
import sys
import datetime
now = datetime.datetime.now()
creation_time = now.strftime("%Y-%m-%d %H:%M:%S")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="SILICON"
)

mycursor = mydb.cursor()

mycursor.execute('''
    SELECT column_name
FROM information_schema.columns
WHERE  table_name = 'BOT_JAVASCRIPT'
   AND table_schema = 'SILICON'
''')

myresult = mycursor.fetchall()


classname = sys.argv[1]

fullclass = '''
import json
from Kernel.Management.Security.Constants import Constants
from Kernel.Management.Security.Globals import Debug
from Kernel.Management.Security.JSON import JSON


class {}:
   def __init__(self, jsData):
'''.format(classname)

self_variable = ''

copyTobject = '''
    def CopyTObject(self, jsData):
        if JSON().isJson(jsData):
            try:
                jsData = json.loads(jsData)
                COPIES++;
                except TypeError:
                    Debug(Constants.JSON_WRONG_KEY)
                except KeyError as key:
                    Debug(Constants.JSON_WRONG_KEY.format(key))

'''
setters = ''
for columns in myresult:

    self_variable += '      self.{}: str = Constants.EMPTY\r\n'.format(columns[0])
    setters += "                self.{}: str = jsData['{}']\r\n".format(columns[0], columns[0])

fullclass += self_variable + '      self.CopyTObject(jsData) \r\n' + copyTobject.replace('COPIES++;',setters)

print(fullclass)