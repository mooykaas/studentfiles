import math
#invoer gegevens
#
#
aantal_mensen = 5
aantal_stukken = 2.5
aantal_stukken_in_pizza = 8

totaal_benodigde_stukken = aantal_mensen * aantal_stukken
print (math.ceil(totaal_benodigde_stukken / aantal_stukken_in_pizza))
overgebleven_stukken = ( aantal_stukken_in_pizza)- totaal_benodigde_stukken
#berekening gegevens
#
#

print (math.ceil(totaal_benodigde_stukken / aantal_stukken_in_pizza))
# concole output
#
#
print("je hebt", totaal_benodigde_stukken ,"pizzas nodig om",aantal_mensen,"mensen te voeden")
print('er zullen nog',overgebleven_stukken, 'stukken overblijven')

#print (totaal_benodigde_stukken)
#print (' hoeveel mensen eten?', aantal mensen)

import math
#invoer gegevens
aantal_mensen = 25
aantal_stukken = 2
aantal_aantal_stukken_in_pizza = 8

totaal_benodigde_stukken = aantal_mensen* aantal_stukken
#berekening gegevens

# concole output
print(math.ceil(totaal_benodigde_stukken/aantal_stukken_in_pizza))



# met int en float erbij


import math

#
# invoer gegevens
#
def gegevens_invoer():
    aantal_mensen = int(input("Hoeveel mensen eten? "))
    aantal_stukken = float(input("Hoeveel stukken per persoon? "))
    aantal_stukken_in_pizza = int(input("Hoeveel stukken per pizza? "))
    return (aantal_mensen, aantal_stukken,aantal_stukken_in_pizza)
#
# berekening gegevens
#
def bereken_aantal_pizzas(aantal_mensen, aantal_stukken, aantal_stukken_in_pizza):
    totaal_benodigde_stukken = aantal_mensen * aantal_stukken
    benodigde_pizzas = math.ceil(totaal_benodigde_stukken / aantal_stukken_in_pizza)
    overgebleven_stukken = (benodigde_pizzas * aantal_stukken_in_pizza) - totaal_benodigde_stukken
    return (benodigde_pizzas, overgebleven_stukken)

#
# console output
#
def output(benodigde_pizzas, aantal_mensen, overgebleven_stukken):
    print("Je hebt", benodigde_pizzas ,"pizza's nodig om", aantal_mensen ,"mensen te voeden." )
    print('Er zullen nog', overgebleven_stukken ,'stukken overblijven')



def main():
    lijst2 = gegevens_invoer()
    lijst1 = bereken_aantal_pizzas(lijst2[0], lijst2[1], lijst2[2])
    output(lijst1[0],lijst2[0],lijst1[1])


main()    


import pizza



lijst = pizza.gegevens_invoer()

print(lijst)










