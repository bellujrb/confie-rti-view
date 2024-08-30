import streamlit as st
import pandas as pd

ncs = {
    "NC 1": {"Conforme": 20, "Não Conforme": 5, "Solicitado": True},
    "NC 2": {"Conforme": 40, "Não Conforme": 10, "Solicitado": False},
    "NC 3": {"Conforme": 15, "Não Conforme": 30, "Solicitado": True},
}

planos_de_acao = {
    "NC 1": [
        {"Ação": "Revisar processos", "Responsável": "João", "Prazo": "2024-09-15"},
        {"Ação": "Realizar treinamento", "Responsável": "Maria", "Prazo": "2024-09-20"},
    ],
    "NC 3": [
        {"Ação": "Ajustar procedimentos", "Responsável": "Carlos", "Prazo": "2024-09-10"},
        {"Ação": "Implementar melhorias", "Responsável": "Ana", "Prazo": "2024-09-25"},
    ],
}

def run():
    st.title("Planos de Ação para Não Conformidades (NCs)")

    nc_selecionada = st.selectbox("Selecione a NC para visualizar o plano de ação:", list(ncs.keys()))

    if ncs[nc_selecionada]["Solicitado"]:
        st.subheader(f"Plano de Ação para {nc_selecionada}")
        plano_data = planos_de_acao.get(nc_selecionada, [])
        if plano_data:
            df = pd.DataFrame(plano_data)
            st.table(df)
        else:
            st.write("Nenhum plano de ação foi definido ainda para esta NC.")
    else:
        st.error("Plano de Ação ainda não foi solicitado para esta NC.")