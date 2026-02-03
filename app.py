import streamlit as st
import os

st.title("Mes Rihab")

# المجلد اللي فيه الملفات
BASE_DIR = "documents"
os.makedirs(BASE_DIR, exist_ok=True)

st.subheader("Fichiers et dossiers disponibles:")

# استعراض المجلدات والملفات
for item in os.listdir(BASE_DIR):
    item_path = os.path.join(BASE_DIR, item)
    if os.path.isdir(item_path):
        st.write(f"📁 Dossier: {item}")
        # لو تحب تعرض الملفات داخل هذا المجلد مباشرة:
        for f in os.listdir(item_path):
            st.write(f"    - {f}")
    else:
        st.write(f"📄 Fichier: {item}")
