import streamlit as st
import os

st.title("Mes documents")

UPLOAD_DIR = "documents"
os.makedirs(UPLOAD_DIR, exist_ok=True)

uploaded_file = st.file_uploader("Uploader un fichier")

if uploaded_file:
    with open(os.path.join(UPLOAD_DIR, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Fichier sauvegardé")

st.subheader("Fichiers disponibles")
for file in os.listdir(UPLOAD_DIR):
    st.write(file)
