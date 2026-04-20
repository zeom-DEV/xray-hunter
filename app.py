import streamlit as st
import dns.resolver
import smtplib
import socket

# Configuration de la page
st.set_page_config(page_title="Quantum SMTP | Moez Thabet", page_icon="⚡", layout="centered")

# Style CSS Custom pour garder l'ambiance "Quantum"
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00FF41; }
    .stTextInput>div>div>input { background-color: #050505; color: #00FF41; border: 1px solid #00FF41; }
    div[data-testid="stButton"] > button { 
        background-color: #00FF41 !important; 
        color: black !important; 
        font-weight: bold; 
        width: 100%; 
        border: none; 
    }
    .result-box { border: 1px solid #333; padding: 15px; border-radius: 5px; background-color: #111; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ QUANTUM SMTP VALIDATOR")
st.write("**Architecte : Moez Thabet** | Validation d'emails B2B sans base de données")

st.info("💡 **Comment ça marche ?** L'outil génère les combinaisons d'emails possibles et interroge directement le serveur de l'entreprise (Ping SMTP) pour savoir laquelle est réelle, sans envoyer de message.")

# Interface utilisateur
col1, col2 = st.columns(2)
with col1:
    prenom = st.text_input("👤 Prénom", placeholder="Ex: Jean").strip().lower()
    nom = st.text_input("👤 Nom", placeholder="Ex: Dupont").strip().lower()
with col2:
    domaine = st.text_input("🏢 Domaine entreprise", placeholder="Ex: decathlon.com").strip().lower()

def generate_patterns(p, n, d):
    """Génère les combinaisons d'emails B2B les plus courantes"""
    return [
        f"{p}.{n}@{d}",
        f"{p[0]}{n}@{d}",
        f"{p}{n[0]}@{d}",
        f"{p}@{d}",
        f"{n}@{d}",
        f"{p}_{n}@{d}"
    ]

def verify_email(email):
    """Fait un Ping SMTP pour vérifier si l'adresse existe"""
    try:
        name, domain = email.split('@')
        # 1. Chercher le serveur mail
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)
        
        # 2. Se connecter au serveur (Timeout de 3s pour ne pas bloquer)
        server = smtplib.SMTP(timeout=3)
        server.set_debuglevel(0)
        server.connect(mx_record)
        server.helo(socket.getfqdn())
        server.mail('contact@ton-domaine.com')
        
        # 3. Poser la question
        code, message = server.rcpt(str(email))
        server.quit()
        
        if code == 250:
            return True, f"✅ VALIDE : **{email}**"
        else:
            return False, f"❌ Rejeté (Code {code}) : {email}"
            
    except smtplib.SMTPConnectError:
         return False, f"⚠️ Connexion SMTP bloquée (Le serveur refuse le ping) : {email}"
    except Exception as e:
        return False, f"⚠️ Erreur ou Timeout sur : {email}"

if st.button("LANCER LE SCAN (PING SERVEUR)"):
    if prenom and nom and domaine:
        with st.spinner("Analyse DNS et Ping des serveurs en cours..."):
            emails_to_test = generate_patterns(prenom, nom, domaine)
            
            st.write("### 📊 Résultats du Scan :")
            success_found = False
            
            # Tester chaque email généré
            for email in emails_to_test:
                is_valid, message = verify_email(email)
                if is_valid:
                    st.success(message)
                    success_found = True
                    break # On arrête dès qu'on trouve le bon !
                else:
                    st.write(message)
            
            if not success_found:
                st.warning("Aucune adresse valide trouvée. Le serveur est peut-être protégé (Catch-all) ou le port de scan est bloqué par l'hébergeur.")
    else:
        st.error("Veuillez remplir tous les champs (Prénom, Nom, Domaine).")
