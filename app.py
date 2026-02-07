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
    margin-top: 10px;
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
    width: 1000%;
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
    margin-bottom: 50px;
    max-width: 1000px;
    width: 1000%;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.5);
}

/* STYLE SPÉCIFIQUE POUR LES BOUTONS "Ouvrir MEDICOFI" ET "Ouvrir PORTFOLIO PDF" */
div[data-testid="column"]:nth-child(1) .st-emotion-cache-1anq8dj,
div[data-testid="column"]:nth-child(2) .st-emotion-cache-1anq8dj {
    background:
        radial-gradient(circle at 0% 0%, rgba(251, 189, 250, 0.55), transparent 55%),
        radial-gradient(circle at 100% 100%, rgba(140, 210, 255, 0.40), transparent 55%),
        radial-gradient(circle at 0% 100%, rgba(255, 255, 255, 0.70), transparent 60%),
        #fdfefe !important;
    color: #202124 !important;
    border: 1px solid rgba(251, 189, 250, 0.5) !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    margin-top: 15px !important;
}

div[data-testid="column"]:nth-child(1) .st-emotion-cache-1anq8dj:hover,
div[data-testid="column"]:nth-child(2) .st-emotion-cache-1anq8dj:hover {
    box-shadow: 0 5px 15px rgba(251, 189, 250, 0.4) !important;
    transform: translateY(-2px) !important;
    border-color: rgba(251, 189, 250, 0.8) !important;
}

div[data-testid="column"]:nth-child(1) .st-emotion-cache-1anq8dj:active,
div[data-testid="column"]:nth-child(2) .st-emotion-cache-1anq8dj:active {
    transform: translateY(0) !important;
}

/* Alternative plus directe avec JavaScript injection */
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
    # display: flex;
    flex-wrap: nowrap;
    gap: 10px;
    justify-content: flex-start;
    width: 115%;
    overflow: visible;
    position: relative;
    right: 10px;
}
.contact-icon {
    # width: 18px;
    height: 18px;
    stroke: #202124;
    fill: none;
    transition: all 0.3s ease;
}

.contact-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin: 0.2rem;
    padding: 10px 10px;
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

.contact-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(251, 189, 250, 0.3);
    background-color: #fff2ff;
    border-color: #FBBDFA;
    color: #202124 !important;
}

.contact-btn:hover .contact-icon {
    stroke: #202124;
}

.contact-whatsapp:hover {
    background-color: #fff2ff !important;
    border-color: #FBBDFA !important;
}

.contact-btn:active {
    transform: translateY(0);
    background-color: #f0e0ef;
}
.st-emotion-cache-2fgyt4 h1 {
    font-size: 2.75rem;
    color: #202124;
    font-weight: 700;
    padding: 1.25rem 0px 1rem;
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
        gap: 10px;
        width: 75%;
        overflow: visible;
        position: relative;
        right: -45px;
    }
    .st-emotion-cache-2fgyt4 h1 {
    font-size: 1.75rem;
    font-weight: 700;
    position: relative;
    left: 10px;
    /* padding: 1.25rem 0px 1rem; */
}
    .contact-btn {
        flex: 0 0 calc(50% - 10px);
        max-width: calc(50% - 10px);
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

/* Styles pour les cartes de dossiers */
.folder-card {
    background: white;
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 10px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    cursor: pointer;
    border: 1px solid #f0f0f0;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.folder-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(251, 189, 250, 0.25) !important;
    border-color: #FBBDFA !important;
}

@media (max-width: 768px) {
    .cards-grid {
        grid-template-columns: 1fr !important;
    }
}

/* Style pour les boutons de carte */
.card-button {
    all: unset;
    width: 100%;
    cursor: pointer;
}

/* Style pour le conteneur de grille */
.cards-grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 20px;
    width: 100%;
}
.st-emotion-cache-1anq8dj {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    text-transform: none;
    font-size: inherit;
    font-family: inherit;
    color: inherit;
    width: 100%;
    cursor: pointer;
    user-select: none;
    background-color: rgba(172, 177, 195, 0.25);
    border: 1px solid rgba(250, 250, 250, 0.2);
}

h3 svg {
    display: none !important;
}

h3::before, h3::after {
    content: none !important;
}
.st-emotion-cache-2fgyt4 hr {
    margin: 2em 0px;
    padding: 0px;
    color: inherit;
    background-color: #fbbdfa;
    border-top: none;
    border-right: none;
    border-left: none;
    border-image: initial;
    border-bottom: 1px solid rgba(250, 250, 250, 0.2);
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
    .profile-circle-large {
        width: 45px;
        height: 45px;
        background-color: white;
        border-radius: 50%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        cursor: pointer;
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
    # Slide image qui sort de la boîte des éléments
    st.markdown(f"""
    <div class="slide-container">
        <img src="{behance_cover_url}" class="slide-image">
    </div>
    """, unsafe_allow_html=True)

    # Carte de profil avec photo - CENTRÉE
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
                        <a href="mailto:harrabi.ines@yahoo.fr" class="contact-btn contact-email">
                            <svg class="contact-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                                <polyline points="22,6 12,13 2,6"/>
                            </svg>
                            Email
                        </a>
                        <a href="https://www.linkedin.com/in/inesharrabi" target="_blank" class="contact-btn contact-linkedin">
                            <svg class="contact-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
                                <rect x="2" y="9" width="4" height="12"/>
                                <circle cx="4" cy="4" r="2"/>
                            </svg>
                            LinkedIn
                        </a>
                        <a href="https://www.behance.net/harrabiines" target="_blank" class="contact-btn contact-behance">
                            <svg class="contact-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#000000">
                                <path d="M22 7h-7v-2h7v2zm1.726 10c-.442 1.297-2.029 3-5.101 3-3.074 0-5.564-1.729-5.564-5.675 0-3.91 2.325-5.92 5.466-5.92 3.082 0 4.964 1.782 5.375 4.426.078.506.109 1.188.095 2.14h-8.027c.13 3.211 3.483 3.312 4.588 2.029h3.168zm-7.686-4h4.965c-.105-1.547-1.136-2.219-2.477-2.219-1.466 0-2.277.768-2.488 2.219zm-9.574 6.988h-6.466v-14.967h6.953c5.476.081 5.58 5.444 2.72 6.906 3.461 1.26 3.577 8.061-3.207 8.061zm-3.466-8.988h3.584c2.508 0 2.906-3-.312-3h-3.272v3zm3.391 3h-3.391v3.016h3.341c3.055 0 2.868-3.016.05-3.016z"/>
                            </svg>
                            Behance
                        </a>
                        <a href="https://wa.me/21656171036" target="_blank" class="contact-btn contact-whatsapp">
                            <svg class="contact-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
                            </svg>
                            WhatsApp
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Espace après la carte de profil
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # NOUVELLE CARTE MES DOSSIERS avec boutons intégrés
    st.markdown("""
    <div style="display: flex; justify-content: center;">
        <div class="gradient-card" style="padding: 40px 30px;">
            <div style="text-align: center;">
                <p style="color: #202124; font-size: 16px;">As my <strong>Behance portfolio</strong> is currently being updated, I have gathered here a selected overview of my work. Below, you will find<strong> a PDF featuring my earlier projects</strong>, along with <strong>a folder showcasing my most recent work</strong>.</p>
            </div>
    """, unsafe_allow_html=True)

  # SUPPRIMER LES PARENTHESES AU DÉBUT ET À LA FIN !
# Utiliser des colonnes Streamlit pour créer les cartes
    col1, col2 = st.columns(2)

    # Carte MEDICOFI
    with col1:
        st.markdown("""
            <div class="folder-card">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div style="background: white; padding: 10px; border-radius: 12px; display: flex; align-items: center; justify-content: center; position: absolute; right: 19px; border: 2px solid #FBBDFA;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2">
                            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
                        </svg>
                    </div>
                    <div style="flex: 1;">
                        <h3 style="color: #202124;  font-size: 18px; font-weight: 600;padding-bottom:5px">My Recent Projects</h3>
                        <p style="color: #888; margin: 0; font-size: 14px;">Recent applications and projects</p>
                    </div>
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </div>
            </div>
        """, unsafe_allow_html=True)
        # Bouton MEDICOFI
        if st.button("OPEN", key="medicofi_card_btn", use_container_width=True):
            st.session_state.page = "medicofi"
            st.rerun()

    # Carte PORTFOLIO PDF
    with col2:
        st.markdown("""
            <div class="folder-card">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div style="background: white; padding: 10px; border-radius: 12px; display: flex; align-items: center; justify-content: center; position: absolute; right: 19px; border: 2px solid #9fd8fd;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#9fd8fd" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                            <polyline points="14,2 14,8 20,8"/>
                            <line x1="16" y1="13" x2="8" y2="13"/>
                            <line x1="16" y1="17" x2="8" y2="17"/>
                            <polyline points="10,9 9,9 8,9"/>
                        </svg>
                    </div>
                    <div style="flex: 1;">
                        <h3 style="color: #202124; font-size: 18px; font-weight: 600;padding-bottom:5px">My Earlier Projects </h3>
                        <p style="color: #888; margin: 0; font-size: 14px;">My old portfolio in PDF version</p>
                    </div>
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Bouton PORTFOLIO PDF
        if st.button("OPEN", key="pdf_card_btn", use_container_width=True):
            st.session_state.page = "pdf_viewer"
            st.rerun()

    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Injection JavaScript pour cibler les boutons spécifiques
    st.markdown("""
    <script>
    // Attendre que la page soit chargée
    setTimeout(function() {
        // Trouver tous les boutons avec la classe spécifique
        const buttons = document.querySelectorAll('.st-emotion-cache-1anq8dj');

        // Appliquer le style aux boutons dans les colonnes
        buttons.forEach((button, index) => {
            // Vérifier si le bouton est dans la première ou deuxième colonne
            const parentColumn = button.closest('[data-testid="column"]');
            if (parentColumn) {
                const columnIndex = Array.from(parentColumn.parentElement.children).indexOf(parentColumn);

                // Appliquer le style seulement aux boutons des deux premières colonnes
                if (columnIndex === 0 || columnIndex === 1) {
                    button.style.background = 'radial-gradient(circle at 0% 0%, rgba(251, 189, 250, 0.55), transparent 55%), radial-gradient(circle at 100% 100%, rgba(140, 210, 255, 0.40), transparent 55%), radial-gradient(circle at 0% 100%, rgba(255, 255, 255, 0.70), transparent 60%), #fdfefe';
                    button.style.color = '#202124';
                    button.style.border = '1px solid rgba(251, 189, 250, 0.5)';
                    button.style.fontWeight = '600';

                    // Ajouter les effets hover
                    button.addEventListener('mouseenter', function() {
                        this.style.boxShadow = '0 5px 15px rgba(251, 189, 250, 0.4)';
                        this.style.transform = 'translateY(-2px)';
                        this.style.borderColor = 'rgba(251, 189, 250, 0.8)';
                    });

                    button.addEventListener('mouseleave', function() {
                        this.style.boxShadow = '';
                        this.style.transform = '';
                        this.style.borderColor = 'rgba(251, 189, 250, 0.5)';
                    });

                    button.addEventListener('mousedown', function() {
                        this.style.transform = 'translateY(0)';
                    });

                    button.addEventListener('mouseup', function() {
                        this.style.transform = 'translateY(-2px)';
                    });
                }
            }
        });
    }, 1000); // Délai pour s'assurer que tout est chargé
    </script>
    """, unsafe_allow_html=True)

    # Espace entre les sections
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

elif st.session_state.page == "medicofi":
    if st.button("←"):
        st.session_state.page = "accueil"
        st.rerun()

    st.title("Work Portfolio")

    # Créer trois colonnes
    col1, col2, col3 = st.columns(3)

    # URLs des images spécifiques
    medicofi_image_url = get_image_url("img3.png")  # Image pour MEDICOFI
    freelance_image_url = get_image_url("img4.png")  # Image pour FREELANCE
    tse_image_url = get_image_url("img1.png")  # Image pour TSE

    # CSS pour le responsive et les boutons
    responsive_style = """
    <style>
    .responsive-image-container {
        width: 200px;
        height: 160px;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 5px;
        border: 2px solid white;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    @media (max-width: 768px) {
        .responsive-image-container {
        width: 435px;
        height: 215px;
        }
    }

    @media (max-width: 480px) {
        .responsive-image-container {
        width: 370px;
        height: 210px;
        }
    }

    /* Responsive pour les cartes sur mobile */
    @media (max-width: 768px) {
        .responsive-card {
            min-height: 200px !important;
            padding: 12px !important;
        }

        .responsive-card h3 {
            font-size: 16px !important;
        }

        .responsive-card p {
            font-size: 12px !important;
        }
    }

    @media (max-width: 480px) {
        .responsive-card {
            min-height: 180px !important;
            padding: 10px !important;
        }

        .responsive-card h3 {
            font-size: 14px !important;
        }

        .responsive-card p {
            font-size: 11px !important;
        }
    }
    
    /* Style personnalisé pour les boutons avec titre et sous-titre */
    .stButton > button {
        height: auto !important;
        white-space: normal !important;
        line-height: 1.4 !important;
        margin-top: 10px;
        
    }
    
    .custom-button-container {
        margin-bottom: 8px;
    }
    </style>
    """

    st.markdown(responsive_style, unsafe_allow_html=True)

    # Colonne 1: MEDICOFI (avec 8 projets) - Utilise img1.png
    with col1:
        st.markdown(f"""
        <div class="responsive-card" style="
            background:
                radial-gradient(circle at 0% 0%, rgba(251, 189, 250, 0.55), transparent 55%),
                radial-gradient(circle at 100% 100%, rgba(140, 210, 255, 0.40), transparent 55%),
                radial-gradient(circle at 0% 100%, rgba(255, 255, 255, 0.70), transparent 60%),
                #fdfefe;
            border-radius: 20px;
            padding: 8px;
            margin-bottom: 20px;
            box-shadow: 0 18px 40px rgba(17, 24, 39, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.5);
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 250px;
        ">
            <div class="responsive-image-container">
                <img src="{medicofi_image_url}"
                     style="width: 100%; height: 100%; object-fit: cover;"
                     alt="MEDICOFI">
            </div>
            <!-- MC Consulting (MEDICOFI) -->
            <div style="color: #202124; font-family: 'Montserrat', sans-serif; padding-bottom: 4px;">
                <span style="font-size: 18px; font-weight: 600; margin: 0;">MC CONLUTING</span>
                <div style="font-size: 14px; font-weight: 500; margin: 2px 0 0 0;">(MEDICOFI)</div>
            </div>
            <p style="color: #666; margin: 0; font-size: 14px; font-family: 'Montserrat', sans-serif;">
                Medicofi Group  ↓
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Liste des 8 boutons pour MEDICOFI avec titre et pays
        projects_medicofi = [
            ("Tire Lait Express Company", "(in France)", "medicofi8"),
            ("ApniDoc Company   ", "(in France)", "apnidoc"),
            ("Mamivac France Company", "", "medicofi2"),
            ("MC Consulting Company", "(in Tunisia)", "medicofi3"),
            ("MCM Externalisation Company  ", "(in Madagascar)", "medicofi4"),
            ("Respi Express Company", "(in France)", "medicofi5"),
            ("Sanibiose Company  ", "(in France)", "medicofi6"),
            ("Seinbiose Company  ", "(in France)", "medicofi7")
         ]

        for idx, (company_name, country, page_key) in enumerate(projects_medicofi):
            # Créer le label du bouton avec formatage HTML-like
            button_label = f"{company_name}\n{country}" if country else company_name
            
            if st.button(button_label, use_container_width=True, key=f"medicofi_{page_key}"):
                st.session_state.page = page_key
                st.rerun()

     # Colonne 2: FREELANCE - Utilise img2.png
    with col2:
        st.markdown(f"""
        <div class="responsive-card" style="
            background:
                radial-gradient(circle at 0% 0%, rgba(251, 189, 250, 0.55), transparent 55%),
                radial-gradient(circle at 100% 100%, rgba(140, 210, 255, 0.40), transparent 55%),
                radial-gradient(circle at 0% 100%, rgba(255, 255, 255, 0.70), transparent 60%),
                #fdfefe;
            border-radius: 20px;
            padding: 8px;
            margin-bottom: 20px;
            box-shadow: 0 18px 40px rgba(17, 24, 39, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.5);
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 250px;
        ">
            <div class="responsive-image-container">
                <img src="{freelance_image_url}"
                     style="width: 100%; height: 100%; object-fit: cover;"
                     alt="FREELANCE">
            </div>
            <!-- FREELANCE -->
            <div style="color: #202124; font-family: 'Montserrat', sans-serif; padding-bottom: 4px;">
                <span style="font-size: 18px; font-weight: 600; margin: 0;">FREELANCE</span>
                <div style="font-size: 14px; font-weight: 500; margin: 6px 0 0 0; height: 19px;">&nbsp;</div>
            </div>
            <p style="color: #666; margin: 0; font-size: 14px; font-family: 'Montserrat', sans-serif;">
                Independent Projects ↓
            </p>
        </div>
        """, unsafe_allow_html=True)

        # REMPLACÉ: Trois boutons au lieu d'un seul
        freelance_projects = [
            ("Chabeb Ennour\n(volunteer group)", "freelance_chabeb"),
            ("Clorex        \n    Company", "freelance_clorex"),
            ("Mayar Auto     \n    Company", "freelance_mayar")
        ]

        for project_name, page_key in freelance_projects:
            if st.button(project_name, use_container_width=True, key=f"freelance_{page_key}"):
                st.session_state.page = page_key
                st.rerun()


    # Colonne 3: TSE - Utilise img3.png
    with col3:
        st.markdown(f"""
        <div class="responsive-card" style="
            background:
                radial-gradient(circle at 0% 0%, rgba(251, 189, 250, 0.55), transparent 55%),
                radial-gradient(circle at 100% 100%, rgba(140, 210, 255, 0.40), transparent 55%),
                radial-gradient(circle at 0% 100%, rgba(255, 255, 255, 0.70), transparent 60%),
                #fdfefe;
            border-radius: 20px;
            padding: 8px;
            margin-bottom: 20px;
            box-shadow: 0 18px 40px rgba(17, 24, 39, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.5);
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 250px;
        ">
            <div class="responsive-image-container">
                <img src="{tse_image_url}"
                     style="width: 100%; height: 100%; object-fit: cover;"
                     alt="TSE">
            </div>
            <div style="color: #202124; font-family: 'Montserrat', sans-serif; padding-bottom: 4px;">
                <span style="font-size: 18px; font-weight: 600; margin: 0;">TSE</span>
                <div style="font-size: 14px; font-weight: 500; margin: 2px 0 0 0;">(Poli)</div>
            </div>
            <p style="color: #666; margin: 0; font-size: 14px; font-family: 'Montserrat', sans-serif;">
                Sportswear Design ↓
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Design    \n   & Layout", use_container_width=True, key="tse_btn"):
            st.session_state.page = "tse"
            st.rerun()
    # Page Mamivac France Company
elif st.session_state.page == "medicofi2":
    if st.button("←"):
        st.session_state.page = "medicofi"
        st.rerun()

    # Titre avec icône SVG de boîte (pour "Coque de l'appareil")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
        </svg>
        <h3 style="margin: 0; color: #202124;">Coque de l'appareil Sensitive C (Design Produit)</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Contrainte Principale - Affichage du contenu texte
    st.markdown("""
    <div style="background: #f9f9f9; padding: 15px; border-radius: 10px; border-left: 4px solid #FBBDFA; margin-bottom: 20px;">
         <div style="color: #666; font-size: 14px; line-height: 1.6;">
            Cette proposition de design a été conçue dans Photoshop, et non avec un logiciel de modélisation 3D.<br><br>
            La contrainte principale consiste à conserver l'intérieur du produit tout en modifiant uniquement la coque extérieure.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Bouton pour voir les propositions
    if st.button("PROPOSITIONS COQUE SENSITIVE C", use_container_width=True):
        st.session_state.page = "mamivac_propositions"
        st.rerun()
    
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    # Séparateur
    st.markdown("---")
    
    # Section Emailings et Newsletters avec icône
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
            <polyline points="22,6 12,13 2,6"></polyline>
        </svg>
        <h3 style="margin: 0; color: #202124;">Emailing et Newsletters</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Description
    st.markdown('<div style="color: #666; margin-bottom: 20px;">Design and integration of email campaigns & newsletters</div>', unsafe_allow_html=True)
    
    # Affichage des 4 images d'emailing
    emailing_images = [
        "Medicofi/Société Mamivac France/Emailing et Newsletters/Emailing 1.png",
        "Medicofi/Société Mamivac France/Emailing et Newsletters/Emailing 2.png",
        "Medicofi/Société Mamivac France/Emailing et Newsletters/Emailing 3.png",
        "Medicofi/Société Mamivac France/Emailing et Newsletters/Emailing 4.png"
    ]
    
    # Afficher les images en 2 colonnes
    col1, col2 = st.columns(2)
    
    with col1:
        # Email 1
        email1_url = get_image_url(emailing_images[0])
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="{email1_url}" style="width: 500px; max-width: 100%; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
        
        # Email 2
        email2_url = get_image_url(emailing_images[1])
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="{email2_url}" style="width: 500px; max-width: 100%; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Email 3
        email3_url = get_image_url(emailing_images[2])
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="{email3_url}" style="width: 500px; max-width: 100%; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
        
        # Email 4
        email4_url = get_image_url(emailing_images[3])
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="{email4_url}" style="width: 500px; max-width: 100%; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
            # Séparateur
    st.markdown("---")
    
    # Section Sensitive C & Breast Pump Shields Brochure avec icône
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="3" width="20" height="18" rx="2" ry="2"></rect>
            <line x1="9" y1="21" x2="15" y2="21"></line>
            <line x1="12" y1="17" x2="12" y2="21"></line>
        </svg>
        <h3 style="margin: 0; color: #202124;">Sensitive C & Breast Pump Shields Brochure</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Description
    st.markdown('<div style="color: #666; margin-bottom: 20px;">PLV Mar Plaquette Sensitive C & Téterelles</div>', unsafe_allow_html=True)
    
    # Affichage des 2 images de la plaquette
    plaquette_images = [
        "Medicofi/Société Mamivac France/Plaquette Sensitive C & Téterelles/Recto.png",
        "Medicofi/Société Mamivac France/Plaquette Sensitive C & Téterelles/Verso.png"
    ]
    
    # Afficher les images côte à côte avec leurs titres
    col1, col2 = st.columns(2)
    
    with col1:
        # Recto
        recto_url = get_image_url(plaquette_images[0])
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 10px;">
            <div style="color: #202124; font-weight: 600; font-size: 16px; margin-bottom: 10px;">Recto</div>
            <div style="display: flex; justify-content: center;">
                <img src="{recto_url}" style="width: 500px; max-width: 100%; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Verso
        verso_url = get_image_url(plaquette_images[1])
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 10px;">
            <div style="color: #202124; font-weight: 600; font-size: 16px; margin-bottom: 10px;">Verso</div>
            <div style="display: flex; justify-content: center;">
                <img src="{verso_url}" style="width: 500px; max-width: 100%; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
        </div>
        """, unsafe_allow_html=True)
    # Séparateur
    st.markdown("---")
    
    # Section PLV Mamivac avec icône
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <line x1="3" y1="9" x2="21" y2="9"></line>
            <line x1="9" y1="21" x2="9" y2="9"></line>
        </svg>
        <h3 style="margin: 0; color: #202124;">PLV Mamivac</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Description
    st.markdown('<div style="color: #666; margin-bottom: 20px;">Point de vente PLV Mamivac</div>', unsafe_allow_html=True)
    
    # Affichage de l'image PLV Mamivac
    plv_url = get_image_url("Medicofi/Société Mamivac France/PLV Mamivac/PLV Mamivac.png")
    st.markdown(f"""
    <div style="display: flex; justify-content: center; margin: 20px 0;">
        <img src="{plv_url}" style="width: 600px; max-width: 100%; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    </div>
    """, unsafe_allow_html=True)
    
    # Espacement avant le bouton Social Media
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    
    # Bouton Social Media
    if st.button("SOCIAL MEDIA", use_container_width=True):
        st.session_state.page = "mamivac_social_media"
        st.rerun()
    # Espace après la carte de profil
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
# Page des propositions PDF pour Mamivac
elif st.session_state.page == "mamivac_propositions":
    if st.button("←"):
        st.session_state.page = "medicofi2"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
            <polyline points="10 9 9 9 8 9"></polyline>
        </svg>
        <h3 style="margin: 0; color: #202124;">Propositions Coque Sensitive C</h3>
    </div>
    """, unsafe_allow_html=True)

    # URLs des PDFs
    pdf1_url = get_image_url("Medicofi/Société Mamivac France/Coque de l'appareil Sensitive C (Design Produit)/Propositions 1-PLANCHE Sensitive C.pdf")
    pdf2_url = get_image_url("Medicofi/Société Mamivac France/Coque de l'appareil Sensitive C (Design Produit)/Propositions 2-PLANCHE Sensitive C.pdf")
    
    # Encoder les URLs pour Google Viewer
    pdf1_encoded = urllib.parse.quote(pdf1_url, safe='')
    pdf2_encoded = urllib.parse.quote(pdf2_url, safe='')
    
    google_viewer_url1 = f"https://docs.google.com/viewer?url={pdf1_encoded}&embedded=true"
    google_viewer_url2 = f"https://docs.google.com/viewer?url={pdf2_encoded}&embedded=true"

    # Affichage du premier PDF
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin: 20px 0 10px 0;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Proposition 1</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<iframe width="100%" height="600" src="{google_viewer_url1}"></iframe>', unsafe_allow_html=True)
    
    # Boutons pour le PDF 1
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<a href="{pdf1_url}" download="Proposition_1_PLANCHE_Sensitive_C.pdf" style="text-decoration: none;">', unsafe_allow_html=True)
        if st.button("📥 Télécharger PDF 1", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<a href="{google_viewer_url1}" target="_blank" style="text-decoration: none;">', unsafe_allow_html=True)
        if st.button("🔗 Ouvrir PDF 1", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Affichage du deuxième PDF
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin: 20px 0 10px 0;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Proposition 2</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<iframe width="100%" height="600" src="{google_viewer_url2}"></iframe>', unsafe_allow_html=True)
    
    # Boutons pour le PDF 2
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<a href="{pdf2_url}" download="Proposition_2_PLANCHE_Sensitive_C.pdf" style="text-decoration: none;">', unsafe_allow_html=True)
        if st.button("📥 Télécharger PDF 2", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<a href="{google_viewer_url2}" target="_blank" style="text-decoration: none;">', unsafe_allow_html=True)
        if st.button("🔗 Ouvrir PDF 2", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)

elif st.session_state.page == "mamivac_social_media":
    if st.button("←"):
        st.session_state.page = "medicofi2"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
        </svg>
        <h3 style="margin: 0; color: #202124;">Social Media Content</h3>
    </div>
    """, unsafe_allow_html=True)

    # Description
    st.markdown('<div style="color: #666; margin-bottom: 30px;">Social media content for Mamivac France</div>', unsafe_allow_html=True)

    # Créer 3 colonnes pour les boutons
    col1, col2, col3 = st.columns(3)

    with col1:
        # Bouton Post Carrousel avec icône
        st.markdown("""
        <div style="text-align: center; margin-bottom: 10px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 10px;">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <circle cx="8.5" cy="8.5" r="1.5"></circle>
                <polyline points="21 15 16 10 5 21"></polyline>
            </svg>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Post Carrousel", use_container_width=True):
            st.session_state.page = "mamivac_post_carrousel"
            st.rerun()

    with col2:
        # Bouton Post Statique avec icône
        st.markdown("""
        <div style="text-align: center; margin-bottom: 10px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 10px;">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <circle cx="8.5" cy="8.5" r="1.5"></circle>
                <polyline points="21 15 16 10 5 21"></polyline>
                <line x1="17" y1="5" x2="17" y2="19"></line>
            </svg>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Post Statique", use_container_width=True):
            st.session_state.page = "mamivac_post_statique"
            st.rerun()

    with col3:
        # Bouton Story avec icône
        st.markdown("""
        <div style="text-align: center; margin-bottom: 10px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 10px;">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <circle cx="12" cy="12" r="3"></circle>
                <line x1="12" y1="5" x2="12" y2="5.01"></line>
                <line x1="12" y1="19" x2="12" y2="19.01"></line>
                <line x1="5" y1="12" x2="5.01" y2="12"></line>
                <line x1="19" y1="12" x2="19.01" y2="12"></line>
            </svg>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Story", use_container_width=True):
            st.session_state.page = "mamivac_story"
            st.rerun()
            # Page Post Carrousel
# Page Post Carrousel
# Page Post Carrousel
# Page Post Carrousel
elif st.session_state.page == "mamivac_post_carrousel":
    if st.button("←"):
        st.session_state.page = "mamivac_social_media"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <circle cx="8.5" cy="8.5" r="1.5"></circle>
            <polyline points="21 15 16 10 5 21"></polyline>
        </svg>
        <h3 style="margin: 0; color: #202124;">Post Carrousel</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="color: #666; margin-bottom: 30px;">Carousel posts for social media</div>', unsafe_allow_html=True)
    
    # Liste des 9 images avec les chemins corrigés
    # Selon votre structure: Post carrousel/1.png, 2.png, 3.png directement
    carrousel_images = [
        # Images dans Post carrousel/ directement
        "Medicofi/Société Mamivac France/Réseaux Sociaux/Post & story Facebook Instagram et LinkedIn/Post carrousel/1/1.png",
        "Medicofi/Société Mamivac France/Réseaux Sociaux/Post & story Facebook Instagram et LinkedIn/Post carrousel/1/2.png",
        "Medicofi/Société Mamivac France/Réseaux Sociaux/Post & story Facebook Instagram et LinkedIn/Post carrousel/1/3.png",
        
        # Pour afficher 9 images, je répète les mêmes 3 images 3 fois
        # Si vous avez plus d'images, ajustez les chemins
        "Medicofi/Société Mamivac France/Réseaux Sociaux/Post & story Facebook Instagram et LinkedIn/Post carrousel/2/1.png",
        "Medicofi/Société Mamivac France/Réseaux Sociaux/Post & story Facebook Instagram et LinkedIn/Post carrousel/2/2.png",
        "Medicofi/Société Mamivac France/Réseaux Sociaux/Post & story Facebook Instagram et LinkedIn/Post carrousel/2/3.png",
        
        "Medicofi/Société Mamivac France/Réseaux Sociaux/Post & story Facebook Instagram et LinkedIn/Post carrousel/3/1.png",
        "Medicofi/Société Mamivac France/Réseaux Sociaux/Post & story Facebook Instagram et LinkedIn/Post carrousel/3/2.png",
        "Medicofi/Société Mamivac France/Réseaux Sociaux/Post & story Facebook Instagram et LinkedIn/Post carrousel/3/3.png"
    ]
    
    # Titres pour chaque groupe de 3 images
    group_titles = ["Carrousel 1", "Carrousel 2", "Carrousel 3"]
    
    # Afficher les images en 3 groupes (3 lignes)
    for group_index in range(3):
        # Titre du groupe
        st.markdown(f"""
        <div style="margin: 30px 0 15px 0; padding-bottom: 10px; border-bottom: 2px solid #FBBDFA;">
            <h4 style="color: #202124; margin: 0;">{group_titles[group_index]}</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Créer 3 colonnes pour les 3 images du groupe
        col1, col2, col3 = st.columns(3)
        
        # Calculer l'index de départ pour ce groupe
        start_index = group_index * 3
        
        with col1:
            img_url = get_image_url(carrousel_images[start_index])
            # Test d'affichage simple d'abord
            try:
                st.image(img_url, use_container_width=True, caption=f"Slide 1")
            except Exception as e:
                st.error(f"Erreur chargement image 1: {e}")
                st.write(f"URL: {img_url}")
        
        with col2:
            img_url = get_image_url(carrousel_images[start_index + 1])
            try:
                st.image(img_url, use_container_width=True, caption=f"Slide 2")
            except Exception as e:
                st.error(f"Erreur chargement image 2: {e}")
                st.write(f"URL: {img_url}")
        
        with col3:
            img_url = get_image_url(carrousel_images[start_index + 2])
            try:
                st.image(img_url, use_container_width=True, caption=f"Slide 3")
            except Exception as e:
                st.error(f"Erreur chargement image 3: {e}")
                st.write(f"URL: {img_url}")
        
        # Espacement entre les groupes
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# Page Post Statique
elif st.session_state.page == "mamivac_post_statique":
    if st.button("←"):
        st.session_state.page = "mamivac_social_media"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <circle cx="8.5" cy="8.5" r="1.5"></circle>
            <polyline points="21 15 16 10 5 21"></polyline>
            <line x1="17" y1="5" x2="17" y2="19"></line>
        </svg>
        <h3 style="margin: 0; color: #202124;">Post Statique</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="color: #666; margin-bottom: 30px;">Static posts for social media</div>', unsafe_allow_html=True)
    
    # Liste des images pour les posts statiques avec leurs descriptions
    static_posts = [
        ("11-Mars-kitt-Teterelles-double-2.png", "11 Mars - Kit Téterelles Double"),
        ("15-Avril-Jeu-tirage-au-sort-Mamivac.png", "15 Avril - Jeu Tirage au Sort"),
        ("15-Juillet-Surproduction-de-lait-maternel.png", "15 Juillet - Surproduction de Lait"),
        ("17-Juin-Comment-laver-vos-teterelles-efficacement-.png", "17 Juin - Nettoyage Téterelles"),
        ("19-Juin-Combien-de-temps-une-maman-peut-produire-du-lait.png", "19 Juin - Production de Lait"),
        ("22-Juillet-Citation.png", "22 Juillet - Citation"),
        ("24-Juillet-apparition-des-dents-de-bebe.png", "24 Juillet - Dents de Bébé"),
        ("26-Juin-donner-de-l'eau-à-un-bébé-allaité.png", "26 Juin - Eau pour Bébé Allaité"),
        ("8-Juillet-rechauffer-le-lait-maternel-conserve.png", "8 Juillet - Réchauffer Lait Maternel"),
        ("kitt-Teterellesss-double.png", "Kit Téterelles Double")
    ]
    
    # Afficher les images en 3 colonnes
    num_columns = 3
    num_images = len(static_posts)
    
    for i in range(0, num_images, num_columns):
        # Créer les colonnes pour cette ligne
        cols = st.columns(num_columns)
        
        # Afficher jusqu'à 3 images par ligne
        for col_idx in range(num_columns):
            img_idx = i + col_idx
            
            if img_idx < num_images:
                file_name, description = static_posts[img_idx]
                
                # Chemin complet de l'image
                image_path = f"Medicofi/Société Mamivac France/Réseaux Sociaux/Post & story Facebook Instagram et LinkedIn/Post statique/{file_name}"
                
                with cols[col_idx]:
                    # Afficher l'image avec sa description
                    try:
                        img_url = get_image_url(image_path)
                        
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 25px;">
                            <div style="display: flex; justify-content: center; margin-bottom: 8px;">
                                <img src="{img_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                            </div>
                            <div style="color: #202124; font-size: 14px; font-weight: 500; margin-bottom: 5px;">
                                {description}
                            </div>
                            <div style="color: #888; font-size: 12px;">
                                {file_name}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    except Exception as e:
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 25px;">
                            <div style="display: flex; justify-content: center; align-items: center; height: 200px; background: #f9f9f9; border-radius: 10px; margin-bottom: 8px; border: 2px dashed #ddd;">
                                <div style="color: #888;">Image non disponible</div>
                            </div>
                            <div style="color: #202124; font-size: 14px; font-weight: 500; margin-bottom: 5px;">
                                {description}
                            </div>
                            <div style="color: #888; font-size: 12px;">
                                {file_name}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

# Page Story
elif st.session_state.page == "mamivac_story":
    if st.button("←"):
        st.session_state.page = "mamivac_social_media"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <circle cx="12" cy="12" r="3"></circle>
            <line x1="12" y1="5" x2="12" y2="5.01"></line>
            <line x1="12" y1="19" x2="12" y2="19.01"></line>
            <line x1="5" y1="12" x2="5.01" y2="12"></line>
            <line x1="19" y1="12" x2="19.01" y2="12"></line>
        </svg>
        <h3 style="margin: 0; color: #202124;">Story</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="color: #666; margin-bottom: 30px;">Stories for social media</div>', unsafe_allow_html=True)
    
    # Liste des images pour les stories avec leurs descriptions
    story_posts = [
        ("12-Juin-reussir-la-promenade-avec-bebe-Story-01.png", "12 Juin - Réussir la promenade avec bébé"),
        ("24-Juin-Citation-de-Victor-Hugo-Story-01.png", "24 Juin - Citation de Victor Hugo"),
        ("3-Juillet-la-duree-ideale-de-la-sieste-Story-01.png", "3 Juillet - Durée idéale de la sieste"),
        ("Mamivac-Proteges-mamelons-CONE-S-M-L.png", "Mamivac - Protège-mamelons Cône S/M/L"),
        ("sorty-conserv.png", "Conservation du lait maternel")
    ]
    
    # Afficher les images en 2 colonnes
    num_columns = 2
    num_images = len(story_posts)
    
    for i in range(0, num_images, num_columns):
        # Créer les colonnes pour cette ligne
        cols = st.columns(num_columns)
        
        # Afficher jusqu'à 2 images par ligne
        for col_idx in range(num_columns):
            img_idx = i + col_idx
            
            if img_idx < num_images:
                file_name, description = story_posts[img_idx]
                
                # Chemin complet de l'image
                image_path = f"Medicofi/Société Mamivac France/Réseaux Sociaux/Post & story Facebook Instagram et LinkedIn/Story/{file_name}"
                
                with cols[col_idx]:
                    # Afficher l'image avec sa description
                    try:
                        img_url = get_image_url(image_path)
                        
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 30px;">
                            <div style="display: flex; justify-content: center; margin-bottom: 10px;">
                                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.15);">
                            </div>
                            <div style="color: #202124; font-size: 15px; font-weight: 500; margin-bottom: 8px; padding: 0 10px;">
                                {description}
                            </div>
                            <div style="color: #888; font-size: 13px; padding: 0 10px;">
                                {file_name}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    except Exception as e:
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 30px;">
                            <div style="display: flex; justify-content: center; align-items: center; height: 250px; background: linear-gradient(135deg, #f5f7fa 0%, #f9f9f9 100%); border-radius: 15px; margin-bottom: 10px; border: 2px dashed #FBBDFA;">
                                <div style="color: #888; font-size: 16px;">Story non disponible</div>
                            </div>
                            <div style="color: #202124; font-size: 15px; font-weight: 500; margin-bottom: 8px; padding: 0 10px;">
                                {description}
                            </div>
                            <div style="color: #888; font-size: 13px; padding: 0 10px;">
                                {file_name}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
        
        # Ajouter un séparateur entre les lignes (sauf après la dernière)
        if i + num_columns < num_images:
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
  # Page MC Consulting Company (Tunisia)
elif st.session_state.page == "medicofi3":
    if st.button("←"):
        st.session_state.page = "medicofi"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
        </svg>
        <h3 style="margin: 0; color: #202124;">MC Consulting Company</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="color: #666; margin-bottom: 30px;">Carte de Voeux - Greeting Cards</div>', unsafe_allow_html=True)
    
    # Liste des images pour MC Consulting
    mc_consulting_images = [
        ("Carte de voeux 2024.png", "Carte de Voeux 2024"),
        ("Carte de voeux 2025.png", "Carte de Voeux 2025")
    ]
    
    # Afficher les 2 images en 2 colonnes
    col1, col2 = st.columns(2)
    
    with col1:
        file_name, description = mc_consulting_images[0]
        image_path = f"Medicofi/Société MC Consulting (Tunisie)/Carte de Voeux/{file_name}"
        
        try:
            img_url = get_image_url(image_path)
            
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 30px;">
                <div style="display: flex; justify-content: center; margin-bottom: 15px;">
                    <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 6px 20px rgba(0,0,0,0.15);">
                </div>
                <div style="color: #202124; font-size: 18px; font-weight: 600; margin-bottom: 8px;">
                    {description}
                </div>
                <div style="color: #888; font-size: 14px;">
                    New Year Greeting Card
                </div>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 30px;">
                <div style="display: flex; justify-content: center; align-items: center; height: 300px; background: linear-gradient(135deg, #f5f7fa 0%, #f9f9f9 100%); border-radius: 10px; margin-bottom: 15px; border: 2px dashed #FBBDFA;">
                    <div style="color: #888; font-size: 16px;">Image non disponible</div>
                </div>
                <div style="color: #202124; font-size: 18px; font-weight: 600; margin-bottom: 8px;">
                    {description}
                </div>
                <div style="color: #888; font-size: 14px;">
                    New Year Greeting Card
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        file_name, description = mc_consulting_images[1]
        image_path = f"Medicofi/Société MC Consulting (Tunisie)/Carte de Voeux/{file_name}"
        
        try:
            img_url = get_image_url(image_path)
            
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 30px;">
                <div style="display: flex; justify-content: center; margin-bottom: 15px;">
                    <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 6px 20px rgba(0,0,0,0.15);">
                </div>
                <div style="color: #202124; font-size: 18px; font-weight: 600; margin-bottom: 8px;">
                    {description}
                </div>
                <div style="color: #888; font-size: 14px;">
                    New Year Greeting Card
                </div>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 30px;">
                <div style="display: flex; justify-content: center; align-items: center; height: 300px; background: linear-gradient(135deg, #f5f7fa 0%, #f9f9f9 100%); border-radius: 10px; margin-bottom: 15px; border: 2px dashed #FBBDFA;">
                    <div style="color: #888; font-size: 16px;">Image non disponible</div>
                </div>
                <div style="color: #202124; font-size: 18px; font-weight: 600; margin-bottom: 8px;">
                    {description}
                </div>
                <div style="color: #888; font-size: 14px;">
                    New Year Greeting Card
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Description supplémentaire
    st.markdown("""
    <div style="background: #f9f9f9; padding: 20px; border-radius: 10px; margin-top: 30px; border-left: 4px solid #FBBDFA;">
        <h4 style="color: #202124; margin: 0 0 10px 0;">About MC Consulting</h4>
        <div style="color: #666; font-size: 14px; line-height: 1.6;">
            Design of greeting cards for MC Consulting Company based in Tunisia. 
            These New Year cards were created for corporate communications and client relations.
        </div>
    </div>
    """, unsafe_allow_html=True)          
# Page MCM Outsourcing Company (Madagascar)
elif st.session_state.page == "medicofi4":
    if st.button("←"):
        st.session_state.page = "medicofi"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
        </svg>
        <h3 style="margin: 0; color: #202124;">MCM Outsourcing Company</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="color: #666; margin-bottom: 30px;">Emailing Campaign</div>', unsafe_allow_html=True)
    
    # Chemin de l'image unique
    image_path = "Medicofi/Société MCM Externalisation (à Madagascar)/Emailing/Emailing MCM Externalisation.png"
    
    try:
        img_url = get_image_url(image_path)
        
        # Afficher l'image unique au centre
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 30px 0 40px 0;">
            <div style="text-align: center; max-width: 800px; width: 100%;">
                <img src="{img_url}" style="width: 100%; max-width: 600px; border-radius: 12px; box-shadow: 0 8px 25px rgba(0,0,0,0.2);">
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Description de l'image
        st.markdown("""
        <div style="text-align: center; margin-bottom: 40px;">
            <div style="color: #202124; font-size: 20px; font-weight: 600; margin-bottom: 10px;">
                Emailing MCM Externalisation
            </div>
            <div style="color: #666; font-size: 16px; max-width: 600px; margin: 0 auto;">
                Email campaign design for MCM Outsourcing Company based in Madagascar
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        # Placeholder si l'image n'est pas disponible
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 30px 0 40px 0;">
            <div style="text-align: center; max-width: 800px; width: 100%;">
                <div style="display: flex; justify-content: center; align-items: center; height: 400px; background: linear-gradient(135deg, #f5f7fa 0%, #f9f9f9 100%); border-radius: 12px; margin-bottom: 20px; border: 3px dashed #FBBDFA;">
                    <div style="color: #888; font-size: 18px;">Emailing MCM Externalisation image not available</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-bottom: 40px;">
            <div style="color: #202124; font-size: 20px; font-weight: 600; margin-bottom: 10px;">
                Emailing MCM Externalisation
            </div>
            <div style="color: #666; font-size: 16px; max-width: 600px; margin: 0 auto;">
                Email campaign design for MCM Outsourcing Company based in Madagascar
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Section d'information supplémentaire
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(251, 189, 250, 0.1) 0%, rgba(140, 210, 255, 0.1) 100%); 
                padding: 25px; border-radius: 12px; margin-top: 20px; border: 1px solid rgba(251, 189, 250, 0.3);">
        <div style="display: flex; align-items: flex-start; gap: 15px;">
            <div style="background: white; padding: 12px; border-radius: 10px; display: flex; align-items: center; justify-content: center; border: 2px solid #FBBDFA;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                    <polyline points="22,6 12,13 2,6"></polyline>
                </svg>
            </div>
            <div style="flex: 1;">
                <h4 style="color: #202124; margin: 0 0 10px 0;">Project Details</h4>
                <div style="color: #666; font-size: 14px; line-height: 1.6;">
                    <p><strong>Client:</strong> MCM Externalisation (Madagascar)</p>
                    <p><strong>Service:</strong> Email marketing campaign design</p>
                    <p><strong>Objective:</strong> Corporate communication and client engagement</p>
                    <p><strong>Tools:</strong> Photoshop, Illustrator</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
# Page Respi Express Company (France)
elif st.session_state.page == "medicofi5":
    if st.button("←"):
        st.session_state.page = "medicofi"
        st.rerun()


    # ========== SECTION 1: Carte Zone Partenaire ==========
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
            <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <h4 style="margin: 0; color: #202124;">Partner Zone Card</h4>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        carte_url = get_image_url("Medicofi/Société Respi Express (en France)/Carte Zone Partenaire/Code-postal-91-Respi.png")
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="{carte_url}" style="width: 100%; max-width: 600px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin: 20px 0;">
            <div style="color: #888;">Carte Zone Partenaire image not available</div>
        </div>
        """, unsafe_allow_html=True)
    
    # ========== SECTION 2: Création illustrations et affiche ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
            <polyline points="2 17 12 22 22 17"></polyline>
            <polyline points="2 12 12 17 22 12"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Illustrations and poster design</h4>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        affiche_url = get_image_url("Medicofi/Société Respi Express (en France)/Création illustrations et affiche/Comprendre l’apnée obstructive du sommeil.png")
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="{affiche_url}" style="width: 100%; max-width: 600px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin: 20px 0;">
            <div style="color: #888;">Illustration image not available</div>
        </div>
        """, unsafe_allow_html=True)
    
    # ========== SECTION 3: Dépliants 1 pli 2 volets ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="3" width="20" height="18" rx="2" ry="2"></rect>
            <line x1="9" y1="21" x2="15" y2="21"></line>
            <line x1="12" y1="17" x2="12" y2="21"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">Single-fold - two-panel brochures</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            recto_url = get_image_url("Medicofi/Société Respi Express (en France)/Dépliants 1 pli 2 volets/Recto.png")
            st.markdown(f"""
            <div style="text-align: center;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Double</div>
                <img src="{recto_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">sided</div>
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">Image not available</div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            verso_url = get_image_url("Medicofi/Société Respi Express (en France)/Dépliants 1 pli 2 volets/Verso.png")
            st.markdown(f"""
            <div style="text-align: center;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">sided</div>
                <img src="{verso_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Verso</div>
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">Image not available</div>
            </div>
            """, unsafe_allow_html=True)
    
    # ========== SECTION 4: Emailing et Newsletters ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
            <polyline points="22,6 12,13 2,6"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Email Marketing</h4>
    </div>
    """, unsafe_allow_html=True)
    
    emailing_images = [
        "Medicofi/Société Respi Express (en France)/Emailing et Newsletters/Emailing 1.png",
        "Medicofi/Société Respi Express (en France)/Emailing et Newsletters/Emailing 2.png",
        "Medicofi/Société Respi Express (en France)/Emailing et Newsletters/Emailing 3.png",
        "Medicofi/Société Respi Express (en France)/Emailing et Newsletters/Emailing 4.png",
        "Medicofi/Société Respi Express (en France)/Emailing et Newsletters/Emailing 5.png"
    ]
    
    # Afficher les 5 images (2 lignes: 3 + 2)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        try:
            email1_url = get_image_url(emailing_images[0])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="{email1_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown('<div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin-bottom: 20px;">Email 1</div>', unsafe_allow_html=True)
    
    with col2:
        try:
            email2_url = get_image_url(emailing_images[1])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="{email2_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown('<div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin-bottom: 20px;">Email 2</div>', unsafe_allow_html=True)
    
    with col3:
        try:
            email3_url = get_image_url(emailing_images[2])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="{email3_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown('<div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin-bottom: 20px;">Email 3</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            email4_url = get_image_url(emailing_images[3])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="{email4_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown('<div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin-bottom: 20px;">Email 4</div>', unsafe_allow_html=True)
    
    with col2:
        try:
            email5_url = get_image_url(emailing_images[4])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="{email5_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown('<div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin-bottom: 20px;">Email 5</div>', unsafe_allow_html=True)
    
   # ========== SECTION 5: Kakémono ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <line x1="3" y1="9" x2="21" y2="9"></line>
            <line x1="9" y1="21" x2="9" y2="9"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">roll banner</h4>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        # CORRECTION : Société Tire Lait Express (en France) au lieu de Respi Express
        # CORRECTION : Pas de sous-dossier "Kakémono", le fichier est directement dans la société
        kakemono_url = get_image_url("Medicofi/Société Respi Express (en France)/Kakémono/Kakémono Respi express.png")
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="{kakemono_url}" style="width: 100%; max-width: 600px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        # Ajouter un message d'erreur pour déboguer
        st.error(f"Erreur de chargement du Kakémono: {str(e)}")
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin: 20px 0;">
            <div style="color: #888;">Kakémono image not available</div>
        </div>
        """, unsafe_allow_html=True)
    
    # ========== BOUTON: Livret d'accueil ==========
    st.markdown("---")
    if st.button("Welcome guide", use_container_width=True):
        st.session_state.page = "respi_livret"
        st.rerun()
    
    # ========== SECTION 6: Quick start ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 16 14"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Quick start</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            quick_recto_url = get_image_url("Medicofi/Société Respi Express (en France)/Quick start/Recto.png")
            st.markdown(f"""
            <div style="text-align: center;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Double</div>
                <img src="{quick_recto_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Recto</div>
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">Image not available</div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            quick_verso_url = get_image_url("Medicofi/Société Respi Express (en France)/Quick start/Verso.png")
            st.markdown(f"""
            <div style="text-align: center;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">sided</div>
                <img src="{quick_verso_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Verso</div>
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">Image not available</div>
            </div>
            """, unsafe_allow_html=True)
    
    # ========== BOUTON: Réseaux Sociaux ==========
    st.markdown("---")
    if st.button("Social Media", use_container_width=True):
        st.session_state.page = "respi_reseaux_sociaux"
        st.rerun()
   # ========== SECTION: Stand Parapluie ==========
        st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M23 12a11.05 11.05 0 0 0-22 0zm-5 7a3 3 0 0 1-6 0v-7"></path>
        </svg>
        <h4 style="margin: 0; color: #202124;">Pop-up stand</h4>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        # Afficher seulement l'image principale
        try:
            img_url = get_image_url("Medicofi/Société Respi Express (en France)/Stand Parapluie/Stand Parapluie Respi-express.png")
            st.markdown(f"""
            <div style="text-align: center; margin: 20px 0 40px 0;">
                <img src="{img_url}" style="width: 100%; max-width: 800px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);">
                <div style="color: #202124; font-weight: 600; margin-top: 15px; font-size: 16px;">
                    Stand Parapluie - Vue principale
                </div>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown("""
            <div style="text-align: center; margin: 20px 0 40px 0;">
                <div style="padding: 60px; background: #f9f9f9; border-radius: 10px; max-width: 800px; margin: 0 auto;">
                    <div style="color: #888; font-size: 16px;">Stand Parapluie image not available</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
                
    except Exception as e:
        st.error(f"Erreur de chargement du Stand Parapluie: {str(e)}")
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin: 20px 0;">
            <div style="color: #888;">Stand Parapluie image not available</div>
        </div>
        """, unsafe_allow_html=True)
        
# Page Livret d'accueil Respi Express (PDF Viewer)
elif st.session_state.page == "respi_livret":
    if st.button("←"):
        st.session_state.page = "medicofi5"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
            <polyline points="10 9 9 9 8 9"></polyline>
        </svg>
        <h3 style="margin: 0; color: #202124;">Livret d'accueil Respi Express</h3>
    </div>
    """, unsafe_allow_html=True)

    # URL du PDF
    pdf_url = get_image_url("Medicofi/Société Respi Express (en France)/Livret d'accueil/Livret d'accueil resp express.pdf")
    pdf_encoded = urllib.parse.quote(pdf_url, safe='')
    google_viewer_url = f"https://docs.google.com/viewer?url={pdf_encoded}&embedded=true"

    # PDF Viewer
    st.markdown(f'<iframe width="100%" height="800" src="{google_viewer_url}"></iframe>', unsafe_allow_html=True)

    # Boutons d'action
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<a href="{pdf_url}" download="Livret_accueil_Respi_Express.pdf" style="text-decoration: none;">', unsafe_allow_html=True)
        if st.button("📥 Télécharger le PDF", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<a href="{google_viewer_url}" target="_blank" style="text-decoration: none;">', unsafe_allow_html=True)
        if st.button("Ouvrir dans Google Viewer", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)

# Page Réseaux Sociaux Respi Express
elif st.session_state.page == "respi_reseaux_sociaux":
    if st.button("←"):
        st.session_state.page = "medicofi5"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
        </svg>
        <h3 style="margin: 0; color: #202124;">Social Media Respi Express</h3>
    </div>
    """, unsafe_allow_html=True)

    # ========== SECTION: Bannière ==========
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <line x1="3" y1="9" x2="21" y2="9"></line>
            <line x1="9" y1="21" x2="9" y2="9"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">Web banner</h4>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        banniere_url = get_image_url("Medicofi/Société Respi Express (en France)/Réseaux Sociaux/Bannière/Bannière-respi.png")
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="{banniere_url}" style="width: 100%; max-width: 800px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin: 20px 0;">
            <div style="color: #888;">Bannière image not available</div>
        </div>
        """, unsafe_allow_html=True)
    
    # ========== BOUTON: Post carrousel ==========
    st.markdown("---")
    if st.button("Carousel Post", use_container_width=True):
        st.session_state.page = "respi_post_carrousel"
        st.rerun()
    
    # ========== SECTION: Post statique ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <circle cx="8.5" cy="8.5" r="1.5"></circle>
            <polyline points="21 15 16 10 5 21"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Single Post</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Liste des 12 images de posts statiques
    static_images = []
    for i in range(1, 13):
        static_images.append(f"Medicofi/Société Respi Express (en France)/Réseaux Sociaux/Post statique/{i}.png")
    
    # Afficher les images en 3 colonnes (4 lignes de 3)
    num_columns = 3
    num_images = len(static_images)
    
    for i in range(0, num_images, num_columns):
        cols = st.columns(num_columns)
        
        for col_idx in range(num_columns):
            img_idx = i + col_idx
            
            if img_idx < num_images:
                with cols[col_idx]:
                    try:
                        img_url = get_image_url(static_images[img_idx])
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 20px;">
                            <img src="{img_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                            <div style="color: #666; font-size: 14px; margin-top: 8px;">Post {img_idx + 1}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    except:
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 20px;">
                            <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">
                                <div style="color: #888;">Post {img_idx + 1}</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
   
    
# Page Post Carrousel Respi Express
elif st.session_state.page == "respi_post_carrousel":
    if st.button("←"):
        st.session_state.page = "respi_reseaux_sociaux"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <circle cx="8.5" cy="8.5" r="1.5"></circle>
            <polyline points="21 15 16 10 5 21"></polyline>
        </svg>
        <h3 style="margin: 0; color: #202124;">Post Carrousel Respi Express</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="color: #666; margin-bottom: 30px;">Carousel posts for Respi Express social media</div>', unsafe_allow_html=True)
    
    # Définir les groupes d'images
    groupes = {
        "groupe_1": ["1.png", "2.png", "3.png", "4.png", "5.png"],
        "groupe_2": ["1.png", "2.png", "3.png", "4.png"],
        "groupe_3": ["01.png", "02.png", "03.png"],
        "groupe_4": ["1.png", "2.png", "3.png", "4.png"],
        "groupe_5": ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"],
        "groupe_6": ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"],
        "groupe_7": ["1.png", "2.png", "3.png", "4.png", "5.png"]
    }
    
    # Afficher chaque groupe avec son titre stylisé
    for i, (groupe_key, images) in enumerate(groupes.items(), 1):
        # ========== Titre du groupe ==========
        st.markdown("---")
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <circle cx="8.5" cy="8.5" r="1.5"></circle>
                <polyline points="21 15 16 10 5 21"></polyline>
            </svg>
            <h4 style="margin: 0; color: #202124;">Groupe {i}</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Créer des colonnes pour afficher les images
        cols = st.columns(min(3, len(images)))
        
        for idx, image_name in enumerate(images):
            col_idx = idx % 3
            with cols[col_idx]:
                # Ici, vous devrez charger les images depuis leur chemin réel
                # Exemple: image_path = f"path/to/images/{groupe_key}/{image_name}"
                # image = Image.open(image_path)
                # st.image(image, caption=image_name, use_container_width=True)
                
                # Pour l'instant, afficher un placeholder
                st.markdown(f"""
                <div style="text-align: center; padding: 20px; background: #f5f5f5; border-radius: 8px; margin: 10px 0;">
                    <div style="color: #666; font-size: 14px; margin-bottom: 10px;">{image_name}</div>
                    <div style="color: #999; font-size: 12px;">Image placeholder</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Ajouter un espace entre les groupes
        st.markdown("<br>", unsafe_allow_html=True)

# Page Sanibiose Company (France)
elif st.session_state.page == "medicofi6":
    if st.button("←"):
        st.session_state.page = "medicofi"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
        </svg>
        <h3 style="margin: 0; color: #202124;">Sanibiose Company</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # ========== SECTION 2: Emailing et Newsletters ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
            <polyline points="22,6 12,13 2,6"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Emailing et Newsletters</h4>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        emailing_url = get_image_url("Medicofi/Société Sanibiose (en France)/Emailing et Newsletters/Emailing CBD.png")
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="{emailing_url}" style="width: 100%; max-width: 600px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        <div style="text-align: center; color: #666; margin-bottom: 20px;">
            Emailing CBD - Sanibiose
        </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin: 20px 0;">
            <div style="color: #888;">Emailing CBD image not available</div>
        </div>
        """, unsafe_allow_html=True)
    
    # ========== SECTION 3: étiquettes pour les Produits Sanibiose ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect>
            <line x1="7" y1="2" x2="7" y2="22"></line>
            <line x1="17" y1="2" x2="17" y2="22"></line>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <line x1="2" y1="7" x2="7" y2="7"></line>
            <line x1="2" y1="17" x2="7" y2="17"></line>
            <line x1="17" y1="17" x2="22" y2="17"></line>
            <line x1="17" y1="7" x2="22" y2="7"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">étiquettes pour les Produits Sanibiose</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Liste des 21 images d'étiquettes (de 1 à 21)
    etiquettes_images = []
    for i in range(1, 22):
        etiquettes_images.append(f"Medicofi/Société Sanibiose (en France)/étiquettes pour les Produits Sanibiose/{i}.png")
    
    # Afficher les 21 images en 3 colonnes (7 lignes de 3)
    num_columns = 3
    num_images = len(etiquettes_images)
    
    for i in range(0, num_images, num_columns):
        cols = st.columns(num_columns)
        
        for col_idx in range(num_columns):
            img_idx = i + col_idx
            
            if img_idx < num_images:
                with cols[col_idx]:
                    try:
                        img_url = get_image_url(etiquettes_images[img_idx])
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 20px;">
                            <img src="{img_url}" style="width: 100%; max-width: 300px; border-radius: 8px; box-shadow: 0 3px 10px rgba(0,0,0,0.1);">
                            <div style="color: #666; font-size: 13px; margin-top: 5px;">Étiquette {img_idx + 1}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    except:
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 20px;">
                            <div style="padding: 30px; background: #f9f9f9; border-radius: 8px;">
                                <div style="color: #888; font-size: 13px;">Étiquette {img_idx + 1}</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
    
    # ========== SECTION 4: Réseaux Sociaux ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
        </svg>
        <h4 style="margin: 0; color: #202124;">Réseaux Sociaux</h4>
    </div>
    <div style="color: #666; margin-bottom: 20px; font-size: 14px;">
        Post statique pour Facebook, Instagram et LinkedIn
    </div>
    """, unsafe_allow_html=True)
    
    # Liste des 20 images de réseaux sociaux (de 1 à 20)
    reseaux_images = []
    for i in range(1, 21):
        reseaux_images.append(f"Medicofi/Société Sanibiose (en France)/Réseaux Sociaux/Post statique pour Facebook Instagram et LinkedIn/{i}.png")
    
    # Afficher les 20 images en 3 colonnes (7 lignes: 6 lignes de 3 + 1 ligne de 2)
    num_columns = 3
    num_images = len(reseaux_images)
    
    for i in range(0, num_images, num_columns):
        cols = st.columns(num_columns)
        
        for col_idx in range(num_columns):
            img_idx = i + col_idx
            
            if img_idx < num_images:
                with cols[col_idx]:
                    try:
                        img_url = get_image_url(reseaux_images[img_idx])
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 20px;">
                            <img src="{img_url}" style="width: 100%; max-width: 300px; border-radius: 8px; box-shadow: 0 3px 10px rgba(0,0,0,0.1);">
                            <div style="color: #666; font-size: 13px; margin-top: 5px;">Post {img_idx + 1}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    except:
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 20px;">
                            <div style="padding: 30px; background: #f9f9f9; border-radius: 8px;">
                                <div style="color: #888; font-size: 13px;">Post {img_idx + 1}</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
    
    # ========== SECTION 5: Stand Parapluie ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M23 12a11.05 11.05 0 0 0-22 0zm-5 7a3 3 0 0 1-6 0v-7"></path>
        </svg>
        <h4 style="margin: 0; color: #202124;">Stand Parapluie</h4>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        stand_url = get_image_url("Medicofi/Société Sanibiose (en France)/Stand Parapluie/Stand parapluie Sanibiose.png")
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0 40px 0;">
            <img src="{stand_url}" style="width: 100%; max-width: 700px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);">
        </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style="text-align: center; padding: 60px; background: #f9f9f9; border-radius: 10px; margin: 20px 0 40px 0;">
            <div style="color: #888;">Stand Parapluie image not available</div>
        </div>
        """, unsafe_allow_html=True)
        
elif st.session_state.page == "medicofi7":
    if st.button("←"):
        st.session_state.page = "medicofi"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
        </svg>
        <h3 style="margin: 0; color: #202124;">Seinbiose Company (France)</h3>
    </div>
    """, unsafe_allow_html=True)

    # ========== SECTION 1: Emailing ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
            <polyline points="22,6 12,13 2,6"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Emailing</h4>
    </div>
    """, unsafe_allow_html=True)

    # Trois images en trois colonnes
    emailing_images = [
        "Medicofi/Société Seinbiose (en France)/Emailing/Emailing Liberty presentation.png",
        "Medicofi/Société Seinbiose (en France)/Emailing/Emailing Promo de rentrée.png",
        "Medicofi/Société Seinbiose (en France)/Emailing/les masques et les gels antiseptiques.png"
    ]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        try:
            email1_url = get_image_url(emailing_images[0])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="{email1_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <div style="color: #666; font-size: 14px; margin-top: 8px;">Emailing Liberty presentation</div>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">Emailing Liberty presentation</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            email2_url = get_image_url(emailing_images[1])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="{email2_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <div style="color: #666; font-size: 14px; margin-top: 8px;">Emailing Promo de rentrée</div>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">Emailing Promo de rentrée</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        try:
            email3_url = get_image_url(emailing_images[2])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="{email3_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <div style="color: #666; font-size: 14px; margin-top: 8px;">Masques et gels antiseptiques</div>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">Masques et gels antiseptiques</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ========== SECTION 2: Fiche technique ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Fiche technique</h4>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        fiche_url = get_image_url("Medicofi/Société Seinbiose (en France)/Fiche technique/FT-masque enfant.png")
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="{fiche_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin: 20px 0;">
            <div style="color: #888;">Fiche technique image not available</div>
        </div>
        """, unsafe_allow_html=True)

    # ========== SECTION 3: Flyer ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="3" width="20" height="18" rx="2" ry="2"></rect>
            <line x1="9" y1="21" x2="15" y2="21"></line>
            <line x1="12" y1="17" x2="12" y2="21"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">Flyer</h4>
    </div>
    """, unsafe_allow_html=True)

    # Deux images en deux colonnes
    flyer_images = [
        "Medicofi/Société Seinbiose (en France)/Flyer/Recto.png",
        "Medicofi/Société Seinbiose (en France)/Flyer/Verso.png"
    ]
    
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            recto_url = get_image_url(flyer_images[0])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Recto</div>
                <img src="{recto_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Recto</div>
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">Image not available</div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            verso_url = get_image_url(flyer_images[1])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Verso</div>
                <img src="{verso_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Verso</div>
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">Image not available</div>
            </div>
            """, unsafe_allow_html=True)

    # ========== SECTION 4: Packaging Liberty ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
            <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
            <line x1="12" y1="22.08" x2="12" y2="12"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">Packaging Liberty</h4>
    </div>
    """, unsafe_allow_html=True)

    # PDF Viewer
    try:
        pdf_url = get_image_url("Medicofi/Société Seinbiose (en France)/Packaging Liberty/Packaging TL LIBERTY Seinbiose.pdf")
        pdf_encoded = urllib.parse.quote(pdf_url, safe='')
        google_viewer_url = f"https://docs.google.com/viewer?url={pdf_encoded}&embedded=true"
        
        st.markdown(f'<iframe width="100%" height="500" src="{google_viewer_url}"></iframe>', unsafe_allow_html=True)
        
        # Boutons d'action
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'<a href="{pdf_url}" download="Packaging_TL_LIBERTY_Seinbiose.pdf" style="text-decoration: none;">', unsafe_allow_html=True)
            if st.button("📥 Télécharger PDF", use_container_width=True):
                pass
            st.markdown('</a>', unsafe_allow_html=True)
        
        with col2:
            st.markdown(f'<a href="{google_viewer_url}" target="_blank" style="text-decoration: none;">', unsafe_allow_html=True)
            if st.button("🔗 Ouvrir PDF", use_container_width=True):
                pass
            st.markdown('</a>', unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style="text-align: center; padding: 60px; background: #f9f9f9; border-radius: 10px; margin: 20px 0;">
            <div style="color: #888;">Packaging PDF not available</div>
        </div>
        """, unsafe_allow_html=True)

    # ========== SECTION 5: Plaquette ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="3" width="20" height="18" rx="2" ry="2"></rect>
            <line x1="9" y1="21" x2="15" y2="21"></line>
            <line x1="12" y1="17" x2="12" y2="21"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">Plaquette</h4>
    </div>
    """, unsafe_allow_html=True)

    # Deux images en deux colonnes
    plaquette_images = [
        "Medicofi/Société Seinbiose (en France)/Plaquette/Recto.png",
        "Medicofi/Société Seinbiose (en France)/Plaquette/Verso.png"
    ]
    
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            plaquette_recto_url = get_image_url(plaquette_images[0])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Recto</div>
                <img src="{plaquette_recto_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Recto</div>
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">Image not available</div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            plaquette_verso_url = get_image_url(plaquette_images[1])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Verso</div>
                <img src="{plaquette_verso_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Verso</div>
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">Image not available</div>
            </div>
            """, unsafe_allow_html=True)

    # ========== SECTION 6: Quick Start ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 16 14"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Quick Start</h4>
    </div>
    """, unsafe_allow_html=True)

    # Deux images en deux colonnes
    quick_images = [
        "Medicofi/Société Seinbiose (en France)/Quick Start/Recto.png",
        "Medicofi/Société Seinbiose (en France)/Quick Start/Verso.png"
    ]
    
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            quick_recto_url = get_image_url(quick_images[0])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Recto</div>
                <img src="{quick_recto_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Recto</div>
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">Image not available</div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            quick_verso_url = get_image_url(quick_images[1])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Verso</div>
                <img src="{quick_verso_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-bottom: 10px;">Verso</div>
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">Image not available</div>
            </div>
            """, unsafe_allow_html=True)

    # ========== SECTION 7: Réglette ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">Réglette</h4>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        reglette_url = get_image_url("Medicofi/Société Seinbiose (en France)/Réglette/Réglette Seinbiose 2025.png")
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="{reglette_url}" style="width: 100%; max-width: 600px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: #f9f9f9; border-radius: 10px; margin: 20px 0;">
            <div style="color: #888;">Réglette image not available</div>
        </div>
        """, unsafe_allow_html=True)

    # ========== SECTION 8: Réseaux Sociaux ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
        </svg>
        <h4 style="margin: 0; color: #202124;">Réseaux Sociaux</h4>
    </div>
    """, unsafe_allow_html=True)

    # Bouton pour accéder à la page des réseaux sociaux
    if st.button("Post & story Facebook Instagram et LinkedIn", use_container_width=True):
        st.session_state.page = "seinbiose_reseaux_sociaux"
        st.rerun()

    # ========== SECTION 9: Stand Parapluie ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M23 12a11.05 11.05 0 0 0-22 0zm-5 7a3 3 0 0 1-6 0v-7"></path>
        </svg>
        <h4 style="margin: 0; color: #202124;">Stand Parapluie</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Liste des images
    stand_images = [
        "Medicofi/Société Seinbiose (en France)/Stand Parapluie/1.jpg",
        "Medicofi/Société Seinbiose (en France)/Stand Parapluie/2.jpg",
        "Medicofi/Société Seinbiose (en France)/Stand Parapluie/3.jpg"
    ]
    
    # Image 1 seule dans une colonne (grande)
    try:
        stand1_url = get_image_url(stand_images[0])
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="{stand1_url}" style="width: 100%; max-width: 800px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            <div style="color: #666; font-size: 14px; margin-top: 8px;">Image 1</div>
        </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 30px;">
            <div style="padding: 60px; background: #f9f9f9; border-radius: 10px;">
                <div style="color: #888; font-size: 16px;">Stand Parapluie 1</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Images 2 et 3 dans deux colonnes côte à côte (ligne suivante)
    col1, col2 = st.columns(2)
    
    # Image 2
    with col1:
        try:
            stand2_url = get_image_url(stand_images[1])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="{stand2_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <div style="color: #666; font-size: 14px; margin-top: 8px;">Image 2</div>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">Stand Parapluie 2</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Image 3
    with col2:
        try:
            stand3_url = get_image_url(stand_images[2])
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="{stand3_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <div style="color: #666; font-size: 14px; margin-top: 8px;">Image 3</div>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">Stand Parapluie 3</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
elif st.session_state.page == "medicofi8":
    if st.button("←"):
        st.session_state.page = "medicofi"
        st.rerun()

    # ========== SECTION 1: Affiche Pour les cabinet Sage-femme ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <line x1="3" y1="9" x2="21" y2="9"></line>
            <line x1="9" y1="21" x2="9" y2="9"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">Affiche Pour les cabinet Sage-femme</h4>
    </div>
    """, unsafe_allow_html=True)

    # Quatre images en deux colonnes (2x2)
    affiche_images = [
        ("Affiche les positions d’allaitements.png", "Breastfeeding Positions Poster"),
        ("affiche publicitaire.png", "Advertising Poster"),
        ("affiche sein artistique-Lactant.png", "Artistic Poster"),
        ("Affiche Taille de téterelles.png", "Nipple Size Poster")
    ]
    
    # Première ligne
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Affiche Pour les cabinet Sage-femme/{affiche_images[0][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 15px;">{affiche_images[0][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{affiche_images[0][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Affiche Pour les cabinet Sage-femme/{affiche_images[1][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 15px;">{affiche_images[1][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{affiche_images[1][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Deuxième ligne
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Affiche Pour les cabinet Sage-femme/{affiche_images[2][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 15px;">{affiche_images[2][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{affiche_images[2][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Affiche Pour les cabinet Sage-femme/{affiche_images[3][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 15px;">{affiche_images[3][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{affiche_images[3][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ========== SECTION 2: Boite thé Packaging ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
            <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
            <line x1="12" y1="22.08" x2="12" y2="12"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">Tea Box Packaging</h4>
    </div>
    """, unsafe_allow_html=True)

    # Quatre images en deux colonnes (2x2)
    packaging_images = [
        ("Boite thé Packaging création.png", "Tea Box Packaging Design"),
        ("Mockup boite thè 3.png", "Mockup 1 "),
        ("Mockup boite thè 1.png", "Mockup 2 "),
        ("Mockup boite thè 2.png", "Mockup 3 ")
    ]
    
    # Première ligne
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Boite thé Packaging/{packaging_images[0][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 15px;">{packaging_images[0][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{packaging_images[0][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Boite thé Packaging/{packaging_images[1][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 15px;">{packaging_images[1][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{packaging_images[1][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Deuxième ligne
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Boite thé Packaging/{packaging_images[2][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 15px;">{packaging_images[2][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{packaging_images[2][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Boite thé Packaging/{packaging_images[3][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 15px;">{packaging_images[3][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{packaging_images[3][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

       # ========== SECTION 3: Création d'un avatar pour un chatbot IA (Version 2) ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
            <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <h4 style="margin: 0; color: #202124;">Création d'un avatar pour un chatbot IA</h4>
    </div>
    """, unsafe_allow_html=True)

    # Trois images - 2 premières côte à côte, 3ème seule
    avatar_images = [
        ("Avatar Lea.png", "Avatar Design"),
        ("Image d'origine reçue.jpeg", "Original Image Received"),
        ("Planche de personnage de l'avatar.png", "Planche de personnage de l'avatar")
    ]
    
    # Première ligne : 2 premières images côte à côte (col1, col2)
    col1, col2 = st.columns(2)
    
    # Première image (Avatar Lea)
    with col1:
        try:
            # CORRECTION : Enlever "mes_documents/" et utiliser l'apostrophe courbe
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Création d’un avatar pour un chatbot IA/Avatar Lea.png"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 16px;">{avatar_images[0][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 60px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{avatar_images[0][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Deuxième image (Image d'origine reçue)
    with col2:
        try:
            # CORRECTION : Enlever "mes_documents/" et utiliser l'apostrophe courbe
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Création d’un avatar pour un chatbot IA/Image d’origine reçue.jpeg"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 16px;">{avatar_images[1][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 60px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{avatar_images[1][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Deuxième ligne : 3ème image seule sur toute la largeur (plus grande)
    st.markdown("""
    <div style="color: #202124; font-weight: 600; margin-top: 40px; margin-bottom: 15px; font-size: 18px; text-align: center;">
       Character Model Sheet
    </div>
    """, unsafe_allow_html=True)
    
    try:
        # CORRECTION : Enlever "mes_documents/" et utiliser l'apostrophe courbe
        img_path = f"Medicofi/Société Tire Lait Express (en France)/Création d’un avatar pour un chatbot IA/Planche de personnage de l’avatar.png"
        img_url = get_image_url(img_path)
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 40px;">
            <img src="{img_url}" style="width: 100%; max-width: 800px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);">
        </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 40px;">
            <div style="padding: 80px; background: #f9f9f9; border-radius: 10px; max-width: 800px; margin: 0 auto;">
                <div style="color: #888; font-size: 16px;">{avatar_images[2][1]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Phrase sous les images
    st.markdown("""
    <div style="text-align: center; margin: 20px 0 30px 0; padding: 15px; background: #f9f9f9; border-radius: 10px; border-left: 4px solid #FBBDFA;">
        <div style="color: #202124; font-size: 16px; font-weight: 500;">
            Designed with Photoshop and AI tools.
        </div>
    </div>
    """, unsafe_allow_html=True)
       # ========== SECTION 4: Dépliant ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="3" width="20" height="18" rx="2" ry="2"></rect>
            <line x1="9" y1="21" x2="15" y2="21"></line>
            <line x1="12" y1="17" x2="12" y2="21"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">Dépliant</h4>
    </div>
    """, unsafe_allow_html=True)

    # Deux images chacune dans sa propre colonne (pleine largeur)
    depliant_images = [
        ("Recto.png", "Double"),
        ("Verso.png", "sided")
    ]
    
    # Première image seule (pleine largeur)
    st.markdown("""
    <div style="color: #202124; font-weight: 600; margin-top: 20px; margin-bottom: 15px; font-size: 18px; text-align: center;">
        Double
    </div>
    """, unsafe_allow_html=True)
    
    try:
        img_path = f"Medicofi/Société Tire Lait Express (en France)/Dépliant/{depliant_images[0][0]}"
        img_url = get_image_url(img_path)
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 40px;">
            <img src="{img_url}" style="width: 100%; max-width: 800px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);">
        </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 40px;">
            <div style="padding: 80px; background: #f9f9f9; border-radius: 10px; max-width: 800px; margin: 0 auto;">
                <div style="color: #888; font-size: 16px;">{depliant_images[0][1]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Deuxième image seule (pleine largeur)
    st.markdown("""
    <div style="color: #202124; font-weight: 600; margin-top: 20px; margin-bottom: 15px; font-size: 18px; text-align: center;">
        sided
    </div>
    """, unsafe_allow_html=True)
    
    try:
        img_path = f"Medicofi/Société Tire Lait Express (en France)/Dépliant/{depliant_images[1][0]}"
        img_url = get_image_url(img_path)
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 40px;">
            <img src="{img_url}" style="width: 100%; max-width: 800px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);">
        </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 40px;">
            <div style="padding: 80px; background: #f9f9f9; border-radius: 10px; max-width: 800px; margin: 0 auto;">
                <div style="color: #888; font-size: 16px;">{depliant_images[1][1]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    # ========== SECTION 5: Emailing et Newsletters ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
            <polyline points="22,6 12,13 2,6"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Email Marketing</h4>
    </div>
    """, unsafe_allow_html=True)

    # Cinq images dans une seule colonne
    emailing_images = [
        ("Capture d'écran 2025-06-19 090912.png", "-"),
        ("Dernière relance avant transmission au service contentieux.png", "-"),
        ("Emailing sages femmes Secteur.png", "-"),
        ("La SMAM approche.png", "-"),
        ("Simplifiez l’allaitement de vos patientes.png", "-")
    ]
    
    for idx, (file_name, description) in enumerate(emailing_images):
        try:
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Emailing et Newsletters/{file_name}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 30px;">
                <div style="display: flex; justify-content: center; margin-bottom: 10px;">
                    <img src="{img_url}" style="width: 100%; max-width: 600px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                </div>
                <div style="color: #202124; font-weight: 600; font-size: 16px; margin-bottom: 5px;">
                    {description}
                </div>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 30px;">
                <div style="padding: 60px; background: #f9f9f9; border-radius: 10px; margin-bottom: 10px;">
                    <div style="color: #888; font-size: 16px;">{description}</div>
                </div>
                <div style="color: #666; font-size: 14px;">
                    Email {idx + 1}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ========== SECTION 6: Flyer ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="3" width="20" height="18" rx="2" ry="2"></rect>
            <line x1="9" y1="21" x2="15" y2="21"></line>
            <line x1="12" y1="17" x2="12" y2="21"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">Flyer</h4>
    </div>
    """, unsafe_allow_html=True)

    # Deux images en deux colonnes
    flyer_images = [
        ("Recto.png", "Double"),
        ("Verso.png", "sided")
    ]
    
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Flyer/{flyer_images[0][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 16px;">{flyer_images[0][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{flyer_images[0][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            img_path = f"Medicofi/Société Tire Lait Express (en France)/Flyer/{flyer_images[1][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 16px;">{flyer_images[1][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{flyer_images[1][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ========== SECTION 7: Guide ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
            <polyline points="10 9 9 9 8 9"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Guidebook</h4>
    </div>
    """, unsafe_allow_html=True)

    # PDF Viewer
    try:
        pdf_url = get_image_url("Medicofi/Société Tire Lait Express (en France)/Guide/Guide Bienvenue web-Graine de vie PAGE.pdf")
        pdf_encoded = urllib.parse.quote(pdf_url, safe='')
        google_viewer_url = f"https://docs.google.com/viewer?url={pdf_encoded}&embedded=true"
        
        st.markdown(f'<iframe width="100%" height="600" src="{google_viewer_url}"></iframe>', unsafe_allow_html=True)
        
        # Boutons d'action
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'<a href="{pdf_url}" download="Guide_Bienvenue_web_Graine_de_vie_PAGE.pdf" style="text-decoration: none;">', unsafe_allow_html=True)
            if st.button("Download the guidebook", use_container_width=True):
                pass
            st.markdown('</a>', unsafe_allow_html=True)
        
        with col2:
            st.markdown(f'<a href="{google_viewer_url}" target="_blank" style="text-decoration: none;">', unsafe_allow_html=True)
            if st.button("Open PDF", use_container_width=True):
                pass
            st.markdown('</a>', unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style="text-align: center; padding: 60px; background: #f9f9f9; border-radius: 10px; margin: 20px 0;">
            <div style="color: #888; font-size: 16px;">Guide PDF not available</div>
        </div>
        """, unsafe_allow_html=True)

    # ========== SECTION 8: Kakémono ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <line x1="3" y1="9" x2="21" y2="9"></line>
            <line x1="9" y1="21" x2="9" y2="9"></line>
        </svg>
        <h4 style="margin: 0; color: #202124;">roll banner</h4>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        kakemono_url = get_image_url("Medicofi/Société Tire Lait Express (en France)/Kakémono/Kakémono TLE.png")
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="{kakemono_url}" style="width: 100%; max-width: 500px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style="text-align: center; padding: 60px; background: #f9f9f9; border-radius: 10px; margin: 20px 0;">
            <div style="color: #888; font-size: 16px;">Kakémono image not available</div>
        </div>
        """, unsafe_allow_html=True)

    # ========== SECTION 9: Réseaux Sociaux ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
        </svg>
        <h4 style="margin: 0; color: #202124;">Social Media</h4>
    </div>
    """, unsafe_allow_html=True)

    # Bouton pour accéder à la page des réseaux sociaux
    if st.button("SOCIAL MADIA", use_container_width=True):
        st.session_state.page = "tle_reseaux_sociaux"
        st.rerun()

    # ========== SECTION 10: Roll-up ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M23 12a11.05 11.05 0 0 0-22 0zm-5 7a3 3 0 0 1-6 0v-7"></path>
        </svg>
        <h4 style="margin: 0; color: #202124;">Roll-up</h4>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        rollup_url = get_image_url("Medicofi/Société Tire Lait Express (en France)/Roll-up/Roll-up TLE recrute.png")
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0 40px 0;">
            <img src="{rollup_url}" style="width: 100%; max-width: 500px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style="text-align: center; padding: 60px; background: #f9f9f9; border-radius: 10px; margin: 20px 0 40px 0;">
            <div style="color: #888; font-size: 16px;">Roll-up image not available</div>
        </div>
        """, unsafe_allow_html=True)

# ========== PAGE Réseaux Sociaux TLE ==========
elif st.session_state.page == "tle_reseaux_sociaux":
    if st.button("←"):
        st.session_state.page = "medicofi8"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
        </svg>
        <h3 style="margin: 0; color: #202124;">Social Media - Tire Lait Express</h3>
    </div>
    """, unsafe_allow_html=True)

    # ========== SECTION 1: Vidéo youtube ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="23 7 16 12 23 17 23 7"></polygon>
            <rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect>
        </svg>
        <h4 style="margin: 0; color: #202124;">YouTube Video</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Afficher la vidéo
    try:
        video_url = get_image_url("Medicofi/Société Tire Lait Express (en France)/Réseaux Sociaux/Vidéo youtube/Bordeaux.mp4")
        st.video(video_url)
    except:
        st.markdown("""
        <div style="text-align: center; padding: 60px; background: #f9f9f9; border-radius: 10px; margin: 20px 0;">
            <div style="color: #888; font-size: 16px;">Vidéo non disponible</div>
        </div>
        """, unsafe_allow_html=True)

    # ========== SECTION 2: Post Facebook Instagram et LinkedIn ==========
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <circle cx="8.5" cy="8.5" r="1.5"></circle>
            <polyline points="21 15 16 10 5 21"></polyline>
        </svg>
        <h4 style="margin: 0; color: #202124;">Facebook, Instagram, and LinkedIn Posts</h4>
    </div>
    """, unsafe_allow_html=True)

    # Deux boutons en deux colonnes
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Carousel Post", use_container_width=True):
            st.session_state.page = "tle_post_carrousel"
            st.rerun()
    
    with col2:
        if st.button("Single Post", use_container_width=True):
            st.session_state.page = "tle_post_statique"
            st.rerun()
    # Espace après la carte de profil
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
# ========== PAGE Post Carrousel TLE ==========
elif st.session_state.page == "tle_post_carrousel":
    if st.button("←"):
        st.session_state.page = "tle_reseaux_sociaux"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <circle cx="8.5" cy="8.5" r="1.5"></circle>
            <polyline points="21 15 16 10 5 21"></polyline>
        </svg>
        <h3 style="margin: 0; color: #202124;">Carousel Post - Tire Lait Express</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="color: #666; margin-bottom: 30px;">Carousel posts for social media</div>', unsafe_allow_html=True)
    
    # Structure des 8 carrousels
    carrousels = [
        {
            "name": "Carrousel 1",
            "images": ["1.png", "2.png", "3.png", "4.png", "5.png"]
        },
        {
            "name": "Carrousel 2", 
            "images": ["1.png", "2.png", "3.png", "4.png"]
        },
        {
            "name": "Carrousel 3",
            "images": ["1.png", "2.png", "3.png", "4.png", "5.png"]
        },
        {
            "name": "Carrousel 4",
            "images": ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]
        },
        {
            "name": "Carrousel 5",
            "images": ["1.png", "2.png", "3.png", "4.png", "5.png"]
        },
        {
            "name": "Carrousel 6",
            "images": ["1.png", "2.png", "3.png", "4.png"]
        },
        {
            "name": "Carrousel 7",
            "images": ["1.png", "2.png", "3.png", "4.png", "5.png"]
        },
        {
            "name": "Carrousel 8",
            "images": ["1.png", "2.png", "3.png", "4.png"]
        }
    ]
    
    # Afficher chaque carrousel
    for carrousel in carrousels:
        st.markdown(f"""
        <div style="margin: 30px 0 15px 0; padding-bottom: 10px; border-bottom: 2px solid #FBBDFA;">
            <h4 style="color: #202124; margin: 0;">{carrousel['name']}</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Créer des colonnes selon le nombre d'images (max 6)
        num_cols = min(len(carrousel['images']), 6)
        cols = st.columns(num_cols)
        
        for idx, img_name in enumerate(carrousel['images']):
            if idx < num_cols:
                try:
                    img_path = f"Medicofi/Société Tire Lait Express (en France)/Réseaux Sociaux/Post Facebook Instagram et LinkedIn/Post carrousel/{carrousel['name'].split()[1]}/{img_name}"
                    img_url = get_image_url(img_path)
                    
                    with cols[idx]:
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 20px;">
                            <img src="{img_url}" style="width: 100%; max-width: 200px; border-radius: 8px; box-shadow: 0 3px 10px rgba(0,0,0,0.1);">
                            <div style="color: #666; font-size: 12px; margin-top: 5px;">Post {img_name.split('.')[0]}</div>
                        </div>
                        """, unsafe_allow_html=True)
                except:
                    with cols[idx]:
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 20px;">
                            <div style="padding: 30px; background: #f9f9f9; border-radius: 8px;">
                                <div style="color: #888; font-size: 12px;">Slide {img_name.split('.')[0]}</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
        
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# ========== PAGE Post Statique TLE ==========
elif st.session_state.page == "tle_post_statique":
    if st.button("←"):
        st.session_state.page = "tle_reseaux_sociaux"
        st.rerun()

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <circle cx="8.5" cy="8.5" r="1.5"></circle>
            <polyline points="21 15 16 10 5 21"></polyline>
        </svg>
        <h3 style="margin: 0; color: #202124;">Single Post - Tire Lait Express</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="color: #666; margin-bottom: 30px;">Single Post for social media</div>', unsafe_allow_html=True)
    
    # Liste des 11 images
    static_images = []
    for i in range(1, 12):
        static_images.append(f"{i}.png")
    
    # Afficher 3 images par ligne
    num_columns = 3
    num_images = len(static_images)
    
    for i in range(0, num_images, num_columns):
        cols = st.columns(num_columns)
        
        for col_idx in range(num_columns):
            img_idx = i + col_idx
            
            if img_idx < num_images:
                try:
                    img_path = f"Medicofi/Société Tire Lait Express (en France)/Réseaux Sociaux/Post Facebook Instagram et LinkedIn/Post statique/{static_images[img_idx]}"
                    img_url = get_image_url(img_path)
                    
                    with cols[col_idx]:
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 20px;">
                            <img src="{img_url}" style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                            <div style="color: #666; font-size: 14px; margin-top: 8px;">Post {static_images[img_idx].split('.')[0]}</div>
                        </div>
                        """, unsafe_allow_html=True)
                except:
                    with cols[col_idx]:
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 20px;">
                            <div style="padding: 40px; background: #f9f9f9; border-radius: 10px;">
                                <div style="color: #888; font-size: 14px;">Post {static_images[img_idx].split('.')[0]}</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)                    
# Page CHabeb Ennour (volunteer group)
elif st.session_state.page == "freelance_chabeb":
    if st.button("←"):
        st.session_state.page = "medicofi"
        st.rerun()

    # Titre avec icône
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px; margin-top: 30px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
            <circle cx="9" cy="7" r="4"></circle>
            <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
            <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
        </svg>
        <h3 style="margin: 0; color: #202124;">Chabeb Ennour (volunteer group)</h3>
    </div>
    """, unsafe_allow_html=True)

    # Deux images dans une seule colonne
    chabeb_images = [
        ("affiche rentree sdf.jpg", "Poster 1"),
        ("تغذية صحية للعائلات المعوزة.png", "Poster 2")
    ]
    
    # Affichage des images dans une seule colonne
    for file_name, description in chabeb_images:
        try:
            img_path = f"Freelance/CHabeb Ennour (volunteer group)/{file_name}"
            img_url = get_image_url(img_path)
            
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 40px; padding: 20px; background: white; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
                <div style="color: #202124; font-weight: 700; font-size: 18px; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #FBBDFA;">
                    {description}
                </div>
                <div style="display: flex; justify-content: center;">
                    <img src="{img_url}" style="width: 100%; max-width: 900px; border-radius: 10px; box-shadow: 0 6px 25px rgba(0,0,0,0.1);">
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 40px; padding: 50px; background: #f9f9f9; border-radius: 12px; border: 2px dashed #FBBDFA;">
                <div style="color: #888; font-size: 18px; margin-bottom: 15px;">
                    Image non disponible
                </div>
                <div style="color: #202124; font-weight: 600; font-size: 16px; margin-bottom: 10px;">
                    {description}
                </div>
                <div style="color: #666; font-size: 14px;">
                    {file_name}
                </div>
            </div>
            """, unsafe_allow_html=True)
# Page Clorex Company
elif st.session_state.page == "freelance_clorex":
    if st.button("←"):
        st.session_state.page = "medicofi"
        st.rerun()

    # Titre avec icône
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px; margin-top: 30px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
        </svg>
        <h3 style="margin: 0; color: #202124;">Clorex Company</h3>
    </div>
    """, unsafe_allow_html=True)

    # Quatre images en deux colonnes (2x2)
    clorex_images = [
        ("Assouplissant magic-01.png", "Label 1"),
        ("Assouplissant naturel-01.png", "Label 2"),
        ("CLOREX Vaisselle pomme-01.png", "Label 3"),
        ("etiquette gel machine Ariel-01.png", "Label 4")
    ]
    
    # Première ligne
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            img_path = f"Freelance/Clorex Company/{clorex_images[0][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 15px;">{clorex_images[0][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{clorex_images[0][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            img_path = f"Freelance/Clorex Company/{clorex_images[1][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 15px;">{clorex_images[1][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{clorex_images[1][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Deuxième ligne
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            img_path = f"Freelance/Clorex Company/{clorex_images[2][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 15px;">{clorex_images[2][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{clorex_images[2][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            img_path = f"Freelance/Clorex Company/{clorex_images[3][0]}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="color: #202124; font-weight: 600; margin-top: 10px; font-size: 15px;">{clorex_images[3][1]}</div>
                <img src="{img_url}" style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="padding: 50px; background: #f9f9f9; border-radius: 10px;">
                    <div style="color: #888;">{clorex_images[3][1]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Page Mayar Auto Company
elif st.session_state.page == "freelance_mayar":
    if st.button("←"):
        st.session_state.page = "medicofi"
        st.rerun()

    # Titre avec icône
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px; margin-top: 30px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="7" cy="17" r="2"></circle>
            <circle cx="17" cy="17" r="2"></circle>
            <path d="M5 17H3v-6l2-5h9l4 5h5v6h-2m-14 0v-6h14v6"></path>
            <path d="M9 17v-6h5v6"></path>
        </svg>
        <h3 style="margin: 0; color: #202124;">Mayar Auto Company</h3>
    </div>
    """, unsafe_allow_html=True)

    # Quatre images dans une seule colonne
    mayar_images = [
        ("3D 2.jpg", "Selected proposals"),
        ("Mar P4.png", "Design Proposal 1"),
        ("Mayar P4.png", "Design Proposal 2"),
        ("Mr P4.png", "Design Proposal  4")
    ]
    
    # Conteneur unique pour toutes les images
    for image_name, image_label in mayar_images:
        # Label avant l'image
        st.markdown(f"""
        <div style="color: #202124; font-weight: 600; margin-top: 25px; margin-bottom: 10px; font-size: 16px; padding-left: 10px;">
            {image_label}
        </div>
        """, unsafe_allow_html=True)
        
        # Image centrée
        try:
            img_path = f"Freelance/Mayar Auto Company/{image_name}"
            img_url = get_image_url(img_path)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 30px;">
                <img src="{img_url}" style="width: 100%; max-width: 500px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 30px;">
                <div style="padding: 60px; background: #f9f9f9; border-radius: 10px; max-width: 500px; margin: 0 auto;">
                    <div style="color: #888; font-size: 14px;">Image non disponible</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
elif st.session_state.page == "tse":
    if st.button("←"):
        st.session_state.page = "medicofi"
        st.rerun()

    # Titre principal

    # SECTION 1: Guide mise en page 2021 avec icône PDF
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
            <polyline points="10 9 9 9 8 9"></polyline>
        </svg>
        <h3 style="margin: 0; color: #202124;">Sportswear Layout</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # AFFICHAGE DU PDF
    try:
        display_path = "TSE/Guide mise en page2021.pdf"
        pdf_url = get_image_url(display_path)
        pdf_encoded = urllib.parse.quote(pdf_url, safe='')
        google_viewer_url = f"https://docs.google.com/viewer?url={pdf_encoded}&embedded=true"
        
        st.markdown(f'<iframe width="100%" height="600" src="{google_viewer_url}"></iframe>', unsafe_allow_html=True)
    except:
        st.write("PDF en cours d'affichage...")

    # LES DEUX BOUTONS IDENTIQUES - STYLE IDENTIQUE
    col1, col2 = st.columns(2)
    
    # Bouton 1: Télécharger
    with col1:
        download_path = "mes_documents/TSE/Guide mise en page2021.pdf"
        try:
            with open(download_path, "rb") as f:
                pdf_data = f.read()
            
            # Même style que le bouton "Ouvrir PDF"
            if st.button("Download the guidebook", use_container_width=True):
                # Créer un lien de téléchargement
                import base64
                b64 = base64.b64encode(pdf_data).decode()
                href = f'<a href="data:application/pdf;base64,{b64}" download="Guide mise en page 2021.pdf" style="text-decoration: none; color: inherit;">Télécharger en cours...</a>'
                st.markdown(href, unsafe_allow_html=True)
        except Exception as e:
            st.button("Download the guidebook", disabled=True, use_container_width=True)
    
    # Bouton 2: Ouvrir PDF
    with col2:
        if st.button("Open PDF", use_container_width=True):
            # Ouvre le PDF dans un nouvel onglet
            js = f"window.open('{google_viewer_url}', '_blank');"
            st.markdown(f"<script>{js}</script>", unsafe_allow_html=True)

    st.markdown("---")  # Séparateur

  # SECTION 2: Images SportsWear Design avec icône t-shirt
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20.38 3.46L16 2a4 4 0 0 1-8 0L3.62 3.46a2 2 0 0 0-1.34 2.23l.58 3.47a1 1 0 0 0 .99.84H6v10c0 1.1.9 2 2 2h8a2 2 0 0 0 2-2V10h2.15a1 1 0 0 0 .99-.84l.58-3.47a2 2 0 0 0-1.34-2.23z"></path>
        </svg>
        <h3 style="margin: 0; color: #202124;">SportsWear Design</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # VOUS ORDONNEZ LES IMAGES COMME VOUS VOULEZ
    votre_ordre_images = [
        "TSE/SportsWear Design/11.png",   # Image 3 en premier
        "TSE/SportsWear Design/12.png",   # Puis image 1
        "TSE/SportsWear Design/7.png",   # Puis image 5
        "TSE/SportsWear Design/6.png",   # etc.
        "TSE/SportsWear Design/5.png",
        "TSE/SportsWear Design/3.png",
        "TSE/SportsWear Design/1.png",
        "TSE/SportsWear Design/2.png",
        "TSE/SportsWear Design/9.png",
        "TSE/SportsWear Design/8.png",
        "TSE/SportsWear Design/10.png",
        "TSE/SportsWear Design/4.png"
    ]
    
    # Variable pour suivre la proposition
    current_proposition = None
    
    # Afficher chaque image dans VOTRE ordre
    for idx, img_path in enumerate(votre_ordre_images):
        img_number = idx + 1
        
        # Déterminer la proposition (6 premières = Proposition 1, 6 suivantes = Proposition 2)
        proposition = "Proposition 1" if idx < 6 else "Proposition 2"
        
        # Afficher le titre de la proposition quand elle change
        if proposition != current_proposition:
            current_proposition = proposition
            st.markdown(f"""
            <div style="margin: 40px 0 20px 0; padding-bottom: 10px; border-bottom: 2px solid #FBBDFA;">
                <h3 style="color: #202124; margin: 0; font-size: 24px; font-weight: 600;">{proposition}</h3>
            </div>
            """, unsafe_allow_html=True)
        
        try:
            img_url = get_image_url(img_path)
            
            # Récupérer le numéro réel du fichier
            file_number = img_path.split("/")[-1].split(".")[0]
            
            # Conteneur pour chaque image avec son numéro
            st.markdown(f"""
            <div style="margin-bottom: 40px; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
                    <div style="background: #FBBDFA; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">
                        {img_number}
                    </div>
                    <div style="color: #202124; font-weight: 600; font-size: 18px;">{proposition} - Image {img_number}</div>
                </div>
                <div style="text-align: center;">
                    <img src="{img_url}" style="width: 100%; max-width: 900px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <div style="color: #666; font-size: 14px; margin-top: 10px; font-style: italic;">
                        File: {file_number}.png
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:  # CORRECTION : Cette ligne doit être alignée avec le 'try'
            st.markdown(f"""
            <div style="margin-bottom: 30px; padding: 40px; background: #f9f9f9; border-radius: 10px; text-align: center;">
                <div style="color: #888; font-size: 16px; margin-bottom: 10px;">
                    <span style="background: #ffebee; color: #c62828; padding: 5px 10px; border-radius: 5px; font-size: 14px;">
                        ⚠️ Non trouvé
                    </span>
                </div>
                <div style="color: #666; font-size: 14px;">{img_path}</div>
                <div style="color: #999; font-size: 13px; margin-top: 10px;">{proposition} - Image {img_number}</div>
            </div>
            """, unsafe_allow_html=True)
    
# La page apnidoc reste la même
elif st.session_state.page == "apnidoc":
    if st.button("←"):
        st.session_state.page = "medicofi"
        st.rerun()

    # Titre avec icône SVG de feuille
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14 2 14 8 20 8"/>
            <line x1="16" y1="13" x2="8" y2="13"/>
            <line x1="16" y1="17" x2="8" y2="17"/>
            <polyline points="10 9 9 9 8 9"/>
        </svg>
        <h3 style="margin: 0; color: #202124;">Flyer Apnidoc</h3>
    </div>
    """, unsafe_allow_html=True)

    # Flyer Image
    st.markdown(f"""
    <div style="display: flex; justify-content: center; margin: 20px 0;">
        <img src="{flyer_url}" style="width: 500px; max-width: 100%;">
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px;padding-bottom: 10px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"/>
            <line x1="2" y1="12" x2="22" y2="12"/>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
        </svg>
        <h3 style="margin: 0; color: #202124;">Web Site ApniDoc</h3>
    </div>
    """, unsafe_allow_html=True)
    # Design Interface Button
    if st.button("DESIGN INTERFACE WEB SITE APNIDOC (RESPONSIVE)", use_container_width=True):
        st.session_state.page = "design_folders"
        st.rerun()
        
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

elif st.session_state.page == "design_folders":
    if st.button("←"):
        st.session_state.page = "apnidoc"
        st.rerun()

    st.title("DESIGN INTERFACE WEB SITE APNIDOC")

    # Website Link Section
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"/>
            <line x1="2" y1="12" x2="22" y2="12"/>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
        </svg>
        <h3 style="margin: 0; color: #202124;">Web Site ApniDoc</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(
        '<span style="color: #666666;">The website is already online, but it is still under development.</span>',
        unsafe_allow_html=True
    )
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 8px; margin: 15px 0;">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0563C1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
            <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
        </svg>
        <a href="https://apnidoc.fr/" target="_blank" style="color: #0563C1; text-decoration: none; font-weight: 500; font-size: 16px;">Visiter https://apnidoc.fr/</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 8px; margin: 15px 0;">
        <span style="color: #202124; text-decoration: none; font-weight: 500; font-size: 16px;">Responsive</span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        # Bouton DESKTOP avec icône SVG
        desktop_html = """
        <div style="text-align: center; margin-bottom: 10px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#202124" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 10px;">
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
                <line x1="8" y1="21" x2="16" y2="21"/>
                <line x1="12" y1="17" x2="12" y2="21"/>
            </svg>
        </div>
        """
        st.markdown(desktop_html, unsafe_allow_html=True)
        
        if st.button("DESKTOP", use_container_width=True):
            st.session_state.current_device = "Desktop"
            st.session_state.page = "device_images"
            st.rerun()

    with col2:
        # Bouton IPAD avec icône SVG
        ipad_html = """
            <div style="text-align: center; margin-bottom: 10px;">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#202124" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 10px;">
                    <rect x="5" y="2" width="14" height="20" rx="2" ry="2"/>
                    <line x1="12" y1="18" x2="12" y2="18"/>
                </svg>
            </div>
            """
        st.markdown(ipad_html, unsafe_allow_html=True)
        
        if st.button("IPAD", use_container_width=True):
            st.session_state.current_device = "iPad"
            st.session_state.page = "device_images"
            st.rerun()

    with col3:
        # Bouton PHONE avec icône SVG
        phone_html = """
        <div style="text-align: center; margin-bottom: 10px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#202124" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 10px;">
                <rect x="5" y="2" width="14" height="20" rx="2" ry="2"/>
                <line x1="12" y1="18" x2="12" y2="18"/>
            </svg>
        </div>
        """
        st.markdown(phone_html, unsafe_allow_html=True)
        
        if st.button("PHONE", use_container_width=True):
            st.session_state.current_device = "Phone"
            st.session_state.page = "device_images"
            st.rerun()
            
elif st.session_state.page == "device_images":
    if st.button("←"):
        st.session_state.page = "design_folders"
        st.session_state.current_device = None
        st.rerun()

    device = st.session_state.current_device
    device_icons = {
        "Desktop": "",
        "iPad": "",
        "Phone": ""
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
    if st.button("←"):
        st.session_state.page = "accueil"
        st.rerun()

    # Titre avec le même design
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FBBDFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
            <polyline points="10 9 9 9 8 9"></polyline>
        </svg>
        <h1 style="margin: 0; color: #202124; font-size: 32px; font-weight: 700;">Selected Works – (2012–2019)</h1>
    </div>
    """, unsafe_allow_html=True)

    # PDF Viewer
    st.markdown(f'<iframe width="100%" height="800" src="{google_viewer_url}"></iframe>', unsafe_allow_html=True)

    # Action Buttons
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f'<a href="{pdf_url_raw}" download="Portfolio_Ines_HARRABI_2024.pdf" style="text-decoration: none; color: #666666;">', unsafe_allow_html=True)
        if st.button("Download PDF", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<a href="{google_viewer_url}" target="_blank" style="text-decoration: none; color: #666666;">', unsafe_allow_html=True)
        if st.button("Open with Google Viewer", use_container_width=True):
            pass
        st.markdown('</a>', unsafe_allow_html=True)
