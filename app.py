import streamlit as st
import urllib.parse

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
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
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
    }
    
    .pdf-frame {
        width: 100%;
        height: 700px;
        border: 3px solid white;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .action-buttons {
        display: flex;
        gap: 20px;
        justify-content: center;
        margin-top: 20px;
    }
    
    .action-btn {
        padding: 12px 25px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s;
        border: none;
        cursor: pointer;
    }
    
    .download-btn {
        background: #4CAF50;
        color: white;
    }
    
    .download-btn:hover {
        background: #2E7D32;
        transform: translateY(-3px);
    }
    
    .newtab-btn {
        background: #2196F3;
        color: white;
    }
    
    .newtab-btn:hover {
        background: #0D47A1;
        transform: translateY(-3px);
    }
</style>
""", unsafe_allow_html=True)

# ========== روابط الملفات ==========
image_url = f"{BASE_URL}mes_documents/Medicofi/Société%20ApniDoc%20(en%20France)/Flyer%20ApniDoc.png"
pdf_url_raw = f"{BASE_URL}mes_documents/Portfolio%20Ines%20HARRABI%202024.pdf"

# ترميح URL لاستخدامه مع Google Docs
pdf_url_encoded = urllib.parse.quote(pdf_url_raw, safe='')
google_viewer_url = f"https://docs.google.com/viewer?url={pdf_url_encoded}&embedded=true"

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📂 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏥 Medicofi", use_container_width=True):
            st.session_state.page = "medicofi"
            st.rerun()
    
    with col2:
        if st.button("📄 Portfolio PDF", use_container_width=True):
            st.session_state.page = "pdf_viewer"
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
    
    st.image(image_url, width=300, caption="Flyer ApniDoc")

elif st.session_state.page == "pdf_viewer":
    if st.button("← Retour"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>📄 Portfolio Ines HARRABI 2024</h1>", unsafe_allow_html=True)
    
    # عرض PDF باستخدام Google Docs Viewer
    st.markdown(f"""
    <iframe class="pdf-frame" src="{google_viewer_url}"></iframe>
    """, unsafe_allow_html=True)
    
    # أزرار للتحميل والفتح
    st.markdown(f"""
    <div class="action-buttons">
        <a href="{pdf_url_raw}" download="Portfolio_Ines_HARRABI_2024.pdf" class="action-btn download-btn">
            📥 Télécharger le PDF
        </a>
        <a href="{google_viewer_url}" target="_blank" class="action-btn newtab-btn">
            🔗 Ouvrir dans Google Viewer
        </a>
    </div>
    """, unsafe_allow_html=True)
