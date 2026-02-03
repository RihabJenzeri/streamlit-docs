import streamlit as st

# ========== الإعدادات ==========
GITHUB_USER = "RihabJenzeri"
REPO_NAME = "streamlit-docs"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/"

# ========== حالة التطبيق ==========
if 'page' not in st.session_state:
    st.session_state.page = "accueil"

# ========== تنسيق مع إخفاء الشريط ==========
st.markdown("""
<style>
    /* إخفاء شريط Streamlit الافتراضي */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* إخفاء زر القائمة في الزاوية */
    .stDeployButton {display:none;}
    
    /* إخفاء أيقونة القائمة في الزاوية اليمنى العليا */
    #stDecoration {display:none;}
    
    /* إخفاء عناصر واجهة Streamlit الإضافية */
    .st-emotion-cache-1dp5vir {display: none;}
    .st-emotion-cache-z5fcl4 {padding-top: 0rem;}
    
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
    
    .stButton > button {
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
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }
    
    .stButton > button:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
        border-color: #FFD700;
    }
    
    .pdf-btn {
        background: rgba(76, 175, 80, 0.2) !important;
        border-color: #4CAF50 !important;
    }
    
    .pdf-btn:hover {
        background: rgba(76, 175, 80, 0.3) !important;
        border-color: #2E7D32 !important;
    }
</style>
""", unsafe_allow_html=True)

# ========== روابط الملفات ==========
image_url = f"{BASE_URL}mes_documents/Medicofi/Société%20ApniDoc%20(en%20France)/Flyer%20ApniDoc.png"
pdf_url = f"{BASE_URL}mes_documents/Portfolio%20Ines%20HARRABI%202024.pdf"
pdf_name = "Portfolio Ines HARRABI 2024.pdf"

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📂 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    # زر Medicofi
    if st.button("🏥 Medicofi", key="medicofi"):
        st.session_state.page = "medicofi"
        st.rerun()
    
    # زر PDF Portfolio
    if st.button("📄 Portfolio Ines HARRABI 2024", key="portfolio"):
        # يفتح PDF في نافذة جديدة
        st.markdown(f'<meta http-equiv="refresh" content="0; url={pdf_url}">', unsafe_allow_html=True)

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
