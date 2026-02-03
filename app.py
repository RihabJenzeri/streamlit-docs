import streamlit as st
import os
import base64
from pathlib import Path

# ========== CSS للتنسيق والخلفية ==========
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Poppins', sans-serif;
        min-height: 100vh;
    }
    
    .title-container {
        text-align: center;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .main-title {
        color: white;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .subtitle {
        color: #f0f0f0;
        font-size: 1.5rem;
        font-weight: 300;
        opacity: 0.9;
    }
    
    .folder-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 2rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
        padding: 1.5rem;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.05);
    }
    
    .folder-container:hover {
        transform: scale(1.05);
        background: rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    .folder-icon {
        font-size: 5rem;
        color: #FFD700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 0.5rem;
    }
    
    .folder-name {
        color: white;
        font-size: 1.8rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    
    .folder-desc {
        color: #e0e0e0;
        font-size: 1.1rem;
        text-align: center;
        max-width: 400px;
        margin-top: 0.5rem;
    }
    
    .back-button {
        margin-bottom: 2rem;
        padding: 0.8rem 1.8rem;
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-weight: 500;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .back-button:hover {
        background: rgba(255, 255, 255, 0.25);
        transform: translateX(-5px);
    }
    
    .file-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }
    
    .file-item {
        background: rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 180px;
    }
    
    .file-item:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
    }
    
    .file-icon {
        font-size: 3rem;
        color: #4FC3F7;
        margin-bottom: 1rem;
    }
    
    .file-name {
        color: white;
        font-weight: 500;
        word-break: break-word;
        font-size: 1.1rem;
    }
    
    .image-container {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        border: 2px dashed rgba(255, 255, 255, 0.1);
    }
    
    .section-title {
        color: white;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 2rem;
        position: relative;
        display: inline-block;
        left: 50%;
        transform: translateX(-50%);
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 25%;
        width: 50%;
        height: 3px;
        background: linear-gradient(90deg, transparent, #FFD700, transparent);
    }
    
    .info-box {
        background: rgba(255, 255, 255, 0.08);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        border-left: 5px solid #4FC3F7;
    }
    
    .download-btn {
        display: inline-block;
        padding: 0.8rem 2rem;
        background: linear-gradient(90deg, #4FC3F7, #2979FF);
        color: white;
        border-radius: 25px;
        text-decoration: none;
        font-weight: 600;
        margin-top: 1rem;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(41, 121, 255, 0.3);
    }
    
    .download-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(41, 121, 255, 0.4);
        background: linear-gradient(90deg, #2979FF, #4FC3F7);
    }
</style>
""", unsafe_allow_html=True)

# ========== الإعدادات ==========
GITHUB_USER = "RihabJenzeri"
REPO_NAME = "streamlit-docs"
BRANCH = "main"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/{BRANCH}/"

# ========== حالة التطبيق ==========
if 'current_folder' not in st.session_state:
    st.session_state.current_folder = None

# ========== دالة لعرض الصور ==========
def display_image_from_github(image_path):
    try:
        full_url = BASE_URL + image_path
        
        # عرض الصورة مع تنسيق
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(full_url, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # زر التحميل
        file_name = os.path.basename(image_path)
        st.markdown(f'''
        <div style="text-align: center; margin-top: 1.5rem;">
            <a href="{full_url}" download="{file_name}" class="download-btn">
                📥 Télécharger "{file_name}"
            </a>
        </div>
        ''', unsafe_allow_html=True)
        
        # معلومات الملف
        st.markdown(f'''
        <div style="text-align: center; margin-top: 1rem; color: rgba(255,255,255,0.7);">
            <small>URL: <code style="background: rgba(0,0,0,0.2); padding: 2px 5px; border-radius: 3px;">{full_url}</code></small>
        </div>
        ''', unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"❌ Erreur de chargement: {str(e)}")
        st.info(f"Vérifiez que le fichier existe à l'URL: {BASE_URL + image_path}")

# ========== الصفحة الرئيسية ==========
if st.session_state.current_folder is None:
    # عنوان الترحيب
    st.markdown("""
    <div class="title-container">
        <h1 class="main-title">👋 Bonjour, je suis Iness Harrabi</h1>
        <p class="subtitle">🚀 Bienvenue sur mon Portfolio Professionnel Digital</p>
    </div>
    """, unsafe_allow_html=True)
    
    # وصف
    st.markdown("""
    <div style="text-align: center; color: rgba(255,255,255,0.9); margin: 2rem 0; font-size: 1.1rem;">
        <p>📊 Consultante en transformation digitale & santé connectée</p>
        <p>💡 Explorez mes projets et réalisations ci-dessous</p>
    </div>
    """, unsafe_allow_html=True)
    
    # أيقونة مجلد Medicofi
    st.markdown('<h2 class="section-title">📂 Mes Projets</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="folder-container" onclick="this.nextElementSibling.click()">
        <div class="folder-icon">🏥</div>
        <h2 class="folder-name">Medicofi</h2>
        <p class="folder-desc">Société de conseil en santé digitale - Innovation médicale & télémédecine</p>
        <p style="color: #81C784; margin-top: 0.5rem; font-size: 0.9rem;">Cliquez pour explorer →</p>
    </div>
    """, unsafe_allow_html=True)
    
    # زر مخفي للنقر
    if st.button("Ouvrir Medicofi", key="open_medicofi", type="primary"):
        st.session_state.current_folder = "Medicofi"
        st.rerun()

# ========== صفحة Medicofi ==========
elif st.session_state.current_folder == "Medicofi":
    # زر العودة
    if st.button("← Retour au portfolio", key="back_from_medicofi"):
        st.session_state.current_folder = None
        st.rerun()
    
    st.markdown('<h1 class="section-title">🏥 Medicofi</h1>', unsafe_allow_html=True)
    
    # معلومات عن Medicofi
    st.markdown("""
    <div class="info-box">
        <h3 style="color: #4FC3F7; margin-bottom: 1rem;">À propos de Medicofi</h3>
        <p style="color: white; line-height: 1.6;">
            Société spécialisée dans le conseil en santé digitale et l'innovation médicale. 
            Nous accompagnons les acteurs de la santé dans leur transformation numérique avec 
            des solutions sur mesure et innovantes.
        </p>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 1.5rem;">
            <div style="text-align: center;">
                <div style="font-size: 2rem; color: #FFD700;">📍</div>
                <p style="color: white; font-weight: 500;">Siège Social</p>
                <p style="color: #ccc;">Paris, France</p>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 2rem; color: #FFD700;">🎯</div>
                <p style="color: white; font-weight: 500;">Secteur</p>
                <p style="color: #ccc;">Santé Digitale</p>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 2rem; color: #FFD700;">📈</div>
                <p style="color: white; font-weight: 500;">Expertise</p>
                <p style="color: #ccc;">Consulting & Innovation</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # قائمة المحتويات
    st.markdown('<h3 style="color: white; margin: 2rem 0 1rem 0;">📁 Contenu du dossier</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="folder-container" onclick="this.nextElementSibling.click()" style="height: 100%;">
            <div class="folder-icon">🇫🇷</div>
            <h3 class="folder-name">Société ApniDoc France</h3>
            <p class="folder-desc" style="font-size: 0.95rem;">Projet de télémédecine innovant en France</p>
            <p style="color: #81C784; margin-top: 0.5rem; font-size: 0.85rem;">Cliquez pour explorer →</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Ouvrir ApniDoc", key="open_apnidoc_col1"):
            st.session_state.current_folder = "ApniDoc_France"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="file-item">
            <div class="file-icon">📊</div>
            <p class="file-name">Rapports Annuels 2024</p>
            <p style="color: #ccc; font-size: 0.9rem; margin-top: 0.5rem;">Documents financiers stratégiques</p>
            <div style="margin-top: 1rem; padding: 0.3rem 0.8rem; background: rgba(76, 175, 80, 0.2); border-radius: 10px;">
                <small style="color: #81C784;">PDF • 5.2MB</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="file-item">
            <div class="file-icon">📄</div>
            <p class="file-name">Présentation Corporate</p>
            <p style="color: #ccc; font-size: 0.9rem; margin-top: 0.5rem;">Deck d'entreprise complet</p>
            <div style="margin-top: 1rem; padding: 0.3rem 0.8rem; background: rgba(41, 121, 255, 0.2); border-radius: 10px;">
                <small style="color: #4FC3F7;">PDF • 8.7MB</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ========== صفحة ApniDoc France ==========
elif st.session_state.current_folder == "ApniDoc_France":
    # زر العودة
    col1, col2 = st.columns([1, 6])
    with col1:
        if st.button("← Retour", key="back_from_apnidoc"):
            st.session_state.current_folder = "Medicofi"
            st.rerun()
    
    st.markdown('<h1 class="section-title">🇫🇷 Société ApniDoc (France)</h1>', unsafe_allow_html=True)
    
    # معلومات عن ApniDoc
    st.markdown("""
    <div class="info-box">
        <h3 style="color: #4FC3F7; margin-bottom: 1rem;">🏥 À propos d'ApniDoc</h3>
        <p style="color: white; line-height: 1.6;">
            Startup innovante spécialisée dans la télémédecine et les solutions digitales pour la santé. 
            ApniDoc propose une plateforme complète de consultation à distance avec intégration 
            des données médicales et suivi patient intelligent.
        </p>
        
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem; margin-top: 1.5rem;">
            <div>
                <h4 style="color: #81C784; margin-bottom: 0.5rem;">📍 Implantation</h4>
                <p style="color: #e0e0e0;">Paris (Siège) + Lyon + Bordeaux</p>
            </div>
            <div>
                <h4 style="color: #81C784; margin-bottom: 0.5rem;">🎯 Marché</h4>
                <p style="color: #e0e0e0;">France & Europe Francophone</p>
            </div>
            <div>
                <h4 style="color: #81C784; margin-bottom: 0.5rem;">📅 Lancement</h4>
                <p style="color: #e0e0e0;">Janvier 2023</p>
            </div>
            <div>
                <h4 style="color: #81C784; margin-bottom: 0.5rem;">👥 Équipe</h4>
                <p style="color: #e0e0e0;">15 collaborateurs</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # عرض Flyer ApniDoc
    st.markdown('<h2 style="color: white; margin: 3rem 0 1.5rem 0;">🖼️ Flyer ApniDoc - Support de Communication</h2>', unsafe_allow_html=True)
    
    # المسار الصحيح للصورة
    image_path = "mes_documents/Medicofi/Société ApniDoc (en France)/Flyer ApniDoc.jpg"
    
    # محاولة عرض الصورة
    display_image_from_github(image_path)
    
    # إذا كانت هناك مشكلة في الصورة
    if st.button("🔄 Rafraîchir l'image", key="refresh_image"):
        st.rerun()
    
    # ملفات أخرى في المجلد
    st.markdown('<h3 style="color: white; margin: 3rem 0 1.5rem 0;">📚 Autres documents du projet</h3>', unsafe_allow_html=True)
    
    other_files = [
        {
            "name": "Business Plan ApniDoc.pdf", 
            "icon": "📋", 
            "size": "2.1MB",
            "desc": "Plan d'affaires détaillé"
        },
        {
            "name": "Logo ApniDoc Officiel.png", 
            "icon": "🏢", 
            "size": "540KB",
            "desc": "Logo corporate haute résolution"
        },
        {
            "name": "Brochure Services 2024.pdf", 
            "icon": "📘", 
            "size": "4.8MB",
            "desc": "Catalogue des services"
        },
        {
            "name": "Étude Marché France.pdf", 
            "icon": "📈", 
            "size": "3.2MB",
            "desc": "Analyse du marché santé digital"
        }
    ]
    
    cols = st.columns(4)
    for idx, file_info in enumerate(other_files):
        with cols[idx % 4]:
            st.markdown(f"""
            <div class="file-item">
                <div class="file-icon">{file_info['icon']}</div>
                <p class="file-name">{file_info['name']}</p>
                <p style="color: #ccc; font-size: 0.9rem; margin-top: 0.5rem;">{file_info['desc']}</p>
                <div style="margin-top: 1rem; padding: 0.3rem 0.8rem; background: rgba(255, 193, 7, 0.1); border-radius: 10px;">
                    <small style="color: #FFD700;">{file_info['size']}</small>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ========== JavaScript للتفاعل ==========
st.markdown("""
<script>
    // جعل جميع الأيقونات قابلة للنقر
    document.querySelectorAll('.folder-container').forEach(container => {
        container.style.cursor = 'pointer';
        container.addEventListener('click', function() {
            this.nextElementSibling.click();
        });
    });
    
    // تأثير عند تحميل الصفحة
    document.addEventListener('DOMContentLoaded', function() {
        const title = document.querySelector('.main-title');
        if (title) {
            title.style.opacity = '0';
            title.style.transform = 'translateY(20px)';
            
            setTimeout(() => {
                title.style.transition = 'all 0.8s ease';
                title.style.opacity = '1';
                title.style.transform = 'translateY(0)';
            }, 300);
        }
    });
</script>
""", unsafe_allow_html=True)

# ========== معلومات التطبيق ==========
st.markdown("""
---
<div style="text-align: center; color: rgba(255,255,255,0.6); padding: 2rem 0; font-size: 0.9rem;">
    <p>📁 Portfolio Digital • Iness Harrabi • Tous droits réservés © 2024</p>
    <p>🔗 <strong>Repository GitHub:</strong> <code>{GITHUB_USER}/{REPO_NAME}</code></p>
    <p>🔄 Les fichiers sont chargés directement depuis GitHub</p>
</div>
""".format(GITHUB_USER=GITHUB_USER, REPO_NAME=REPO_NAME), unsafe_allow_html=True)
