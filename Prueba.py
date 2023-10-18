import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
cantidad = int(input("Ingresa la cantidad de caracteres que quieres que tenga tu contraseña"))
contrasena = ""
for i in range(cantidad):
    x = random.randint(0, len(caracteres) - 1)
    y = caracteres[x]
    contrasena += y
print(contrasena)
