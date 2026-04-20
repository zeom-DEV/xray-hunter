import streamlit as st
import urllib.parse

# Configuration de la page
st.set_page_config(page_title="Moez Thabet | Quantum V17 Pro", page_icon="🧬", layout="wide")

# Style Custom (Thème Matrix/Dark)
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00FF41; }
    .stTextInput>div>div>input { background-color: #050505; color: #00FF41; border: 1px solid #00FF41; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #111; border: 1px solid #333; color: white; border-radius: 5px; padding: 10px;
    }
    .stTabs [aria-selected="true"] { border-color: #00FF41; color: #00FF41; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧬 THE QUANTUM V17.1 - SOURCING DASHBOARD")
st.write("**Architecte Système : Moez Thabet** | Stratégie d'Exploitation de Données")

# Initialisation du Session State pour garder les résultats affichés
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

c1, c2 = st.columns([2, 1])
with c1:
    job = st.text_input("🎯 Métier (ex: \"Chef d'équipe\")", value="Chef d'équipe")
    loc = st.text_input("📍 Zone (ex: Creuse OR 23000)", value="Guéret OR Creuse OR 23000")
with c2:
    st.info("🚀 **Optimisation V17.1 :** Les filtres de recherche ont été durcis pour éliminer 80% du bruit (dates, doublons, documents administratifs).")

def generate_queries(j, l):
    # Protection des expressions exactes
    if not j.startswith('"'): j = f'"{j}"'
    
    # 1. SNIPER (Focus Emails & Patterns mobiles plus précis)
    # On cherche des patterns de mails ou des indicateurs de contact direct
    q_sniper = f'site:linkedin.com/in/ {j} ({l}) ("@gmail.com" OR "@outlook.fr" OR "@orange.fr" OR "contactez-moi")'
    
    # 2. SCOUT (Clean LinkedIn Search)
    q_scout = f'site:linkedin.com/in/ {j} ({l}) -intitle:offres -inurl:jobs'
    
    # 3. MINER (Extraction de CV PDF réels)
    # Utilisation de intitle et de patterns de fichiers pour éviter les rapports gouv/pro
    q_miner = f'filetype:pdf (intitle:CV OR intitle:Resume) {j} ({l}) -inurl:offre -site:gouv.fr'
    
    return q_sniper, q_scout, q_miner

if st.button("DÉPLOYER LE SCAN MULTI-NIVEAUX", use_container_width=True):
    if job:
        st.session_state.clicked = True
    else:
        st.error("Veuillez saisir un métier.")

# Affichage permanent si le bouton a été cliqué une fois
if st.session_state.clicked:
    q_sniper, q_scout, q_miner = generate_queries(job, loc)
    
    tab1, tab2, tab3 = st.tabs(["🎯 SNIPER (Contacts)", "🔍 SCOUT (Volume)", "📄 MINER (Documents)"])
    
    with tab1:
        st.subheader("Objectif : Coordonnées directes")
        st.write("Cible les profils ayant laissé une adresse mail publique ou un appel à l'action.")
        st.link_button("LANCER LE SCAN SNIPER", f"https://www.google.com/search?q={urllib.parse.quote(q_sniper)}")
        st.code(q_sniper, language="text")

    with tab2:
        st.subheader("Objectif : Visibilité Totale")
        st.write("Affiche tous les profils indexés sur la zone géographique sans filtrage restrictif.")
        st.link_button("LANCER LE SCAN SCOUT", f"https://www.google.com/search?q={urllib.parse.quote(q_scout)}")
        st.code(q_scout, language="text")

    with tab3:
        st.subheader("Objectif : CVs PDF Indexés")
        st.write("Recherche spécifiquement des fichiers PDF nommés 'CV' pour extraction directe.")
        st.link_button("LANCER LE SCAN MINER", f"https://www.google.com/search?q={urllib.parse.quote(q_miner)}")
        st.code(q_miner, language="text")
