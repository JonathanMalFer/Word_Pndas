

import smtplib
import os
from email.message import EmailMessage


def enviar_correo(contenido, asunto, destinatario, remitente, clave, archivo_adjunto=None):
    # Crear el mensaje
    mensaje = EmailMessage()
    mensaje.set_content(contenido)
    mensaje['Subject'] = asunto
    mensaje['From'] = remitente
    mensaje['To'] = destinatario

    # Agregar archivo adjunto si existe
    if archivo_adjunto and os.path.isfile(archivo_adjunto):
        with open(archivo_adjunto, 'rb') as adjunto:
            mensaje.add_attachment(adjunto.read(),
                                   maintype='application',
                                   subtype=os.path.splitext(archivo_adjunto)[1],
                                   filename=os.path.basename(archivo_adjunto))

    # Configuración del servidor SMTP de Gmail
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(remitente, clave)
            servidor.send_message(mensaje)
            print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")


# Ejemplo de uso
contenido = "Este es el cuerpo del correo."
asunto = "Asunto del correo"
destinatario = "jonathanmldnd9@gmail.com"
remitente = "mendezangy200@gmail.com"
clave = "Angymendez03+"

enviar_correo(contenido, asunto, destinatario, remitente, clave)
