name = input("What is your name? ")
outf = open("name.txt", "w")
outf.write(name)
outf.close()
