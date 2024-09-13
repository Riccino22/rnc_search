import requests
import io
import zipfile

def get():
    url = "https://www.dgii.gov.do/app/WebApps/Consultas/RNC/DGII_RNC.zip"

    # Hacer una solicitud GET para obtener el archivo ZIP
    print("steps")
    response = requests.get(url, verify=False)
    text = ''
    print("Step 1")
    # Verificar que la solicitud fue exitosa
    if response.status_code == 200:
        print("Step 2")
        # Convertir el contenido en un archivo en memoria
        file_bytes = io.BytesIO(response.content)
        print("Step 3")
        # Abrir el archivo ZIP desde la memoria
        with zipfile.ZipFile(file_bytes, 'r') as zip_ref:
            # Listar los archivos en el ZIP
            print(zip_ref.namelist())

            # Leer un archivo específico dentro del ZIP
            print("Step 5")
            with zip_ref.open('TMP/DGII_RNC.TXT') as file:
                contenido = file.read()
#                print(contenido.decode('latin-1'))  # Decodificación en latin-1
                text = contenido.decode('latin-1')
                empresas  = text.split('\n')
                return empresas


#with open("DGII_RNC.TXT", encoding="latin-1") as file:
#    contenido = file.read()
    #                print(contenido.decode('latin-1'))  # Decodificación en latin-1



#empresas = contenido.split("\n")
empresas = get()
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
