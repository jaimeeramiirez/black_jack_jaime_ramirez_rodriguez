#EJERCICIO BLACK JACK
import reglas_juego

from random import choice, sample


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


lista_cartas = list(cartas)
print("\n")


print("Ha seleccionado:", end=" ")
carta = choice(lista_cartas)
score = cartas[carta]
print(carta, end=" ")
carta = choice(lista_cartas)
print(carta, end=" ")
score += cartas[carta]
print(" >>> su puntuación es de", score)

main_banca = sample(lista_cartas, 2)
score_banca = sum(cartas[carta] for carta in main_banca)
print("La banca tiene: {} {}  >> su score es {}".format(main_banca[0], main_banca[1], score_banca))

