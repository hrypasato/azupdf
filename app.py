import streamlit as st
from services.pdf_extractor import extract_pdf_url

st.set_page_config(page_title="Extractor de PDF")

st.title("🔍 Extractor de PDF")

url = st.text_input("Pega el enlace:", placeholder = "https://example.com/mydocument.pdf")

if st.button("Obtener PDF"):
    try:
        pdf_url = extract_pdf_url(url)

        st.success("PDF encontrado ✅")

        st.markdown(f"[📂 Abrir PDF]({pdf_url})")

        st.markdown(
            f'<iframe src="{pdf_url}" width="100%" height="600px"></iframe>',
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(str(e))