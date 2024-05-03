import smtplib

def mail_inscription(mail_receiver:str) -> None:
    # Établir une connexion SMTP sécurisée avec le serveur mailersenders
    server = smtplib.SMTP('smtp.mailersend.net', 587)
    server.starttls()  # Activer le mode TLS (Transport Layer Security)

    # Créer le message à envoyer
    sujet = "le chat de pallas : inscription server"
    corps_du_message = "Hello, ceci est un e-mail envoyé depuis Python ! Tu es bien inscript sur le server "
    msg = f'Subject: {sujet}\n\n{corps_du_message}'.encode('utf-8')


    # Envoyer l'e-mail
    server.sendmail("MS_LSSQpN@trial-jy7zpl93o5pl5vx6.mlsender.net", mail_receiver, msg)

    # Fermer la connexion
    server.quit()
