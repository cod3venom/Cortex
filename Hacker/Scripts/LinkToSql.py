import  sys , os
inp = sys.argv[1]
outp = sys.argv[2]
if __name__ == "__main__":
    if os.path.isfile(inp):
        if os.path.isfile(outp) == False:
            with open(outp,"w") as writer:
                writer.write("")
        with open(inp, "r") as reader:
            _lines = reader.read().split("\n")
            with open(outp, "a") as writer:
                counter = 0
                for line in _lines:
                    counter+=1
                    sql = "INSERT INTO Links(Address) VALUES('{}'); \n".format(line)
                    print("[{}] {} --- {}".format(str(counter),outp, sql))
                    writer.write(sql)

