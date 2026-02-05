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

# ========== تنسيق ==========
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    .stApp {
        background: #0a0a0a;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 0;
        min-height: 100vh;
    }
    
    /* Banner Slider Styles */
    .banner-container {
        position: relative;
        width: 100%;
        height: 400px;
        overflow: hidden;
        margin-bottom: 40px;
        border-radius: 0 0 30px 30px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.8);
    }
    
    .banner-slide {
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        animation: slideAnimation 15s infinite;
    }
    
    @keyframes slideAnimation {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .banner-content {
        text-align: center;
        color: white;
        z-index: 10;
        padding: 40px;
    }
    
    .banner-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 20px;
        text-shadow: 0 4px 20px rgba(0,0,0,0.5);
        letter-spacing: 2px;
    }
    
    .banner-subtitle {
        font-size: 1.5rem;
        font-weight: 300;
        opacity: 0.95;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }
    
    /* Container Styles */
    .content-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 40px 20px;
    }
    
    h1 {
        color: #ffffff;
        text-align: center;
        margin-bottom: 40px;
        font-size: 2.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 3px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Button Styles */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 20px 30px;
        border-radius: 15px;
        font-size: 1.2rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.4s ease;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Back Button */
    .back-button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%) !important;
        padding: 12px 25px !important;
        margin-bottom: 30px;
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.4) !important;
    }
    
    .back-button:hover {
        background: linear-gradient(135deg, #ee5a6f 0%, #ff6b6b 100%) !important;
        box-shadow: 0 15px 40px rgba(255, 107, 107, 0.6) !important;
    }
    
    /* Card Styles for Images */
    .image-card {
        background: #1a1a1a;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.6);
        border: 2px solid #333;
        transition: all 0.3s ease;
    }
    
    .image-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        border-color: #667eea;
    }
    
    .image-caption {
        color: #ffffff;
        text-align: center;
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 15px;
        padding: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    /* PDF Frame */
    .pdf-frame {
        width: 100%;
        height: 800px;
        border: 3px solid #667eea;
        border-radius: 20px;
        margin: 20px 0;
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.5);
        background: #1a1a1a;
    }
    
    /* Action Buttons */
    .action-buttons {
        display: flex;
        gap: 25px;
        justify-content: center;
        margin-top: 30px;
        flex-wrap: wrap;
    }
    
    .action-btn {
        padding: 15px 35px;
        border-radius: 15px;
        text-decoration: none;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    }
    
    .download-btn {
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        color: white;
    }
    
    .download-btn:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(76, 175, 80, 0.6);
    }
    
    .newtab-btn {
        background: linear-gradient(135deg, #2196F3 0%, #0D47A1 100%);
        color: white;
    }
    
    .newtab-btn:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(33, 150, 243, 0.6);
    }
    
    .website-btn {
        background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);
        color: white;
    }
    
    .website-btn:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(255, 152, 0, 0.6);
    }
    
    /* Website Link Section */
    .website-section {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        padding: 30px;
        border-radius: 20px;
        margin: 40px 0;
        text-align: center;
        border: 2px solid #667eea;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
    }
    
    .website-title {
        color: #ffffff;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 15px;
    }
    
    .website-subtitle {
        color: #aaaaaa;
        font-size: 1rem;
        margin-bottom: 25px;
        font-style: italic;
    }
    
    .website-link {
        color: #667eea;
        font-size: 1.3rem;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        padding: 15px 30px;
        background: rgba(102, 126, 234, 0.1);
        border-radius: 10px;
        transition: all 0.3s ease;
        border: 2px solid #667eea;
    }
    
    .website-link:hover {
        background: #667eea;
        color: white;
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.5);
    }
    
    /* Device Folder Cards */
    .device-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px;
        margin: 30px 0;
    }
    
    .device-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        border: 2px solid #333;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .device-card:hover {
        border-color: #667eea;
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
    }
    
    .device-icon {
        font-size: 4rem;
        margin-bottom: 20px;
    }
    
    .device-name {
        color: white;
        font-size: 1.5rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Image Gallery */
    .image-gallery {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 30px;
        margin: 30px 0;
    }
    
    @media (max-width: 768px) {
        .banner-title {
            font-size: 2rem;
        }
        
        .banner-subtitle {
            font-size: 1rem;
        }
        
        .image-gallery {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

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

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    # Banner Slider
    st.markdown("""
    <div class="banner-container">
        <div class="banner-slide">
            <div class="banner-content">
                <div class="banner-title">📂 MES DOSSIERS</div>
                <div class="banner-subtitle">Portfolio Professionnel & Projets Design</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏥 MEDICOFI", use_container_width=True):
            st.session_state.page = "medicofi"
            st.rerun()
    
    with col2:
        if st.button("📄 PORTFOLIO PDF", use_container_width=True):
            st.session_state.page = "pdf_viewer"
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "medicofi":
    if st.button("← RETOUR", key="back_medicofi"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>🏥 MEDICOFI</h1>", unsafe_allow_html=True)
    
    if st.button("🇫🇷 SOCIÉTÉ APNIDOC (EN FRANCE)", use_container_width=True):
        st.session_state.page = "apnidoc"
        st.rerun()

elif st.session_state.page == "apnidoc":
    if st.button("← RETOUR", key="back_apnidoc"):
        st.session_state.page = "medicofi"
        st.rerun()
    
    st.markdown("<h1>🇫🇷 SOCIÉTÉ APNIDOC</h1>", unsafe_allow_html=True)
    
    # Flyer Image
    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    st.image(flyer_url, use_container_width=True)
    st.markdown('<div class="image-caption">📄 Flyer ApniDoc</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Design Interface Button
    if st.button("🎨 DESIGN INTERFACE WEB SITE APNIDOC (RESPONSIVE)", use_container_width=True):
        st.session_state.page = "design_folders"
        st.rerun()

elif st.session_state.page == "design_folders":
    if st.button("← RETOUR", key="back_design"):
        st.session_state.page = "apnidoc"
        st.rerun()
    
    st.markdown("<h1>🎨 DESIGN INTERFACE WEB SITE APNIDOC</h1>", unsafe_allow_html=True)
    
    # Website Link Section
    st.markdown("""
    <div class="website-section">
        <div class="website-title">🌐 Site Web ApniDoc</div>
        <div class="website-subtitle">(Le site web est déjà en ligne, mais il est toujours en cours de développement.)</div>
        <a href="https://apnidoc.fr/" target="_blank" class="website-link">
            🔗 Visiter https://apnidoc.fr/
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Device Selection
    st.markdown('<h2 style="color: white; text-align: center; margin: 40px 0;">Choisissez un format :</h2>', unsafe_allow_html=True)
    
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
    if st.button("← RETOUR", key="back_device"):
        st.session_state.page = "design_folders"
        st.session_state.current_device = None
        st.rerun()
    
    device = st.session_state.current_device
    device_icons = {
        "Desktop": "🖥️",
        "iPad": "📱",
        "Phone": "📱"
    }
    
    st.markdown(f"<h1>{device_icons.get(device, '📱')} DESIGN {device.upper()}</h1>", unsafe_allow_html=True)
    
    # Display images
    if device in design_images:
        st.markdown('<div class="image-gallery">', unsafe_allow_html=True)
        
        for img_path in design_images[device]:
            img_url = get_image_url(img_path)
            img_name = img_path.split('/')[-1].replace('.png', '').replace('_', ' ')
            
            st.markdown('<div class="image-card">', unsafe_allow_html=True)
            st.image(img_url, use_container_width=True)
            st.markdown(f'<div class="image-caption">{img_name}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "pdf_viewer":
    if st.button("← RETOUR", key="back_pdf"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>📄 PORTFOLIO INES HARRABI 2024</h1>", unsafe_allow_html=True)
    
    # PDF Viewer
    st.markdown(f"""
    <iframe class="pdf-frame" src="{google_viewer_url}"></iframe>
    """, unsafe_allow_html=True)
    
    # Action Buttons
    st.markdown(f"""
    <div class="action-buttons">
        <a href="{pdf_url_raw}" download="Portfolio_Ines_HARRABI_2024.pdf" class="action-btn download-btn">
            📥 Télécharger le PDF
        </a>
        <a href="{google_viewer_url}" target="_blank" class="action-btn newtab-btn">
            🔗 Ouvrir dans Google Viewer
        </a>
    </div>
    """, unsafe_allow_html=True)
