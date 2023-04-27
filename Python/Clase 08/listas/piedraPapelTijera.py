from random import choice

opciones = ["piedra", "papel", "tijera"]

computadora = choice(opciones)

print("\n bienvenido al juego piedra , papel y tijera")
print("--------------------------------------------- \n")


persona = input("ingresa una opcion: ").lower()


if computadora == persona:
    print("Es empate, Ya que eligieron lo mismo")

if computadora == "piedra" and persona == "tijera":
    print(f"Gano la computadora , ya que eligio  {computadora} y la persona eligio {persona}")
    
if computadora == "papel" and persona == "tijera":
    print(f"Gano la persona , ya que eligio {persona} y la computadora eligio {computadora}")

if computadora == "piedra" and persona == "papel":
     print(f"Gano la persona , ya que eligio {persona} y la computadora eligio {computadora}")


if computadora == "tijera" and persona == "papel":
     print(f"Gano la computadora , ya que eligio {computadora} y la persona eligio {persona}")

if computadora == "tijera" and persona == "piedra":
     print(f"Gano la persona , ya que eligio {persona} y la computadora eligio {computadora}")

if computadora == "papel" and persona == "piedra":
     print(f"Gano la computadora , ya que eligio {computadora} y la persona eligio {persona}")