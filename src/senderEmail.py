import smtplib
from email.mime.text import MIMEText

def sendmail(email):
    sender = ""
    receiver = email
    password = ""  # Usa un método seguro para manejar contraseñas
    subject = "Asunto del correo"
    body = "Bienvenido a nuestra web"
    
    msg = MIMEText(body, "plain")
    msg["From"] = sender  # Aquí debería ser 'sender', no 'sendmail'
    msg["To"] = receiver
    msg["Subject"] = subject
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)  # Usa 'sender', no 'sender_email'
        server.sendmail(sender, receiver, msg.as_string())  # Usa 'sender' y 'receiver'
    
    print("Correo Enviado")

# Llamada a la función con un email de prueba
sendmail("destinatario@example.com")
