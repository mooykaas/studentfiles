def main():
    #maak een lege dictionary
    cijfers = {}
    #vul de dictionary via user input...    
    # ...met vakken en het cijfer
    cijfer = int(input('voer het cijfer in voor Engels: '))
    cijfers['Engels']= cijfer
    cijfer = int(input('voer het cijfer in voor Wiskunde: '))
    cijfers['Wiskunde']= cijfer
    cijfer = int(input('voer het cijfer in voor Aardrijkskunde: '))
    cijfers['Aardrijkskunde']= cijfer
    cijfer = int(input('voer het cijfer in voor Nederlands: '))
    cijfers['Nederlands']= cijfer
    cijfer = int(input('voer het cijfer in voor Geschiedenis: '))
    cijfers['Geschiedenis']= cijfer

    # print(cijfers)
    #bereken het gemiddelde cijfer mbv    
    #de values(), sum() en len() functies
    som = sum(cijfers.values())
    aantal = len(cijfers)
    print('Het gemiddelde cijfer is:',som/aantal)

main()

# zo kan het ook als voorbeeld:

#def main():
#vakken =()


#vakken = ['engels'] =int(8)
#vakken =['wiskunden']= int(9)
#vakken =['algemeen studies'](7)
#vakken =['kunst'](9)
#vakken =['muziek'](8)

#punten = vakken.values()

    #gemiddelde = (sum(punten)/len(punten))

    #print("Je gemiddelde cijfer is: ", gemiddelde, "Zou je het cijfer voor Algemeen studies willen veranderen naar een 8? ")

    #vakken["Algemeen studie"] = int(input("Voer hier het nieuwe cijfer in: "))

    #gemiddelde_update = (sum(punten)/len(punten))
    
    #print("Je gemiddelde cijfer is nu weer up-to-date ",gemiddelde_update)
   

#main()




# zo kan het ook als voorbeeld:

#def main():
    #vakken = {}
    #vakken['Engels'] = int(8)
    #vakken['Wiskunde'] = int(7)
    #vakken["algemeen studies"] = int(6)
    #vakken["Kunst"] = int(9)
    #vakken["Muziek"] = int(9)
    

    #punten = vakken.values()

    #gemiddelde = (sum(punten)/len(punten))

    #print("Je gemiddelde cijfer is: ", gemiddelde, "Zou je het cijfer voor Algemeen studies willen veranderen naar een 8? ")

    #vakken["Algemeen studie"] = int(input("Voer hier het nieuwe cijfer in: "))

    #gemiddelde_update = (sum(punten)/len(punten))
    
 #   print("Je gemiddelde cijfer is nu weer up-to-date ",gemiddelde_update)
   

#main()

#zo kan het ook als voorbeeld:

#def main():    

 #   vakkenlijst = {'Engels':0,'Wiskunde':0,'Algemene studies':0,'Kunst':0,'Muziek':0}

    # print(list(vakkenlijst.keys())[0])
    # vakkenlijst['Engels'] = int(input('Wat was het cijfer voor ' +list(vakkenlijst.keys())[0]+' ?'))
    # vakkenlijst[1] = int(input('Wat was het cijfer voor'vakkenlijst[1]'?'))
    # vakkenlijst[2] = int(input('Wat was het cijfer voor'vakkenlijst[2]'?'))
    # vakkenlijst[3] = int(input('Wat was het cijfer voor'vakkenlijst[3]'?'))
    # vakkenlijst[4] = int(input('Wat was het cijfer voor'vakkenlijst[4]'?'))
    
  #  print(vakkenlijst)
   # for vak in vakkenlijst:
    #    vakkenlijst[vak] = int(input('Wat was het cijfer voor ' +vak+' ?'))
    
    #print(vakkenlijst)

#main()

# Dit kan ook als voorbeeld:

#def main():    

    #vakkenlijst = {'Engels':0,'Wiskunde':0,'Algemene studies':0,'Kunst':0,'Muziek':0}

    # print(list(vakkenlijst.keys())[0])
    # vakkenlijst['Engels'] = int(input('Wat was het cijfer voor ' +list(vakkenlijst.keys())[0]+' ?'))
    # vakkenlijst[1] = int(input('Wat was het cijfer voor'vakkenlijst[1]'?'))
    # vakkenlijst[2] = int(input('Wat was het cijfer voor'vakkenlijst[2]'?'))
    # vakkenlijst[3] = int(input('Wat was het cijfer voor'vakkenlijst[3]'?'))
    # vakkenlijst[4] = int(input('Wat was het cijfer voor'vakkenlijst[4]'?'))
    
    # print(vakkenlijst)
    #for vak, cijfer in vakkenlijst.items():
     #   print('het oorsponkelijke cijfer van', vak, 'was', cijfer )
      #  vakkenlijst[vak] = int(input('Voer het nieuwe cijfer in voor ' +vak+' ?'))
    
    #print(vakkenlijst)


    # print(vakkenlijst)
    # for vak, cijfer in vakkenlijst.items():
    #     print(vak, cijfer)
    #     vakkenlijst[vak] = int(input('Wat was het cijfer voor ' +vak+' ?'))
    
    # print(vakkenlijst)

#main()