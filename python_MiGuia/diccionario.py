
edificio = {"A" : [1,0,0],"B" : [2,0,2],"C" : [3,0,0],"D" : [5,0,0],"E" : [3,0,0] }

for clave, valor in edificio.items():
    print(f"{clave}: {valor}")

print("----------------")

edificio = {"A" : [0,0,0],"B" : [0,0,0],"C" : [0,0,0],"D" : [0,0,0],"E" : [0,0,0] }
edificio["A"][0] += 3
edificio["C"][1] += 2
edificio["A"][2] += 1
for clave, valor in edificio.items():
    print(f"{clave}: {valor}")

print("----------------")