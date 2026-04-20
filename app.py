import streamlit as st
import urllib.parse

st.set_page_config(page_title="Moez Thabet | The Vault V13", page_icon="🏦", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #ff0000; font-family: 'Courier'; }
    .stButton>button { background: #ff0000; color: white; border: none; font-weight: bold; height: 4em; width: 100%; }
    .vault-box { border: 2px solid #ff0000; padding: 20px; background: #110000; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏦 THE VAULT V13.0 - CLOUD LEAK SOURCING")
st.write("**Architecte Sécurité & Sourcing : Moez Thabet**")

col1, col2 = st.columns(2)
with col1:
    job = st.text_input("🎯 Poste Cible", placeholder="ex: Chef de chantier")
    loc = st.text_input("📍 Zone", placeholder="ex: Sousse OR Tunisie")
with col2:
    source = st.selectbox("🌐 Serveur de Stockage", [
        "Cloud Storage (S3/Azure/Google)",
        "Open Directories (Index of /)",
        "Social Private Leaks (Drive/Dropbox)",
        "Recruitment Software Leaks (Lever/Greenhouse)"
    ])

def build_vault_query(job, loc, source):
    area = f'"{loc}"' if loc else ""
    if "Cloud" in source:
        return f'site:s3.amazonaws.com OR site:blob.core.windows.net OR site:storage.googleapis.com "{job}" {area} filetype:pdf'
    elif "Directories" in source:
        return f'intitle:"index of" "{job}" {area} (cv OR resume) filetype:pdf'
    elif "Social" in source:
        return f'site:drive.google.com OR site:dropbox.com/s/ "{job}" {area} filetype:pdf'
    else: # ATS Leaks
        return f'site:lever.co OR site:greenhouse.io "{job}" {area} -inurl:jobs'

if st.button("DÉVERROUILLER L'ACCÈS"):
    if job:
        query = build_vault_query(job, loc, source)
        url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
        st.markdown(f'<div class="vault-box"><code>{query}</code><br><br><a href="{url}" target="_blank"><button>ASPIRER LES DOCUMENTS</button></a></div>', unsafe_allow_html=True)
