import streamlit as st

# ========== الإعدادات ==========
GITHUB_USER = "RihabJenzeri"
REPO_NAME = "streamlit-docs"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/"

# ========== حالة التطبيق ==========
if 'page' not in st.session_state:
    st.session_state.page = "accueil"

if 'show_big_image' not in st.session_state:
    st.session_state.show_big_image = False

# ========== تنسيق ==========
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
        justify-content: center;
        margin: 20px 0;
    }
    
    .small-image {
        width: 400px;
        height: 400px;
        object-fit: contain;
        border: 3px solid white;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .small-image:hover {
        transform: scale(1.02);
        box-shadow: 0 15px 40px rgba(0,0,0,0.4);
        border-color: #FFD700;
    }
    
    .big-image-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.9);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    }
    
    .big-image-container {
        position: relative;
        max-width: 90%;
        max-height: 90%;
    }
    
    .big-image {
        width: 100%;
        height: auto;
        max-height: 80vh;
        border-radius: 10px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    
    .close-btn {
        position: absolute;
        top: -40px;
        right: -10px;
        background: rgba(255, 255, 255, 0.2);
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 50%;
        font-size: 20px;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .close-btn:hover {
        background: rgba(255, 255, 255, 0.3);
        transform: scale(1.1);
    }
    
    .download-btn {
        display: inline-block;
        background: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        text-decoration: none;
        margin-top: 15px;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .download-btn:hover {
        background: #45a049;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# ========== رابط الصورة ==========
image_url = f"{BASE_URL}mes_documents/Medicofi/Société%20ApniDoc%20(en%20France)/Flyer%20ApniDoc.png"

# ========== نافذة الصورة الكبيرة ==========
if st.session_state.show_big_image:
    st.markdown("""
    <div class="big-image-overlay">
        <div class="big-image-container">
            <button class="close-btn" onclick="this.nextElementSibling.click()">✕</button>
            <img src="{}" class="big-image" alt="Flyer ApniDoc">
            <div style="text-align: center; margin-top: 20px;">
                <a href="{}" download="Flyer_ApniDoc.png" class="download-btn">
                    📥 Télécharger l'image
                </a>
            </div>
        </div>
    </div>
    """.format(image_url, image_url), unsafe_allow_html=True)
    
    # زر إغلاق مخفي
    if st.button("✕ Fermer", key="close_big_image", type="primary"):
        st.session_state.show_big_image = False
        st.rerun()

# ========== الصفحات ==========
if st.session_state.page == "accueil":
    st.markdown("<h1>📂 Mes Dossiers</h1>", unsafe_allow_html=True)
    
    if st.button("Medicofi", key="medicofi"):
        st.session_state.page = "medicofi"
        st.rerun()

elif st.session_state.page == "medicofi":
    if st.button("← Retour"):
        st.session_state.page = "accueil"
        st.rerun()
    
    st.markdown("<h1>Medicofi</h1>", unsafe_allow_html=True)
    
    if st.button("Société ApniDoc (en France)"):
        st.session_state.page = "apnidoc"
        st.rerun()

elif st.session_state.page == "apnidoc":
    if st.button("← Retour"):
        st.session_state.page = "medicofi"
        st.rerun()
    
    st.markdown("<h1>Société ApniDoc</h1>", unsafe_allow_html=True)
    
    # عرض الصورة 500x500
    st.markdown("""
    <div class="image-container">
        <img src="{}" class="small-image" alt="Flyer ApniDoc" 
             onclick="this.nextElementSibling.click()">
    </div>
    """.format(image_url), unsafe_allow_html=True)
    
    # زر مخفي لفتح الصورة الكبيرة
    if st.button("🖼️ Ouvrir en grand", key="open_big_image"):
        st.session_state.show_big_image = True
        st.rerun()
    
    # زر تحميل
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <a href="{}" download="Flyer_ApniDoc.png" class="download-btn">
            📥 Télécharger
        </a>
    </div>
    """.format(image_url), unsafe_allow_html=True)

# ========== JavaScript للتفاعل ==========
st.markdown("""
<script>
    // جعل الصورة قابلة للنقر
    const smallImage = document.querySelector('.small-image');
    if (smallImage) {
        smallImage.style.cursor = 'pointer';
        smallImage.addEventListener('click', function() {
            // البحث عن الزر المخفي والنقر عليه
            const buttons = document.querySelectorAll('button');
            for (let btn of buttons) {
                if (btn.textContent.includes('Ouvrir en grand')) {
                    btn.click();
                    break;
                }
            }
        });
    }
    
    // إغلاق الصورة الكبيرة بالضغط على ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const closeBtn = document.querySelector('.close-btn');
            if (closeBtn) closeBtn.click();
        }
    });
    
    // إغلاق الصورة الكبيرة بالضغط خارجها
    document.addEventListener('click', function(e) {
        const overlay = document.querySelector('.big-image-overlay');
        const container = document.querySelector('.big-image-container');
        if (overlay && !container.contains(e.target) && !e.target.classList.contains('small-image')) {
            const closeBtn = document.querySelector('.close-btn');
            if (closeBtn) closeBtn.click();
        }
    });
</script>
""", unsafe_allow_html=True)
