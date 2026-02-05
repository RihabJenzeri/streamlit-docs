import streamlit as st
import urllib.parse

# ========== الإعدادات ==========
GITHUB_USER = "RihabJenzeri"
REPO_NAME = "streamlit-docs"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/"

# ========== حالة التطبيق ==========
if 'page' not in st.session_state:
    st.session_state.page = "accueil"
if 'current_image' not in st.session_state:
    st.session_state.current_image = None

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
    
    h1, h2, h3 {
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    
    h1 {
        font-size: 2.5rem;
        margin-bottom: 30px;
    }
    
    h2 {
        font-size: 2rem;
        margin-top: 20px;
    }
    
    .info-box {
        background: rgba(255, 255, 255, 0.1);
        border-left: 5px solid #4CAF50;
        padding: 15px;
        border-radius: 10px;
        margin: 20px 0;
        color: white;
    }
    
    .folder-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    
    .folder-card {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 20px;
        cursor: pointer;
        transition: all 0.3s;
        text-align: center;
        color: white;
    }
    
    .folder-card:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-5px);
        border-color: #FFD700;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    
    .folder-icon {
        font-size: 3rem;
        margin-bottom: 10px;
    }
    
    .folder-name {
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    .image-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    
    .image-card {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 15px;
        cursor: pointer;
        transition: all 0.3s;
        text-align: center;
    }
    
    .image-card:hover {
        transform: translateY(-3px);
        border-color: #4CAF50;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }
    
    .image-preview {
        width: 100%;
        height: 200px;
        object-fit: contain;
        border-radius: 8px;
        margin-bottom: 10px;
        border: 2px solid rgba(255, 255, 255, 0.1);
    }
    
    .image-name {
        color: white;
        font-size: 0.9rem;
        word-break: break-word;
    }
    
    .back-btn {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 10px 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        cursor: pointer;
        font-size: 16px;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        transition: all 0.3s;
    }
    
    .back-btn:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateX(-5px);
    }
    
    .large-image-container {
        text-align: center;
        margin: 30px 0;
    }
    
    .large-image {
        max-width: 80%;
        max-height: 600px;
        border: 3px solid white;
        border-radius: 15px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }
    
    .site-link {
        display: inline-block;
        background: linear-gradient(90deg, #FF6B6B, #FF8E53);
        color: white;
        padding: 12px 25px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        font-size: 18px;
        margin: 20px 0;
        transition: all 0.3s;
        box-shadow: 0 5px 15px rgba(255, 107, 107, 0.3);
    }
    
    .site-link:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# ========== روابط الملفات ==========
# رابط الموقع
site_url = "https://apnidoc.fr/"

# ========== دالة لبناء مسارات GitHub ==========
def build_github_path(folder_path, file_name=""):
    if file_name:
        return f"{BASE_URL}{folder_path}/{urllib.parse.quote(file_name)}"
    return f"{BASE_URL}{folder_path}"

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📂 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    # رابط الموقع
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 30px;">
        <a href="{site_url}" target="_blank" class="site-link">
            🌐 Consulter le site: apnidoc.fr
        </a>
        <p style="color: rgba(255,255,255,0.8); font-size: 14px; margin-top: 5px;">
            Le site web est déjà en ligne, mais il est toujours en cours de développement.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏥 Medicofi", key="medicofi", use_container_width=True):
            st.session_state.page = "medicofi"
            st.rerun()
    
    with col2:
        if st.button("📄 Portfolio PDF", key="portfolio", use_container_width=True):
            st.session_state.page = "pdf_viewer"
            st.rerun()

elif st.session_state.page == "medicofi":
    if st.button("← Retour"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>🏥 Medicofi</h1>", unsafe_allow_html=True)
    
    # عرض مجلدات Medicofi
    st.markdown('<div class="folder-grid">', unsafe_allow_html=True)
    
    # مجلد Société ApniDoc
    st.markdown("""
    <div class="folder-card" onclick="this.nextElementSibling.click()">
        <div class="folder-icon">🇫🇷</div>
        <div class="folder-name">Société ApniDoc (en France)</div>
        <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">Projet de télémédecine</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Ouvrir Société ApniDoc", key="apnidoc"):
        st.session_state.page = "apnidoc_folder"
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "apnidoc_folder":
    if st.button("← Retour"):
        st.session_state.page = "medicofi"
        st.rerun()
    
    st.markdown("<h1>🇫🇷 Société ApniDoc</h1>", unsafe_allow_html=True)
    
    # عرض محتويات مجلد Société ApniDoc
    st.markdown('<div class="folder-grid">', unsafe_allow_html=True)
    
    # Flyer ApniDoc
    flyer_url = build_github_path("mes_documents/Medicofi/Société ApniDoc (en France)", "Flyer ApniDoc.png")
    
    st.markdown(f"""
    <div class="folder-card" onclick="this.nextElementSibling.click()">
        <div class="folder-icon">🖼️</div>
        <div class="folder-name">Flyer ApniDoc</div>
        <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">Support de communication</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Voir Flyer", key="flyer"):
        st.session_state.page = "view_image"
        st.session_state.current_image = flyer_url
        st.session_state.image_name = "Flyer ApniDoc.png"
        st.rerun()
    
    # Design Interface
    st.markdown("""
    <div class="folder-card" onclick="this.nextElementSibling.click()">
        <div class="folder-icon">🎨</div>
        <div class="folder-name">Design Interface web site ApniDoc</div>
        <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">Design responsive</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Ouvrir Design Interface", key="design"):
        st.session_state.page = "design_folder"
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "design_folder":
    if st.button("← Retour"):
        st.session_state.page = "apnidoc_folder"
        st.rerun()
    
    st.markdown("<h1>🎨 Design Interface web site ApniDoc</h1>", unsafe_allow_html=True)
    
    # عرض المجلدات الفرعية
    st.markdown('<div class="folder-grid">', unsafe_allow_html=True)
    
    # Desktop
    st.markdown("""
    <div class="folder-card" onclick="this.nextElementSibling.click()">
        <div class="folder-icon">💻</div>
        <div class="folder-name">Desktop</div>
        <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">Version ordinateur</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Ouvrir Desktop", key="desktop"):
        st.session_state.page = "desktop_images"
        st.rerun()
    
    # Ipad
    st.markdown("""
    <div class="folder-card" onclick="this.nextElementSibling.click()">
        <div class="folder-icon">📱</div>
        <div class="folder-name">Ipad</div>
        <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">Version tablette</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Ouvrir Ipad", key="ipad"):
        st.session_state.page = "ipad_images"
        st.rerun()
    
    # Phone
    st.markdown("""
    <div class="folder-card" onclick="this.nextElementSibling.click()">
        <div class="folder-icon">📲</div>
        <div class="folder-name">Phone</div>
        <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">Version mobile</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Ouvrir Phone", key="phone"):
        st.session_state.page = "phone_images"
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# ========== صفحات عرض الصور حسب الجهاز ==========
elif st.session_state.page == "desktop_images":
    if st.button("← Retour"):
        st.session_state.page = "design_folder"
        st.rerun()
    
    st.markdown("<h1>💻 Desktop</h1>", unsafe_allow_html=True)
    
    # قائمة صور Desktop
    desktop_images = [
        "Desktop Accueil.png",
        "Desktop Bouton Prise de RDV.png", 
        "Desktop Comment ça marche.png",
        "Desktop Qui sommes-nous.png",
        "Desktop Vous êtes médecin ...png",
        "Desktop la polygraphie.png"
    ]
    
    # عرض الصور في grid
    st.markdown('<div class="image-grid">', unsafe_allow_html=True)
    
    for img_name in desktop_images:
        img_url = build_github_path("mes_documents/Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Desktop", img_name)
        
        st.markdown(f"""
        <div class="image-card" onclick="this.nextElementSibling.click()">
            <img src="{img_url}" class="image-preview" alt="{img_name}">
            <div class="image-name">{img_name}</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Voir {img_name}", key=f"desktop_{img_name}"):
            st.session_state.page = "view_image"
            st.session_state.current_image = img_url
            st.session_state.image_name = img_name
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "ipad_images":
    if st.button("← Retour"):
        st.session_state.page = "design_folder"
        st.rerun()
    
    st.markdown("<h1>📱 Ipad</h1>", unsafe_allow_html=True)
    
    # (يمكن إضافة صور Ipad هنا عندما تتوفر)
    st.info("Les images Ipad seront ajoutées bientôt...")

elif st.session_state.page == "phone_images":
    if st.button("← Retour"):
        st.session_state.page = "design_folder"
        st.rerun()
    
    st.markdown("<h1>📲 Phone</h1>", unsafe_allow_html=True)
    
    # (يمكن إضافة صور Phone هنا عندما تتوفر)
    st.info("Les images Phone seront ajoutées bientôt...")

# ========== صفحة عرض الصورة الكبيرة ==========
elif st.session_state.page == "view_image":
    if st.button("← Retour"):
        # العودة للصفحة السابقة بناءً على نوع الصورة
        if "Desktop" in st.session_state.get('image_name', ''):
            st.session_state.page = "desktop_images"
        else:
            st.session_state.page = "apnidoc_folder"
        st.rerun()
    
    st.markdown(f"<h1>{st.session_state.get('image_name', 'Image')}</h1>", unsafe_allow_html=True)
    
    # عرض الصورة الكبيرة
    if st.session_state.current_image:
        st.markdown(f"""
        <div class="large-image-container">
            <img src="{st.session_state.current_image}" class="large-image">
        </div>
        """, unsafe_allow_html=True)
        
        # زر التحميل
        st.markdown(f"""
        <div style="text-align: center; margin-top: 20px;">
            <a href="{st.session_state.current_image}" download="{st.session_state.get('image_name', 'image.png')}" 
               style="background: #4CAF50; color: white; padding: 10px 20px; border-radius: 8px; text-decoration: none;">
                📥 Télécharger l'image
            </a>
        </div>
        """, unsafe_allow_html=True)

# ========== صفحة PDF ==========
elif st.session_state.page == "pdf_viewer":
    if st.button("← Retour"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>📄 Portfolio Ines HARRABI 2024</h1>", unsafe_allow_html=True)
    
    pdf_url_raw = build_github_path("mes_documents", "Portfolio Ines HARRABI 2024.pdf")
    pdf_url_encoded = urllib.parse.quote(pdf_url_raw, safe='')
    google_viewer_url = f"https://docs.google.com/viewer?url={pdf_url_encoded}&embedded=true"
    
    # عرض PDF
    st.markdown(f"""
    <iframe class="pdf-frame" src="{google_viewer_url}"></iframe>
    """, unsafe_allow_html=True)
