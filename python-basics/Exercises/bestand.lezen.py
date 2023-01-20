

f = open("../data/1880-boys.txt")
boys = f.read()

f2 = open("../data/-al.txt", "w")
f2.write(boys)

f = open("../data/1880-girls.txt")
girls = f.read()
girls ="\n"+girls

f2 = open("../data/-al.txt", "a")
f2.write(girls)





