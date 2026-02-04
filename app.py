import streamlit as st
import urllib.parse

# ========== الإعدادات ==========
GITHUB_USER = "RihabJenzeri"
REPO_NAME = "streamlit-docs"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/"

# ========== حالة التطبيق ==========
if 'page' not in st.session_state:
    st.session_state.page = "accueil"
if 'current_device' not in st.session_state:
    st.session_state.current_device = None

# ========== CSS PERSONNALISÉ ==========
st.markdown("""
<style>
/* Reset et fond général */
.stApp {
    background-color: #000000 !important;
    color: #ffffff !important;
}

/* Container principal */
.main-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    min-height: 100vh;
}

/* Header avec background vert/noir */
.app-header {
    background: linear-gradient(135deg, #0a1929 0%, #001e3c 100%);
    padding: 15px 30px;
    border-radius: 12px;
    margin-bottom: 30px;
    box-shadow: 0 4px 20px rgba(0, 100, 255, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* Titre principal */
.main-title {
    color: #ffffff;
    font-size: 24px;
    font-weight: 600;
    margin: 0;
}

/* Navigation moderne */
.nav-container {
    display: flex;
    gap: 10px;
    align-items: center;
}

.nav-button {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    color: #ffffff !important;
    border-radius: 8px !important;
    padding: 8px 16px !important;
    font-size: 14px !important;
    transition: all 0.3s ease !important;
}

.nav-button:hover {
    background: rgba(255, 255, 255, 0.2) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 12px rgba(0, 150, 255, 0.2) !important;
}

/* Bouton de profil */
.profile-btn {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    color: #ffffff !important;
    border-radius: 50% !important;
    width: 40px !important;
    height: 40px !important;
    padding: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

/* Contenu principal */
.content-area {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 30px;
    margin-top: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Section des dossiers */
.folders-section {
    text-align: center;
    margin-top: 40px;
}

.folders-title {
    color: #ffffff;
    font-size: 28px;
    margin-bottom: 10px;
    font-weight: 600;
}

.folders-subtitle {
    color: rgba(255, 255, 255, 0.7);
    font-size: 16px;
    margin-bottom: 40px;
}

/* Boutons des dossiers */
.folder-buttons-container {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-top: 30px;
}

.folder-btn {
    background: linear-gradient(135deg, #0066cc 0%, #004d99 100%) !important;
    border: none !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 20px 40px !important;
    font-size: 16px !important;
    font-weight: 500 !important;
    min-width: 200px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(0, 102, 204, 0.3) !important;
}

.folder-btn:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 8px 25px rgba(0, 102, 204, 0.4) !important;
    background: linear-gradient(135deg, #0077e6 0%, #0059b3 100%) !important;
}

/* Style pour les titres de page */
.page-title {
    color: #ffffff;
    font-size: 32px;
    margin-bottom: 20px;
    font-weight: 600;
    text-align: center;
}

/* Style pour les boutons de retour */
.back-button {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    color: #ffffff !important;
    border-radius: 8px !important;
    padding: 10px 20px !important;
    margin-bottom: 20px !important;
}

/* Image container */
.image-container {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 20px;
    margin: 20px 0;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Style pour les cartes */
.card {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 20px;
    margin: 10px 0;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.3s ease;
}

.card:hover {
    background: rgba(255, 255, 255, 0.1);
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(0, 100, 255, 0.2);
}

/* Style pour les séparateurs */
hr {
    border-color: rgba(255, 255, 255, 0.1) !important;
    margin: 30px 0 !important;
}

/* Style pour les légendes */
.caption-text {
    color: rgba(255, 255, 255, 0.7) !important;
    font-size: 14px !important;
    text-align: center !important;
    margin-top: 10px !important;
}

/* Réduire le padding par défaut de Streamlit */
.block-container {
    padding-top: 10px !important;
    padding-bottom: 10px !important;
}

/* Style pour les liens */
a {
    color: #66b3ff !important;
    text-decoration: none !important;
}

a:hover {
    color: #99ccff !important;
    text-decoration: underline !important;
}
</style>
""", unsafe_allow_html=True)

# ========== HEADER SIMPLE ==========
def create_header():
    # Header avec navigation
    st.markdown('<div class="app-header">', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
    
    with col1:
        st.markdown('<div class="main-title">📁 MES DOSSIERS</div>', unsafe_allow_html=True)
    
    with col2:
        if st.button("Accueil", key="header_accueil", help="Retour à l'accueil"):
            st.session_state.page = "accueil"
            st.rerun()
    
    with col3:
        if st.button("Medicofi", key="header_medicofi", help="Accéder à Medicofi"):
            st.session_state.page = "medicofi"
            st.rerun()
    
    with col4:
        if st.button("Portfolio", key="header_portfolio", help="Voir le portfolio PDF"):
            st.session_state.page = "pdf_viewer"
            st.rerun()
    
    with col5:
        if st.button("👤", key="header_profile", help="Profil"):
            # Vous pouvez ajouter une action pour le profil ici
            st.info("Fonctionnalité profil à venir")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Afficher le header
create_header()

# ========== روابط الملفات ==========
def get_image_url(path):
    """Generate GitHub raw URL for images"""
    return f"{BASE_URL}mes_documents/{urllib.parse.quote(path)}"

# Define all image paths
design_images = {
    "Desktop": [
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Desktop/Desktop Accueil.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Desktop/Desktop Bouton Prise de RDV.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Desktop/Desktop Comment ça marche.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Desktop/Desktop Qui sommes-nous.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Desktop/Desktop Vous êtes médecin _.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Desktop/Desktop la polygraphie.png"
    ],
    "iPad": [
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Ipad/iPad Accueil.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Ipad/iPad Comment ça marche.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Ipad/iPad Qui sommes-nous.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Ipad/iPad la polygraphie.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Ipad/ipad Bouton Prise de RDV.png"
    ],
    "Phone": [
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Phone/Phone Bouton Prise de RDV.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Phone/iPhone 13 & 14 Accueil.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Phone/iPhone 13 & 14 Comment ça marche.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Phone/iPhone 13 & 14 Qui la polygraphie.png",
        "Medicofi/Société ApniDoc (en France)/Design Interface web site ApniDoc (responsive)/Phone/iPhone 13 & 14 Qui sommes-nous.png"
    ]
}

flyer_url = get_image_url("Medicofi/Société ApniDoc (en France)/Flyer ApniDoc.png")
pdf_url_raw = f"{BASE_URL}mes_documents/Portfolio%20Ines%20HARRABI%202024.pdf"
pdf_url_encoded = urllib.parse.quote(pdf_url_raw, safe='')
google_viewer_url = f"https://docs.google.com/viewer?url={pdf_url_encoded}&embedded=true"

# Gérer la navigation par paramètres URL
query_params = st.query_params
if "page" in query_params:
    st.session_state.page = query_params["page"]

# ========== CONTENU PRINCIPAL ==========
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown('<div class="content-area">', unsafe_allow_html=True)
    
    st.markdown('<div class="folders-section">', unsafe_allow_html=True)
    st.markdown('<h1 class="folders-title">MES DOSSIERS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="folders-subtitle">Portfolio Professionnel & Projets Design</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏥 MEDICOFI", key="home_medicofi", use_container_width=True):
            st.session_state.page = "medicofi"
            st.rerun()
    
    with col2:
        if st.button("📄 PORTFOLIO PDF", key="home_portfolio", use_container_width=True):
            st.session_state.page = "pdf_viewer"
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "medicofi":
    st.markdown('<div class="content-area">', unsafe_allow_html=True)
    
    if st.button("← RETOUR", key="back_from_medicofi"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown('<h1 class="page-title">🏥 MEDICOFI</h1>', unsafe_allow_html=True)
    
    if st.button("🇫🇷 SOCIÉTÉ APNIDOC (EN FRANCE)", key="medicofi_apnidoc", use_container_width=True):
        st.session_state.page = "apnidoc"
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "apnidoc":
    st.markdown('<div class="content-area">', unsafe_allow_html=True)
    
    if st.button("← RETOUR", key="back_from_apnidoc"):
        st.session_state.page = "medicofi"
        st.rerun()
    
    st.markdown('<h1 class="page-title">🇫🇷 SOCIÉTÉ APNIDOC</h1>', unsafe_allow_html=True)
    
    # Flyer Image
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image(flyer_url, use_container_width=True)
    st.markdown('<p class="caption-text">📄 Flyer ApniDoc</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Design Interface Button
    if st.button("🎨 DESIGN INTERFACE WEB SITE APNIDOC (RESPONSIVE)", key="apnidoc_design", use_container_width=True):
        st.session_state.page = "design_folders"
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "design_folders":
    st.markdown('<div class="content-area">', unsafe_allow_html=True)
    
    if st.button("← RETOUR", key="back_from_design"):
        st.session_state.page = "apnidoc"
        st.rerun()
    
    st.markdown('<h1 class="page-title">🎨 DESIGN INTERFACE WEB SITE APNIDOC</h1>', unsafe_allow_html=True)
    
    # Website Link Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🌐 Site Web ApniDoc")
    st.write("(Le site web est déjà en ligne, mais il est toujours en cours de développement.)")
    st.markdown("🔗 **[Visiter https://apnidoc.fr/](https://apnidoc.fr/)**")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Device Selection
    st.markdown("### Choisissez un format :")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🖥️ DESKTOP", key="device_desktop", use_container_width=True):
            st.session_state.current_device = "Desktop"
            st.session_state.page = "device_images"
            st.rerun()
    
    with col2:
        if st.button("📱 IPAD", key="device_ipad", use_container_width=True):
            st.session_state.current_device = "iPad"
            st.session_state.page = "device_images"
            st.rerun()
    
    with col3:
        if st.button("📱 PHONE", key="device_phone", use_container_width=True):
            st.session_state.current_device = "Phone"
            st.session_state.page = "device_images"
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "device_images":
    st.markdown('<div class="content-area">', unsafe_allow_html=True)
    
    if st.button("← RETOUR", key="back_from_device"):
        st.session_state.page = "design_folders"
        st.session_state.current_device = None
        st.rerun()
    
    device = st.session_state.current_device
    device_icons = {
        "Desktop": "🖥️",
        "iPad": "📱",
        "Phone": "📱"
    }
    
    st.markdown(f'<h1 class="page-title">{device_icons.get(device, "📱")} DESIGN {device.upper()}</h1>', unsafe_allow_html=True)
    
    # Display images
    if device in design_images:
        for img_path in design_images[device]:
            img_url = get_image_url(img_path)
            img_name = img_path.split('/')[-1].replace('.png', '').replace('_', ' ')
            
            st.markdown('<div class="image-container">', unsafe_allow_html=True)
            st.image(img_url, use_container_width=True)
            st.markdown(f'<p class="caption-text">{img_name}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "pdf_viewer":
    st.markdown('<div class="content-area">', unsafe_allow_html=True)
    
    if st.button("← RETOUR", key="back_from_pdf"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown('<h1 class="page-title">📄 PORTFOLIO INES HARRABI 2024</h1>', unsafe_allow_html=True)
    
    # PDF Viewer
    st.markdown(f'<iframe width="100%" height="800" src="{google_viewer_url}"></iframe>', unsafe_allow_html=True)
    
    # Action Buttons
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f'<a href="{pdf_url_raw}" download="Portfolio_Ines_HARRABI_2024.pdf" style="text-decoration: none;">', unsafe_allow_html=True)
        if st.button("📥 Télécharger le PDF", key="download_pdf", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<a href="{google_viewer_url}" target="_blank" style="text-decoration: none;">', unsafe_allow_html=True)
        if st.button("🔗 Ouvrir dans Google Viewer", key="open_viewer", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
