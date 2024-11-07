import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate


doc = DocxTemplate('plantilla.docx')

nombre ="Jonathan Maldonado"
telefono = "4272783448"
correo = "jonathan.maldonado.ferrer1@gmail.com"
fecha = datetime.today().strftime('%Y-%m-%d')

constantes = {'nombre':nombre, 'telefono':telefono, 'correo':correo
              ,'fecha':fecha}


df = pd.read_excel('plantilla_alumnos.xlsx')

# itero sobre la fila y la columna
for colum,fila in df.iterrows():
    # Lleno el diccionario
    #fila[df.columns[0] Obtengo el nombre de la columna del excel
    contenido = {'nombre_alumno':fila[df.columns[0]],
                 'nota_mat':fila[df.columns[1]],
                 'nota_fis':fila[df.columns[2]],
                 'nota_qui':fila[df.columns[3]],}
    contenido.update(constantes)
    doc.render(contenido)
    doc.save(f"prueba_"+fila['Nombre']+".docx")