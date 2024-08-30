import streamlit as st
from fpdf import FPDF
import os

def create_blank_pdf(filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=" ", ln=True, align="C")  
    pdf.output(filename)

def run():
    st.title("Lista de Conformidades")

    conformidades = {
        "Conformidade 1": ["documento1.pdf", "documento2.pdf"],
        "Conformidade 2": ["documento3.pdf", "documento4.pdf"],
        "Conformidade 3": ["documento5.pdf", "documento6.pdf"],
    }

    for conformidade, documentos in conformidades.items():
        for doc in documentos:
            if not os.path.exists(doc):
                create_blank_pdf(doc)

    for conformidade, documentos in conformidades.items():
        with st.expander(conformidade):
            st.write(f"Documentos disponíveis para {conformidade}:")
            for doc in documentos:
                with open(doc, "rb") as file:
                    st.download_button(label=f"Baixar {doc}", data=file, file_name=doc)