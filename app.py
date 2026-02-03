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
    }
    
    h1 {
        color: white;
        text-align: center;
        margin-bottom: 30px;
        font-size: 2.5rem;
    }
    
    .file-item {
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
        text-align: center;
        display: block;
        text-decoration: none;
    }
    
    .file-item:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
        border-color: #FFD700;
    }
    
    .pdf-item {
        background: rgba(76, 175, 80, 0.2);
        border-color: #4CAF50;
    }
    
    .pdf-item:hover {
        background: rgba(76, 175, 80, 0.3);
        border-color: #2E7D32;
    }
</style>
""", unsafe_allow_html=True)

# ========== روابط الملفات ==========
image_url = f"{BASE_URL}mes_documents/Medicofi/Société%20ApniDoc%20(en%20France)/Flyer%20ApniDoc.png"
pdf_url = f"{BASE_URL}mes_documents/Portfolio%20Ines%20HARRABI%202024.pdf"

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📂 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    # زر Medicofi
    st.markdown(f"""
    <a href="#" onclick="event.preventDefault(); window.parent.postMessage({{'type': 'streamlit:setComponentValue', 'value': 'medicofi'}}, '*');" class="file-item">
        🏥 Medicofi
    </a>
    """, unsafe_allow_html=True)
    
    # زر PDF Portfolio
    st.markdown(f"""
    <a href="{pdf_url}" target="_self" class="file-item pdf-item">
        📄 Portfolio Ines HARRABI 2024
    </a>
    """, unsafe_allow_html=True)
    
    # زر JavaScript للتنقل
    if st.button("", key="hidden_button", type="secondary"):
        pass

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
