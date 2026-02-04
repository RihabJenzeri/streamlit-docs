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
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

* {
    font-family: 'Montserrat', "Helvetica Neue", Helvetica, Arial, sans-serif !important;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp {
    background-color: white;
    font-family: 'Montserrat', "Helvetica Neue", Helvetica, Arial, sans-serif !important;
}
.stButton > button {
    color: #666666;
    font-family: 'Montserrat', "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.caption-text {
    color: #888888;
    font-size: 14px;
    font-family: 'Montserrat', "Helvetica Neue", Helvetica, Arial, sans-serif;
}
/* Supprimer les marges et paddings par défaut */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    font-family: 'Montserrat', "Helvetica Neue", Helvetica, Arial, sans-serif;
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
    object-fit: cover;
}
/* Style pour la carte de profil */
.profile-card {
    background: linear-gradient(135deg, rgba(251, 189, 250, 0.1) 0%, rgba(108, 212, 255, 0.1) 100%);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 25px;
    margin: -30px auto 30px auto;
    max-width: 1000px;
    width: 90%;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.5);
}
/* Nouvelle carte avec dégradé radial */
.gradient-card {
    background:
        radial-gradient(circle at 0% 0%, rgba(251, 189, 250, 0.55), transparent 55%),
        radial-gradient(circle at 100% 100%, rgba(140, 210, 255, 0.40), transparent 55%),
        radial-gradient(circle at 0% 100%, rgba(255, 255, 255, 0.70), transparent 60%),
        #fdfefe;
    border-radius: 20px;
    padding: 25px;
    margin: 20px auto;
    max-width: 1000px;
    width: 90%;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.5);
}

.st-emotion-cache-tn0cau {
    gap: 0.61rem !important;
}
.profile-content {
    display: flex;
    align-items: center;
    gap: 25px;
}
.profile-avatar {
    position: relative;
    min-width: 120px;
    flex-shrink: 0;
}
.avatar-circle {
    width: 170px;
    height: 170px;
    border-radius: 50%;
    padding: 3px;
    border: 3px solid #E4E4E4;
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
    min-width: 0;
}
.profile-title {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 8px;
    color: #202124 !important;
    font-family: 'Montserrat', "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.profile-subtitle {
    font-size: 16px;
    color: #666666;
    margin-bottom: 20px;
    font-family: 'Montserrat', "Helvetica Neue", Helvetica, Arial, sans-serif;
}
/* Styles pour les boutons de contact */
.contact-links {
    display: flex;
    flex-wrap: nowrap;
    gap: 10px;
    justify-content: flex-start;
    width: 100%;
    overflow: visible;
}

.contact-icon {
    width: 20px;
    height: 20px;
    color: #202124;
    transition: all 0.3s ease;
}

.contact-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 10px 15px;
    border-radius: 25px;
    text-decoration: none !important;
    font-weight: 500;
    font-size: 14px;
    transition: all 0.3s ease;
    font-family: 'Montserrat', "Helvetica Neue", Helvetica, Arial, sans-serif;
    background-color: #f5f5f5;
    color: #202124 !important;
    border: 1px solid #e0e0e0;
    cursor: pointer;
    white-space: nowrap;
    flex: 1;
    min-width: 0;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Effet hover pour tous les boutons */
.contact-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(251, 189, 250, 0.3);
    background-color: #fff2ff;
    border-color: #FBBDFA;
    color: #202124 !important;
}

/* Icônes restent foncées au hover */
.contact-btn:hover .contact-icon {
    color: #202124;
}

/* WhatsApp avec le même hover rose */
.contact-whatsapp:hover {
    background-color: #fff2ff !important;
    border-color: #FBBDFA !important;
}

/* Effet de clic */
.contact-btn:active {
    transform: translateY(0);
    background-color: #f0e0ef;
}

/* Styles pour la grille de projets */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.project-card {
    position: relative;
    background-color: white;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    border: 1px solid #f0f0f0;
    text-decoration: none !important;
    transition: all 0.3s ease;
    overflow: hidden;
}

.project-card:hover {
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    transform: translateY(-5px);
    border-color: transparent;
}

.hover-gradient {
    position: absolute;
    inset: 0;
    opacity: 0;
    transition: opacity 0.5s ease;
}

.project-card:hover .hover-gradient {
    opacity: 0.1;
}

.project-content {
    position: relative;
    display: flex;
    align-items: center;
    gap: 16px;
}

.project-icon {
    width: 56px;
    height: 56px;
    border-radius: 12px;
    background: linear-gradient(to bottom right, #f9f9f9, #f0f0f0);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.project-card:hover .project-icon {
    background: linear-gradient(to bottom right, white, rgba(255, 255, 255, 0.8));
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.project-text {
    flex: 1;
}

.project-title {
    font-weight: 600;
    color: #202124;
    margin-bottom: 4px;
    transition: color 0.3s ease;
}

.project-card:hover .project-title {
    color: #FBBDFA;
}

.project-description {
    font-size: 14px;
    color: #666666;
    line-height: 1.4;
}

.project-arrow {
    width: 20px;
    height: 20px;
    color: #d0d0d0;
    transition: all 0.3s ease;
}

.project-card:hover .project-arrow {
    color: #FBBDFA;
    transform: translate(2px, -2px);
}

/* Ajustement pour les écrans plus petits */
@media (max-width: 768px) {
    .profile-card, .gradient-card {
        max-width: 95%;
        padding: 20px;
    }
    
    .profile-content {
        flex-direction: column;
        text-align: center;
        gap: 20px;
    }
    
    .contact-links {
        flex-wrap: wrap;
        justify-content: center;
    }
    
    .contact-btn {
        flex: 0 0 calc(50% - 10px);
        max-width: calc(50% - 10px);
    }
    
    .projects-grid {
        grid-template-columns: 1fr;
    }
}

/* Styles pour les titres Streamlit */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', "Helvetica Neue", Helvetica, Arial, sans-serif !important;
    font-weight: 600;
}

/* Styles pour le texte standard */
p, div, span {
    font-family: 'Montserrat', "Helvetica Neue", Helvetica, Arial, sans-serif !important;
}
</style>
"""
st.markdown(hide_default_menu, unsafe_allow_html=True)

# ========== MENU DE NAVIGATION SIMPLE AVEC DÉGRADÉ ==========
def create_menu():
    menu_style = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');
    
.full-width-navbar {
    background:
    radial-gradient(circle at 0% 0%, rgba(251, 189, 250, 0.55), transparent 55%),
    radial-gradient(circle at 100% 100%, rgba(140, 210, 255, 0.40), transparent 55%),
    radial-gradient(circle at 0% 100%, rgba(255, 255, 255, 0.70), transparent 60%),
    #fdfefe;
    height: 30px;
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
    font-family: 'Montserrat', "Helvetica Neue", Helvetica, Arial, sans-serif;
}
    </style>
    """
    
    st.markdown(menu_style, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="full-width-navbar">
    </div>
    """, unsafe_allow_html=True)

# Afficher le menu
create_menu()

# ========== روابط الملفات ==========
def get_image_url(path):
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
behance_cover_url = get_image_url("Behance Cover F.jpg")
profile_image_url = get_image_url("image.jpeg")
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
    # Slide image
    st.markdown(f"""
    <div class="slide-container">
        <img src="{behance_cover_url}" class="slide-image">
    </div>
    """, unsafe_allow_html=True)
    
    # Carte de profil AVEC ICÔNES CORRIGÉES
    st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <div class="profile-card">
            <div class="profile-content">
                <div class="profile-avatar">
                    <div class="avatar-circle">
                        <img src="{profile_image_url}" class="avatar-image" alt="Photo de profil">
                    </div>
                </div>
                <div class="profile-info">
                    <h1 class="profile-title">My Portfolio</h1>
                    <p class="profile-subtitle">Senior Graphic Designer</p>
                    <div class="contact-links">
                        <a href="mailto:inesharrabi.dev@gmail.com" class="contact-btn contact-email">
                            <span class="contact-icon">✉️</span>
                            Email
                        </a>
                        <a href="https://linkedin.com/in/ines-harrabi" target="_blank" class="contact-btn contact-linkedin">
                            <span class="contact-icon">👔</span>
                            LinkedIn
                        </a>
                        <a href="https://behance.net/inesharrabi" target="_blank" class="contact-btn contact-behance">
                            <span class="contact-icon">🎨</span>
                            Behance
                        </a>
                        <a href="https://wa.me/1234567890" target="_blank" class="contact-btn contact-whatsapp">
                            <span class="contact-icon">💬</span>
                            WhatsApp
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Espace
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
    
    # NOUVELLE SECTION PROJETS AVEC ICÔNES SIMPLES
    st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 40px;">
        <div class="gradient-card">
            <h2 style="text-align: center; color: #202124; margin-bottom: 30px;">Mes Projets Récents</h2>
            
            <div class="projects-grid">
                <!-- Projet 1 -->
                <a href="#" class="project-card">
                    <div class="hover-gradient" style="background: linear-gradient(to bottom right, #FBBDFA, #6cd4ff);"></div>
                    <div class="project-content">
                        <div class="project-icon">
                            <span>🎨</span>
                        </div>
                        <div class="project-text">
                            <h3 class="project-title">ApniDoc Website</h3>
                            <p class="project-description">Design d'interface responsive pour une plateforme médicale</p>
                        </div>
                        <div class="project-arrow">→</div>
                    </div>
                </a>
                
                <!-- Projet 2 -->
                <a href="#" class="project-card">
                    <div class="hover-gradient" style="background: linear-gradient(to bottom right, #6cd4ff, #34D399);"></div>
                    <div class="project-content">
                        <div class="project-icon">
                            <span>💼</span>
                        </div>
                        <div class="project-text">
                            <h3 class="project-title">Brand Identity</h3>
                            <p class="project-description">Création d'identité visuelle pour une startup tech</p>
                        </div>
                        <div class="project-arrow">→</div>
                    </div>
                </a>
                
                <!-- Projet 3 -->
                <a href="#" class="project-card">
                    <div class="hover-gradient" style="background: linear-gradient(to bottom right, #34D399, #FBBDFA);"></div>
                    <div class="project-content">
                        <div class="project-icon">
                            <span>📱</span>
                        </div>
                        <div class="project-text">
                            <h3 class="project-title">Mobile App UI</h3>
                            <p class="project-description">Design d'interface pour application mobile de fitness</p>
                        </div>
                        <div class="project-arrow">→</div>
                    </div>
                </a>
                
                <!-- Projet 4 -->
                <a href="#" class="project-card">
                    <div class="hover-gradient" style="background: linear-gradient(to bottom right, #FFC107, #FBBDFA);"></div>
                    <div class="project-content">
                        <div class="project-icon">
                            <span>📊</span>
                        </div>
                        <div class="project-text">
                            <h3 class="project-title">Dashboard Design</h3>
                            <p class="project-description">Interface de dashboard analytique pour SaaS</p>
                        </div>
                        <div class="project-arrow">→</div>
                    </div>
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
