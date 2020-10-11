import  sys , os
inp = sys.argv[1]
outp = sys.argv[2]
tableName = sys.argv[3]
sql = 'CREATE TABLE '+tableName + '(' \
                                  ''
if __name__ == "__main__":
    if os.path.isfile(inp):
        if os.path.isfile(outp) == False:
            with open(outp,"w") as writer:
                writer.write("")
        with open(inp, "r") as reader:
            _lines = reader.read().split("\n")
            i = 0
            for line in _lines:
                if "~" in line:
                    spl = line.split("~")
                    sql += "        {} text, \n".format(spl[0])
sql += ')'
print(sql)