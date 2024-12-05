"""
1. Calcular precio en funcion de la edad
2. Pedir la edad
    Validar que sea entero positivo
    Pedir edades hasta que se introduzca ""
3. Calcular el precio total del grupo
4. Mostrar el precio total y el desglose por tipo de entrada

"""

grupoPersonas = []
tipos_entradas = ["GRATUITA", "NINYOS", "ADULTOS", "JUBILADOS"]
precios = [0, 14, 23, 18]
contadores_entradas = [0, 0, 0, 0]
totales_entradas = [0, 0, 0, 0]
edades_umbral = [3, 13, 65, float('inf')]


def calculoPrecioYTipoBillete(edad):
    precio = 0
    tipo = 0

    for i, edad_umbral in enumerate(edades_umbral):
        if edad < edad_umbral:
            precio = precios[i]
            tipo = i
            break

    return precio, tipo

def validarEnteroPositivo(dato: str):
    try:
        int(dato)
        return True
    except ValueError:
        return False

while True:
    edad = input("Introduce la edad del visitante (deja vacio para terminar) ")
    if edad == "":
        break
    elif validarEnteroPositivo(edad):
        grupoPersonas.append(calculoPrecioYTipoBillete(int(edad)))

totalEntradas = 0
"""
totalNinyos = totalAdultos = totalJubilados = 0 
contadorNinyos = contadorAdultos = contadorJubilados = 0
for precio, tipo in grupoPersonas:
    totalEntradas += precio
    if tipo == NINYOS:
        totalNinyos += precio
        contadorNinyos += 1
    elif tipo == ADULTOS:
        totalAdultos += precio
        contadorAdultos += 1
    elif tipo == JUBILADOS:
        totalJubilados += precio
        contadorJubilados += 1

print(f"Precio totl del grupo: {totalEntradas:6.2f}")
print("Detalle por edades:")
print(""-"" * 25)
print(f"Niños (3-12 años): {contadorNinyos:2d} x 14 euros = {totalNinyos:6.2f}")                
print(f"Niños (13-64 años): {contadorAdultos:2d} x 23 euros = {totalAdultos:6.2f}")                
print(f"Niños (65+ años):  {contadorJubilados:2d} x 18 euros = {totalJubilados:6.2f}")                        
"""

for precio, tipo in grupoPersonas:
    totalEntradas += precio
    contadores_entradas[tipo] += 1
    totales_entradas[tipo] += precio

for i, tipo in enumerate(tipos_entradas):
    print(f"{contadores_entradas[i]:2d} entradas {tipo.lower()}: {totales_entradas[i]:6.2f} €")


