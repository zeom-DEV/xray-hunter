import streamlit as st
import urllib.parse
import re

# Configuration de la page
st.set_page_config(page_title="Moez Thabet | The Quantum V17.2", page_icon="🧬", layout="wide")

# Style CSS Custom
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00FF41; }
    .stTextInput>div>div>input { background-color: #050505; color: #00FF41; border: 1px solid #00FF41; }
    /* Stylisation du nouveau bouton natif Streamlit */
    div[data-testid="stLinkButton"] > a { 
        background-color: #00FF41 !important; 
        color: black !important; 
        font-weight: bold; 
        width: 100%; 
        border: none; 
        text-align: center; 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧬 THE QUANTUM V17.2 - SOURCING DASHBOARD")
st.write("**Architecte Système : Moez Thabet** | Recherche de CVs (X-Ray Search)")

# 1. CORRECTION ARCHITECTURE : Gestion de l'état pour ne pas perdre l'affichage
if 'scan_active' not in st.session_state:
    st.session_state.scan_active = False

c1, c2 = st.columns([2, 1])
with c1:
    job = st.text_input("🎯 Métier (ex: Chef d'équipe OR Superviseur)", value="Chef d'équipe")
    loc = st.text_input("📍 Zone (ex: Guéret OR Creuse OR 23000)", value="Guéret OR Creuse OR 23000")
with c2:
    st.info("💡 **Correction :** Conservation de l'affichage (Session State) et optimisation X-Ray pour extraire les vrais CVs.")

def clean_input(text):
    # 2. CORRECTION SYNTAXE : Enlève les espaces en trop qui causaient les "0 résultats"
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

# Déclencheur du scan
if st.button("DÉPLOYER LE SCAN MULTI-NIVEAUX", use_container_width=True):
    if job and loc:
        st.session_state.scan_active = True
    else:
        st.error("Veuillez remplir les champs Métier et Zone.")

# Affichage persistant après le clic
if st.session_state.scan_active:
    j = clean_input(job)
    l = clean_input(loc)
    
    # --- LOGIQUE D'EXTRACTION OPTIMISÉE ---
    
    # LE MINER (La solution pour les CVs : PDF, Titre = CV, Exclusion des offres)
    q_miner = f'filetype:pdf (intitle:cv OR intitle:resume OR intitle:curriculum) ({j}) ({l}) -offre -emploi -template -modele'
    
    # LE SCOUT (Pour voir tout le monde sur LinkedIn sans bloquer sur l'email)
    q_scout = f'site:linkedin.com/in/ ({j}) ({l}) -intitle:offres -inurl:jobs'

    # LE SNIPER (Emails directs : à n'utiliser que sur les grandes villes)
    q_sniper = f'site:linkedin.com/in/ ({j}) ({l}) ("@gmail.com" OR "@orange.fr" OR "@yahoo.fr")'

    # 3. CORRECTION UI : Création des onglets
    tab1, tab2, tab3 = st.tabs(["📄 MINER (Les CVs PDF)", "🔍 SCOUT (LinkedIn Large)", "🎯 SNIPER (Emails)"])
    
    with tab1:
        st.subheader("La solution infaillible pour les CVs ciblés")
        st.write("Force Google à ne lire que les titres de fichiers PDF, en excluant les templates payants et les annonces Pôle Emploi.")
        # Utilisation de st.link_button au lieu de balises HTML dangereuses
        st.link_button("LANCER LE SCAN MINER", f"https://www.google.com/search?q={urllib.parse.quote(q_miner)}")
        st.code(q_miner, language="text")

    with tab2:
        st.subheader("Bassin de candidats global")
        st.write("Affiche tous les profils de la zone géographique sans imposer de restriction d'adresse mail.")
        st.link_button("LANCER LE SCAN SCOUT", f"https://www.google.com/search?q={urllib.parse.quote(q_scout)}")
        st.code(q_scout, language="text")

    with tab3:
        st.subheader("Contact direct (Attention : Villes Denses uniquement)")
        st.write("Cherche publiquement les emails. Les résultats seront souvent à zéro dans les villes moyennes.")
        st.link_button("LANCER LE SCAN SNIPER", f"https://www.google.com/search?q={urllib.parse.quote(q_sniper)}")
        st.code(q_sniper, language="text")
