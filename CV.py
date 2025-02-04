import streamlit as st
import requests
import io

# GitHub raw URL a PDF fájlhoz (Cseréld ki a sajátodra!)
GITHUB_PDF_URL = "https://github.com/cserpakzalan2002/CV/blob/main/CserpakZalan_CV%20(1).pdf"

def load_pdf(url):
    """Letölti a PDF-et és betölti egy memória-pufferbe."""
    response = requests.get(url)
    if response.status_code == 200:
        return io.BytesIO(response.content)
    else:
        st.error("Hiba történt a PDF betöltésekor. Ellenőrizd az URL-t!")
        return None

# Streamlit oldal beállítása
st.set_page_config(page_title="CV Megjelenítő", page_icon="📄")
st.title("📄 Az Önéletrajzom")

# PDF megjelenítése
pdf_file = load_pdf(GITHUB_PDF_URL)
if pdf_file:
    st.download_button(label="📥 Letöltés", data=pdf_file, file_name="cv.pdf", mime="application/pdf")
    st.write("🔍 **Önéletrajz előnézet**:")
    st.pdf(pdf_file)
