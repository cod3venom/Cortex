import json

from Kernel.Management.Security.Constants import Constants


class JSON:

    def PrettyPrint(self, data):
        if self.isJson(data):
            loaded = json.loads(data)
            jsData = json.dumps(loaded, indent=2)
            print(jsData)

    def isJson(self, data: str) -> bool:
        if data is not None:
            try:
                jsdata = json.loads(data)
                return True
            except ValueError:
                print(Constants.JSON_WRONG_FORMAT)
                return False
            except KeyError:
                print(Constants.JSON_WRONG_FORMAT)
                return False
        print(Constants.JSON_WRONG_FORMAT)
        return False
