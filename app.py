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
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    #stDecoration {display:none;}
    
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
    
    .folder-container {
        display: flex;
        flex-direction: column;
        gap: 15px;
        max-width: 500px;
        margin: 0 auto;
    }
    
    .folder-item {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 15px;
        font-size: 22px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s;
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        text-decoration: none;
    }
    
    .folder-item:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-5px);
        border-color: #FFD700;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    
    .pdf-item {
        background: rgba(76, 175, 80, 0.2);
        border-color: #4CAF50;
    }
    
    .pdf-item:hover {
        background: rgba(76, 175, 80, 0.3);
        border-color: #2E7D32;
    }
    
    .back-btn {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 12px 25px;
        border-radius: 10px;
        margin-bottom: 20px;
        cursor: pointer;
        font-size: 18px;
        display: inline-flex;
        align-items: center;
        gap: 10px;
        transition: all 0.3s;
    }
    
    .back-btn:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateX(-5px);
    }
    
    .pdf-viewer-container {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        border: 2px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# ========== روابط الملفات ==========
image_url = f"{BASE_URL}mes_documents/Medicofi/Société%20ApniDoc%20(en%20France)/Flyer%20ApniDoc.png"
pdf_url = f"{BASE_URL}mes_documents/Portfolio%20Ines%20HARRABI%202024.pdf"

# ========== دالة لعرض PDF ==========
def display_pdf(pdf_url):
    # استخدام Google Docs Viewer لعرض PDF
    google_docs_viewer = f"https://docs.google.com/viewer?url={pdf_url}&embedded=true"
    
    st.markdown(f"""
    <div class="pdf-viewer-container">
        <iframe src="{google_docs_viewer}" 
                width="100%" 
                height="600" 
                frameborder="0" 
                style="border-radius: 10px;">
        </iframe>
        
        <div style="text-align: center; margin-top: 20px;">
            <a href="{pdf_url}" download style="
                display: inline-block;
                background: #4CAF50;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
                margin: 0 10px;
            ">
                📥 Télécharger le PDF
            </a>
            
            <a href="{pdf_url}" target="_blank" style="
                display: inline-block;
                background: #2196F3;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
                margin: 0 10px;
            ">
                🔗 Ouvrir dans un nouvel onglet
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📂 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    st.markdown('<div class="folder-container">', unsafe_allow_html=True)
    
    # زر Medicofi
    if st.button("🏥 Medicofi", key="medicofi_btn", use_container_width=True):
        st.session_state.page = "medicofi"
        st.rerun()
    
    # زر عرض PDF
    if st.button("📄 Portfolio Ines HARRABI 2024", key="pdf_btn", use_container_width=True):
        st.session_state.page = "pdf_viewer"
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "medicofi":
    if st.button("← Retour", key="back1"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>🏥 Medicofi</h1>", unsafe_allow_html=True)
    
    if st.button("🇫🇷 Société ApniDoc (en France)", key="apnidoc_btn", use_container_width=True):
        st.session_state.page = "apnidoc"
        st.rerun()

elif st.session_state.page == "apnidoc":
    if st.button("← Retour", key="back2"):
        st.session_state.page = "medicofi"
        st.rerun()
    
    st.markdown("<h1>🇫🇷 Société ApniDoc</h1>", unsafe_allow_html=True)
    
    st.image(image_url, width=300, caption="Flyer ApniDoc")

elif st.session_state.page == "pdf_viewer":
    if st.button("← Retour", key="back3"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>📄 Portfolio Ines HARRABI 2024</h1>", unsafe_allow_html=True)
    
    # عرض PDF مباشرة في الصفحة
    display_pdf(pdf_url)
