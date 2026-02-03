import streamlit as st

# ========== إعدادات ==========
GITHUB_USER = "RihabJenzeri"
REPO_NAME = "streamlit-docs"
BRANCH = "main"

# ========== حالة التطبيق ==========
if 'page' not in st.session_state:
    st.session_state.page = "accueil"

# ========== تنسيق ==========
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    h1, h2, h3 { color: white !important; }
    .folder-btn { 
        background: rgba(255,255,255,0.15); 
        color: white; 
        border: 2px solid rgba(255,255,255,0.3);
        border-radius: 10px;
        padding: 20px;
        font-size: 24px;
        margin: 10px;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.title("📂 Mes Dossiers")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏥 Medicofi", key="medicofi", use_container_width=True):
            st.session_state.page = "medicofi"
            st.rerun()

elif st.session_state.page == "medicofi":
    st.button("← Retour", on_click=lambda: st.session_state.update(page="accueil"))
    st.title("🏥 Medicofi")
    
    # اختر المسار الصحيح هنا بعد التحقق
    # الخيار 1: إذا كان الاسم به مسافات
    image_path = "mes_documents/Medicofi/Société ApniDoc (en France)/Flyer ApniDoc.jpg"
    
    # الخيار 2: إذا غيرت الاسم
    # image_path = "mes_documents/Medicofi/ApniDoc_France/Flyer_ApniDoc.jpg"
    
    image_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/{BRANCH}/{image_path}"
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🖼️ Flyer ApniDoc")
        try:
            st.image(image_url, use_container_width=True)
            st.success("✅ Image chargée avec succès!")
            
            # زر التحميل
            st.markdown(f'<a href="{image_url}" download style="text-decoration: none;">'
                       f'<button style="background:#4CAF50;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;">'
                       f'📥 Télécharger l\'image</button></a>', 
                       unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"❌ Erreur: Impossible de charger l'image")
            st.info(f"URL essayée: {image_url}")
            st.info("🔧 Solution: Vérifiez le nom du fichier sur GitHub")
    
    with col2:
        st.subheader("📁 Autres dossiers")
        if st.button("📊 Rapports Annuels", use_container_width=True):
            st.info("Ce dossier sera disponible bientôt")
        
        if st.button("📈 Présentations", use_container_width=True):
            st.info("Ce dossier sera disponible bientôt")

# ========== معلومات التصحيح ==========
with st.expander("🔧 Informations de débogage"):
    st.write("**Repository:**", f"{GITHUB_USER}/{REPO_NAME}")
    st.write("**Branch:**", BRANCH)
    st.write("**URL de base:**", f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/{BRANCH}/")
    
    # اختبار اتصال
    import requests
    test_url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}"
    try:
        response = requests.get(test_url)
        if response.status_code == 200:
            st.success("✅ Connection GitHub OK")
        else:
            st.error(f"❌ Erreur de connection: {response.status_code}")
    except:
        st.error("❌ Impossible de se connecter à GitHub")
