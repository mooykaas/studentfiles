
def main():
          zin = input("kies een zin:") 
          print ("jou zin was:" +zin )
          lengte = str(len(zin))
          getal = int(input("voer een getal in tussen 1 en "+ lengte +":"))
          #print (f"op positie {getal} staat {zin[getal-1]}")
          print("oppositie",getal,"staat", zin[getal-1])
main()


