def main():
    today = input("What day is it? ")
    print("Wow! Today is ", today, "? Awesome!", sep="")



main()with open("1880-boys.txt") as f: # Open my-file.txt and assign result to f. 
    content = f.read() # Read contents of file into content variable. 
    print(content) # Print content. 

with open("1880-girls.txt", "w") as f: 
    f.write(content)


    with open("../data/1880-boys.txt") as f_boys:
    boys = f_boys.read()

with open("../data/1880-girls.txt") as f_girls:
    girls = f_girls.read()

with open("../data/1880-all.txt", "w") as f:
    f.write(boys + "\n" + girls)