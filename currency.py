pesos = (int(input("What do you have left in pesos? ")))
soles = (int(input("What do you have left in soles? ")))
reais = (int(input("What do you have left in reais? ")))

co = 0.00031
pe = 0.29
br = 0.2

pesos = pesos * co
soles = soles * pe
reais = reais * br

usd = pesos + soles + reais
print(usd)