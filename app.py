import streamlit as st

# ========== الإعدادات ==========
GITHUB_USER = "RihabJenzeri"
REPO_NAME = "streamlit-docs"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/"

# ========== حالة التطبيق ==========
if 'page' not in st.session_state:
    st.session_state.page = "accueil"
if 'show_large_image' not in st.session_state:
    st.session_state.show_large_image = False

# ========== تنسيق مع JavaScript للنافذة المنبثقة ==========
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Arial', sans-serif;
        padding: 20px;
    }
    
    h1 {
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    
    .folder-btn {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.2);
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        font-size: 20px;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .folder-btn:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }
    
    .image-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 30px 0;
    }
    
    .thumbnail {
        width: 300px;
        height: 300px;
        object-fit: contain;
        border: 3px solid white;
        border-radius: 15px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    .thumbnail:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 35px rgba(0,0,0,0.4);
        border-color: #FFD700;
    }
    
    .click-hint {
        color: #FFD700;
        font-size: 14px;
        margin-top: 10px;
        text-align: center;
    }
    
    /* نافذة الصورة الكبيرة */
    .modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0,0,0,0.9);
        justify-content: center;
        align-items: center;
    }
    
    .modal-content {
        max-width: 90%;
        max-height: 90%;
        border-radius: 10px;
        box-shadow: 0 0 40px rgba(255,255,255,0.2);
    }
    
    .close-btn {
        position: absolute;
        top: 20px;
        right: 30px;
        color: white;
        font-size: 40px;
        font-weight: bold;
        cursor: pointer;
        transition: 0.3s;
    }
    
    .close-btn:hover {
        color: #FFD700;
        transform: scale(1.2);
    }
    
    .download-large {
        position: absolute;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        background: #4CAF50;
        color: white;
        padding: 12px 25px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
        transition: all 0.3s;
    }
    
    .download-large:hover {
        background: #2E7D32;
        transform: translateX(-50%) scale(1.1);
    }
</style>

<div id="imageModal" class="modal">
    <span class="close-btn" onclick="closeModal()">&times;</span>
    <img class="modal-content" id="fullImage">
    <a id="downloadLink" class="download-large" download>📥 Télécharger en grand</a>
</div>

<script>
function openModal(imageUrl, fileName) {
    const modal = document.getElementById('imageModal');
    const fullImage = document.getElementById('fullImage');
    const downloadLink = document.getElementById('downloadLink');
    
    fullImage.src = imageUrl;
    downloadLink.href = imageUrl;
    downloadLink.download = fileName;
    modal.style.display = 'flex';
    
    // Fermer avec la touche Échap
    document.onkeydown = function(evt) {
        evt = evt || window.event;
        if (evt.keyCode === 27) {
            closeModal();
        }
    };
}

function closeModal() {
    document.getElementById('imageModal').style.display = 'none';
    document.onkeydown = null;
}

// Fermer en cliquant en dehors de l'image
window.onclick = function(event) {
    const modal = document.getElementById('imageModal');
    if (event.target === modal) {
        closeModal();
    }
}
</script>
""", unsafe_allow_html=True)

# ========== رابط الصورة ==========
image_url = f"{BASE_URL}mes_documents/Medicofi/Société%20ApniDoc%20(en%20France)/Flyer%20ApniDoc.png"
file_name = "Flyer_ApniDoc.png"

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📂 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    if st.button("🏥 Medicofi", key="medicofi"):
        st.session_state.page = "medicofi"
        st.rerun()

elif st.session_state.page == "medicofi":
    if st.button("← Retour"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>🏥 Medicofi</h1>", unsafe_allow_html=True)
    
    if st.button("🇫🇷 Société ApniDoc (en France)"):
        st.session_state.page = "apnidoc"
        st.rerun()

elif st.session_state.page == "apnidoc":
    if st.button("← Retour"):
        st.session_state.page = "medicofi"
        st.rerun()
    
    st.markdown("<h1>🇫🇷 Société ApniDoc</h1>", unsafe_allow_html=True)
    
    # عرض الصورة المصغرة القابلة للنقر
    st.markdown(f"""
    <div class="image-container">
        <img src="{image_url}" 
             class="thumbnail" 
             alt="Flyer ApniDoc"
             onclick="openModal('{image_url}', '{file_name}')">
        <div class="click-hint">👆 Cliquez pour agrandir l'image</div>
    </div>
    """, unsafe_allow_html=True)
    
    # زر تحميل بسيط
    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <a href="{image_url}" download="{file_name}" style="
            display: inline-block;
            background: rgba(255,255,255,0.15);
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            text-decoration: none;
            border: 1px solid rgba(255,255,255,0.3);
            transition: all 0.3s;
        ">
            📥 Télécharger l'image
        </a>
    </div>
    """, unsafe_allow_html=True)
