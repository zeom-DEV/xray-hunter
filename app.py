import streamlit as st
import urllib.parse

st.set_page_config(page_title="Moez Thabet | Sourcing Pro", page_icon="⚡", layout="wide")

# Style Ultra-Rapide
st.markdown("""
    <style>
    .stApp { background-color: #111; color: #fff; }
    .stButton>button { background: #ff4b4b; color: white; width: 100%; font-weight: bold; height: 3.5em; border-radius: 8px; }
    .stTextInput>div>div>input { background-color: #222; color: #fff; border: 1px solid #444; }
    .res-box { background: #1a1a1a; padding: 20px; border-radius: 10px; border: 1px solid #ff4b4b; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Moteur de Sourcing de Choc")
st.write("**Développé par Moez Thabet** | Objectif : Zéro résultat vide.")

col1, col2 = st.columns(2)
with col1:
    job = st.text_input("🎯 Quel métier ?", placeholder="ex: Chef d'équipe")
    loc = st.text_input("📍 Quelle zone ?", placeholder="ex: Guéret, Creuse")
with col2:
    skills = st.text_input("🔑 Compétence clé", placeholder="ex: BTP")
    method = st.radio("Stratégie", ["Contact Direct (Mail/Tel)", "Recherche de CV PDF", "LinkedIn Global"])

def build_fail_safe_query(job, loc, skills, method):
    # Logique de base souple
    base = f'"{job}"'
    if loc: base += f' {loc}'
    if skills: base += f' "{skills}"'
    
    if method == "Contact Direct (Mail/Tel)":
        # On force Google à trouver des textes qui ressemblent à des coordonnées
        return f'site:linkedin.com/in/ {base} ("@gmail.com" OR "@outlook.com" OR "06" OR "07")'
    
    elif method == "Recherche de CV PDF":
        # On cherche des CVs mais on n'est pas trop strict sur le titre
        return f'filetype:pdf {base} (CV OR Resume OR Curriculum)'
    
    else:
        # LinkedIn standard mais sans les pollutions de pubs
        return f'site:linkedin.com/in/ {base} -intitle:offres -inurl:jobs'

if st.button("LANCER LA RECHERCHE MAINTENANT"):
    if job:
        final_query = build_fail_safe_query(job, loc, skills, method)
        url = f"https://www.google.com/search?q={urllib.parse.quote(final_query)}"
        
        st.markdown(f"""
            <div class="res-box">
                <p style="color:#ff4b4b; font-weight:bold;">✅ Requête optimisée générée :</p>
                <code>{final_query}</code>
                <br><br>
                <a href="{url}" target="_blank" style="text-decoration:none;">
                    <button style="width:100%; background:#28a745; color:white; padding:15px; border:none; border-radius:5px; cursor:pointer; font-weight:bold; font-size:1.1em;">
                        CLIQUE ICI POUR VOIR LES RÉSULTATS SUR GOOGLE
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Indique au moins un métier.")
