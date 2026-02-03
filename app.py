import streamlit as st
import requests

# ========== إعدادات ==========
GITHUB_USER = "RihabJenzeri"
REPO_NAME = "streamlit-docs"
BRANCH = "main"
BASE_URL = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/"

# ========== دالة للتحقق من الملفات ==========
def check_github_files():
    st.title("🔍 التحقق من ملفات GitHub")
    
    try:
        # جلب محتويات الريبو
        response = requests.get(BASE_URL, headers={"Accept": "application/vnd.github.v3+json"})
        
        if response.status_code == 200:
            contents = response.json()
            st.success("✅ تم الاتصال بـ GitHub بنجاح")
            
            # عرض المجلدات والملفات
            st.subheader("📂 محتويات الريبو:")
            for item in contents:
                if item['type'] == 'dir':
                    st.write(f"📁 **{item['name']}**")
                    # يمكن عرض محتويات المجلد
                    sub_response = requests.get(item['url'])
                    if sub_response.status_code == 200:
                        sub_contents = sub_response.json()
                        for sub_item in sub_contents:
                            st.write(f"   └─ {sub_item['name']} ({sub_item['type']})")
                else:
                    st.write(f"📄 {item['name']}")
        else:
            st.error(f"❌ خطأ في الاتصال: {response.status_code}")
            
    except Exception as e:
        st.error(f"❌ خطأ: {str(e)}")

# ========== دالة لعرض الصورة مباشرة ==========
def display_image_simple():
    st.title("🖼️ اختبار عرض الصورة")
    
    # اختبار مسارات مختلفة
    test_paths = [
        "mes_documents/Medicofi/Société ApniDoc (en France)/Flyer ApniDoc.jpg",
        "mes_documents/Medicofi/ApniDoc_France/Flyer_ApniDoc.jpg",
        "mes_documents/Medicofi/Societe_ApniDoc_France/Flyer_ApniDoc.jpg",
        "mes_documents/Medicofi/ApniDoc/Flyer.jpg",
    ]
    
    for path in test_paths:
        image_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/{BRANCH}/{path}"
        
        st.subheader(f"اختبار: {path}")
        st.code(image_url)
        
        # اختبار إذا كان الملف موجود
        try:
            response = requests.head(image_url)
            if response.status_code == 200:
                st.success("✅ الملف موجود!")
                st.image(image_url, caption=path, use_container_width=True)
                break  # توقف عند أول صورة تعمل
            else:
                st.warning(f"⚠️ الملف غير موجود (الكود: {response.status_code})")
        except Exception as e:
            st.error(f"❌ خطأ: {str(e)}")
        
        st.markdown("---")

# ========== التطبيق الرئيسي ==========
st.set_page_config(page_title="GitHub File Checker", layout="wide")

tab1, tab2 = st.tabs(["🔍 تحقق من الملفات", "🖼️ اختبار الصور"])

with tab1:
    check_github_files()

with tab2:
    display_image_simple()
