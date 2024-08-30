import streamlit as st
import plotly.graph_objects as go
from fpdf import FPDF

ncs = {
    "NC 1": {"Conforme": 20, "Não Conforme": 5},
    "NC 2": {"Conforme": 40, "Não Conforme": 10},
    "NC 3": {"Conforme": 15, "Não Conforme": 30},
}

def create_bar_chart(nc, data):
    labels = list(data.keys())
    values = list(data.values())

    fig = go.Figure(data=[go.Bar(x=labels, y=values)])
    fig.update_layout(
        title_text=f"Conformidades e Não Conformidades de {nc}",
        xaxis_title="Status",
        yaxis_title="Quantidade",
    )
    return fig

def generate_pdf(nc, data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Relatório de {nc}", ln=True, align="C")
    pdf.ln(10)
    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
    pdf_file = f"{nc}_relatorio.pdf"
    pdf.output(pdf_file)
    return pdf_file

def run():
    st.title("Visualização de Conformidades por NC")

    nc_selecionada = st.selectbox("Selecione a NC que deseja visualizar:", list(ncs.keys()))

    if nc_selecionada:
        data = ncs[nc_selecionada]
        fig = create_bar_chart(nc_selecionada, data)
        st.plotly_chart(fig)

        if st.button("Gerar PDF"):
            pdf_file = generate_pdf(nc_selecionada, data)
            with open(pdf_file, "rb") as file:
                st.download_button(label="Baixar Relatório em PDF", data=file, file_name=pdf_file)

        if st.button("Solicitar Plano de Ação"):
            st.success(f"Plano de Ação solicitado para {nc_selecionada}.")

