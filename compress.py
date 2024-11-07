import os
import zipfile

def comprimir_docx(carpeta, nombre_zip):
    # Crear el archivo ZIP
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        # Recorrer todos los archivos en la carpeta
        for root, _, files in os.walk(carpeta):
            for file in files:
                # Comprobar si el archivo tiene extensión .docx
                if file.endswith('.docx'):
                    # Ruta completa del archivo
                    ruta_archivo = os.path.join(root, file)
                    # Añadir el archivo al ZIP
                    zipf.write(ruta_archivo, os.path.relpath(ruta_archivo, carpeta))
                    print(f"Archivo '{file}' añadido a '{nombre_zip}'.")

# Usar la función
carpeta = '/home/jona/PycharmProjects/Word_pandas'  # Cambia esto a la ruta de tu carpeta con archivos .docx
nombre_zip = 'archivos_comprimidos.zip'  # Nombre del archivo zip de salida
comprimir_docx(carpeta, nombre_zip)
