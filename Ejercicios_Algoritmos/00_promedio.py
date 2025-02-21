""" Se ingresan 35 números, al finalizar informar cuales y cuántos de ellos superan el promedio de los mismos. """

numeros = [float(input(f"ingresa un numero {i+1}: ")) for i in range(6)] 

promedio = sum (numeros) / len(numeros) 
superan_promedio = [num for num in numeros if num > promedio]


print(f"El promedio es: {promedio}")
print(f"Números que superan el promedio: {superan_promedio}")
print(f"Cantidad que superan el promedio: {len(superan_promedio)}")





