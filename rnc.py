with open("DGII_RNC.TXT", encoding="latin-1") as file:
    contenido = file.read()
    #                print(contenido.decode('latin-1'))  # Decodificación en latin-1


empresas = contenido.split("\n")
empresa1 = empresas[1].split("|")[0]

data = []
for emp in empresas:
    info = emp.split("|")
    try:
        data.append(
            {
                "rnc": info[0],
                "nombre": info[1],
            }
        )
    except IndexError:
        pass

print(data[5])
