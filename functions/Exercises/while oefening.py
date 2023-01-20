paswoord = input ("voer paswoord in:")
wachtwoord= "12345"
teller = 1
while paswoord != wachtwoord:
    teller += 1
    if teller >= 3: # true of false
        print(" 3 verkeerde paswoord ingevoerd")
        quit()
    paswoord = input ("voer paswoordd in:")
    
    print('je bent ingelogd')



