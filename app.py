import streamlit as st
import os
import base64
from pathlib import Path

# ========== الإعدادات ==========
GITHUB_USER = "rihabjenzeri"
REPO_NAME = "repo"  # اسم الـ Repo الخاص بك
BRANCH = "master"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/{BRANCH}/"

# ========== دالة لعرض الصور من GitHub ==========
def display_image_from_github(image_path):
    try:
        st.image(BASE_URL + image_path, caption=os.path.basename(image_path))
    except Exception as e:
        st.error(f"Erreur de chargement: {e}")

# ========== دالة لعرض الملفات ==========
def display_files_from_github(folder_path=""):
    # هنا يمكنك استخدام GitHub API أو إنشاء قائمة يدوية
    # لأبسط حل، نعرف الملفات مسبقًا أو نستخدم قائمة ثابتة
    pass

# ========== واجهة Streamlit ==========
st.title("📁 Mes Dossiers et Images depuis GitHub")

# قائمة الملفات/المجلدات المعروفة (يمكن توسيعها)
known_files = [
    "documents/file1.pdf",
    "documents/file2.txt",
    "images/3db4950c3fa1675cc0aa266ed51ce3c8.jpg",
    "images/img1.png"
]

st.subheader("📂 Fichiers disponibles dans GitHub")
for file in known_files:
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        st.write(f"🖼️ **{file}**")
        display_image_from_github(file)
    else:
        st.write(f"📄 **{file}**")
        st.markdown(f"[Télécharger {file}]({BASE_URL + file})")

# ========== إضافة رفع ملفات جديدة (اختياري) ==========
st.subheader("📤 Uploader un nouveau fichier (optionnel)")
uploaded_file = st.file_uploader("Choisissez un fichier")
if uploaded_file:
    # هنا يمكنك حفظ الملف في GitHub عبر API أو تنبيه المستخدم لرفعه يدويًا
    st.warning("Pour ajouter ce fichier à GitHub, veuillez le téléverser manuellement dans votre repo.")
