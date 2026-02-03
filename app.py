import streamlit as st

# ========== الإعدادات ==========
GITHUB_USER = "RihabJenzeri"
REPO_NAME = "streamlit-docs"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/"

# ========== حالة التطبيق ==========
if 'page' not in st.session_state:
    st.session_state.page = "accueil"

# ========== تنسيق ==========
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Arial', sans-serif;
        min-height: 100vh;
        padding: 20px;
    }
    
    h1 {
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    
    .btn {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.3);
        padding: 15px 30px;
        margin: 10px;
        border-radius: 10px;
        font-size: 18px;
        cursor: pointer;
        transition: all 0.3s;
        width: 100%;
    }
    
    .btn:hover {
        background: rgba(255, 255, 255, 0.3);
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📁 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    if st.button("📁 Medicoi", key="medicoi"):
        st.session_state.page = "medicoi"
        st.rerun()

elif st.session_state.page == "medicoi":
    if st.button("← Retour"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>📁 Medicoi</h1>", unsafe_allow_html=True)
    
    if st.button("📂 Société ApiDiDoc (en France)"):
        st.session_state.page = "apnidoc"
        st.rerun()

elif st.session_state.page == "apnidoc":
    if st.button("← Retour"):
        st.session_state.page = "medicoi"
        st.rerun()
    
    st.markdown("<h1>🏥 Société ApiDiDoc</h1>", unsafe_allow_html=True)
    
    # ========== طريقة مباشرة بدون ترميح ==========
    image_path = "mes_documents/Medicoi/Société ApiDiDoc (en France)/Flyer ApiDiDoc.png"
    
    # جرب عدة طرق لعرض الصورة
    
    st.subheader("🔄 Essai 1: URL direct")
    url1 = f"{BASE_URL}mes_documents/Medicoi/Soci%C3%A9t%C3%A9%20ApiDiDoc%20(en%20France)/Flyer%20ApiDiDoc.png"
    st.write(f"URL: `{url1}`")
    try:
        st.image(url1, use_container_width=True, caption="Méthode 1")
    except:
        st.error("❌ Échec méthode 1")
    
    st.subheader("🔄 Essai 2: URL simplifiée")
    # استبدال الأقواس بشرطات
    url2 = f"{BASE_URL}mes_documents/Medicoi/Société-ApiDiDoc-en-France/Flyer-ApiDiDoc.png"
    st.write(f"URL: `{url2}`")
    try:
        st.image(url2, use_container_width=True, caption="Méthode 2")
    except:
        st.error("❌ Échec méthode 2")
    
    st.subheader("🔄 Essai 3: GitHub Pages")
    # جرب GitHub Pages كبديل
    url3 = f"https://{GITHUB_USER}.github.io/{REPO_NAME}/{image_path}"
    st.write(f"URL: `{url3}`")
    try:
        st.image(url3, use_container_width=True, caption="Méthode 3")
    except:
        st.error("❌ Échec méthode 3")
    
    # زر لفتح الرابط مباشرة
    st.markdown(f"""
    <div style="text-align: center; margin-top: 30px;">
        <a href="{url1}" target="_blank" style="
            display: inline-block;
            padding: 15px 30px;
            background: #2196F3;
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: bold;
        ">
            🔗 Ouvrir l'image dans un nouvel onglet
        </a>
    </div>
    """, unsafe_allow_html=True)
