#EJERCICIO BLACK JACK

print("\n\n")

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

print(cartas)
print("\n\n")
print("Cartas: {}".format(" ".join(cartas.keys())))
print("\n")
print("Putos: {}".format(list(cartas.values())))

print("\n")

for carta, valor in cartas.items():
    print("La carta {} vale {} puntos".format(carta, valor))
