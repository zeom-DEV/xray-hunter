import streamlit as st
import urllib.parse
from datetime import datetime

st.set_page_config(page_title="Moez Thabet | The Kraken V11", page_icon="🐙", layout="wide")

# Design "Cyber-Recruiter"
st.markdown("""
    <style>
    .stApp { background-color: #000500; color: #00FF41; }
    .stButton>button { 
        background: #00FF41; color: black; border-radius: 0; font-weight: bold; height: 4em; border: 2px solid #fff;
    }
    .stTextInput>div>div>input { background-color: #050505; color: #00FF41; border: 1px solid #00FF41; }
    .kraken-box { border: 3px double #00FF41; padding: 20px; background: #001100; }
    </style>
    """, unsafe_allow_html=True)

st.title("🐙 THE KRAKEN V11.0 - DEEP SOURCING")
st.write("**Directeur d'Opération : Moez Thabet** | Extraction hors-réseaux")

col1, col2 = st.columns(2)
with col1:
    job = st.text_input("🎯 Métier (ex: Chef d'équipe)", placeholder="Cible")
    loc = st.text_input("📍 Zone (ex: Guéret OR Creuse)", placeholder="Localisation")
with col2:
    method = st.selectbox("🚀 Méthode d'Infiltration", [
        "DATABASE : Fichiers Excel/Membres (xls/csv)", 
        "BYPASS : CV Indeed & France Travail",
        "LEAK : Listes d'entreprises & Annuaire Pro",
        "SOCIAL : Profils avec Mobile Direct"
    ])

def build_kraken_query(job, loc, method):
    area = f'("{loc}")' if loc else ""
    
    if "Excel" in method:
        # Cherche des listes de contacts, des annuaires d'adhérents ou des tableaux de bord
        return f'filetype:xlsx OR filetype:csv "{job}" {area} (contact OR email OR tel OR portable)'
    
    elif "Indeed" in method:
        # Bypass Indeed pour voir les CV sans payer le compte recruteur
        return f'site:indeed.fr/resume "{job}" {area} -inurl:login -inurl:search'
    
    elif "Annuaire" in method:
        # Cherche dans les annuaires spécialisés (BTP, Industrie) et les listes de membres
        return f'intitle:"liste des" OR intitle:"annuaire" "{job}" {area} (BTP OR Industrie)'
    
    else: # Social Mobile
        return f'site:linkedin.com/in/ "{job}" {area} ("06" OR "07" OR "@gmail.com")'

if st.button("LANCER L'ASPI-DONNÉES"):
    if job:
        query = build_kraken_query(job, loc, method)
        url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
        
        st.markdown(f"""
            <div class="kraken-box">
                <p>⚡ <b>Séquence d'attaque générée :</b></p>
                <code>{query}</code>
                <br><br>
                <a href="{url}" target="_blank" style="text-decoration:none;">
                    <button style="width:100%; cursor:pointer;">
                        DÉPLOYER LE KRAKEN SUR GOOGLE
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Précise la cible.")

st.divider()
st.caption(f"Système de Sourcing Révolutionnaire - Moez Thabet Edition - {datetime.now().year}")
