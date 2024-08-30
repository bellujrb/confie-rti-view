import streamlit as st
import time

import start, documents_screen, ncs_screen, plan_screen

def check_credentials(username, password):
    return username == "admin" and password == "admin"

def main():
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
        st.session_state['show_animation'] = False

    if not st.session_state['authenticated']:
        if not st.session_state['show_animation']:
            st.title("Login")
            with st.form(key='login_form'):
                username = st.text_input("Nome de Usuário")
                password = st.text_input("Senha", type="password")
                login_button = st.form_submit_button("Login")
                if login_button:
                    if check_credentials(username, password):
                        st.session_state['show_animation'] = True
                        st.experimental_rerun()
                    else:
                        st.error("Credenciais incorretas, por favor tente novamente.")
            return
        else:
            show_animation()
            time.sleep(7)  
            st.session_state['authenticated'] = True
            st.experimental_rerun()

    st.sidebar.title('Navegação')
    PAGES_INDIVIDUAL = {
        "Inicio": start,
        "Documentos de Conformidade": documents_screen,
        "NCS Realizadas": ncs_screen,
        "Plano": plan_screen
    }

    selection = st.sidebar.radio("Ir para", list(PAGES_INDIVIDUAL.keys()), key='page')
    page = PAGES_INDIVIDUAL[selection]
    page.run()

def show_animation():
    st.markdown("""
        <div style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); display: flex; justify-content: center; align-items: center; background-color: #fff; height: 100vh; width: 100vw;">
            <div style="text-align: center;">
                <h2 style="font-size: 2em; font-weight: bold; animation: fadeIn 1.5s ease-in-out;">Conformetec</h2>
                <div style="border: 2px solid #00c853; padding: 10px; border-radius: 5px; display: inline-block; animation: pulse 1.5s infinite;">
                    <p style="font-size: 1.5em; font-weight: bold; color: #00c853;">Carregando...</p>
                </div>
            </div>
        </div>

        <style>
            @keyframes fadeIn {
                0% {opacity: 0;}
                100% {opacity: 1;}
            }
            @keyframes pulse {
                0% {transform: scale(1);}
                50% {transform: scale(1.05);}
                100% {transform: scale(1);}
            }
            body { margin: 0; padding: 0; overflow: hidden; }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
