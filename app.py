import streamlit as st
import urllib.parse

# ========== إعدادات ==========
GITHUB_USER = "RihabJenzeri"
REPO_NAME = "streamlit-docs"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/"

# ========== حالة التطبيق ==========
if 'page' not in st.session_state:
    st.session_state.page = "accueil"

# ========== تنسيق ==========
st.markdown("""
<style>
    .folder {background: rgba(255,255,255,0.1); padding: 15px; margin: 10px; border-radius: 10px; cursor: pointer;}
    .folder:hover {background: rgba(255,255,255,0.2);}
</style>
""", unsafe_allow_html=True)

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.title("📂 Mes Dossiers")
    if st.button("Medicofi", key="m1"):
        st.session_state.page = "medicofi"
        st.rerun()

elif st.session_state.page == "medicofi":
    st.button("← Retour", on_click=lambda: st.session_state.update(page="accueil"))
    st.title("Medicofi")
    if st.button("Société ApniDoc"):
        st.session_state.page = "apnidoc"
        st.rerun()

elif st.session_state.page == "apnidoc":
    st.button("← Retour", on_click=lambda: st.session_state.update(page="medicofi"))
    st.title("Société ApniDoc")
    
    # المسار بدون مسافات
    image_path = "mes_documents/Medicofi/ApniDoc_France/Flyer_ApniDoc.jpg"
    image_url = BASE_URL + image_path
    
    try:
        st.image(image_url)
        st.success("Image chargée!")
    except:
        st.error(f"Impossible de charger: {image_url}")
        st.info("Renommez le fichier sans espaces et rechargez la page")
