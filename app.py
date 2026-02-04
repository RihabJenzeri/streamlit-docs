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

# ========== CSS PERSONNALISÉ POUR LE MENU ==========
st.markdown("""
<style>
/* Container principal pour le menu */
.menu-container {
    background-image: 
        radial-gradient(circle at 0% 0%, #ffbdfa 0, transparent 55%), 
        radial-gradient(circle at 100% 0%, #6cd4ff 0, transparent 50%), 
        radial-gradient(circle at 20% 90%, #34d399 0, transparent 55%);
    padding: 20px 40px;
    border-radius: 0;
    margin: -50px -16px 30px -16px;
    min-height: 100px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
}

/* Icône de profil dans un cercle à droite */
.profile-circle {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, #ffffff55, #ffffff22);
    backdrop-filter: blur(10px);
    border: 2px solid #ffffff44;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    margin-left: 20px;
}

.profile-circle:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.profile-icon {
    font-size: 28px;
    color: white;
    text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
}

/* Style des boutons de navigation */
.menu-button {
    background: rgba(255, 255, 255, 0.15) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    color: white !important;
    font-weight: 500 !important;
    border-radius: 12px !important;
    padding: 10px 20px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1) !important;
    margin: 0 5px !important;
    min-width: 120px !important;
}

.menu-button:hover {
    background: rgba(255, 255, 255, 0.25) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15) !important;
    color: white !important;
}

/* Style pour les conteneurs de boutons */
.stButton > button {
    border: none;
}

/* Style des titres et texte */
h1, h2, h3 {
    color: #2c3e50;
}

/* Style pour le conteneur principal */
.main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Ajustement pour le layout */
.block-container {
    padding-top: 0 !important;
}

/* Centrer le contenu du menu */
.menu-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
}

.menu-buttons {
    display: flex;
    gap: 10px;
    flex: 1;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

# ========== MENU DE NAVIGATION AVEC DÉGRADÉ ==========
def create_menu():
    # Création du menu avec dégradé radial
    st.markdown('<div class="menu-container">', unsafe_allow_html=True)
    st.markdown('<div class="menu-content">', unsafe_allow_html=True)
    
    # Colonne pour les boutons de navigation
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    # Boutons de navigation
    with col1:
        if st.button("🏠 Accueil", key="menu_accueil", help="Retour à l'accueil"):
            st.session_state.page = "accueil"
            st.rerun()
    
    with col2:
        if st.button("🏥 Medicofi", key="menu_medicofi", help="Accéder à Medicofi"):
            st.session_state.page = "medicofi"
            st.rerun()
    
    with col3:
        if st.button("📄 Portfolio", key="menu_portfolio", help="Voir le portfolio PDF"):
            st.session_state.page = "pdf_viewer"
            st.rerun()
    
    with col4:
        # Cercle de profil à droite
        st.markdown("""
        <div class="profile-circle">
            <div class="profile-icon">👤</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Afficher le menu sur toutes les pages
create_menu()

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
st.markdown('<div class="main">', unsafe_allow_html=True)

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.title("📂 MES DOSSIERS")
    st.subheader("Portfolio Professionnel & Projets Design")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏥 MEDICOFI", use_container_width=True):
            st.session_state.page = "medicofi"
            st.rerun()
    
    with col2:
        if st.button("📄 PORTFOLIO PDF", use_container_width=True):
            st.session_state.page = "pdf_viewer"
            st.rerun()

elif st.session_state.page == "medicofi":
    if st.button("← RETOUR"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.title("🏥 MEDICOFI")
    
    if st.button("🇫🇷 SOCIÉTÉ APNIDOC (EN FRANCE)", use_container_width=True):
        st.session_state.page = "apnidoc"
        st.rerun()

elif st.session_state.page == "apnidoc":
    if st.button("← RETOUR"):
        st.session_state.page = "medicofi"
        st.rerun()
    
    st.title("🇫🇷 SOCIÉTÉ APNIDOC")
    
    # Flyer Image
    st.image(flyer_url, use_container_width=True)
    st.caption("📄 Flyer ApniDoc")
    
    st.markdown("---")
    
    # Design Interface Button
    if st.button("🎨 DESIGN INTERFACE WEB SITE APNIDOC (RESPONSIVE)", use_container_width=True):
        st.session_state.page = "design_folders"
        st.rerun()

elif st.session_state.page == "design_folders":
    if st.button("← RETOUR"):
        st.session_state.page = "apnidoc"
        st.rerun()
    
    st.title("🎨 DESIGN INTERFACE WEB SITE APNIDOC")
    
    # Website Link Section
    st.markdown("---")
    st.markdown("### 🌐 Site Web ApniDoc")
    st.write("(Le site web est déjà en ligne, mais il est toujours en cours de développement.)")
    st.markdown("🔗 **[Visiter https://apnidoc.fr/](https://apnidoc.fr/)**")
    st.markdown("---")
    
    # Device Selection
    st.subheader("Choisissez un format :")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🖥️ DESKTOP", use_container_width=True):
            st.session_state.current_device = "Desktop"
            st.session_state.page = "device_images"
            st.rerun()
    
    with col2:
        if st.button("📱 IPAD", use_container_width=True):
            st.session_state.current_device = "iPad"
            st.session_state.page = "device_images"
            st.rerun()
    
    with col3:
        if st.button("📱 PHONE", use_container_width=True):
            st.session_state.current_device = "Phone"
            st.session_state.page = "device_images"
            st.rerun()

elif st.session_state.page == "device_images":
    if st.button("← RETOUR"):
        st.session_state.page = "design_folders"
        st.session_state.current_device = None
        st.rerun()
    
    device = st.session_state.current_device
    device_icons = {
        "Desktop": "🖥️",
        "iPad": "📱",
        "Phone": "📱"
    }
    
    st.title(f"{device_icons.get(device, '📱')} DESIGN {device.upper()}")
    
    # Display images
    if device in design_images:
        for img_path in design_images[device]:
            img_url = get_image_url(img_path)
            img_name = img_path.split('/')[-1].replace('.png', '').replace('_', ' ')
            
            st.image(img_url, use_container_width=True)
            st.caption(img_name)
            st.markdown("---")

elif st.session_state.page == "pdf_viewer":
    if st.button("← RETOUR"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.title("📄 PORTFOLIO INES HARRABI 2024")
    
    # PDF Viewer
    st.markdown(f'<iframe width="100%" height="800" src="{google_viewer_url}"></iframe>', unsafe_allow_html=True)
    
    # Action Buttons
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f'<a href="{pdf_url_raw}" download="Portfolio_Ines_HARRABI_2024.pdf" style="text-decoration: none;">', unsafe_allow_html=True)
        if st.button("📥 Télécharger le PDF", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<a href="{google_viewer_url}" target="_blank" style="text-decoration: none;">', unsafe_allow_html=True)
        if st.button("🔗 Ouvrir dans Google Viewer", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
