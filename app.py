import dns.resolver
import smtplib
import socket

def verify_email(email):
    # Séparer le nom et le domaine
    try:
        name, domain = email.split('@')
    except ValueError:
        return f"❌ Format invalide : {email}"

    # 1. Trouver le serveur mail (MX Record) du domaine
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)
    except Exception:
        return f"❌ Aucun serveur mail trouvé pour {domain}"

    # 2. Ping SMTP (Simuler l'envoi pour voir si l'adresse existe)
    try:
        # Se connecter au serveur
        server = smtplib.SMTP(timeout=3)
        server.set_debuglevel(0)
        server.connect(mx_record)
        server.helo(socket.getfqdn())
        server.mail('hello@ton-domaine.com') # Ton adresse d'expéditeur
        
        # Poser la question au serveur cible
        code, message = server.rcpt(str(email))
        server.quit()

        # Si le serveur répond 250, l'email existe et est valide !
        if code == 250:
            return f"✅ VALIDE : {email}"
        else:
            return f"❌ Invalide (Code {code}) : {email}"

    except Exception as e:
        return f"⚠️ Erreur de connexion : {email}"

# --- Exemple d'utilisation dans ton agence ---
# Tu as trouvé "Jean Dupont" chez "Decathlon"
candidat_tests = [
    "jean.dupont@decathlon.com",
    "j.dupont@decathlon.com",
    "jdupont@decathlon.com"
]

for test in candidat_tests:
    resultat = verify_email(test)
    print(resultat)
    if "✅" in resultat:
        break # On arrête de chercher dès qu'on a trouvé le bon !
