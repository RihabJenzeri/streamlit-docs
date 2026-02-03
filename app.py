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
        min-height: 100vh;
    }
    
    h1 {
        color: white;
        text-align: center;
        margin-bottom: 30px;
        font-size: 2.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .folder-btn {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.2);
        padding: 20px;
        margin: 15px 0;
        border-radius: 15px;
        font-size: 24px;
        font-weight: bold;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
    }
    
    .folder-btn:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-5px);
        border-color: #FFD700;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    
    .back-btn {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 10px 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        cursor: pointer;
        font-size: 16px;
        transition: all 0.3s;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .back-btn:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateX(-5px);
    }
    
    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 40px 0;
        padding: 20px;
    }
    
    .clickable-image {
        width: 400px;
        height: 400px;
        object-fit: contain;
        border: 4px solid white;
        border-radius: 20px;
        cursor: pointer;
        transition: all 0.4s ease;
        box-shadow: 0 15px 35px rgba(0,0,0,0.4);
    }
    
    .clickable-image:hover {
        transform: scale(1.08);
        border-color: #FFD700;
        box-shadow: 0 20px 45px rgba(0,0,0,0.5);
    }
    
    .image-caption {
        color: #FFD700;
        text-align: center;
        margin-top: 15px;
        font-size: 16px;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# ========== رابط الصورة ==========
image_url = f"{BASE_URL}mes_documents/Medicofi/Société%20ApniDoc%20(en%20France)/Flyer%20ApniDoc.png"

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📂 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    if st.button("🏥 Medicofi", key="medicofi", use_container_width=True):
        st.session_state.page = "medicofi"
        st.rerun()

elif st.session_state.page == "medicofi":
    if st.button("← Retour", key="back1"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>🏥 Medicofi</h1>", unsafe_allow_html=True)
    
    if st.button("🇫🇷 Société ApniDoc (en France)", key="apnidoc", use_container_width=True):
        st.session_state.page = "apnidoc"
        st.rerun()

elif st.session_state.page == "apnidoc":
    if st.button("← Retour", key="back2"):
        st.session_state.page = "medicofi"
        st.rerun()
    
    st.markdown("<h1>🇫🇷 Société ApniDoc</h1>", unsafe_allow_html=True)
    
    # عرض الصورة فقط (قابلة للنقر)
    st.markdown(f"""
    <div class="image-container">
        <a href="{image_url}" target="_blank">
            <img src="{image_url}" class="clickable-image" alt="Flyer ApniDoc">
        </a>
    </div>
    <p class="image-caption">👆 Cliquez sur l'image pour l'ouvrir en grand dans un nouvel onglet</p>
    """, unsafe_allow_html=True)
