"""
1. Calcular precio en funcion de la edad
2. Pedir la edad
    Validar que sea entero positivo
    Pedir edades hasta que se introduzca ""
3. Calcular el precio total del grupo
4. Mostrar el precio total y el desglose por tipo de entrada

"""

catalogo_entradas = {
    "GRATUITA": {"precio": 0, "e_umbral": 3},
    "NINYOS": {"precio": 14, "e_umbral": 13},
    "ADULTOS": {"precio": 23, "e_umbral": 65},
    "JUBILADOS": {"precio": 18, "e_umbral": float('inf')},
}

def calculoPrecioYTipoBillete(edad):
    precio = 0
    tipo = 0

    for tipo in catalogo_entradas:
        if edad < catalogo_entradas[tipo]["e_umbral"]:
            precio = catalogo_entradas[tipo]["precio"]
            break

    return precio, tipo

def validarEnteroPositivo(dato: str):
    try:
        int(dato)
        return True
    except ValueError:
        return False

def tramitarEntradas(precioTotal, grupoPersonas, factura):    
    while True:
        edad = input("Introduce la edad del visitante (deja vacio para terminar) ")
        if edad == "":
            break
        elif validarEnteroPositivo(edad):
            grupoPersonas.append(calculoPrecioYTipoBillete(int(edad)))

    num_entradas = len(grupoPersonas)


    for precio, tipo in grupoPersonas:
        precioTotal += precio
        factura[tipo] += 1
    

    for clave in factura:
        print(f"{factura[clave]:2d} entradas {clave.lower()}: {factura[clave] * catalogo_entradas[clave]["precio"]:6.2f} €")

    print("-" * 25)
    print(f"Numero de entradas: {num_entradas:3d}")
    print(f"Total a pagar......: {precioTotal:.2f} €")

while True:
    precioTotal = 0
    grupoPersonas = []
    factura = {
        "GRATUITA": 0,
        "NINYOS": 0,
        "ADULTOS": 0,
        "JUBILADOS": 0
    }     
    tramitarEntradas(precioTotal, grupoPersonas, factura)
    print("-" * 25)
    continuar = input("Continuar s/n [s]")
    if continuar.lower() == "n":
        break


