import streamlit as st
import urllib.parse
from datetime import datetime

# Configuration Ultra-Premium
st.set_page_config(page_title="Moez Thabet | OSINT Sourcing Machine", page_icon="🕵️‍♂️", layout="wide")

# UI Styling (Dark Gold & Professional)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stButton>button { 
        background: linear-gradient(135deg, #ffd700 0%, #b8860b 100%); 
        color: black; border: none; padding: 15px; font-weight: bold; width: 100%; border-radius: 10px;
    }
    .result-box { background-color: #1a1c23; padding: 20px; border-radius: 15px; border-left: 5px solid #ffd700; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ OSINT Sourcing Machine v6.0")
st.write(f"**Expert Système : Moez Thabet** | Stratégie d'extraction de données réelles (CV & Mail)")

# --- Sidebar Configuration ---
with st.sidebar:
    st.header("🎯 Objectif de Recherche")
    target_type = st.radio("Que cherchez-vous ?", ["Direct CV (PDF/Docs)", "LinkedIn + Public Mail", "GitHub Tech Leads"])
    freshness = st.toggle("Profils récents (2025-2026)", value=True)

# --- Inputs ---
c1, c2 = st.columns(2)
with c1:
    role = st.text_input("🎯 Poste (ex: Développeur, Commercial)", placeholder="Indispensable")
    location = st.text_input("📍 Ville / Pays", placeholder="ex: Tunis, France")
with c2:
    keywords = st.text_input("🔑 Mots-clés / Compétences", placeholder="ex: Python, B2B, Sales")
    provider = st.multiselect("📧 Domaines Email (si LinkedIn)", ["gmail.com", "outlook.com", "proton.me", "yahoo.fr"])

# --- Logic Engine ---
def build_concrete_query(role, location, keywords, target_type, provider):
    query = ""
    
    if target_type == "Direct CV (PDF/Docs)":
        # Cherche directement des fichiers PDF/DOCX indexés par Google (Vrais CVs)
        query = f'(intitle:resume OR intitle:cv OR intitle:curriculum) filetype:pdf "{role}"'
        if location: query += f' "{location}"'
        if keywords: query += f' "{keywords}"'
        
    elif target_type == "LinkedIn + Public Mail":
        # Force Google à trouver des mails écrits dans la bio ou le post
        email_str = " OR ".join([f'"{p}"' for p in provider]) if provider else '"@gmail.com"'
        query = f'site:linkedin.com/in/ "{role}"'
        if location: query += f' "{location}"'
        if keywords: query += f' "{keywords}"'
        query += f' ({email_str}) -inurl:jobs -intitle:recrutement'
        
    elif target_type == "GitHub Tech Leads":
        # Cherche les mails dans les fichiers README ou profils GitHub
        query = f'site:github.com "{role}" "{location}" "@gmail.com"'
    
    return query

# --- Execution ---
if st.button("🚀 LANCER L'EXTRACTION DE DONNÉES"):
    if role:
        final_query = build_concrete_query(role, location, keywords, target_type, provider)
        tbs = "&tbs=qdr:y" if freshness else ""
        search_url = f"https://www.google.com/search?q={urllib.parse.quote(final_query)}{tbs}"
        
        st.markdown(f'<div class="result-box">', unsafe_allow_html=True)
        st.info("✅ Stratégie d'extraction générée avec succès.")
        st.code(final_query)
        
        st.markdown(f"""
            <a href="{search_url}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#ffd700; color:black; padding:18px; text-align:center; border-radius:8px; font-weight:bold; font-size:1.2em;">
                    ACCÉDER AUX DOCUMENTS ET EMAILS RÉELS
                </div>
            </a>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.warning("💡 **Note :** Si vous cherchez des CVs, les résultats Google seront des liens de téléchargement direct PDF.")
    else:
        st.error("L'intitulé du poste est obligatoire.")

st.divider()
st.caption(f"Propulsé par la technologie OSINT - Moez Thabet © {datetime.now().year}")
    
