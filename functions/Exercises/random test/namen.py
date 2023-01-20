f = open("../python-basics/data/1880-boys.txt")
namen  = f.read()
losse_namen = namen.split('\n')
f.close()

print(losse_namen)

# for naam in losse_namen:
#     print(naam)