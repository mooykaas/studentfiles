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
# def bereken_aantal_pizzas(aantal_mensen, aantal_stukken, aantal_stukken_in_pizza):
def bereken_aantal_pizzas(gegevens):
    aantal_mensen = gegevens[0]
    aantal_stukken = gegevens[1]
    aantal_stukken_in_pizza = gegevens[2]
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
    lijst1 = bereken_aantal_pizzas(lijst2)
    # lijst1 = bereken_aantal_pizzas(lijst2[0], lijst2[1], lijst2[2])
    output(lijst1[0],lijst2[0],lijst1[1])


if __name__ == '__main__':
    main()    