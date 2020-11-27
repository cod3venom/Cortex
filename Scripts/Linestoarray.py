with open('links.txt','r') as reader:
    content =reader.read()
    lines = content.split("\n")
    for line in lines:
        with open("outLinkstoArray.txt","a") as writer:
            writer.write('"{}",\n'.format(line))
            print(line)