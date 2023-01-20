def divide(getal, deler):
    print(getal,deler)
   # de deling doen
   # de uitkomst berekenen
   # alles afdrukken naar consule
print("")
    #uitkomst=getal//deler
    #rest=getal%deler
    #print(getal,"gedeeld door" , deler, "is gelijk aan", uitkomst, "met een rest van rest", rest)

#zo kan het ook zie onder aan

def divide (num1, num2):
    restgetal = num1%num2
    gelijk_aan = num1//num2
    print("Als je ", num1,"deelt door ",num2, "dan krijg je ", gelijk_aan, "als antwoord met een restwaarde van, ", restgetal )

num1 = int(input("geef een getal op "))
num2 = int(input("geef nog een getal op "))

# voorbeeld van de demos
def main():
    divide(5, 2)
    divide(6, 3)
    divide(12, 5)
    divide(1, 2)

main()