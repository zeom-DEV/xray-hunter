import streamlit as st
import urllib.parse

st.set_page_config(page_title="Moez Thabet | OSINT Industrial", page_icon="🏗️", layout="wide")

# Style "Command Center"
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #00ff41; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background: #00ff41; color: black; font-weight: bold; border: none; height: 3em; width: 100%; }
    .stTextInput>div>div>input { background-color: #161b22; color: #00ff41; border: 1px solid #00ff41; }
    .status { border: 1px solid #00ff41; padding: 15px; border-radius: 5px; background: #0d1117; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏗️ SOURCING INDUSTRIAL V9.0")
st.write("**Opérateur : Moez Thabet** | Extraction de données brutes")

col1, col2 = st.columns(2)
with col1:
    job = st.text_input("🎯 Poste précis", placeholder="ex: Chef d'équipe BTP")
    loc = st.text_input("📍 Secteur (Ville/Dept)", placeholder="ex: Guéret OR Creuse")
with col2:
    target = st.selectbox("🎯 Cible de donnée", [
        "Leaking d'Emails (LinkedIn)", 
        "Téléchargement Direct CV (PDF)", 
        "Numéros de Téléphone (Public)",
        "Annuaires Professionnels"
    ])

def build_pro_dork(job, loc, target):
    # Élargissement automatique pour les petites villes comme Guéret
    location_query = f'("{loc}")' if loc else ""
    
    if target == "Leaking d'Emails (LinkedIn)":
        return f'site:linkedin.com/in/ "{job}" {location_query} ("@gmail.com" OR "@outlook.com" OR "@wanadoo.fr" OR "@orange.fr")'
    
    elif target == "Téléchargement Direct CV (PDF)":
        # On évite les formulaires vides en forçant des mots-clés d'expérience
        return f'filetype:pdf "{job}" {location_query} (Expérience OR "Parcours professionnel") -intitle:formulaire -intitle:modèle'
    
    elif target == "Numéros de Téléphone (Public)":
        return f'site:linkedin.com/in/ "{job}" {location_query} ("06" OR "07" OR "+336" OR "+337")'
    
    else: # Annuaires
        return f'("{job}" AND "{loc}") (annuaire OR "liste des membres" OR "trombinoscope")'

if st.button("LANCER L'EXTRACTION"):
    if job:
        query = build_pro_dork(job, loc, target)
        url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
        
        st.markdown(f"""
            <div class="status">
                <p>🚀 <b>Requête OSINT générée :</b></p>
                <code>{query}</code>
                <br><br>
                <a href="{url}" target="_blank" style="text-decoration:none;">
                    <button style="width:100%; background:#00ff41; color:black; padding:15px; border:none; cursor:pointer; font-weight:bold;">
                        DÉVERROUILLER LES DONNÉES SUR GOOGLE
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Le poste est obligatoire.")
