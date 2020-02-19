name = input("What is your name? ")
outf = open("name.txt", "a")
outf.write(name + "\n")
outf.close()
