import streamlit as st

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
</style>
""", unsafe_allow_html=True)

# ========== رابط الصورة ==========
image_url = f"{BASE_URL}mes_documents/Medicofi/Société%20ApniDoc%20(en%20France)/Flyer%20ApniDoc.png"

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
    
    st.image(image_url, width=300, caption="Flyer ApniDoc")
