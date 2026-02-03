import streamlit as st
import urllib.parse

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
    
    .folder-btn {
        background: rgba(255, 255, 255, 0.15);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.3);
        padding: 20px;
        margin: 15px 0;
        border-radius: 15px;
        font-size: 20px;
        font-weight: bold;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .folder-btn:hover {
        background: rgba(255, 255, 255, 0.25);
        transform: translateY(-3px);
        border-color: rgba(255, 255, 255, 0.5);
    }
    
    h1 {
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📂 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    if st.button("📁 Medicoi", key="medicoi_btn", use_container_width=True):
        st.session_state.page = "medicoi"
        st.rerun()

elif st.session_state.page == "medicoi":
    st.button("← Retour", on_click=lambda: st.session_state.update(page="accueil"))
    st.markdown("<h1>📁 Medicoi</h1>", unsafe_allow_html=True)
    
    if st.button("📂 Société ApiDiDoc (en France)", key="apnidoc_btn", use_container_width=True):
        st.session_state.page = "apnidoc"
        st.rerun()

elif st.session_state.page == "apnidoc":
    st.button("← Retour", on_click=lambda: st.session_state.update(page="medicoi"))
    st.markdown("<h1>🏥 Société ApiDiDoc</h1>", unsafe_allow_html=True)
    
    # ========== المسار الصحيح تماماً ==========
    image_path = "mes_documents/Medicoi/Société ApiDiDoc (en France)/Flyer ApiDiDoc.png"
    image_url = BASE_URL + urllib.parse.quote(image_path)
    
    st.markdown(f"**URL:** `{image_url}`")
    
    try:
        # محاولة عرض الصورة
        st.image(image_url, use_container_width=True, caption="Flyer ApiDiDoc")
        st.success("✅ Image chargée avec succès!")
        
        # زر التحميل
        st.markdown(f'<a href="{image_url}" download="Flyer_ApiDiDoc.png" style="display: inline-block; padding: 10px 20px; background: #4CAF50; color: white; border-radius: 10px; text-decoration: none; margin-top: 20px;">📥 Télécharger l\'image</a>', unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"❌ Erreur: Impossible de charger l'image")
        st.info("**Vérifiez:**")
        st.code(f"""
        Dossier: Medicoi
        Sous-dossier: Société ApiDiDoc (en France)
        Fichier: Flyer ApiDiDoc.png
        
        URL complète:
        {image_url}
        """)
        
        # زر للتحقق
        st.markdown(f'[🔗 Vérifier le lien dans le navigateur]({image_url})', unsafe_allow_html=True)
