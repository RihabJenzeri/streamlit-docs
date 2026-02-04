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

# ========== SUPPRIMER LE MENU PAR DÉFAUT DE STREAMLIT ET CHANGER LE BACKGROUND ==========
hide_default_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp {
    background-color: white;
}
/* Changer la couleur de police en gris pour tout le texte */
h1, h2, h3, h4, h5, h6, p, div, span, label, .stMarkdown, .stTitle {
    color: #666666 !important;
}
.stButton > button {
    color: #666666;
}
.caption-text {
    color: #888888;
    font-size: 14px;
}
/* Supprimer les marges et paddings par défaut */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}
/* Style pour le slide image */
.slide-container {
    position: relative;
    width: 100vw;
    margin-left: calc(-50vw + 50%);
    overflow: hidden;
}
.slide-image {
    width: 100%;
    height: 400px;
    object-fit: cover;
}
/* Style pour la carte de profil */
.profile-card {
    background: linear-gradient(135deg, rgba(251, 189, 250, 0.1) 0%, rgba(108, 212, 255, 0.1) 100%);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 25px;
    margin: -50px auto 30px auto;
    max-width: 800px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.5);
}
.profile-content {
    display: flex;
    align-items: center;
    gap: 25px;
}
.profile-avatar {
    position: relative;
    min-width: 120px;
}
.avatar-circle {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background: linear-gradient(135deg, #FBBDFA, #6cd4ff);
    padding: 5px;
}
.avatar-image {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}
.status-dot {
    position: absolute;
    bottom: 10px;
    right: 10px;
    width: 20px;
    height: 20px;
    background-color: #34D399;
    border-radius: 50%;
    border: 4px solid white;
}
.profile-info {
    flex: 1;
}
.profile-title {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 8px;
    color: #202124 !important;
}
.profile-subtitle {
    font-size: 16px;
    color: #666666;
    margin-bottom: 20px;
}
.contact-links {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}
.contact-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    border-radius: 25px;
    text-decoration: none !important;
    font-weight: 500;
    font-size: 14px;
    transition: all 0.3s ease;
}
.contact-email {
    background-color: rgba(251, 189, 250, 0.2);
    color: #202124 !important;
}
.contact-linkedin {
    background-color: rgba(32, 33, 36, 0.05);
    color: #202124 !important;
}
.contact-github {
    background-color: rgba(32, 33, 36, 0.05);
    color: #202124 !important;
}
.contact-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}
</style>
"""
st.markdown(hide_default_menu, unsafe_allow_html=True)

# ========== MENU DE NAVIGATION SIMPLE AVEC DÉGRADÉ ==========
def create_menu():
    # Style CSS pour le menu avec dégradé radial
    menu_style = """
    <style>
    .full-width-navbar {
        background-image: radial-gradient(circle at 0% 0%, #fbBDFA 0, transparent 55%), 
                          radial-gradient(circle at 100% 0%, #6cd4ff 0, transparent 50%), 
                          radial-gradient(circle at 20% 90%, #34d399 0, transparent 55%);
        height: 60px;
        width: 100%;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 20px;
    }
    .profile-circle-large {
        width: 45px;
        height: 45px;
        background-color: white;
        border-radius: 50%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        cursor: pointer;
    }
    </style>
    """
    
    st.markdown(menu_style, unsafe_allow_html=True)
    
    # Navbar avec seulement le dégradé et le cercle de profil
    st.markdown("""
    <div class="full-width-navbar">
        <div class="profile-circle-large"></div>
    </div>
    """, unsafe_allow_html=True)

# Afficher le menu
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

# URL pour les images
behance_cover_url = get_image_url("Behance Cover.jpeg")
profile_image_url = get_image_url("image.png")
flyer_url = get_image_url("Medicofi/Société ApniDoc (en France)/Flyer ApniDoc.png")
pdf_url_raw = f"{BASE_URL}mes_documents/Portfolio%20Ines%20HARRABI%202024.pdf"
pdf_url_encoded = urllib.parse.quote(pdf_url_raw, safe='')
google_viewer_url = f"https://docs.google.com/viewer?url={pdf_url_encoded}&embedded=true"

# Gérer la navigation par paramètres URL
query_params = st.query_params
if "page" in query_params:
    st.session_state.page = query_params["page"]

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    # Slide image qui sort de la boîte des éléments
    st.markdown(f"""
    <div class="slide-container">
        <img src="{behance_cover_url}" class="slide-image">
    </div>
    """, unsafe_allow_html=True)
    
    # Carte de profil avec photo
    st.markdown(f"""
    <div class="profile-card">
        <div class="profile-content">
            <div class="profile-avatar">
                <div class="avatar-circle">
                    <img src="{profile_image_url}" class="avatar-image" alt="Photo de profil">
                </div>
                <div class="status-dot"></div>
            </div>
            <div class="profile-info">
                <h1 class="profile-title">Mon Portfolio</h1>
                <p class="profile-subtitle">Designer & Développeuse Web Créative</p>
                <div class="contact-links">
                    <a href="mailto:contact@example.com" class="contact-btn contact-email">
                        ✉️ Contact
                    </a>
                    <a href="https://linkedin.com" target="_blank" class="contact-btn contact-linkedin">
                        🔗 LinkedIn
                    </a>
                    <a href="https://github.com" target="_blank" class="contact-btn contact-github">
                        🎨 GitHub
                    </a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Espace après la carte de profil
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    # Contenu normal
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
    st.markdown("<p class='caption-text'>📄 Flyer ApniDoc</p>", unsafe_allow_html=True)
    
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
            st.markdown(f"<p class='caption-text'>{img_name}</p>", unsafe_allow_html=True)
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
        st.markdown(f'<a href="{pdf_url_raw}" download="Portfolio_Ines_HARRABI_2024.pdf" style="text-decoration: none; color: #666666;">', unsafe_allow_html=True)
        if st.button("📥 Télécharger le PDF", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<a href="{google_viewer_url}" target="_blank" style="text-decoration: none; color: #666666;">', unsafe_allow_html=True)
        if st.button("🔗 Ouvrir dans Google Viewer", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)
