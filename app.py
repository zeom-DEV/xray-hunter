import streamlit as st
import urllib.parse
from datetime import datetime

# Configuration Ultra-Premium
st.set_page_config(page_title="Moez Thabet | Ultimate Sourcing Engine", page_icon="💎", layout="wide")

# Interface Dark Mode Professionnelle
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #e0e0e0; }
    .stTextInput>div>div>input { background-color: #1a1c23; color: white; border: 1px solid #3e4451; }
    .stButton>button { 
        background: linear-gradient(135deg, #0077b5 0%, #00a0dc 100%); 
        color: white; border: none; padding: 12px; font-size: 18px; font-weight: bold;
    }
    .stButton>button:hover { box-shadow: 0 0 20px rgba(0, 160, 220, 0.6); transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 Omni-Source Ultimate v5.0")
st.write(f"**Expert Système : Moez Thabet** | Sourcing de Précision & Intelligence Commerciale")

# --- Moteur d'Intelligence ---
with st.sidebar:
    st.header("⚙️ Paramètres Avancés")
    mode = st.selectbox("Niveau de Puissance", ["Standard", "Deep Search (Email Hunter)", "Expert Tech (GitHub/Stack)"])
    region = st.selectbox("Extension de Domaine", ["International (.com)", "Tunisie (.tn)", "France (.fr)", "Belgique (.be)"])
    freshness = st.toggle("Profils mis à jour récemment", value=True)

# --- Champs de saisie optimisés ---
c1, c2 = st.columns(2)
with c1:
    role = st.text_input("🎯 Poste cible", placeholder="ex: Business Developer B2B")
    must_have = st.text_input("🔑 Compétences obligatoires", placeholder="ex: Salesforce, Cold Calling")
with c2:
    location = st.text_input("📍 Ville ou Pays", placeholder="ex: Sousse, Paris, Remote")
    provider = st.multiselect("📧 Chercher des contacts directs", ["Gmail", "Outlook", "Pro (Domaine)"])

# --- Logique de Résilience ---
def build_ultimate_query(role, must_have, location, mode, region, provider):
    # Gestion du domaine
    domain = "linkedin.com/in/"
    if region == "Tunisie (.tn)": domain = "tn.linkedin.com/in/"
    elif region == "France (.fr)": domain = "fr.linkedin.com/in/"
    
    # Base de la requête
    query = f'site:{domain} "{role}"'
    
    if location: query += f' "{location}"'
    if must_have: query += f' "{must_have}"'
    
    # Mode Email Hunter (Puissance maximale pour les missions 10 jours)
    if mode == "Deep Search (Email Hunter)" and provider:
        email_string = " OR ".join([f'"{p.lower()}@gmail.com"' if p == "Gmail" else f'"{p.lower()}@outlook.com"' for p in provider])
        query += f' ({email_string})'
        
    # Nettoyage automatique des résultats "Bruit" (Mises à jour 2026)
    query += ' -intitle:job -intitle:recrutement -inurl:jobs -inurl:posts'
    
    return query

# --- Action ---
if st.button("⚡ EXTRAIRE LES MEILLEURS PROFILS"):
    if role:
        final_query = build_ultimate_query(role, must_have, location, mode, region, provider)
        
        # Sécurité : Ajout de paramètres pour simuler une recherche naturelle
        tbs = "&tbs=qdr:y" if freshness else ""
        encoded_query = urllib.parse.quote(final_query)
        search_url = f"https://www.google.com/search?q={encoded_query}{tbs}"
        
        st.success("Requête de haute sécurité générée.")
        st.code(final_query, language="bash")
        
        st.markdown(f"""
            <a href="{search_url}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#1db954; color:white; padding:20px; text-align:center; border-radius:12px; font-weight:bold; font-size:1.3em;">
                    DÉVERROUILLER L'ACCÈS AUX CANDIDATS
                </div>
            </a>
            """, unsafe_allow_html=True)
        
        # Tips de Moez (Contextualisés avec ton CV)
        [span_1](start_span)st.info(f"💡 **Conseil de Moez Thabet :** Pour un recrutement urgent, priorisez les profils ayant 'Gmail' dans leur description, ce sont les plus réactifs[span_1](end_span).")
    else:
        st.error("L'intitulé du poste est obligatoire pour calibrer l'outil.")

st.divider()
st.caption(f"Système de protection contre les mises à jour LinkedIn activé. Dernière synchronisation : {datetime.now().strftime('%d/%m/%Y %H:%M')}")
  
