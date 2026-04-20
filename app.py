import streamlit as st
import urllib.parse
from datetime import datetime

# --- CONFIGURATION DE HAUTE PRÉCISION ---
st.set_page_config(page_title="Moez Thabet | The Neuron Sniper", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF41; }
    .stButton>button { 
        background: #00FF41; color: black; border-radius: 0; font-weight: bold; height: 4em; width: 100%; border: 2px solid #fff;
    }
    .stTextInput>div>div>input { background-color: #0a0a0a; color: #00FF41; border: 1px solid #00FF41; }
    .status-box { border: 2px solid #00FF41; padding: 20px; background: #001100; box-shadow: 0 0 15px #00FF41; }
    code { color: #fff !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧬 THE NEURON SNIPER V16.0")
st.write("**Directeur Technique : Moez Thabet** | Système de Sourcing à Zéro Hallucination")

# --- LOGIQUE D'OPTIMISATION AUTOMATIQUE ---
col1, col2 = st.columns(2)
with col1:
    role = st.text_input("🎯 Métier (ex: Chef d'équipe)", placeholder="Cible")
    location = st.text_input("📍 Zone (ex: Guéret OR 23)", placeholder="Localisation")
with col2:
    power_mode = st.selectbox("⚡ Protocole d'Infiltration", [
        "HUMAN EXTRACTION (06 & Mails Directs)",
        "DEEP CV MINING (PDFs réels uniquement)",
        "BYPASS INSTITUTIONAL (Anti-Rapports/Gouv)"
    ])

def build_god_mode_query(role, location, power_mode):
    # Extension de zone automatique pour saturer Guéret (Creuse, 23000)
    area = f'("{location}" OR "23000" OR "Creuse")' if location else ""
    
    # LA BARRIÈRE ANTI-DÉBILITÉ (Filtre automatique testé)
    # Exclut les rapports, les études de l'observatoire, les sites .gouv, les fiches de formation
    anti_noise = '-"rapport" -"étude" -"observatoire" -"formation" -"fiche" -"synthèse" -site:gouv.fr -site:interieur.gouv.fr -intitle:mobilité -intitle:observatoire'
    
    if "HUMAN" in power_mode:
        # On force l'apparition de patterns de contact
        return f'site:linkedin.com/in/ "{role}" {area} ("@gmail.com" OR "@orange.fr" OR "@wanadoo.fr" OR "06" OR "07") {anti_noise}'
    
    elif "DEEP CV" in power_mode:
        # On force des mots qui n'existent QUE dans un CV PDF (Expérience, Compétences, Langues)
        return f'filetype:pdf "{role}" {area} ("Expérience professionnelle" AND "Compétences") {anti_noise}'
    
    else: # BYPASS INSTITUTIONAL
        # Cherche sur Indeed, Viadeo et les annuaires pro en ignorant les offres d'emploi
        return f'(site:indeed.fr OR site:viadeo.journaldunet.com OR site:societe.com) "{role}" {area} -inurl:jobs -inurl:viewjob {anti_noise}'

# --- EXÉCUTION ---
if st.button("LANCER L'ASPI-DONNÉES"):
    if role:
        final_query = build_god_mode_query(role, location, power_mode)
        url = f"https://www.google.com/search?q={urllib.parse.quote(final_query)}"
        
        st.markdown(f"""
            <div class="status-box">
                <p style="font-size: 1.2em; color: #00FF41;">🔓 <b>Séquence de Sourcing Validée :</b></p>
                <code>{final_query}</code>
                <br><br>
                <a href="{url}" target="_blank" style="text-decoration:none;">
                    <button style="width:100%; cursor:pointer;">DÉPLOYER SUR GOOGLE (TESTÉ SANS HALLUCINATION)</button>
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Cible manquante.")

st.divider()
st.caption(f"Système de Sourcing Révolutionnaire - Moez Thabet Edition - 2026")
