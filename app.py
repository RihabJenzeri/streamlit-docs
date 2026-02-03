import streamlit as st

# ========== الإعدادات الصحيحة ==========
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
    
    h1, h2, h3 {
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .btn-folder {
        background: rgba(255, 255, 255, 0.15);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.3);
        padding: 20px;
        margin: 15px 0;
        border-radius: 15px;
        font-size: 22px;
        font-weight: bold;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
    }
    
    .btn-folder:hover {
        background: rgba(255, 255, 255, 0.25);
        transform: translateY(-5px);
        border-color: #FFD700;
    }
    
    .btn-back {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 10px 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        cursor: pointer;
        font-size: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📂 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    if st.button("🏥 Medicofi", key="medicofi_btn", use_container_width=True):
        st.session_state.page = "medicofi"
        st.rerun()

elif st.session_state.page == "medicofi":
    if st.button("← Retour", key="back_to_accueil"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>🏥 Medicofi</h1>", unsafe_allow_html=True)
    
    if st.button("🇫🇷 Société ApniDoc (en France)", key="apnidoc_btn", use_container_width=True):
        st.session_state.page = "apnidoc"
        st.rerun()

elif st.session_state.page == "apnidoc":
    if st.button("← Retour", key="back_to_medicofi"):
        st.session_state.page = "medicofi"
        st.rerun()
    
    st.markdown("<h1>🇫🇷 Société ApniDoc</h1>", unsafe_allow_html=True)
    
    # ========== المسار الصحيح تماماً ==========
    # بناء على الصورة التي رأيتها
    image_path = "mes_documents/Medicofi/Société ApniDoc (en France)/Flyer ApniDoc.png"
    
    # URL الصحيح (بدون ترميح إضافي)
    image_url = f"{BASE_URL}mes_documents/Medicofi/Société%20ApniDoc%20(en%20France)/Flyer%20ApniDoc.png"
    
    st.markdown("### 🖼️ Flyer ApniDoc")
    
    # عرض معلومات المسار
    st.code(f"""
    Dossier: Medicofi
    Sous-dossier: Société ApniDoc (en France)
    Fichier: Flyer ApniDoc.png
    
    URL complète:
    {image_url}
    """)
    
    # محاولة عرض الصورة
    try:
        st.image(image_url, use_container_width=True)
        st.success("✅ Image chargée avec succès!")
        
        # زر التحميل
        st.markdown(f"""
        <div style="text-align: center; margin-top: 20px;">
            <a href="{image_url}" download="Flyer_ApniDoc.png" style="
                display: inline-block;
                padding: 12px 25px;
                background: linear-gradient(90deg, #4CAF50, #2E7D32);
                color: white;
                border-radius: 10px;
                text-decoration: none;
                font-weight: bold;
                font-size: 16px;
                box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
                transition: all 0.3s;
            ">
                📥 Télécharger Flyer ApniDoc
            </a>
        </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"❌ Erreur de chargement: {str(e)}")
        
        # زر لفتح الرابط يدوياً
        st.markdown(f"""
        <div style="text-align: center; margin-top: 20px;">
            <a href="{image_url}" target="_blank" style="
                display: inline-block;
                padding: 12px 25px;
                background: linear-gradient(90deg, #2196F3, #0D47A1);
                color: white;
                border-radius: 10px;
                text-decoration: none;
                font-weight: bold;
                font-size: 16px;
            ">
                🔗 Ouvrir l'URL dans un nouvel onglet
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # اختبار بسيط
        st.info("""
        **Pour tester:**
        1. Cliquez sur le bouton bleu ci-dessus
        2. Si l'image s'affiche dans le nouvel onglet, le problème est dans Streamlit
        3. Si l'image ne s'affiche pas, vérifiez que le fichier existe bien à cet emplacement
        """)
