import streamlit as st
import webbrowser

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
        transition: all 0.3s;
    }
    
    .folder-btn:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }
    
    .image-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 30px 0;
        gap: 15px;
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
        box-shadow: 0 12px 35px rgba(0,0,0,0.4);
        border-color: #FFD700;
    }
    
    .click-hint {
        color: #FFD700;
        font-size: 14px;
        text-align: center;
        margin-top: 5px;
    }
    
    .buttons-container {
        display: flex;
        gap: 15px;
        margin-top: 20px;
        justify-content: center;
    }
    
    .action-btn {
        background: rgba(255, 255, 255, 0.15);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 10px 20px;
        border-radius: 8px;
        cursor: pointer;
        text-decoration: none;
        transition: all 0.3s;
        display: inline-block;
    }
    
    .action-btn:hover {
        background: rgba(255, 255, 255, 0.25);
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# ========== رابط الصورة ==========
image_url = f"{BASE_URL}mes_documents/Medicofi/Société%20ApniDoc%20(en%20France)/Flyer%20ApniDoc.png"
file_name = "Flyer_ApniDoc.png"

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📂 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    if st.button("🏥 Medicofi", key="medicofi"):
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
    
    # عرض الصورة مع زر النقر
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # عرض الصورة المصغرة
        st.image(image_url, width=300, caption="Flyer ApniDoc")
        
        st.markdown('<p class="click-hint">👆 Cliquez sur les boutons ci-dessous</p>', unsafe_allow_html=True)
        
        # زر لفتح الصورة في نافذة جديدة
        if st.button("🔍 Voir en grand (nouvel onglet)", use_container_width=True):
            webbrowser.open_new_tab(image_url)
        
        # زر التحميل
        st.markdown(f"""
        <div style="margin-top: 10px;">
            <a href="{image_url}" download="{file_name}" class="action-btn" style="width: 100%; text-align: center; display: block;">
                📥 Télécharger l'image
            </a>
        </div>
        """, unsafe_allow_html=True)
