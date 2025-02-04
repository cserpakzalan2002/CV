import streamlit as st
import requests
import base64

# GitHub raw URL a PDF fájlhoz (cseréld ki a sajátodra!)
GITHUB_PDF_URL = "https://github.com/cserpakzalan2002/CV/blob/main/CserpakZalan_CV%20(1).pdf"

def get_pdf_from_github(url):
    """Letölti a PDF-et a GitHub-ról."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        st.error("Hiba történt a PDF letöltésekor. Ellenőrizd az URL-t!")
        return None

# Streamlit oldal beállítása
st.set_page_config(page_title="CV Megjelenítő", page_icon="📄")
st.title("📄 Az Önéletrajzom")

# PDF letöltése GitHub-ról
pdf_data = get_pdf_from_github(GITHUB_PDF_URL)

if pdf_data:
    # Letöltés gomb
    st.download_button(label="📥 Letöltés", data=pdf_data, file_name="cv.pdf", mime="application/pdf")

    # PDF megjelenítése
    st.write("🔍 **Önéletrajz előnézet**:")

    # Base64 kódolás és beágyazás
    base64_pdf = base64.b64encode(pdf_data).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
