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
    width: 18px;
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
                            <svg class="contact-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640" fill="#202124">
                                <path d="M185.577 119.517c18.862 0 35.847 1.642 51.331 5.008 15.52 3.236 28.63 8.752 39.757 16.24 10.996 7.512 19.476 17.516 25.748 29.989 6 12.354 9 27.862 9 46.229 0 19.878-4.476 36.355-13.512 49.63-9.118 13.24-22.358 24-40.122 32.516 24.236 6.993 42.118 19.24 54.118 36.627 11.989 17.516 17.753 38.504 17.753 63.225 0 19.996-3.886 37.11-11.469 51.615-7.748 14.634-18.248 26.492-31.11 35.634-12.993 9.236-27.993 15.992-44.753 20.363-16.642 4.346-33.756 6.626-51.45 6.626H0V119.553l185.601.012-.023-.048zm232.042 31.76h159.616v38.883l-159.616-.012v-38.883.012zm35.469 293.448c11.764 11.469 28.63 17.233 50.646 17.233 15.745 0 29.516-4.016 40.867-12.012 11.35-7.996 18.248-16.465 20.882-25.229l68.965.012c-11.126 34.347-27.874 58.749-50.859 73.5-22.642 14.753-50.35 22.241-82.5 22.241-22.524 0-42.627-3.65-60.757-10.772-18.119-7.24-33.237-17.35-45.993-30.638-12.366-13.24-22.11-28.984-28.996-47.493-6.756-18.354-10.229-38.752-10.229-60.744 0-21.367 3.52-41.245 10.477-59.623 7.122-18.52 16.878-34.359 29.87-47.753 12.98-13.382 28.229-24 46.24-31.748 17.883-7.76 37.631-11.646 59.505-11.646 24.107 0 45.225 4.642 63.356 14.126 18 9.355 32.87 21.993 44.492 37.749 11.646 15.768 19.878 33.874 25.004 54.107 5.126 20.232 6.875 41.35 5.469 63.508H433.706c0 22.359 7.512 43.76 19.358 55.1l.024.082zm89.871-149.707c-9.236-10.24-25.122-15.874-44.233-15.874-12.52 0-22.866 2.114-31.11 6.366-8.115 4.229-14.752 9.473-19.878 15.745-4.997 6.248-8.516 13.004-10.465 20.102-1.996 6.874-3.236 13.24-3.65 18.756l127.502-.012c-1.878-19.984-8.752-34.736-18.118-45.106l-.047.023zm-368.662-16.524c15.355 0 28.099-3.65 38.091-11.008 9.992-7.24 14.752-19.24 14.752-35.752 0-9.106-1.63-16.76-4.878-22.642-3.354-5.87-7.76-10.512-13.37-13.748-5.516-3.355-11.74-5.646-19.099-6.886-7.122-1.358-14.634-1.984-22.24-1.984H86.576v91.973h87.745l-.024.047zm4.748 167.59c8.528 0 16.642-.757 24.213-2.528 7.748-1.748 14.634-4.359 20.363-8.35 5.752-3.887 10.641-8.989 14.114-15.745 3.52-6.638 5.126-15.118 5.126-25.477 0-20.232-5.764-34.748-17.114-43.512-11.351-8.646-26.47-12.874-45.214-12.874H86.552V445.93l92.493-.012v.165z"/>
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
                <p style="color: #666666; font-size: 16px;">As my Behance portfolio is currently being updated, I have gathered here a selected overview of my work. Below, you will find a PDF featuring my earlier projects, along with a folder showcasing my most recent work.</p>
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
                <div style="background: linear-gradient(135deg, #FFE5E5 0%, #FFD6D6 100%); padding: 15px; border-radius: 12px; display: flex; align-items: center; justify-content: center; position: absolute; right: 19px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#ff80bd" stroke-width="2">
                        <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
                    </svg>
                </div>
                <div style="flex: 1;">
                    <h3 style="color: #202124; margin: 0 0 5px 0; font-size: 18px; font-weight: 600;">My New Works</h3>
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
                <div style="background: linear-gradient(135deg, #E8F4FF 0%, #D6EBFF 100%); padding: 15px; border-radius: 12px; display: flex; align-items: center; justify-content: center; position: absolute;right: 19px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#4A90E2" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14,2 14,8 20,8"/>
                        <line x1="16" y1="13" x2="8" y2="13"/>
                        <line x1="16" y1="17" x2="8" y2="17"/>
                        <polyline points="10,9 9,9 8,9"/>
                    </svg>
                </div>
                <div style="flex: 1;">
                    <h3 style="color: #202124; margin: 0 0 5px 0; font-size: 18px; font-weight: 600;">My OLD PORTFOLIO PDF</h3>
                    <p style="color: #888; margin: 0; font-size: 14px;">My old portfolio in PDF versionF</p>
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
