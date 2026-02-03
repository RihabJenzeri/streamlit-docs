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
        padding: 20px;
    }
    
    h1 {
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    
    .folder-btn {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.2);
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        font-size: 20px;
        width: 100%;
        cursor: pointer;
    }
    
    .image-link {
        display: block;
        text-align: center;
        margin: 20px 0;
    }
    
    .thumbnail {
        width: 300px;
        height: 300px;
        object-fit: contain;
        border: 3px solid white;
        border-radius: 15px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    .thumbnail:hover {
        transform: scale(1.05);
        border-color: #FFD700;
        box-shadow: 0 12px 35px rgba(0,0,0,0.4);
    }
    
    .action-buttons {
        display: flex;
        gap: 15px;
        justify-content: center;
        margin-top: 20px;
    }
    
    .action-btn {
        background: rgba(255, 255, 255, 0.15);
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        text-decoration: none;
        transition: all 0.3s;
    }
    
    .action-btn:hover {
        background: rgba(255, 255, 255, 0.25);
    }
</style>
""", unsafe_allow_html=True)

# ========== رابط الصورة ==========
image_url = f"{BASE_URL}mes_documents/Medicofi/Société%20ApniDoc%20(en%20France)/Flyer%20ApniDoc.png"
file_name = "Flyer_ApniDoc.png"

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📂 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    if st.button("🏥 Medicofi"):
        st.session_state.page = "medicofi"
        st.rerun()

elif st.session_state.page == "medicofi":
    if st.button("← Retour"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>🏥 Medicofi</h1>", unsafe_allow_html=True)
    
    if st.button("🇫🇷 Société ApniDoc (en France)"):
        st.session_state.page = "apnidoc"
        st.rerun()

elif st.session_state.page == "apnidoc":
    if st.button("← Retour"):
        st.session_state.page = "medicofi"
        st.rerun()
    
    st.markdown("<h1>🇫🇷 Société ApniDoc</h1>", unsafe_allow_html=True)
    
    # رابط للصورة يفتح في نافذة جديدة
    st.markdown(f"""
    <div class="image-link">
        <a href="{image_url}" target="_blank">
            <img src="{image_url}" class="thumbnail" alt="Flyer ApniDoc">
        </a>
        <p style="color: #FFD700; margin-top: 10px;">👆 Cliquez sur l'image pour l'ouvrir en grand</p>
    </div>
    """, unsafe_allow_html=True)
    
    # أزرار إضافية
    st.markdown(f"""
    <div class="action-buttons">
        <a href="{image_url}" target="_blank" class="action-btn">
            🔍 Ouvrir dans un nouvel onglet
        </a>
        <a href="{image_url}" download="{file_name}" class="action-btn">
            📥 Télécharger
        </a>
    </div>
    """, unsafe_allow_html=True)
